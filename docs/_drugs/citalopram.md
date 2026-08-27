---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the drug-repurposing evaluation report template supplied in this prompt to produce the report below (no other skill applies to this content-authoring task).

# Citalopram: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) whose well-established original use is the treatment of depression (major depressive disorder); this specific detail is not captured in the current evidence pack, which records no UK licensing information for the drug. The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, with **30 clinical trials** and **16 publications** identified in this evidence pack, although most of the trial evidence concerns escitalopram (citalopram's active enantiomer) rather than citalopram itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (Major Depressive Disorder) — well-established public indication for citalopram; not captured in this evidence pack |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| UK Market Status | Not marketed (per evidence pack; no MHRA licence records present) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, citalopram is a selective serotonin reuptake inhibitor (SSRI); its efficacy in depression has long been established, and mechanistically it may be applicable to OCD.

Dysregulation of the serotonergic system is one of the well-established core pathological mechanisms of OCD. Escitalopram, citalopram's pharmacologically active S-enantiomer, is already approved in several countries for OCD, reflecting a mechanism that is highly transferable between the two molecules. This provides reasonable mechanistic support for the TxGNN prediction, even though direct clinical evidence for citalopram (rather than escitalopram) in OCD remains comparatively limited.

An important caveat flagged directly in the evidence rationale: OCD treatment typically requires SSRI doses higher than the standard antidepressant dose, and citalopram carries a well-documented, dose-dependent risk of QTc prolongation (subject to regulatory dose-ceiling warnings in other jurisdictions). This is a key safety guardrail that must be factored into any repurposing pathway for OCD, where higher-than-standard dosing is often used off-label.

---

## Clinical Trial Evidence

*Note: the majority of trials below tested escitalopram, citalopram's active enantiomer, rather than citalopram itself — relevant supporting evidence for the SSRI class effect, but not direct citalopram data.*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00708240](https://clinicaltrials.gov/study/NCT00708240) | Phase 4 | Unknown (not confirmed completed) | 40 | Escitalopram efficacy, safety and cognitive/metacognitive changes in adolescents with OCD |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Compared SSRIs, exposure and response prevention (ERP), and combination therapy for OCD; explored predictors of treatment response |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Assessed escitalopram efficacy and optimal dosing for OCD |
| [NCT00115011](https://clinicaltrials.gov/study/NCT00115011) | Phase 4 | Completed | 30 | Escitalopram for self-injurious skin picking, an OCD-spectrum condition |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomised comparison of group CBT versus fluoxetine (an SSRI) for OCD |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomised, double-blind comparison of conventional-dose (20 mg) versus high-dose (40 mg) escitalopram in OCD |
| [NCT01936051](https://clinicaltrials.gov/study/NCT01936051) | N/A | Completed | 12 | Modelled plasma concentration vs. serotonin transporter occupancy of escitalopram in OCD patients |
| [NCT00708396](https://clinicaltrials.gov/study/NCT00708396) | Phase 4 | Unknown | 20 | Open-label study of high-dose escitalopram (20–40 mg/day) in patients with comorbid schizophrenia and OCD |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label study of high-dose escitalopram (up to 50 mg/day) for tolerability and efficacy in adult OCD |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Evaluated whether adjunctive CBT improves SRI treatment response in paediatric OCD partial responders |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Open-label Trial | European Psychiatry | Direct citalopram evidence: citalopram alone vs. citalopram + clomipramine in treatment-resistant OCD (n=16) |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Clinical Report | International Clinical Psychopharmacology | Direct citalopram evidence: reviews citalopram's use for OCD beyond its depression indication |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label Study | Psychiatry and Clinical Neurosciences | Direct citalopram evidence: 8-week open-label study of citalopram (20–30 mg/day) in children/adolescents with OCD (n=15) |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Network Meta-analysis | Journal of Psychiatric Research | Compared pharmacological and psychological treatments, alone and combined, for paediatric/adolescent OCD |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Review | Comprehensive Psychiatry | Long-term safety and tolerability of off-label high-dose SSRIs in OCD |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Frontiers in Psychiatry | Antidepressant efficacy, tolerability and suicidality in children/adolescents, including OCD |
| [30973183](https://pubmed.ncbi.nlm.nih.gov/30973183/) | 2019 | Neuroimaging Study | Psychiatry and Clinical Neurosciences | 1H-MRS brain neurochemistry changes after 12-week escitalopram treatment in unmedicated OCD patients |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | Pharmacogenetic Study | CNS Spectrums | BDNF Val66Met polymorphism and response to escitalopram/paroxetine in OCD |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World Journal of Biological Psychiatry | Reviews serotonergic and broader neurobiological mechanisms underlying OCD |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clinical Evidence | General clinical evidence review of OCD, including pharmacological treatment |

---

## UK Market Information

No marketing authorisation records for citalopram are present in this evidence pack (`total_licenses: 0`, market status "Not marketed"). Citalopram is, in fact, a long-established generic antidepressant widely available in the UK (BNF section 4.3.3, SSRIs) — but specific MHRA product licence numbers, brand names and SmPC-approved indication text were not returned by the data sources queried for this pack and should be sourced directly from the MHRA Products database before any UK-facing decision is finalised.

---

## Safety Considerations

**Known Safety Signal (from evidence rationale):** Citalopram carries a well-documented, dose-dependent risk of QTc interval prolongation. This is particularly relevant for a potential OCD indication, since OCD treatment typically requires higher SSRI doses than standard depression dosing, which would amplify cardiac risk.

No further structured safety data (key warnings, contraindications, drug–drug interactions) is available in this evidence pack. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Direct citalopram evidence in OCD is limited but present (three tier-1 studies, including one RCT-style open-label comparison), and this is substantially reinforced by consistent Phase 3/4 evidence for escitalopram (citalopram's active enantiomer) across multiple completed trials, supporting a plausible SSRI class effect. However, the evidence pack flags a **Blocking** data gap (DG001: UK SmPC warnings/contraindications) that currently prevents a full safety assessment, and citalopram itself has no confirmed UK marketing authorisation on record in this pack.

**To proceed, the following is needed:**
- UK/MHRA SmPC safety data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002, High severity)
- Verification of citalopram's actual UK marketing/licensing status (product name, PL number, approved indications)
- Additional citalopram-specific (not just escitalopram) trial data in OCD populations, given known enantiomer-specific differences in potency and tolerability
- A dose-dependent QTc monitoring plan, given that OCD dosing regimens often exceed standard depression doses

---

### Additional Note: Other Model-Predicted Indications (Not Recommended)

The evidence pack also returned four lower-ranked predictions — paranoid, schizotypal, histrionic and schizoid personality disorder (TxGNN scores ~99.68%, ranks 3666–3669). All are scored **Hold** with evidence levels L4–L5: little to no clinical trial or literature support exists, and the available literature is either off-topic, comorbidity-context only, or unrelated case reports. These are considered likely artefacts of knowledge-graph clustering among personality-disorder nodes rather than drug-specific signals, and are not recommended for further evaluation at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

