"""本站（UkTxGNN）查核機制的在地設定（2026-11-12 建）：頁面文字、資料來源、頁首規則、許可證格式、歷史刪改提交。

同目錄 page_format／licenses／withdrawn 與 scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py 都讀這裡；核心流程比照 TwTxGNN 與 UsTxGNN，只有這份是本站自己的寫法。
本站的市場資料是 NHSBSA BNF 處方代碼清單（NHS 處方用的 BNF presentation code），不是 MHRA 許可證。
"""
import gzip
import importlib.util
import json
import re
from pathlib import Path

SITE = "UkTxGNN"
CODE = "uk"
BUNDLE_KEY = "tfda"  # 證據包裡本站市場資料的鍵（收集器沿用的欄位名）

# ---------- 頁首等級（page_format） ----------
LEVEL_LABELS = ["Evidence Level"]          # Quick Overview 與其他預測表的證據等級欄名
HEADER_LABEL = r"Evidence Level"           # 頁首「Evidence Level: **Lx**」
WITHDRAWN = r"Withdrawn\b"                 # 重審撤回後總覽格的開頭
# 頁首規則：2026-11-12 實測 551 頁有總覽等級，頁首全部＝格裡第一個等級（主預測）；整格取最高會有 10 頁不同
HEADER_RULE = "first"
DESC_LEVEL_RE = re.compile(r"evidence level (L[1-5]|N/A)", re.I)


def desc_level_text(level):
    return "known uses only" if level == "N/A" else f"evidence level {level}"


DISCLAIMER_RE = re.compile(r"^## Disclaimer\b", re.M)

# ---------- 頁面文字（apply_drug_reviews） ----------
T = {
    "label": {"correct": "Review correction", "annotate": "Review note", "rereview": "Pending re-review",
              "rereview_result": "Re-review result"},
    "action": {"correct": "Corrected", "annotate": "Annotated", "rereview": "Marked for re-review",
               "section": "Added a sourced section", "rereview_result": "Re-review completed",
               "header_level": "Header evidence level recomputed from the Quick Overview",
               "description_level": "Page description evidence level set to the header level"},
    "verdict": {"maintain": "Maintained", "downgrade": "Downgraded", "upgrade": "Upgraded", "withdraw": "Withdrawn"},
    "log_head": "## Review Log",
    "log_cols": "| Review date | Item | Action | Source |",
    "head": "> **{label} ({date})**: ",
    "originally": "Originally stated: \"{claim}\"",
    "source": "Source: {src}.",
    "decision": "Decision recommendation: {note}",
    "level_same": "evidence level {o} unchanged",
    "level_change": "evidence level {o} → {n}",
    "table_updated": " The {labels} on this page were updated to the re-review result; the original values are listed in the Review Log below.",
    "rereviewed": "Marked for re-review → re-reviewed (see the re-review result)",
    "hdr": "Header evidence level recomputed from the Quick Overview ({o} → {n})",
    "hdr_withdraw": "Main prediction withdrawn on re-review; header evidence level recomputed ({o} → {n})",
    "listed_under": ", now listed under \"{t}\"",
    "rr": "Re-review: {v}, {c}",
    "tu": "; {l}: \"{a}\" → \"{b}\"",
    "desc": "Page description: \"evidence level {o}\" changed to \"{n}\" (follows the header level; other text unchanged, original kept in the record)",
    "revised": " (revised {d}; earlier version kept in the record)",
    "superseded": "Superseded by the program-generated BNF code table (was: {a})",
    "regen": "No longer present after the report was regenerated ({d}: {n}; was: {a})",
    "prog": "No longer present after a program fix ({d}: {n}; was: {a})",
    "wd": "Review withdrawn ({d}: {n}; was: {a})",
    "intro": ("Below is the review log for this page: statements checked against the official data this site uses "
              "(the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic "
              "factual statements; model predictions, evidence levels, and conclusions were not rewritten."),
    "intro_levels": ("Below is the review log for this page; the header evidence level follows the Quick Overview. "
                     "Model predictions, the overview table, and conclusions were not rewritten."),
    "intro_rr": ("Below is the review log for this page. Corrections are limited to basic factual statements and model prediction text "
                 "was not rewritten; evidence levels and decisions were changed only by a re-review result (downgrade, upgrade, or "
                 "withdrawal), with the original values listed below."),
}

# ---------- 許可證（licenses、build_license_snapshot） ----------
MARKET_SEC = re.compile(r"^## UK Market Information\s*$")
ID_RE = re.compile(r"\b\d{7}[0-9A-Z]{8}\b")  # BNF presentation code（15 碼；2026-11-12 依證據包實測的格式）


def own_ids(tf):
    return sorted({str(r.get("license_id") or "").strip() for r in tf.get("records") or [] if r.get("license_id")})


