---
layout: default
title: Atomoxetine
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Atomoxetine
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

# Atomoxetine: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Atomoxetine is a selective norepinephrine reuptake inhibitor (NET inhibitor) with established international use for the treatment of Attention-Deficit/Hyperactivity Disorder (ADHD), a condition classified within the specific developmental disorders spectrum (ICD F90).
The TxGNN model predicts it may be effective more broadly for **Specific Developmental Disorder**, with **8 clinical trials** and **15 publications** currently supporting this direction.
Evidence quality is strong — including multiple completed Phase 3 and Phase 4 RCTs — yielding an L1 evidence classification and a recommendation to proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD (Attention-Deficit/Hyperactivity Disorder) — internationally approved; no UK MHRA authorisation found in current dataset |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L1 |
| UK Market Status | Not marketed (data to be verified with MHRA) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank for this candidate. However, based on information within the evidence pack, atomoxetine is a **selective norepinephrine reuptake inhibitor (NET inhibitor)**. By blocking the norepinephrine transporter in the prefrontal cortex, it increases synaptic norepinephrine (NE) concentrations, enhancing attentional control, executive function, and impulse inhibition. Notably, the NET also partially mediates dopamine (DA) reuptake in the prefrontal cortex, contributing a degree of dual NE/DA modulation in circuits central to neurodevelopmental function.

Specific developmental disorders — encompassing ADHD (ICD F90), autism spectrum disorder (ASD, ICD F84), pervasive developmental disorder (PDD), and related conditions — share a common neuropathological substrate: dysregulation of prefrontal–striatal NE and DA signalling. ADHD, the most extensively studied condition within this category, is characterised precisely by the circuit dysfunction that atomoxetine addresses, making the mechanistic link both direct and well-established rather than inferential.

