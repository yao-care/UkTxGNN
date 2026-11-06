"""依成分重建後，把藥物頁「## UK Market Information」段落的表換成程式產生的 BNF 處方代碼表（2026-11-06，用戶核准；全程不用 AI）。

前置：scripts/rebuild_licenses_by_ingredient.py 已重建 data/bundles（NHSBSA BNF 處方代碼清單，依成分，含複方代碼）。
UK 站的本地資料是 NHS 處方用的 BNF presentation code，不是 MHRA 許可證：
- 段落裡的第一張表（原表頭多寫成「Marketing Authorisation Number …」）換成「| BNF presentation code | BNF presentation | BNF chemical substance |」，
  不放狀態欄（清單沒有許可狀態）；最多列 20 筆，表後註明來源與「Showing 20 of N BNF presentation codes.」。
- 表後 known_use_pages 寫的「Only part of the licence list is held in the data; the list may be incomplete.」一併拿掉（重建後是完整清單）。
- 新資料沒有任何代碼時拿掉表，改一句「Not listed in the NHSBSA BNF prescribing code list used for this report.」
- 概覽表有「UK Market Status」列、卻沒有「Number of BNF Presentation Codes」列的頁（8 頁的張數原本寫在被換掉的舊表裡），
  在狀態列下面補一列，值＝清單筆數（與 check_drug_page.count_text 相同）。
- 段落裡沒有表的頁不新增；表以外的文字不動（跟新事實矛盾的句子由 tools/txgnn/.claude/delete_license_sentences.py 處理）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--dry-run] [頁 ...]
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


def process(text, recs, partial=False):
    lines = ensure_count_row(text.split("\n"), recs, partial)
    if SEC not in lines:
        return None
    a = lines.index(SEC) + 1
    b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        t2 = "\n".join(lines)
        return t2 if t2 != text else None
    x, y = tb[0], tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() != SOURCE and (partial or l.strip() != PART_NOTE)]
    rows = table_rows(recs)
    if rows:
        block = HEAD + rows[:MAX_ROWS] + [""] + ([SHOW.format(n=MAX_ROWS, m=len(rows)) + " " + SOURCE] if len(rows) > MAX_ROWS else [SOURCE])
    else:
        block = [NONE_LINE]
    out = lines[:x] + block + rest + lines[b:]
    if out[x - 1].strip():
        out.insert(x, "")
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return t2 if t2 != text else None


def main(argv):
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
