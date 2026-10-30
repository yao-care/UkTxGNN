"""UK（NHSBSA BNF 代碼清單）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

注意：UK 站的「本地資料」原本就是 NHSBSA 的 BNF presentation code 清單（處方給付用的品項代碼），不是 MHRA 的 PL 許可證；
MHRA 沒有可對應 BNF 代碼的批次許可證檔（用戶 2026-10-30 選「沿用現有來源排程」）。
來源：NHSBSA 開放資料 CKAN 資料集 bnf-code-information-current-year（免金鑰），取最新一期 BNF_CODE_CURRENT_<年月> CSV。
欄位 BNF_PRESENTATION_CODE（＝證據包 license_id，例 0402010D0AAAIAI）。只列當期仍在用的代碼、沒有狀態欄：
在列不改紀錄，新清單查不到的代碼保留原狀態、列在 summary（不推定為撤銷）。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/nhsbsa_bnf_codes.json"
API = "https://opendata.nhsbsa.net/api/3/action/package_show?id=bnf-code-information-current-year"
UA = {"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"}


def _get(url):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=300, headers=UA, allow_redirects=True)
            r.raise_for_status()
            return r
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def fetch():
    res = _get(API).json()["result"]["resources"]
    res = sorted((r for r in res if str(r.get("url", "")).lower().endswith(".csv")), key=lambda r: r["name"])
    if not res:
        raise RuntimeError("資料集沒有 CSV")
    text = _get(res[-1]["url"]).content.decode("utf-8-sig", "replace")
    rows = csv.DictReader(io.StringIO(text))
    if "BNF_PRESENTATION_CODE" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變（可能拿到 HTML）：{(rows.fieldnames or [])[:5]}")
    return [{"bnf": (x["BNF_PRESENTATION_CODE"] or "").strip(), "period": res[-1]["name"]} for x in rows if x.get("BNF_PRESENTATION_CODE")]


def validate(new, old):
    p = []
    if len(new) < 20000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["bnf"]: "listed" for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    return False  # 在列不改紀錄；只用來確認仍在列，查不到的列在 summary
