"""UK 依成分重建證據包的「本地資料」紀錄（2026-11-06，用戶核准；全程不用 AI；做法比照 Za／Us／Sg／Eu）。

UK 站的本地資料是 NHSBSA 的 BNF presentation code 清單（NHS 處方用的品項代碼），不是 MHRA 許可證；這裡只依成分重建這份清單的筆數，
頁面上一律寫成「列在 BNF 處方代碼清單」、不含 MHRA 許可狀態（check_drug_page.SOURCE_STATUS／NO_CENTRAL）。
原收集器（src/uktxgnn/data/loader.py 的 load_bnf_data）以 drop_duplicates(subset=['Active_Substances']) 每個成分只留 1 筆代碼，
所以 841 個證據包只有 1 筆；本腳本改成同一成分的全部代碼。

1. 來源：NHSBSA 開放資料 CKAN 資料集 bnf-code-information-current-year（免金鑰；與 scripts/license_adapter.py 每週更新用的是同一份），
   取最新一期 BNF_CODE_CURRENT_<年月> CSV，存 data/raw/nhsbsa_bnf_code_current.csv（--skip-download 用已存的檔）。
   只收 BNF 第 1–19 章（藥品）；第 20–23 章是敷料、器材、失禁與造口用品，不收。
2. 比對：BNF_CHEMICAL_SUBSTANCE 是成分名（鹽類寫在名稱裡），複方寫成「A/B」「A and B」或「Co-xxx (A/B)」（取括號內的成分）。
   成分名拿掉括號內容、鹽類／水合物字樣，得到有效成分（moiety）；英美名統一（paracetamol＝acetaminophen、ciclosporin＝cyclosporine、
   frusemide＝furosemide…）。頁的 drug.inn 同樣處理，有效成分相同就收（含複方代碼）。
   成分欄是類別名（Other single substance preparations、Tars、Polymyxins、Combined ethinylestradiol…）時，改用品項名拆成分；
   品牌品項名沒寫成分時，另看 BNF 碼對應的學名品項（碼 1–9＋AA＋第 14–15 碼兩次）的品項名；
   成分欄是單一成分、但品項名寫了其他成分（「Prilocaine 54mg/Felypressin 0.054units…」「Hydrocortisone 1% / Pramocaine 1% foam」）時，品項名的成分也收。
3. 寫回證據包 tfda：records＝全部比對到的代碼（單方在前），total_matches＝筆數；原紀錄整批換掉。比對結果是空的、但原紀錄的代碼
   仍在現行清單 → 不改這個證據包、列進報告（疑似比對漏掉，要人看）。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--skip-download] [--dry-run] [--report out.tsv] [頁 ...]
"""
import csv
import io
import json
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data/raw"
CSV_FILE = RAW / "nhsbsa_bnf_code_current.csv"
API = "https://opendata.nhsbsa.net/api/3/action/package_show?id=bnf-code-information-current-year"
UA = {"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"}
# 比對結果確認為空的頁（原收集器用品名字串猜成分，原代碼是別的藥；要附依據）
CONFIRMED_EMPTY = {"cysteine": "原代碼是 Cystrin 5mg tablets（oxybutynin，BNF 成分 Oxybutynin），不是 cysteine；BNF 第 1–19 章沒有 cysteine 品項",
                   "xylitol": "原代碼是 Artificial saliva lozenges（BNF 成分欄是類別 Artificial saliva products、品項名沒寫成分），無法證明含 xylitol"}

SALT = (r"hydrochloride|dihydrochloride|hcl|hydrobromide|hbr|besilate|besylate|maleate|mesilate|mesylate|tartrate|bitartrate|fumarate|"
        r"succinate|citrate|acetate|diacetate|propionate|dipropionate|valerate|butyrate|phosphate|sulfate|sulphate|nitrate|lactate|gluconate|"
        r"palmitate|sodium|disodium|potassium|calcium|magnesium|bromide|chloride|iodide|tosilate|tosylate|pamoate|embonate|stearate|"
        r"mandelate|xinafoate|furoate|hyclate|trometamol|meglumine|olamine|erbumine|benzathine|esilate|isetionate|isethionate|mononitrate|"
        r"oxalate|dihydrogen|hydrogen|decanoate|enanthate|cipionate|undecanoate|pivalate|axetil|cilexetil|medoxomil|dimesylate|"
        r"methylbromide|butylbromide|monohydrate|dihydrate|trihydrate|hemihydrate|anhydrous|hydrate|base|micronised|micronized")
