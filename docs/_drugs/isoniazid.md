---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 1
---

# Isoniazid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line antitubercular agent, established practice for tuberculosis. The TxGNN model predicts it may be relevant to **Conjunctivitis**, but supporting evidence is thin: **1 clinical trial** (not directly testing this indication) and **20 historical publications**, most describing tuberculosis-associated eye disease rather than a direct treatment trial for conjunctivitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (established clinical use; no formal marketing-authorisation indication text on file in this dataset) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap). Based on established pharmacological knowledge, isoniazid is a prodrug activated by mycobacterial catalase-peroxidase (KatG), which inhibits mycolic acid synthesis in *Mycobacterium tuberculosis*; its efficacy in tuberculosis is well proven.

The link to conjunctivitis in the evidence base is not a direct antimicrobial or anti-inflammatory action on the eye itself. Instead, the literature consistently points to **phlyctenular keratoconjunctivitis** and other conjunctival manifestations that occur as a **hypersensitivity reaction to tuberculoprotein**, secondary to underlying (often latent or unrecognised) tuberculosis infection. In this context, isoniazid resolves the conjunctivitis indirectly, by treating the causative tuberculous infection rather than by a distinct ocular mechanism.

This distinction matters clinically: the prediction should be interpreted as "isoniazid may resolve conjunctivitis of tuberculous aetiology," not "isoniazid is a general treatment for conjunctivitis." The one included clinical trial (NCT04094012) does not test this indication at all — it compares isoniazid-containing regimens for latent TB infection safety/tolerability, and was likely surfaced because it involves isoniazid, not because it studies conjunctivitis outcomes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic drug reaction rates between 3-month weekly (3HP) and 1-month daily (1HP) isoniazid + rifapentine regimens for latent tuberculosis infection. Addresses isoniazid safety/tolerability, **not** a conjunctivitis outcome. |

No trial in this evidence pack directly evaluates isoniazid for treatment of conjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Field/Prophylaxis study | Am Rev Respir Dis | Isoniazid prophylaxis studied in a population with phlyctenular keratoconjunctivitis linked to TB exposure (Alaska Eskimo cohort) |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case series | Annales d'oculistique | Local (topical) use of isoniazid reported in treatment of ocular tuberculosis |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Review/Commentary | Can J Ophthalmol | Highlights conjunctival phlyctenulosis as a presenting sign of impending clinical tuberculosis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous phlyctenular keratoconjunctivitis, mostly paediatric, linked to primary TB |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Paediatric sinonasal TB presenting with phlyctenular keratoconjunctivitis |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case report | Cornea | *M. tuberculosis* presenting as chronic red eye (conjunctival TB) |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket following prior miliary TB |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva |
| [4233886](https://pubmed.ncbi.nlm.nih.gov/4233886/) | 1968 | Case report | Arch Ophtalmol | Tuberculosis of the bulbar conjunctiva |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case report | Clin Pediatr | Unusual paediatric conjunctivitis case with a tuberculous cause |

*Note: study-type classification for these records was still "pending" in the source evidence pack; types above are inferred from titles/context and should be verified.* Several additional retrieved records (e.g. BCG-induced polyarthritis reports, a Munchausen syndrome case, a rifampicin monograph) were excluded as not materially relevant to this indication.

---

## UK Market Information

Isoniazid currently has **no marketing authorisation on file** in this jurisdiction (0 licences; market status: not marketed). No product-level licence, dosage form, or approved-indication text is available to report.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: a Blocking data gap exists for local SmPC/label warnings and contraindications, and drug interaction data returned no results — safety information cannot be independently verified from this evidence pack.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap on label warnings/contraindications means safety cannot be assessed at all, the mechanism-of-action record is missing, the drug is not currently marketed in this jurisdiction, and the clinical/literature evidence for "conjunctivitis" is essentially all historical case reports of TB-associated eye disease rather than trials of isoniazid for conjunctivitis itself.

**To proceed, the following is needed:**
- Official SmPC/PIL warnings and contraindications (resolve DG001, Blocking)
- Confirmed mechanism of action from DrugBank (resolve DG002)
- Clarification of the true target population — this signal appears specific to **tuberculosis-associated phlyctenular keratoconjunctivitis**, not conjunctivitis in general — before any indication framing is used
- A regulatory pathway assessment, given isoniazid holds no current marketing authorisation in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

