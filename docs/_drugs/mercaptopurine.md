---
layout: default
title: Mercaptopurine
parent: High Evidence (L1-L2)
nav_order: 365
evidence_level: L1
indication_count: 10
---

# Mercaptopurine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

Using the report already-specified template directly (no additional coding/debugging skill applies here — this is a content-generation task matching the system prompt's own detailed spec).

# Mercaptopurine: From Acute Lymphoblastic Leukaemia (established use) to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine is a thiopurine antimetabolite long established as a backbone maintenance agent for acute lymphoblastic leukaemia (ALL); this dataset does not hold a formal UK-licensed indication record for it.
The TxGNN model predicts it may be effective for **Myeloid Leukemia (AML/APL)**,
with **28 clinical trials** and **20 publications** currently associated with this direction, several of which already use mercaptopurine directly within AML/APL maintenance regimens.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded as a licensed UK indication in this dataset; internationally recognised standard use is maintenance therapy for acute lymphoblastic leukaemia (ALL) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| UK Market Status | Not marketed (no licence on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, mercaptopurine is a purine antimetabolite (thiopurine class) that is incorporated into DNA as thioguanine nucleotides, disrupting purine synthesis and halting proliferation of rapidly dividing haematopoietic cells. Its efficacy as a maintenance-phase agent in acute lymphoblastic leukaemia is well proven.

Myeloid and lymphoid leukaemias share the same underlying vulnerability — malignant clones with high proliferative turnover that are sensitive to antimetabolite interference with nucleotide synthesis. Notably, this is not a purely theoretical extrapolation: several completed Phase 3 trials in the evidence pack (e.g. NCT00003934, NCT00599937, NCT00866918, NCT02688140, NCT00482833) already incorporate mercaptopurine directly into ATRA-based maintenance regimens for acute promyelocytic leukaemia (APL), a recognised subtype of AML. This existing, evidence-based practice substantially strengthens the mechanistic plausibility of the TxGNN prediction for myeloid leukaemia more broadly.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Tretinoin + chemotherapy ± arsenic trioxide as consolidation, then maintenance with intermittent tretinoin ± mercaptopurine/methotrexate, in untreated APL |
| [NCT00599937](https://clinicaltrials.gov/study/NCT00599937) | Phase 3 | Completed | 576 | Assessed optimal timing of chemotherapy with/after ATRA and role of maintenance therapy in APL |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | Completed | 106 | Risk-adapted therapy with arsenic trioxide during consolidation for newly diagnosed childhood APL |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | Completed | 135 | ATO + ATRA + idarubicin vs standard AIDA regimen in high-risk APL |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | Completed | 276 | ATO + ATRA vs standard ATRA/anthracycline (AIDA) in non-high-risk APL |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Phase 3 | Completed | 168 | Two-dose gemtuzumab ozogamicin vs 2-year ATRA + chemotherapy maintenance in intermediate/high-risk APL |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | S0521: maintenance vs observation in previously untreated low/intermediate-risk APL |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Phase 3 | Completed | 330 | Addition of androgen therapy during post-remission maintenance in elderly AML (GOELAMS SA-2002) |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Completed | 238 | Comparison of two multi-agent chemotherapy regimens with different cytarabine dosing in newly diagnosed AML/MDS |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea + valproic acid, or 6-mercaptopurine + valproic acid, in AML/HR-MDS patients unfit for standard induction |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Clinical study | J Korean Med Sci | Oral maintenance chemotherapy with daily 6-MP and weekly methotrexate improved leukaemia-free survival in transplant-ineligible AML |
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematol | JALSG-AML92: randomised trial found no benefit from adding etoposide to daunorubicin/cytarabine/6-MP induction in adult AML |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemother Pharmacol | Nationwide randomised comparison of daunorubicin vs aclarubicin combined with BHAC, 6-MP and prednisolone in untreated AML |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | RCT | J Clin Oncol | Japan Leukemia Study Group randomised trials of BHAC vs cytarabine (± ubenimex) in induction/consolidation/maintenance AML |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Pilot study | Cancer Invest | High-dose continuous IV 6-MP plus intermediate-dose cytarabine explored as first-remission consolidation in childhood AML |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Cohort study | Int J Hematol | Intensive individualised induction with BHAC, daunorubicin and 6-MP achieved 71% CR in adult AML |
| [1657335](https://pubmed.ncbi.nlm.nih.gov/1657335/) | 1991 | Cohort study | Chin Med J (Free China) | Cytarabine, daunorubicin and 6-MP induction/consolidation in 34 adult AML patients |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Review | Rinsho Ketsueki | Overview of current therapy for AML and APL (Japanese) |
| [4518586](https://pubmed.ncbi.nlm.nih.gov/4518586/) | 1973 | Cohort study | Cancer | Cytarabine in combination with 6-MP for adult AML |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Case series | Blood | Sequential subcutaneous cytarabine and oral mercaptopurine showed haematologic response in juvenile chronic myeloid leukaemia |

## UK Market Information

No UK marketing authorisation is currently on record for mercaptopurine in this dataset (`total_licenses = 0`). Any clinical use in AML/myeloid leukaemia would currently require access via an alternative licensed product, import, or off-label prescribing under specialist supervision, subject to MHRA and local Trust governance.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (thiopurine/purine antimetabolite) |
| Myelosuppression Risk | High — dose-limiting toxicity; markedly increased in patients with TPMT or NUDT15 genetic variants, per literature evidence in this evidence pack |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (with differential), liver function tests, renal function; consider TPMT/NUDT15 genotype or phenotype testing before/during therapy |
| Handling Protection | Cytotoxic drug handling precautions apply per local Trust policy, even though oral administration is typical |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Supplementary note from literature evidence (not formal safety labelling data):* multiple studies in this evidence pack indicate substantial interindividual variability in mercaptopurine-related myelosuppression and hepatotoxicity linked to TPMT and NUDT15 polymorphisms — this is a recognised prescribing consideration but should be confirmed against the current SmPC.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by numerous completed Phase 3 RCTs, several of which already use mercaptopurine directly within AML/APL maintenance regimens, giving strong mechanistic and clinical plausibility. However, a Blocking data gap (MHRA/SmPC warnings and contraindications not available) prevents completion of the initial safety review (S1), so this cannot yet be treated as a cleared repurposing candidate.

**To proceed, the following is needed:**
- MHRA-approved SmPC/PIL data (key warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Clarification of the original UK-licensed indication and dosage form(s), since no licences are currently on record
- A pharmacogenomic (TPMT/NUDT15) testing protocol as part of any myeloid leukaemia treatment pathway
- Route-of-administration compatibility check against required routes for myeloid leukaemia treatment settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