SALT_RX = re.compile(r"\b(" + SALT + r")\b")
CANON = [(r"\bparacetamol\b", "acetaminophen"), (r"\bciclosporin\b", "cyclosporine"), (r"\bfrusemide\b", "furosemide"),
         (r"\badrenaline\b", "epinephrine"), (r"\bnoradrenaline\b", "norepinephrine"), (r"\bsalbutamol\b", "albuterol"),
         (r"\bglibenclamide\b", "glyburide"), (r"\blignocaine\b", "lidocaine"), (r"\bsomatotropin\b", "somatropin"),
         (r"\brifampin\b", "rifampicin"), (r"\bacetylsalicylic acid\b", "aspirin"), (r"\bcolecalciferol\b", "cholecalciferol"),
         (r"\bmenotrophin\b", "menotropins"), (r"\bmenotropin\b", "menotropins"), (r"\baluminium\b", "aluminum"),
         (r"\bsimethicone\b", "simeticone"), (r"\bdimethicone\b", "dimeticone"), (r"\bthyroxine\b", "levothyroxine"),
         (r"\bhyoscine\b", "scopolamine"), (r"\bbenzylpenicillin\b", "penicillin g"), (r"\bphenobarbitone\b", "phenobarbital"),
         (r"\bactivated charcoal\b", "charcoal"), (r"\bcharcoal activated\b", "charcoal"), (r"\bglyceryl trinitrate\b", "nitroglycerin"),
         (r"\boestr", "estr"), (r"\bsulph", "sulf"), (r"\bcyclosporin\b", "cyclosporine"), (r"\bamoxycillin\b", "amoxicillin"),
         (r"\bcephalexin\b", "cefalexin"), (r"\bdothiepin\b", "dosulepin"), (r"\bmethotrimeprazine\b", "levomepromazine"),
         (r"\bchlorpheniramine\b", "chlorphenamine"), (r"\bdexchlorpheniramine\b", "dexchlorphenamine"),
         # 2026-11-06 實測：BNF 用英國名（BAN），頁名多是 INN／美國名
         (r"\baciclovir\b", "acyclovir"), (r"\bchlortalidone\b", "chlorthalidone"), (r"\bindometacin\b", "indomethacin"),
         (r"\bmeclozine\b", "meclizine"), (r"\bpericyazine\b", "periciazine"), (r"\bphytomenadione\b", "phylloquinone"),
         (r"\bpodophyllotoxin\b", "podofilox"), (r"\bhydroxycarbamide\b", "hydroxyurea"), (r"\bnicotinic acid\b", "niacin"),
         (r"\bsultiame\b", "sulthiame"), (r"\bflumetasone\b", "flumethasone"), (r"\bdipivefrine\b", "dipivefrin"),
         (r"\bpolyethylene glycol\b", "macrogol"), (r"\bd glucose\b", "glucose"), (r"\bdextrose\b", "glucose"),
         (r"\bracementhol\b", "menthol"), (r"\blevomenthol\b", "menthol"), (r"\bmethyl 5 aminolevulinate\b", "methyl aminolevulinate"),
         (r"\bubiquinone\b", "ubidecarenone"), (r"\bcoenzyme q10\b", "ubidecarenone"), (r"\bphenoxymethylpenicillin\b", "penicillin v")]
