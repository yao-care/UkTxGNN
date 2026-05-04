---
layout: default
title: Benzbromarone
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 1
---

# Benzbromarone
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

# Benzbromarone: From Hyperuricaemia/Gout to Renal Hypouricaemia

---

## One-Sentence Summary

Benzbromarone is a uricosuric agent that lowers serum uric acid by inhibiting the URAT1 renal transporter, used in several countries for the treatment of gout and hyperuricaemia, though it holds no current UK marketing authorisation.
The TxGNN model assigns it a near-perfect prediction score of **99.07%** for **Renal Hypouricaemia**, supported by **20 publications** in which benzbromarone features prominently — yet on mechanistic grounds, this prediction is a **false positive**: benzbromarone acts on the very transporter whose loss of function *causes* this disease, making its use in this indication a potential clinical hazard rather than a therapeutic opportunity.
Evidence level is **L5** (model prediction only; no clinical trials; literature references benzbromarone solely as a diagnostic probe, not as a treatment).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout and hyperuricaemia (uricosuric agent; not currently authorised or marketed in the UK) |
| Predicted New Indication | Renal Hypouricaemia |
| TxGNN Prediction Score | 99.07% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## ⚠️ Critical Mechanistic Alert

> **This TxGNN prediction is a clinically significant false positive and must not be pursued.**
>
> Benzbromarone inhibits URAT1 (SLC22A12), the renal urate reabsorption transporter. Renal Hypouricaemia is caused by *loss-of-function mutations in the same URAT1 transporter*, resulting in pathologically low serum uric acid (< 2 mg/dL). Administering benzbromarone to such patients would further suppress whatever residual URAT1 function remains, deepening hypouricaemia and substantially increasing the risk of **exercise-induced acute renal failure (EIARF)** and **urolithiasis** — the very complications that define the morbidity of this condition.

---

## Why This Prediction is Not Clinically Reasonable

Benzbromarone acts as a potent inhibitor of URAT1 (SLC22A12), the organic anion transporter responsible for urate reabsorption in the proximal renal tubule. By blocking this transporter, the drug markedly increases urinary uric acid excretion and lowers serum uric acid concentration. This is precisely why it is effective — and valued — in the treatment of gout and hyperuricaemia, where uric acid is pathologically elevated.

Renal Hypouricaemia is the mirror image of that clinical scenario. It is a hereditary disorder characterised by *defective* URAT1 function (typically due to homozygous or compound heterozygous loss-of-function mutations in SLC22A12), resulting in near-complete failure of tubular urate reabsorption, chronically low serum uric acid, hyperuricosuria, and episodic EIARF — a serious and potentially life-threatening complication. The literature references in this evidence pack uniformly use benzbromarone in a **diagnostic capacity** (the benzbromarone/pyrazinamide suppression test) to classify subtypes of renal hypouricaemia by pharmacological probing of tubular transport, not as a therapeutic agent.

