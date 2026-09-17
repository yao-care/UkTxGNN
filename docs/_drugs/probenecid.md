---
layout: default
title: Probenecid
parent: Moderate Evidence (L3-L4)
nav_order: 483
evidence_level: L4
indication_count: 3
---

# Probenecid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using the evidence pack as provided. Note: all three TxGNN predictions for Probenecid carry a **Hold** recommendation with an explicitly flagged mechanistic contradiction — I've kept that assessment intact rather than softening it.

---

# Probenecid: From Gout and Hyperuricaemia to Renal Hypouricemia

## One-Sentence Summary

Probenecid is a uricosuric agent traditionally used to treat gout and hyperuricaemia by increasing renal excretion of uric acid. TxGNN predicts a possible link to **Renal Hypouricemia**, but this appears to be a mechanistic false positive: probenecid increases urate excretion, while renal hypouricemia is itself caused by pathologically *excessive* urate excretion. No clinical trials support this indication, and the **20 available publications** are almost entirely historical case reports describing probenecid's use as a diagnostic challenge agent, not as a treatment.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout and hyperuricaemia (uricosuric agent) — inferred from the repurposing rationale text; no UK marketing authorisation data is available to confirm exact licensed wording |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for probenecid is not available in this evidence pack ([Data Gap]). However, the repurposing rationale provided alongside the prediction describes probenecid's known pharmacology: it is a **uricosuric agent** that inhibits renal tubular reabsorption of uric acid via **URAT1 blockade**, thereby *increasing* urinary uric acid excretion. This is the established basis for its use in gout and hyperuricaemia.

Renal hypouricemia, the predicted new indication, has the opposite pathophysiology: it is caused by loss-of-function mutations in *SLC22A12* (URAT1), leading to *excessive* renal urate loss and low serum uric acid. A drug that further promotes urate excretion would be expected to worsen rather than correct this condition. The pharmacological direction of probenecid is therefore mechanistically inconsistent with the proposed indication.

Consistent with this, the literature associated with this prediction does not describe probenecid as a treatment for renal hypouricemia. Instead, probenecid appears repeatedly as part of the **"uricosuric challenge test"** (typically paired with pyrazinamide), a diagnostic tool used to subtype renal hypouricemia (pre-secretory vs post-secretory reabsorption defects), not as a therapeutic intervention. The high TxGNN score most likely reflects shared knowledge-graph nodes around uric acid transport pathways rather than a genuine treat-relationship, and should be treated as a probable **false positive**.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia aetiology and classification for rheumatologists; does not describe probenecid as treatment |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort (molecular analysis) | J Am Soc Nephrol | Molecular/clinical analysis of SLC22A12 (URAT1) mutations in 32 Japanese renal hypouricemia patients |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | Overview of hereditary renal hypouricemia (HRH) caused by URAT1 loss-of-function mutations |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report | Nephron | Patient with renal hypouricemia showed **no response** to probenecid or pyrazinamide — a novel combined secretion/reabsorption defect |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report | Nephron | Familial renal hypouricemia case where urate excretion **paradoxically decreased** after probenecid administration |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Familial hypouricemia with attenuated (not therapeutic) uric acid clearance response to probenecid and pyrazinamide challenge |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report + Review | Am J Kidney Dis | Case of exercise-induced acute renal failure in renal hypouricemia; reviews prevention strategies (not probenecid treatment) |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case series | Arch Intern Med | Seven diabetic patients with renal hypouricemia; probenecid used diagnostically (pyrazinamide-suppressible clearance) |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | Two siblings with hereditary renal hypouricemia and exercise-induced acute renal failure |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Case series | Nephron | 14 Type 1 diabetic patients studied for uricosuric mechanisms of renal hypouricemia |

## UK Market Information

Probenecid currently holds **no marketing authorisation in the UK** (market status: Not marketed; total licences: 0). No product-level data is available to populate a licence table.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Note on Additional TxGNN Predictions

Two further TxGNN predictions for probenecid were reviewed and show the **same contradictory pattern**:

- **Lesch-Nyhan syndrome** (score 99.39%, L4) — a uric acid *overproduction* disorder normally managed with xanthine oxidase inhibitors; a uricosuric agent would be expected to increase urolithiasis/uric acid nephropathy risk. Supporting literature dates from 1968–1976 and is not treatment-focused.
- **HGPRT partial deficiency (Kelley-Seegmiller syndrome)** (score 99.37%, L5) — same overproduction pathophysiology as above, with **no literature or clinical trial support at all**; the prediction reflects knowledge-graph proximity to Lesch-Nyhan and hyperuricemia nodes rather than any evidence base.

Both were independently scored **Hold**, reinforcing the overall conclusion that probenecid's uricosuric mechanism is directionally incompatible with all three top-ranked predicted indications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication's pathophysiology (excessive renal urate loss) is mechanistically opposite to probenecid's pharmacological action (promoting urate excretion). No clinical trials exist, and all literature evidence relates to diagnostic use of probenecid, not therapeutic use. This pattern is repeated across all three top TxGNN predictions for this drug.

**To proceed, the following is needed:**
- MHRA/SmPC-level safety data (key warnings, contraindications) — currently flagged as a **Blocking** data gap (DG001), preventing S1 safety evaluation
- Confirmed mechanism-of-action documentation (DG002 — High severity)
- A pharmacological reassessment specifically addressing whether the uricosuric mechanism could be therapeutically reframed (e.g., adjunctive diagnostic use) rather than treated as a direct repurposing candidate
- If reconsidered, non-clinical/mechanistic studies to resolve the directional conflict identified above before any further clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