# BNF 的「成分」欄有時是類別（Other single substance preparations、Tars、Polymyxins…），這時改用品項名（BNF_PRESENTATION）拆成分
CATEGORY = re.compile(r"\b(other|preparations?|products?|combined|tars|polymyxins|derivatives|agents?|compound)\b", re.I)
FORM = re.compile(r"\b(tablets?|capsules?|cream|ointment|gel|liquid|solution|suspension|powder|drops|eye|ear|nasal|spray|lozenges?|"
                  r"injection|inj|oral|sachets?|granules|mixture|syrup|elixir|paste|lotion|patch(es)?|pessar(y|ies)|suppositor(y|ies)|"
                  r"enema|foam|inhaler|sugar|free|gastro|resistant|modified|release|dispersible|effervescent|chewable|unit|dose|vials?|"
                  r"ampoules?|bottle|tube|including|duty|racemic|strong|light|heavy|npf)\b.*$", re.I)


def norm(x):
    t = str(x or "").lower()
    while re.search(r"\([^()]*\)|\[[^\[\]]*\]", t):
        t = re.sub(r"\([^()]*\)|\[[^\[\]]*\]", " ", t)
    t = " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())
    for a, b in CANON:
        t = re.sub(a, b, t)
    return " ".join(t.split())


def base(t):
    t = re.sub(r"^(l|d|dl)\s+(?=[a-z]{3})", "", t)  # L-lysine、D-glucose
    t = re.sub(r"\s+(k\s*)?\d+$", "", t)  # Macrogol 3350、Povidone K 25
    return " ".join(SALT_RX.sub(" ", t).split()) or t  # 整個名字都是鹽類字（sodium chloride…）→ 保留原名


def keys(c):
    """一個成分的比對鍵：本身；前驅藥字樣（tenofovir disoproxil）另收 moiety；「X oil」另收 X"""
    out = {c}
    m = re.match(r"^(.+?) (disoproxil|alafenamide|oil)$", c)
    if m:
        out.add(m.group(1))
    return out


def from_presentation(pres):
    """品項名（「Coal tar extract 5% / Allantoin 2% cream」）→ 成分：以「 / 」拆開，取劑量數字與劑型字樣之前的字"""
    out = []
    for part in re.split(r" / | with | and ", str(pres or "")):
        w = re.split(r"\d", part, maxsplit=1)[0]
        w = FORM.sub("", norm(w)).strip()
        if len(w) >= 3:
            out.append(base(w))
    return out


def components(sub):
    """BNF 成分名 → 成分清單：「Co-amilofruse (Amiloride hydrochloride/frusemide)」取括號內；「A/B」「A and B」拆開"""
    s = str(sub or "")
    m = re.match(r"\s*co-[\w-]+\s*\(([^()]*)\)", s, re.I)
    if m:
        s = m.group(1)
    ps = re.split(r"/|\band\b|\bwith\b|\+", s, flags=re.I)
    return [p for p in (base(norm(x)) for x in ps) if len(p) >= 3]


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