Critically, the evidence does not merely reflect ADHD in isolation. Multiple completed Phase 3 and Phase 4 RCTs (NCT00498173, NCT00380692, NCT00844753) have enrolled children and adolescents with **autism spectrum disorders** — themselves classified as specific developmental disorders — demonstrating atomoxetine's efficacy in reducing ADHD symptoms across this broader diagnostic group. This cross-diagnostic evidence substantiates the TxGNN prediction and strongly suggests that atomoxetine targets a shared neurobiological pathway relevant to the wider specific developmental disorder category.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00510276](https://clinicaltrials.gov/study/NCT00510276) | Phase 4 | Completed | 445 | Double-blind RCT evaluating atomoxetine efficacy for ADHD symptoms and functional outcomes in young adults; largest completed trial in this dataset with community sample comparator arm |
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Phase 4 | Completed | 396 | Multicentre double-blind RCT comparing guanfacine prolonged-release vs atomoxetine vs placebo in children and adolescents aged 6–17 years with ADHD inadequately controlled by prior stimulants; includes 1-year open-label extension |
| [NCT00498173](https://clinicaltrials.gov/study/NCT00498173) | Phase 3 | Completed | 60 | Double-blind placebo-controlled RCT of atomoxetine for ADHD symptoms in children with **autistic disorder, Asperger's syndrome, and PDD-NOS** — highest-grade direct evidence within the developmental disorder spectrum |
| [NCT00380692](https://clinicaltrials.gov/study/NCT00380692) | Phase 4 | Completed | 97 | Randomised double-blind placebo-controlled trial assessing atomoxetine for ADHD symptom reduction in children and adolescents with **autism spectrum disorder** |
| [NCT00844753](https://clinicaltrials.gov/study/NCT00844753) | Phase 4 | Completed | 128 | Double-blind placebo-controlled RCT evaluating atomoxetine with and without Parent Management Training (PMT) in autism/Asperger's/PDDNOS with ADHD symptoms; 6-week dose titration design |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1,398 | ADDUCE project: prospective observational study examining ADHD medication effects on growth, neurological, psychiatric, and cardiovascular parameters over 2 years; provides real-world safety evidence |
| [NCT05635318](https://clinicaltrials.gov/study/NCT05635318) | N/A | Unknown | 102 | Quantitative EEG neurofeedback as add-on therapy for ADHD; atomoxetine used as active reference arm |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Exploratory study of smoking reinforcement mechanisms in adult ADHD; limited direct relevance to developmental disorder efficacy, included for completeness |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Network Meta-Analysis | *The Lancet Psychiatry* | Comparative efficacy and acceptability of pharmacological, psychological, and neurostimulatory interventions for adult ADHD; highest-level evidence synthesis placing atomoxetine within the treatment hierarchy |
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Meta-Analysis | *Autism Research* | Systematic review and meta-analysis of 3 RCTs (n=241) assessing atomoxetine efficacy and safety in children with ASD and ADHD symptoms; GRADE methodology applied; directly supports developmental disorder indication |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Systematic Review | *Therapeutic Advances in Psychopharmacology* | Review of atomoxetine efficacy in ADHD with comorbidities including pervasive developmental disorders; demonstrates maintained efficacy across neurodevelopmental conditions |
| [32946507](https://pubmed.ncbi.nlm.nih.gov/32946507/) | 2020 | Systematic Review | *PLoS ONE* | Comprehensive review of sex differences in ADHD pharmacotherapy efficacy in girls and women; identifies evidence gaps and clinically relevant treatment response variability |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Cohort Study | *Neuropsychopharmacology Reports* | Retrospective cohort identifying patient-specific predictors of atomoxetine response in adult ADHD; long-term response rate approximately 40% at 6 months, with individual variability |
| [39514707](https://pubmed.ncbi.nlm.nih.gov/39514707/) | 2024 | Case Review | *Journal of Developmental and Behavioral Pediatrics* | Case and review of atomoxetine use in a child with ADHD, anxiety, depression, and suicidal ideation; highlights comorbidity management and monitoring requirements in real-world practice |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Cross-sectional | *Clinical EEG and Neuroscience* | Review of quantitative EEG findings in childhood ADHD and learning disabilities; contextualises neurophysiological underpinnings relevant to specific developmental disorders and personalised treatment response |
| [41332541](https://pubmed.ncbi.nlm.nih.gov/41332541/) | 2025 | Preprint | *bioRxiv* | Structural white-matter connectivity deviations in youth with ADHD across two independent cohorts (n>7,000 total) predict symptom development and treatment outcomes; provides neuroimaging biomarker evidence (preprint — not yet peer-reviewed) |
| [25545605](https://pubmed.ncbi.nlm.nih.gov/25545605/) | 2015 | Review | *Journal of Affective Disorders* | Systematic review of comorbidity patterns in paediatric bipolar disorder, including prevalence of ADHD; contextualises treatment complexity in overlapping developmental conditions |
| [16232017](https://pubmed.ncbi.nlm.nih.gov/16232017/) | 2005 | Observational | *Pharmacotherapy* | Analysis of predictors for selecting atomoxetine in children with ADHD in a managed care setting shortly after market introduction; provides foundational real-world prescribing context |

---

## UK Market Information

No active MHRA marketing authorisations for atomoxetine are recorded in the current dataset. UK market status is listed as **not marketed** with zero registered product licences.

> **Important note for clinicians**: This likely represents a data gap in the current evidence pack rather than a true absence of UK authorisation. Atomoxetine (Strattera®) is known to hold regulatory approvals in the United States, European Union, and numerous other jurisdictions. Healthcare professionals should verify the current MHRA authorisation status via the [MHRA Product Licence Search](https://www.gov.uk/check-if-a-medicine-is-licensed-in-the-uk) and consult the current [BNF entry for atomoxetine](https://bnf.nice.org.uk/) before prescribing. The absence of licence data in this report does **not** imply the product is unlicensed in the UK.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atomoxetine has a mechanistically well-grounded basis for use across the specific developmental disorder spectrum, supported by multiple completed Phase 3 and Phase 4 RCTs, a Lancet Psychiatry network meta-analysis, and a published meta-analysis in autism spectrum disorder — collectively meeting L1 evidence criteria. The TxGNN prediction score of 99.998% reflects strong signal alignment with the knowledge graph, and the biological rationale linking NET inhibition to prefrontal NE/DA dysregulation — the core pathology of specific developmental disorders — is direct and established.

**To proceed, the following is needed:**

- **Verify MHRA authorisation status**: Retrieve current UK marketing authorisation details, approved SmPC, and BNF classification for atomoxetine
- **Retrieve full safety profile (DG001)**: Download and parse the current SmPC for key warnings, contraindications, and special populations — particularly the black-box warning on suicidal ideation in children and adolescents
- **Obtain DrugBank MOA data (DG002)**: Confirm full mechanism of action, pharmacokinetic parameters, and known drug–drug interactions via DrugBank API
- **Define target sub-diagnosis**: Clarify whether the repurposing intent focuses on ADHD, ASD with ADHD symptoms, or broader specific developmental disorder; patient selection criteria should be defined accordingly
- **Assess drug interaction risk**: Atomoxetine is a CYP2D6 substrate; formal DDI screening against common co-prescriptions in the target population is required
- **Design a pharmacovigilance plan**: Align adverse event monitoring with MHRA Yellow Card Scheme requirements, with particular attention to cardiovascular, psychiatric, and growth-related endpoints identified in the ADDUCE study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

