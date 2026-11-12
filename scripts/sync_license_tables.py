"""依成分重建後，把藥物頁「## UK Market Information」段落的表換成程式產生的 BNF 處方代碼表（2026-11-06，用戶核准；全程不用 AI）。

前置：scripts/rebuild_licenses_by_ingredient.py 已重建 data/bundles（NHSBSA BNF 處方代碼清單，依成分，含複方代碼）。
UK 站的本地資料是 NHS 處方用的 BNF presentation code，不是 MHRA 許可證：
- 段落裡的第一張表（原表頭多寫成「Marketing Authorisation Number …」）換成「| BNF presentation code | BNF presentation | BNF chemical substance |」，
  不放狀態欄（清單沒有許可狀態）；最多列 20 筆，表後註明來源與「Showing 20 of N BNF presentation codes.」。
- 表後 known_use_pages 寫的「Only part of the licence list is held in the data; the list may be incomplete.」一併拿掉（重建後是完整清單）。
- 新資料沒有任何代碼時拿掉表，改一句「Not listed in the NHSBSA BNF prescribing code list used for this report.」
- 概覽表有「UK Market Status」列、卻沒有「Number of BNF Presentation Codes」列的頁（8 頁的張數原本寫在被換掉的舊表裡），
  在狀態列下面補一列，值＝清單筆數（與 check_drug_page.count_text 相同）。
- 段落裡沒有表的頁（舊頁只有文字、或矛盾句刪完只剩標題）：在標題下補程式產生的表與來源句（沒有紀錄時補「Not listed …」句，已有就不重複；2026-11-06 第三輪）；
  表以外的文字不動（跟新事實矛盾的句子由 tools/txgnn/.claude/delete_license_sentences.py 處理）。
程式區塊標記（2026-11-12 起）：程式產生的表連同來源句（或 NONE_LINE）前後各有「<!-- licenses:begin -->」「<!-- licenses:end -->」；
--mark-existing 只替現有程式區塊補標記、不改內容；carry_block 給 sync_notes_to_docs.py 重寫頁面時移植程式區塊。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--dry-run] [--mark-existing] [頁 ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = "## UK Market Information"
HEAD = ["| BNF presentation code | BNF presentation | BNF chemical substance |", "|------|------|------|"]
NONE_LINE = "Not listed in the NHSBSA BNF prescribing code list used for this report."
SOURCE = "Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data."
SHOW = "Showing {n} of {m} BNF presentation codes."
SHOW_RX = re.compile(r"^Showing \d+ of \d+ BNF presentation codes\.( .*)?$")
PART_NOTE = "Only part of the licence list is held in the data; the list may be incomplete."
MAX_ROWS = 20
# 程式區塊標記（2026-11-12 起，本站查核機制）：程式產生的表（連同來源句／SHOW 句，或 NONE_LINE）前後各一行，
# 讓查核紀錄、刪句工具與 gate 分得出哪些字是程式寫的；gate 依 snapshots/uk_licenses.json.gz 檢查程式區塊＝快照重算的結果。
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"


def cell(x, n=80):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def table_rows(recs):
    seen, rows = set(), []
    for r in recs:
        k = r.get("license_id")
        if not k or k in seen:
            continue
        seen.add(k)
        rows.append(f"| {k} | {cell(r.get('brand_name_en'), 70)} | {cell(r.get('ingredients'), 60)} |")
    return rows


STATUS_LABEL, COUNT_LABEL = "| UK Market Status |", "| Number of BNF Presentation Codes |"


def ensure_count_row(lines, recs, partial):
    if any(l.startswith(COUNT_LABEL) for l in lines):
        return lines
    for i, l in enumerate(lines):
        if l.startswith(STATUS_LABEL):
            n = len({r.get("license_id") for r in recs if r.get("license_id")})
            return lines[:i + 1] + [f"{COUNT_LABEL} {('at least ' if partial else '')}{n} |"] + lines[i + 1:]
    return lines


def rows_of(tf, fc=None):
    """快照用：(表格列, 總數)，跟 process 用同一套 table_rows"""
    rows = table_rows(tf.get("records") or [])
    return rows, len(rows)


def program_block(rows):
    """程式區塊的內容行（不含標記）"""
    if not rows:
        return [NONE_LINE]
    return HEAD + rows[:MAX_ROWS] + [""] + ([SHOW.format(n=MAX_ROWS, m=len(rows)) + " " + SOURCE] if len(rows) > MAX_ROWS else [SOURCE])


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def process(text, recs, partial=False):
    lines = ensure_count_row(strip_marks(text.split("\n")), recs, partial)
    if SEC not in lines:
        return None
    a = lines.index(SEC) + 1
    b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        rows = table_rows(recs)
        if rows or not any(l.strip() == NONE_LINE for l in lines[a:b]):
            lines = lines[:a] + [""] + wrap(program_block(rows)) + [""] + lines[a:]
        elif not rows:  # 已有 NONE_LINE：只補標記
            k = next(k for k in range(a, b) if lines[k].strip() == NONE_LINE)
            lines = lines[:k] + wrap([NONE_LINE]) + lines[k + 1:]
        t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
        return t2 if t2 != text else None
    x, y = tb[0], tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() != SOURCE and (partial or l.strip() != PART_NOTE)]
    rows = table_rows(recs)
    out = lines[:x] + wrap(program_block(rows)) + [""] + rest + lines[b:]
    if out[x - 1].strip():
        out.insert(x, "")
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return t2 if t2 != text else None


def _section(lines):
    if SEC not in lines:
        return None, None
    a = lines.index(SEC) + 1
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _program_span(lines, a, b):
    """段落裡現有程式區塊（未加標記）的 (起, 迄)：表頭＝HEAD 的表＋緊接的來源句／SHOW 句；或 NONE_LINE 一行"""
    for k in range(a, b):
        if lines[k].strip() == HEAD[0] and k + 1 < b and lines[k + 1].strip() == HEAD[1]:
            y = k + 1
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            j = y + 1
            while j < b and not lines[j].strip():
                j += 1
            if j < b and (lines[j].strip() == SOURCE or (SHOW_RX.match(lines[j].strip()) and lines[j].strip().endswith(SOURCE))):
                return k, j
            return k, y
        if lines[k].strip() == NONE_LINE:
            return k, k
    return None


def mark_existing(text):
    """現有程式區塊補上標記，內容一字不改；已有標記或沒有程式區塊就原樣"""
    lines = text.split("\n")
    if BEGIN in lines:
        return text
    a, b = _section(lines)
    if a is None:
        return text
    sp = _program_span(lines, a, b)
    if not sp:
        return text
    x, y = sp
    head = lines[:x]
    while head and not head[-1].strip():
        head.pop()
    rest = lines[y + 1:]
    while rest and not rest[0].strip():
        rest.pop(0)
    return "\n".join(head + [""] + wrap(lines[x:y + 1]) + [""] + rest)


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊（BEGIN…END）移植到新頁的市場段落，
    取代新頁段落裡的第一張表（連同緊接的來源句／SHOW 句）；新頁段落沒有表時接在段落開頭。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b = _section(lines)
    if a is None:
        return new_text
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() != SOURCE]
        out = lines[:x] + blk + [""] + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def main(argv):
    if "--mark-existing" in argv:
        n = 0
        for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
            raw = page.read_bytes().decode("utf-8")
            if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
                continue
            crlf = "\r\n" in raw[:500]
            t0 = raw.replace("\r\n", "\n")
            new = mark_existing(t0)
            if BEGIN in new and BEGIN not in t0:
                n += 1
                if "--dry-run" not in argv:
                    page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
        print(f"程式區塊標記：補上 {n} 頁")
        return
    dry = "--dry-run" in argv
    only = {a for a in argv if not a.startswith("--")}
    n = 0
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        bf = ROOT / "data/bundles" / page.stem / "drug_bundle.json"
        if not bf.exists():
            bf = ROOT / "data/bundles" / page.stem.replace("-", "_") / "drug_bundle.json"
        if not bf.exists():
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        crlf = "\r\n" in raw[:500]
        reg = json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}
        recs = reg.get("records") or []
        new = process(raw.replace("\r\n", "\n"), recs, int(reg.get("total_matches") or 0) > len(recs))
        if new is None:
            continue
        n += 1
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    print(f"許可證表改 {n} 頁")


if __name__ == "__main__":
    main(sys.argv[1:])