def _slt():
    p = Path(__file__).resolve().parents[3] / "scripts" / "sync_license_tables.py"
    s = importlib.util.spec_from_file_location("uk_sync_license_tables", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def program_block_problems(sec_lines, entry):
    """程式區塊（licenses:begin／end）＝依快照重算的結果（scripts/sync_license_tables.py 的 program_block）"""
    S = _slt()
    has_b, has_e = S.BEGIN in sec_lines, S.END in sec_lines
    if has_b != has_e:
        return ["程式區塊標記不成對"]
    if not has_b:
        if any(l.strip() == S.HEAD[0] for l in sec_lines) or any(l.strip() == S.NONE_LINE for l in sec_lines):
            return ["程式表沒有程式區塊標記（跑 python3 scripts/sync_license_tables.py --mark-existing）"]
        return []
    i, j = sec_lines.index(S.BEGIN), sec_lines.index(S.END)
    got = [x for x in sec_lines[i + 1:j] if x.strip()]
    rows = entry.get("rows") or []
    if entry.get("total", 0) > len(rows):  # 快照只存前 20 列；總數更多時程式表也只列 20 列，SHOW 句用總數
        want = [x for x in S.HEAD + rows[:S.MAX_ROWS] if x.strip()] + [S.SHOW.format(n=S.MAX_ROWS, m=entry["total"]) + " " + S.SOURCE]
    else:
        want = [x for x in S.program_block(rows) if x.strip()]
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        return [f"程式區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 scripts/sync_license_tables.py）"]
    return []


# ---------- 刪改轉紀錄（reviews_from_edits） ----------
# 2026-10-31～11-06 的許可證刪改（git log docs/_drugs；排程狀態格、欄位名統一、排除表、AI 重產、description、表格空行不算）
COMMITS = ["475a71c7c", "7cf28e811", "2c2697644", "67acd88de", "3461c7400", "54b162b61"]
# 期間內以 AI 整份重產報告或套排除表重寫段落的提交
REGEN_COMMITS = ["0b6efadd0", "1b95da805", "f0cb0ba12", "eead0a975", "611adc96e", "de4974fd4", "7ae52acb1", "75c6652e2"]
SOURCES = [{"title": "NHSBSA BNF code information", "url": "https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9(*"\[])|\n')
PROGRAM_LINES = [re.compile(r"^Showing \d+ of \d+ BNF presentation codes\."), re.compile(r"^Source: NHSBSA BNF code information"),
                 re.compile(r"^Not listed in the NHSBSA BNF prescribing code list used for this report\.$"),
                 re.compile(r"^Only part of the licence list is held in the data; the list may be incomplete\.$")]  # known_use_pages 寫的程式句
CLASSIFY = [
    ("tw", re.compile(r"Taiwan|TFDA", re.I)),
    ("pipeline", re.compile(r"\b(re-?run|retriev|fetch|extract|pipeline|populate|load)\w*\b[^.;]{0,80}\b(MHRA|licen[cs]|authori[sz])|"
                            r"\b(MHRA|licen[cs]e)\w*[^.;]{0,40}\b(incomplete|missing|not (yet )?loaded)", re.I)),
    ("list", re.compile(r"licen[cs]|authori[sz]|MHRA|marketing|valid|cancel|withdrawn|registered|PL ?\d", re.I)),
    ("combo", re.compile(r"single[- ]ingredient|combination|combo|multi-ingredient", re.I)),
]


def reason_kind(reason):
    """人工清單（scripts/license_sentence_fixes.json）的中文理由 → 類別；判斷不了回 None（改用被刪文字分類）"""
    if re.search(r"台灣|TFDA", reason):
        return "tw"
    if re.search(r"擷取|重跑|去 MHRA|不完整|尚未載入", reason):
        return "pipeline"
    if re.search(r"BNF|不是 MHRA 許可|許可紀錄|說成許可|有效|市場狀態", reason):
        return "list"
    if re.search(r"單方|複方", reason):
        return "combo"
    return None
SUMMARY = "Removed: \"{text}\""
REGEN_NOTE = "the report was regenerated in 2026-11 and no longer contains this statement"


def _fig(fc):
    if not fc or fc.get("total") is None:
        return ""
    n = fc["total"]
    return (f" This drug has {n} BNF presentation code{'s' if n != 1 else ''} in that list; the Quick Overview and the table under "
            "UK Market Information show the current figures.")


def note_for(kind, date, fc):
    d = f"NHSBSA BNF prescribing code list, rebuilt by ingredient on {date}"
    if kind == "tw":
        return "Removed: leftover template text about Taiwan's TFDA, which does not apply to this UK page."
    if kind == "pipeline":
        return (f"Removed: it said licence data still had to be fetched from the MHRA or that licence records were incomplete; this site's "
                f"market data is the {d}, which does not contain MHRA licences.")
    if kind == "combo":
        return f"Removed: it described the products as single-ingredient or combination products in a way that did not match the {d}." + _fig(fc)
    if kind == "list":
        return (f"Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is "
                f"the {d}, which lists NHS prescribing codes and does not include MHRA licence status." + _fig(fc))
    return f"Removed: it conflicted with the {d}." + _fig(fc)


# ---------- 原適應症交叉驗證（check_original_indications） ----------
ORIG_LABELS = ["Original Indication"]
ORIG_NONE_RE = re.compile(r"^\s*(not (recorded|available|listed)|none|n/a|no (approved )?indication)", re.I)
ORIG_SPLIT_RE = re.compile(r"[;,/()]+|\band\b|\bor\b", re.I)
