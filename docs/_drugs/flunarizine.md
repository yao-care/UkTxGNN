---
layout: default
title: Flunarizine
parent: Model Prediction Only (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Flunarizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Flunarizine: From Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Flunarizine is a calcium channel blocker marketed in the UK as a 5 mg capsule. The data compiled for this report do not specify its original licensed indication.
The TxGNN model predicts it may be effective for **migraine disorder**, supported by **13 registered clinical trials** and **20 publications**. Migraine prophylaxis is already an established use of flunarizine in many countries, so this is better read as a confirmation of an existing use than as a genuinely new one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 (as assigned in the compiled data; see the note under Clinical Trial Evidence) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available. From the data compiled for this report, flunarizine is a non-selective calcium channel blocker with additional antihistaminic and dopamine D2 antagonist activity. Pharmacology records also show activity at T-type calcium channels (Cav3.1, Cav3.2 and Cav3.3) and the D2 receptor.

Blocking neuronal calcium entry and reducing cortical spreading depression are plausible explanations for its migraine-preventive effect. Flunarizine is already recommended as a prophylactic agent in many guidelines outside the US, and a 2023 European Headache Federation meta-analysis describes it as a repurposed first- or second-line option for migraine prophylaxis.

The "repurposing" label here mainly reflects a gap in the original-indication data, not a new therapeutic use.

Other predictions in the list are weaker:
- **Headache disorder** and **migraine with or without aura, susceptibility to** largely duplicate the migraine evidence and are not independent signals.
- **Migraine with brainstem aura** and **trigeminal autonomic cephalalgia** are plausible, but supported only by case reports and reviews (research questions).
- **Nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata, ulerythema ophryogenesis, common cold and insomnia** have no supporting evidence, and some have no plausible mechanism (Hold).

---

## Clinical Trial Evidence

Flunarizine is generally a comparator or one of several arms in these trials, so the table lists the most relevant ones.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not yet recruiting | 460 | PREMI: pragmatic comparison of amitriptyline, flunarizine, topiramate and propranolol for first-line migraine prevention in primary care |
| [NCT07655700](https://clinicaltrials.gov/study/NCT07655700) | Phase 4 | Not yet recruiting | 177 | Propranolol vs flunarizine vs combination for migraine prophylaxis |
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Flunarizine 10 mg/day vs topiramate 50 mg/day for chronic migraine prophylaxis |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completed | 120 | Greater occipital nerve block vs topiramate vs flunarizine in episodic migraine |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Unknown | 84 | Flunarizine vs amitriptyline: attack frequency and pain score |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Recruiting | 44 | Flunarizine vs propranolol in children aged 8-15 (PedMIDAS) |
| [NCT07751497](https://clinicaltrials.gov/study/NCT07751497) | Phase 2 | Not yet recruiting | 400 | Rimegepant vs flunarizine non-inferiority for vestibular migraine prevention |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | N/A | Active, not recruiting | 60 | Transcutaneous pulsed radiofrequency vs calcium channel blockers in childhood migraine |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Pharmacokinetic interaction study of flunarizine and topiramate (safety/DDI, not efficacy) |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | Unknown | 96 | Acupuncture for migraine without aura; flunarizine is the usual-care comparator |

**Note on evidence level:** The compiled data assign L1, but the only completed trials listed are small or non-Phase 3 studies, and none of them is a completed Phase 3 RCT. L1 is therefore supported mainly by the published systematic reviews and meta-analyses below, and should be read with caution.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Meta-analysis | J Headache Pain | European Headache Federation systematic review and meta-analysis of flunarizine's efficacy in migraine prophylaxis |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic review | Health Technol Assess | Preventive drugs for chronic migraine in adults, with economic modelling |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network meta-analysis | JAMA Netw Open | Preventive medications in paediatric migraine |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Meta-analysis | J Assoc Physicians India | Amitriptyline vs propranolol and flunarizine for migraine prophylaxis |
| [37073858](https://pubmed.ncbi.nlm.nih.gov/37073858/) | 2023 | Systematic review | Cochrane Database Syst Rev | Pharmacological prophylaxis of vestibular migraine |
| [42673559](https://pubmed.ncbi.nlm.nih.gov/42673559/) | 2026 | Systematic review | Neurology | AAN/AHS systematic review of pharmacologic migraine prevention in adults |
| [1769820](https://pubmed.ncbi.nlm.nih.gov/1769820/) | 1991 | RCT | Headache | Double-blind trial in 149 patients: flunarizine 10 mg and metoprolol 200 mg each reduced migraine days by 37% |
| [12390610](https://pubmed.ncbi.nlm.nih.gov/12390610/) | 2002 | RCT | Headache | Acupuncture compared with flunarizine for prophylaxis of migraine without aura over 6 months |
| [22268377](https://pubmed.ncbi.nlm.nih.gov/22268377/) | 2012 | Case series | Dev Med Child Neurol | 11 years' experience of flunarizine in childhood migraine, including hemiplegic migraine |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Guideline | Neurology | AAN/AHS update on paediatric migraine prevention |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000E0AAAAAA | Flunarizine HCl capsules 5 mg | Capsule | Not stated in the compiled data |

The identifier shown is a BNF-style product code (section 4.6 area) rather than a standard PL number, and the dosage form and indication fields are blank. These details should be checked against the MHRA record and the current BNF.

---

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. The following is drawn from the supporting literature and pharmacology records:

- **Reported adverse effects (literature):** A 1993 review notes that flunarizine therapy may be limited by extrapyramidal disturbances and depression. Sedation is also a recognised concern given its antihistaminic activity.
- **Drug interactions:** A Phase 1 study ([NCT00752466](https://clinicaltrials.gov/study/NCT00752466)) examined the pharmacokinetic interaction between flunarizine and topiramate; the results are not summarised in the compiled data. The pharmacology records list activity at the D2 receptor and Cav3.1, Cav3.2 and Cav3.3 channels, but no specific interacting drugs were identified.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine prophylaxis is an established use of flunarizine, backed by meta-analyses, systematic reviews and many head-to-head trials. However, the UK licence details (indication and dosage form) are missing, and no label safety data were available. The extrapyramidal and depressive adverse effects reported in the literature call for caution.

**To proceed, the following is needed:**
- Confirmation of the UK licensed indication, dosage form and current SmPC from the MHRA record, including whether migraine prophylaxis is covered
- Label warnings, contraindications and interaction data from the SmPC and BNF
- Detailed mechanism of action data from DrugBank
- A safety monitoring plan covering depression, extrapyramidal symptoms and sedation, with particular attention to older adults and children
- Results from the ongoing Phase 4 comparison trials (e.g. PREMI and NCT07655700) once available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