def load_bnf(download):
    if download:
        res = _get(API).json()["result"]["resources"]
        res = sorted((r for r in res if str(r.get("url", "")).lower().endswith(".csv")), key=lambda r: r["name"])
        if not res:
            raise SystemExit("NHSBSA 資料集沒有 CSV")
        RAW.mkdir(parents=True, exist_ok=True)
        CSV_FILE.write_bytes(_get(res[-1]["url"]).content)
        print("下載", res[-1]["name"])
    rows = list(csv.DictReader(io.StringIO(CSV_FILE.read_bytes().decode("utf-8-sig", "replace"))))
    need = {"BNF_CHAPTER_CODE", "BNF_CHEMICAL_SUBSTANCE", "BNF_PRESENTATION", "BNF_PRESENTATION_CODE"}
    if not rows or not need <= set(rows[0]):
        raise SystemExit(f"NHSBSA 欄位改變（可能拿到 HTML）：{list(rows[0])[:5] if rows else '空檔'}")
    if len(rows) < 20000:
        raise SystemExit(f"NHSBSA 只解析出 {len(rows)} 筆，疑似格式改變")
    return rows


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    rows = load_bnf("--skip-download" not in argv)
    allcodes = {(r.get("BNF_PRESENTATION_CODE") or "").strip() for r in rows}
    prods, by_base = {}, {}
    pres_of = {(r.get("BNF_PRESENTATION_CODE") or "").strip(): r.get("BNF_PRESENTATION") or "" for r in rows}
    for r in rows:
        code = (r.get("BNF_PRESENTATION_CODE") or "").strip()
        ch = (r.get("BNF_CHAPTER_CODE") or "").strip().zfill(2)
        if not code or not ch.isdigit() or int(ch) > 19:
            continue
        sub = r.get("BNF_CHEMICAL_SUBSTANCE") or ""
        pres = from_presentation(re.sub(r"\s*/\s*", " / ", str(r.get("BNF_PRESENTATION") or "")))
        if len(code) == 15 and code[9:11] != "AA":  # 品牌品項（Polyfax、Kalspare…）：再看同成分、同劑量的學名品項名（碼 1–9＋AA＋第 14–15 碼兩次）
            pres += from_presentation(re.sub(r"\s*/\s*", " / ", pres_of.get(code[:9] + "AA" + code[13:15] * 2, "")))
        cs = pres if CATEGORY.search(re.sub(r"\(.*$", "", sub)) else list(dict.fromkeys(components(sub) + pres))
        if not cs:
            continue
        prods[code] = {"r": r, "n": len(cs)}
        for c in cs:
            for k in keys(c):
                by_base.setdefault(k, set()).add(code)
    out, held, n_changed, n_found, n_empty = [], [], 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        key = base(norm(inn))
        hit = set(by_base.get(key, set())) if len(key) >= 3 else set()
        old_ids = sorted({str(x.get("license_id") or "").strip() for x in reg.get("records") or []} - {""})
        old_cur = sorted(set(old_ids) & set(prods))
        if not hit and old_cur and page not in CONFIRMED_EMPTY:
            held.append(page)
            out.append(f"{page}\t{key}\t{reg.get('total_matches')}\t{len(old_ids)}\t-\tHELD\t{';'.join(old_cur[:10])}\t")
            continue
        recs = []
        for code in sorted(hit, key=lambda k: (prods[k]["n"] > 1, prods[k]["r"].get("BNF_PRESENTATION") or "", k)):
            r = prods[code]["r"]
            recs.append({"license_id": code, "brand_name_zh": r.get("BNF_PRESENTATION") or "", "brand_name_en": r.get("BNF_PRESENTATION") or "",
                         "ingredients": r.get("BNF_CHEMICAL_SUBSTANCE") or "", "indication": "", "dosage_form": "", "manufacturer": "",
                         "license_holder": "", "approval_date": "", "expiry_date": "", "status": "",
                         "bnf_product": r.get("BNF_PRODUCT") or "", "bnf_chapter": r.get("BNF_CHAPTER") or "",
                         "kind": "single" if prods[code]["n"] == 1 else "combo",
                         "source": "NHSBSA BNF code information (NHS prescribing codes; not MHRA licences)"})
        new = dict(reg, found=bool(recs), records=recs, total_matches=len(recs),
                   rebuilt="2026-11-06 by ingredient (NHSBSA BNF code information, chapters 1-19)")
        new_ids = [x["license_id"] for x in recs]
        dropped = sorted(set(old_ids) - set(new_ids))
        out.append(f"{page}\t{key}\t{reg.get('total_matches')}\t{len(old_ids)}\t{len(new_ids)}\t{len(dropped)}\t"
                   f"{';'.join(dropped[:15])}{' (not in current list: ' + ';'.join(sorted(set(dropped) - allcodes)) + ')' if set(dropped) - allcodes else ''}\t"
                   f"{';'.join(sorted(set(new_ids) - set(old_ids))[:10])}")
        n_found += bool(recs)
        n_empty += not recs
        if new != reg:
            n_changed += 1
            b["tfda"] = new
            if not dry:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tmatch\told_total_matches\told_records\tnew_records\tdropped\tdropped_ids\tadded_ids\n" + "\n".join(out) + "\n",
                             encoding="utf-8")
    print(f"BNF 第 1–19 章代碼 {len(prods)} 筆；改 {n_changed} 個證據包（有紀錄 {n_found}、查無 {n_empty}、比對落空但原代碼仍在現行清單而保留 {len(held)}）")
    if held:
        print("保留（要人看）：" + ", ".join(held[:40]))


if __name__ == "__main__":
    main(sys.argv[1:])
