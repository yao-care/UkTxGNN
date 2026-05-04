---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 6
---

# Certolizumab Pegol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Certolizumab Pegol: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Certolizumab pegol (Cimzia®) is a PEGylated anti-TNF-α biological agent with established efficacy across rheumatoid arthritis, axial spondyloarthritis, psoriatic arthritis, and Crohn's disease.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** — a rare and severe extra-articular complication of rheumatoid arthritis — with a prediction confidence of **99.78%**.
However, current supporting evidence consists of only **3 peripherally related clinical trials** and **no directly relevant published literature**, placing this prediction at an early mechanistic hypothesis stage (L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis, axial spondyloarthritis, psoriatic arthritis, Crohn's disease (based on published evidence; UK regulatory data not retrieved — see below) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| UK Market Status | No marketing authorisation recorded in system (data gap likely — see UK Market Information) |
| Number of Marketing Authorisations | 0 recorded |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published information, certolizumab pegol is a PEGylated Fab' fragment of a recombinant humanised monoclonal antibody that selectively neutralises both soluble and membrane-bound TNF-α. Three structurally distinctive features carry particular clinical relevance: it lacks an Fc region (which prevents complement-dependent cytotoxicity and antibody-dependent cellular toxicity); its PEGylated architecture enhances penetration into chronically inflamed tissues; and it demonstrates negligible placental transfer (neonatal plasma levels <3 µg/mL), establishing it as the preferred TNF inhibitor for women of childbearing potential among the approved agents in this class.

Rheumatoid vasculitis (RV) develops in fewer than 1% of patients with long-standing, seropositive rheumatoid arthritis. Its core pathology involves immune complex deposition in small-to-medium vessel walls, complement activation, and local TNF-α–driven inflammation leading to vascular occlusion and ischaemic tissue injury. Since TNF-α is the shared upstream driver of both RA-related joint destruction and RV-associated vascular injury, the mechanistic rationale for applying an anti-TNF agent to RV is theoretically coherent and internally consistent with the drug's known mode of action.

The TxGNN model's high-confidence prediction reflects this biological plausibility: RV is a direct complication of RA, the primary disease for which certolizumab pegol is approved, and the knowledge graph is likely identifying the overlap of inflammatory nodes between these two phenotypes. Anti-TNF agents as a class have been used off-label in severe, refractory RV — generally in combination with corticosteroids and cyclophosphamide — based on case reports and expert consensus rather than controlled trial evidence. The principal limitation is the complete absence of prospectively designed, RV-specific clinical trials for any anti-TNF agent, which reflects both the rarity of the condition and the practical difficulties of enrolment at adequate scale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | Observational | Completed | 184 | Non-interventional study of tocilizumab (not certolizumab pegol) in RA patients with inadequate DMARD or biologic response; no rheumatoid vasculitis sub-group; observational design with no active comparator — results cannot be extrapolated to RV |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | Observational | Unknown | 750,000 | Large pharmacovigilance study assessing risk of incident immune-mediated inflammatory diseases (IMIDs) in patients on biologics or immunosuppressants; evaluates safety signal rather than RV therapeutic efficacy; status uncertain |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing elective shoulder arthroplasty; compares discontinuation durations prior to surgery; no relevance to rheumatoid vasculitis treatment outcomes |

> **Note:** None of the identified trials was designed to evaluate certolizumab pegol specifically in rheumatoid vasculitis; all three received a Grade C relevance rating. No ISRCTN or EU Clinical Trials Register (EU CTR) entries were identified for this indication.

---

## Literature Evidence

Currently no related literature directly evaluating certolizumab pegol in rheumatoid vasculitis is available. The PubMed search returned 0 results for this drug–disease combination.

---

## UK Market Information

No MHRA marketing authorisation records for certolizumab pegol were retrieved by this system (0 licences recorded; market status recorded as not marketed). This is very likely a **data gap within the current system** — Cimzia® (certolizumab pegol; UCB Pharma S.A.) is understood to hold MHRA marketing authorisation for multiple inflammatory indications in the United Kingdom, with entries in the BNF under immune system / biological medicines / anti-TNF agents.

Clinicians should verify the current authorisation status and all approved indications via:
- [MHRA Products Licence Database](https://products.mhra.gov.uk/)
- [Electronic Medicines Compendium (eMC) — Cimzia® SmPC](https://www.medicines.org.uk/emc/)
- British National Formulary (BNF) — Biologicals / Tumour necrosis factor alpha inhibitors

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for certolizumab pegol in rheumatoid vasculitis is theoretically sound — RV shares the TNF-α–driven inflammatory driver of RA — but the direct evidence base currently stands at Level 4 (mechanistic plausibility only). No clinical trials have been specifically designed for this indication, no published literature directly evaluates it, and the extreme rarity of RV (<1% of RA patients) makes prospective enrolment logistically demanding. This prediction represents a research hypothesis that requires further investigative work before any clinical development or commissioning decision can be made.

**To proceed, the following is needed:**
- Systematic review of published case reports and case series evaluating anti-TNF agents as a class in rheumatoid vasculitis, to establish whether class-level evidence is sufficient to justify a further step
- Retrospective analysis of the BSRBR-RA (British Society for Rheumatology Biologics Register for Rheumatoid Arthritis) to identify RV events and clinical outcomes in patients treated with certolizumab pegol
- Formal retrieval and review of the Cimzia® MHRA-approved SmPC to document existing labelled warnings, contraindications, and any off-label use guidance relevant to vasculitic presentations
- DrugBank API query (DB08904) to formally document the TNF-α inhibition mechanism of action and support the mechanistic justification section
- Expert opinion from British Society for Rheumatology (BSR) / British Health Professionals in Rheumatology (BHPR) on current clinical practice for anti-TNF use in immunosuppressant-refractory rheumatoid vasculitis

> **Note on other TxGNN predictions:** The same Evidence Pack identifies **Inflammatory Spondylopathy** (rank 3, L1 evidence, 99.73% confidence) and **Vertebral Disease** (rank 6, L1 evidence, 99.26% confidence) as high-confidence predictions supported by multiple completed Phase 3 RCTs and systematic reviews. These indications — encompassing axial spondyloarthritis and ankylosing spondylitis — may warrant separate evaluation reports with a "Proceed with Guardrails" recommendation, given the substantially more mature evidence base available.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

