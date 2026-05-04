---
layout: default
title: Cefixime
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Cefixime
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Cefixime: From Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Cefixime is a third-generation oral cephalosporin antibiotic used to treat a range of bacterial infections, including urinary and respiratory tract infections.
The TxGNN model predicts it may be effective for **Gonococcal Urethritis** — urethral infection caused by *Neisseria gonorrhoeae* —
with **2 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK marketing authorisation data available in this dataset |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L1 |
| UK Market Status | Not marketed (no MHRA licence on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cefixime is a third-generation oral cephalosporin that exerts its antibacterial effect by binding to penicillin-binding proteins (PBPs) in the bacterial cell wall, thereby inhibiting cell wall synthesis and ultimately causing bacterial lysis. Of particular relevance here is its exceptionally high affinity for PBP3 in *Neisseria gonorrhoeae*, the causative pathogen of gonococcal urethritis — a direct mechanistic basis for the TxGNN model's prediction.

Historically, this mechanism translated clearly into clinical practice: both WHO and CDC gonorrhoea treatment guidelines recommended cefixime 400 mg as a single oral dose for first-line management of uncomplicated gonococcal urethritis, and direct RCT evidence (PMID 2183719, PMID 1534422) confirmed microbiological eradication rates of 96–97% in male urethritis. A dose-optimisation study (PMID 12673405) further demonstrated that maintaining drug concentrations above four times the MIC for at least 10 hours was a key determinant of eradication, supporting the pharmacodynamic rationale.

The clinical landscape has, however, shifted significantly. Rising cefixime MICs (≥0.25 μg/mL) and documented treatment failures across Europe, North America, and Asia — including a landmark JAMA cohort study from Toronto (PMID 23299608) — have led current guidelines, including those of BASHH and UKHSA, to recommend intramuscular ceftriaxone as the preferred first-line agent, with oral cefixime retained only where parenteral therapy is not feasible. Any clinical application of this prediction must therefore be conditional on current local resistance surveillance data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03840811](https://clinicaltrials.gov/study/NCT03840811) | Phase 1 | Completed | 27 | Experimental urethral infection model in healthy adult males using isogenic *N. gonorrhoeae* mutants; designed to characterise gonococcal virulence determinants. Provides mechanistic insights into urethral infection biology but does not assess cefixime efficacy directly. |
| [NCT05294588](https://clinicaltrials.gov/study/NCT05294588) | Phase 2 | Completed | 65 | Double-blind RCT evaluating cross-protection from the 4C-MenB (Bexsero) meningococcal B vaccine against experimental *N. gonorrhoeae* urethral infection. An immunological study; not a cefixime treatment trial. |

> **Note**: Neither registered trial directly evaluates cefixime as a treatment. The primary clinical evidence base for this indication resides in the published literature — including the landmark RCT by Megran et al. (PMID 2183719, 1990) and the dose-optimisation trial by Deguchi et al. (PMID 12673405, 2003) — which together underpin the L1 evidence classification.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1534422](https://pubmed.ncbi.nlm.nih.gov/1534422/) | 1992 | RCT | Sexually Transmitted Diseases | Cefixime 400 mg or 800 mg single oral dose vs ceftriaxone 250 mg IM in 155 evaluable patients; bacteriological eradication in 97% of cefixime-treated cases, comparable to ceftriaxone. Core efficacy evidence. |
| [12673405](https://pubmed.ncbi.nlm.nih.gov/12673405/) | 2003 | Clinical Trial | J Infect Chemother | Double-dosing strategy (200 mg × 2 at 6-hour intervals) for gonococcal urethritis; demonstrates that maintaining serum concentrations >4× MIC for ≥10 hours optimises eradication, providing pharmacodynamic rationale for dosing regimens. |
| [23299608](https://pubmed.ncbi.nlm.nih.gov/23299608/) | 2013 | Cohort Study | JAMA | Documents cefixime treatment failures in Toronto associated with rising MICs; critical safety signal that shifted international guidelines away from cefixime as first-line therapy. |
| [17106672](https://pubmed.ncbi.nlm.nih.gov/17106672/) | 2006 | Review | Der Urologe | Comprehensive review of gonorrhoea; notes cefixime single-dose as a standard treatment option in Central Europe, covering transmission, clinical presentation, and management. |
| [20353145](https://pubmed.ncbi.nlm.nih.gov/20353145/) | 2010 | Clinical Review | American Family Physician | Diagnosis and treatment of urethritis in men; discusses cefixime as a CDC-recommended agent for gonococcal urethritis and outlines diagnostic criteria. |
| [36505551](https://pubmed.ncbi.nlm.nih.gov/36505551/) | 2022 | Observational Study | J Family Med Prim Care | Cross-sectional study characterising *N. gonorrhoeae* and *C. trachomatis* in men with urethritis; includes antimicrobial susceptibility profiling of gonococcal isolates. |
| [25410409](https://pubmed.ncbi.nlm.nih.gov/25410409/) | 2015 | Review | Current Drug Targets | Longitudinal analysis of *N. gonorrhoeae* susceptibility to cefixime from the 1980s to 2010s; documents the progressive decline in susceptibility rates and emerging resistance mechanisms. |
| [20643433](https://pubmed.ncbi.nlm.nih.gov/20643433/) | 2010 | Review | J Urology | Reviews the emergence and global spread of drug-resistant *N. gonorrhoeae*, with specific focus on cefixime and fluoroquinolone resistance. |
| [34475363](https://pubmed.ncbi.nlm.nih.gov/34475363/) | 2021 | Surveillance Study | Sexually Transmitted Diseases | US GISP/SURRG data on gonococcal antimicrobial susceptibility by anatomical site among men who have sex with men, 2018–2019; relevant to broader resistance monitoring. |
| [39034819](https://pubmed.ncbi.nlm.nih.gov/39034819/) | 2024 | Cross-sectional Study | Annals of Laboratory Medicine | Prevalence and molecular characterisation of pharyngeal gonorrhoea in Korean men with urethritis; includes antimicrobial susceptibility data for contemporary isolates. |

---

## UK Market Information

No MHRA marketing authorisations for cefixime are recorded in this dataset.

> **Note for UK prescribers**: Cefixime is referenced in the BNF (section 5.1.2 — Cephalosporins) and has historically appeared in BASHH and UKHSA gonorrhoea treatment guidelines as an oral alternative agent. The absence of licensing records in this dataset may reflect incomplete regulatory data capture rather than the drug's true market status. Prescribers should verify current availability via the MHRA Product Licence Register and consult up-to-date BASHH gonorrhoea management guidelines before clinical use.

---

## Safety Considerations

Formal SmPC data — including key warnings, contraindications, and drug–drug interactions — were not available in this evidence pack.

> Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

**Safety signal from literature**: One case report (PMID 35860067) documents cefixime-induced Stevens-Johnson Syndrome — a rare but potentially life-threatening mucocutaneous hypersensitivity reaction. This aligns with the known class risk for beta-lactam antibiotics and warrants standard allergy screening prior to prescribing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs and international clinical guidelines have established cefixime's efficacy against *N. gonorrhoeae*, supporting its role as an oral alternative for uncomplicated gonococcal urethritis; however, well-documented antimicrobial resistance — including verified treatment failures — means its use must be strictly contingent on local susceptibility data and current BASHH/UKHSA guideline alignment.

**To proceed, the following is needed:**

- **Local resistance surveillance data**: Obtain current *N. gonorrhoeae* cefixime MIC distribution for the target population; do not use empirically if the local cefixime resistance rate exceeds acceptable thresholds
- **Guideline alignment check**: Confirm that the intended use pathway is consistent with current BASHH gonorrhoea management guidelines and any UKHSA/NICE position statements
- **UK regulatory status clarification**: Verify MHRA authorisation status; if use would be off-label, document the clinical rationale and obtain appropriate governance approval
- **Full safety review**: Obtain the SmPC to assess contraindications, warnings, and drug interactions — particularly relevant for patients on anticoagulants or with renal impairment, where cephalosporin dosing adjustments may be required
- **Formal MOA documentation**: Retrieve DrugBank pharmacodynamic data to complete the mechanistic dossier and confirm PBP-binding profile

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application in patient care.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

