---
layout: default
title: Midodrine
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrine: From Unlicensed Status in the UK to Hypotensive Disorder

## One-Sentence Summary

Midodrine currently holds no UK marketing authorisation, and no original indication data is recorded in this evidence pack.
The TxGNN model generated 10 candidate indications; only **hypotensive disorder** is backed by real mechanistic and clinical evidence,
with **9 clinical trials** and **18 publications** — including AHA and AGA guidance — supporting this direction.
The other 9 candidates (e.g. prion disease, ADHD, monogenic obesity) show no mechanistic plausibility and are not carried forward in this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no UK licence or original-indication data in this evidence pack |
| Predicted New Indication | Hypotensive disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap — MOA to be sourced from DrugBank). Based on the mechanistic rationale supplied alongside the prediction, midodrine is a prodrug that is enzymatically converted to its active metabolite, desglymidodrine, a peripherally-selective alpha-1 adrenergic receptor agonist causing vasoconstriction and a rise in blood pressure.

This mechanism maps directly onto the pathophysiology of hypotensive disorders — including neurogenic orthostatic hypotension, intradialytic hypotension, and hypotension secondary to spinal cord injury or hepatorenal syndrome — all of which are driven by inadequate vasoconstrictor tone. Unlike several of the other TxGNN candidates (which the evidence pack itself flags as likely model noise, e.g. prion disease or Aarskog syndrome), this indication sits within midodrine's core pharmacological action, which is reflected in the volume and quality of supporting trials and literature below.

Because midodrine is not currently marketed in the UK, this should be read as an assessment of therapeutic plausibility and existing global evidence, rather than confirmation of a novel mechanism — the drug's vasopressor action for hypotensive disorders is already well established internationally.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02307565](https://clinicaltrials.gov/study/NCT02307565) | Phase 3 | Completed | 19 | Midodrine improved blood pressure, cerebral blood flow and cognitive function in spinal cord injury (SCI) patients with chronic hypotension |
| [NCT01030874](https://clinicaltrials.gov/study/NCT01030874) | N/A | Completed | 356 | Multidisciplinary, multicomponent intervention for orthostatic hypotension on a rehabilitation unit |
| [NCT03431194](https://clinicaltrials.gov/study/NCT03431194) | N/A | Completed | 80 | Oral midodrine effective for intradialytic hypotension in critically ill patients with acute kidney injury |
| [NCT05548985](https://clinicaltrials.gov/study/NCT05548985) | N/A | Completed | 58 | Oral midodrine as prophylaxis against post-spinal-anaesthesia hypotension in elderly hip arthroplasty patients |
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Phase 2 | Completed | 21 | Effects of normalising blood pressure (via midodrine) on cerebral blood flow in hypotensive SCI patients |
| [NCT02307526](https://clinicaltrials.gov/study/NCT02307526) | Phase 2 | Completed | 10 | Acetylcholinesterase inhibition compared with midodrine for orthostatic hypotension in SCI |
| [NCT03037879](https://clinicaltrials.gov/study/NCT03037879) | N/A | Completed | 10 | 30-day midodrine-mediated blood pressure elevation to address cognitive deficits after traumatic SCI |
| [NCT05839652](https://clinicaltrials.gov/study/NCT05839652) | Phase 4 | Recruiting | 25 | Pharmacological and non-pharmacological treatment of orthostatic hypotension and autonomic dysreflexia in SCI |
| [NCT06405555](https://clinicaltrials.gov/study/NCT06405555) | Phase 2/3 | Not yet recruiting | 56 | Pilot open-label RCT of midodrine for heart failure with reduced ejection fraction complicated by hypotension |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | RCT | Hepatology | Midodrine + octreotide + albumin compared with terlipressin + albumin for hepatorenal syndrome |
| [39619823](https://pubmed.ncbi.nlm.nih.gov/39619823/) | 2024 | RCT (placebo-controlled) | Topics Spinal Cord Inj Rehabil | 30-day midodrine vs placebo improved blood pressure, cerebral blood flow velocity and cognition in SCI |
| [38123372](https://pubmed.ncbi.nlm.nih.gov/38123372/) | 2024 | Review/Expert Position | Revue Neurologique | Expert position statement on diagnosis and management of orthostatic hypotension |
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Scientific Statement (AHA) | Hypertension | AHA statement on orthostatic hypotension as a comorbidity of hypertension |
| [37978969](https://pubmed.ncbi.nlm.nih.gov/37978969/) | 2024 | Clinical Practice Update | Gastroenterology | AGA review of vasoactive drugs (including midodrine) and IV albumin in cirrhosis |
| [28050656](https://pubmed.ncbi.nlm.nih.gov/28050656/) | 2017 | Consensus Panel Recommendations | Journal of Neurology | Consensus guidance on screening, diagnosis and treatment of neurogenic orthostatic hypotension |
| [40604215](https://pubmed.ncbi.nlm.nih.gov/40604215/) | 2025 | Retrospective cohort | Scientific Reports | Midodrine use associated with clinical outcomes in maintenance haemodialysis patients |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | 2020 | Review | Auton Neurosci | Review of pharmacologic treatment options for neurogenic orthostatic hypotension |
| [35029940](https://pubmed.ncbi.nlm.nih.gov/35029940/) | 2022 | Review | American Family Physician | Practical approach to diagnosis and management of orthostatic hypotension |
| [2480881](https://pubmed.ncbi.nlm.nih.gov/2480881/) | 1989 | Review (pharmacology) | Drugs | Foundational review of midodrine's pharmacological properties and use in orthostatic and secondary hypotension |

## UK Market Information

Midodrine currently holds **no marketing authorisation in the UK** (market status: Not marketed; total licenses: 0). No product-specific licence, brand, or dosage form data is available in this evidence pack.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Key warnings, contraindications and drug interaction data for midodrine are flagged as a Blocking-severity data gap in this evidence pack (source: TFDA label PDF, not yet retrieved) and must be obtained before any safety initial assessment (S1) can proceed.*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Midodrine's alpha-1 agonist prodrug mechanism directly supports its use in hypotensive disorders, and this is backed by 9 clinical trials (including a completed Phase 3 RCT) and 18 publications, including AHA and AGA clinical guidance — evidence level L1. However, the drug has no current UK marketing authorisation and key safety label data is missing, so guardrails are required before advancing.

**To proceed, the following is needed:**
- UK/EU SmPC or full prescribing information, to close the Blocking-severity safety data gap (DG001) and enable an initial safety assessment
- Formal mechanism-of-action documentation from DrugBank (DG002)
- Confirmation of midodrine's licensing status and approved indication in other jurisdictions (e.g. US FDA orthostatic hypotension approval), to properly frame the "original vs new indication" comparison
- A regulatory pathway assessment for obtaining UK marketing authorisation, given current "Not marketed" status
- A safety monitoring plan addressing known class risks (supine hypertension, reflex bradycardia) before use in populations with conduction disease

*The remaining 9 TxGNN-predicted indications (prion disease, Aarskog syndrome, ADHD, monogenic obesity, sinoatrial node disease, etc.) lack mechanistic or evidentiary support and are held at S0/Hold — no further action recommended.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