The high TxGNN score (0.9907) reflects a **target-sharing false positive**: the model correctly recognised that both benzbromarone and renal hypouricaemia involve URAT1, but failed to distinguish between *pharmacological inhibition* (the drug's action) and *structural loss of function* (the disease mechanism). These are directionally opposite perturbations of the same pathway. No mechanistic pathway supports a therapeutic benefit; multiple pathways predict harm.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov search: 0 results; ICTRP search: 0 results).

---

## Literature Evidence

The 20 identified publications reference benzbromarone exclusively in the context of **diagnostic tubular function testing** (benzbromarone/pyrazinamide suppression tests to classify renal hypouricaemia subtypes). None evaluate benzbromarone as a treatment for renal hypouricaemia. The ten most informative studies are presented below.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | *Clinical Rheumatology* | Narrative review of hypouricaemia for rheumatologists; covers aetiology, URAT1 mutations, and diagnostic workup |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort/Molecular | *J Am Soc Nephrology* | Largest Japanese cohort (n=32) of idiopathic renal hypouricaemia; establishes SLC22A12 (URAT1) mutations as the primary cause |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case Report | *Am J Kidney Diseases* | Two male siblings with hereditary renal hypouricaemia and recurrent EIARF; illustrates natural history and risk |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Case Series | *Clinical Nephrology* | Patient with ≥4 EIARF episodes; renal biopsy confirmed acute tubular necrosis; conservative management only |
| [9510398](https://pubmed.ncbi.nlm.nih.gov/9510398/) | 1998 | Case Series | *Internal Medicine* | 16 Japanese patients with isolated renal hypouricaemia; benzbromarone used as diagnostic probe to subtype urate transport defect |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Clinical Study | *Nephron* | Uric acid transport analysis in Fanconi syndrome with marked renal hypouricaemia using pyrazinamide and benzbromarone as pharmacological probes |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case Report | *Acta Paediatrica* | Adolescent male with 4 EIARF episodes; benzbromarone/pyrazinamide test localised defect to presecretory tubular site |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case Series | *Journal of Pediatrics* | Four children with hereditary renal hypouricaemia; **benzbromarone did not reduce clearance ratios**, confirming absent presecretory reabsorption |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Clinical Study | *Nephron* | 22-year-old with low serum urate; pyrazinamide failed to suppress urate clearance, **benzbromarone further increased clearance** — consistent with URAT1 loss |
| [9144014](https://pubmed.ncbi.nlm.nih.gov/9144014/) | 1997 | Case Series | *Internal Medicine* | Two cases of renal hypouricaemia with nephrolithiasis; benzbromarone suppression test (BZB increased CUA/Ccr) used to classify transport defect subtype |

---

## UK Market Information

Benzbromarone holds **no current UK marketing authorisation** and is not available on the UK market. It is not listed in the British National Formulary (BNF). No MHRA product licences are held.

> **Note for prescribers:** Benzbromarone was previously available in several European countries as a uricosuric agent for gout but was withdrawn from most EU markets in the early 2000s following reports of severe hepatotoxicity, including fatal fulminant hepatic failure. Any consideration of its use in a research context would require a Specials licence or Named Patient basis and a full hepatic risk assessment.

---

## Safety Considerations

Detailed SmPC warnings and contraindications for benzbromarone are not available in this evidence pack. Please refer to published pharmacovigilance literature and, if applicable, the summary of product characteristics from markets where the drug remains authorised (e.g., Japan, some Asian markets).

Particular attention is warranted regarding:

- **Severe hepatotoxicity:** Benzbromarone has been associated with rare but potentially fatal fulminant hepatic failure, which contributed to its withdrawal from several European markets. Hepatic monitoring is essential in any research context.
- **Mechanism-specific risk in this indication:** As described above, the drug's URAT1-inhibitory mechanism is directly contraindicated in renal hypouricaemia, where further lowering of serum uric acid may precipitate EIARF or urolithiasis.

Report any suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction scores 99.07% due to shared URAT1 pathway involvement, but represents a **mechanistic contraindication** rather than a therapeutic opportunity: benzbromarone inhibits the very transporter whose inherited dysfunction defines renal hypouricaemia. Pursuing this candidate would expose patients to a documented risk of worsening hypouricaemia and its life-threatening sequelae (EIARF, urolithiasis), with no plausible mechanistic pathway to benefit. The 20 publications in the evidence base confirm this: every reference to benzbromarone in this literature is as a **diagnostic probe**, not a therapeutic agent.

**This case should be flagged to the TxGNN model development team as a confirmed target-sharing false positive, to inform model refinement.**

**To proceed with any future work in this disease area, the following would be needed:**

- Identification of alternative therapeutic targets in renal hypouricaemia (e.g., reduction of oxidative stress associated with xanthine, prophylaxis of EIARF via hydration protocols, or alkalisation of urine to prevent uric acid urolithiasis)
- A systematic review of interventions studied for EIARF prevention in URAT1-deficient patients
- Engagement with specialist renal genetics services, given the rarity and hereditary nature of renal hypouricaemia
- Clarification of benzbromarone's current regulatory status in the UK before any research use, given the historical hepatotoxicity concerns

---

*This report is intended for research purposes only and does not constitute clinical advice. Drug repurposing candidates require prospective clinical validation before any application in patient care. Produced using TxGNN evidence pack v4, data cut-off 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

