---
layout: default
title: Bupropion
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Bupropion
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

# Bupropion: From Depression and Smoking Cessation to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Bupropion is an atypical antidepressant and smoking cessation aid, acting as a norepinephrine-dopamine reuptake inhibitor (NDRI) and nicotinic acetylcholine receptor antagonist, established in clinical practice for major depressive disorder and tobacco dependence.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**,
with **8 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression; smoking cessation (UK MHRA authorisation data not retrieved — see UK Market Information) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| UK Market Status | No authorisation records retrieved (possible data gap — verify via MHRA and BNF) |
| Number of Marketing Authorisations | 0 on record |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bupropion inhibits the dopamine transporter (DAT) and norepinephrine transporter (NET), increasing synaptic availability of dopamine and norepinephrine in the prefrontal cortex — the brain region most critical for attentional control and executive function. Its mechanism closely parallels that of methylphenidate (a DAT inhibitor), the current first-line stimulant for ADHD, yet bupropion carries no controlled substance classification and presents a distinctly different tolerability profile. This makes it a mechanistically coherent non-stimulant alternative for patients who cannot tolerate or do not respond to stimulants.

ADHD is neurobiologically characterised by deficient prefrontal dopaminergic and noradrenergic signalling, precisely the neurotransmitter systems that bupropion targets. The drug's dual DAT/NET inhibition directly addresses both the inattentive (primarily noradrenergic) and hyperactive/impulsive (primarily dopaminergic) symptom dimensions of ADHD. Additional activity at nicotinic acetylcholine receptors may further modulate attentional circuits, providing a complementary mechanism not shared by conventional stimulants.

The TxGNN prediction is therefore grounded in well-characterised pharmacology rather than speculative inference. Bupropion has been evaluated specifically for ADHD in Phase 3 double-blind randomised controlled trials, multiple Phase 2/3 and Phase 4 studies, a Cochrane systematic review, and several large network meta-analyses published in high-impact journals. The convergence of mechanistic plausibility and robust clinical evidence places this prediction in the highest evidence tier.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | 8-week multicentre, double-blind, placebo-controlled RCT of extended-release bupropion hydrochloride 300–450 mg/day in adults with ADHD; primary assessment of efficacy, safety, and health outcomes |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | Treatment of adult ADHD in methadone-maintained patients; evaluates bupropion in a high-complexity comorbid population with opioid dependence |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Post-marketing study of bupropion for ADHD in adolescents with substance use disorders; addresses a historically under-studied, clinically significant population |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | Not specified | Completed | 32 | Open study of bupropion SR in ADHD adults with recent or current substance use disorders; exploratory efficacy and tolerability data |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | Not specified | Completed | 32 | Evaluation of cocaine abuse and co-occurring ADHD; bupropion used as active treatment, providing indirect evidence in a comorbid population |

> **Note:** Three additional trials retrieved (NCT04553263 — withdrawn before enrolment; NCT03326128 — terminated for smoking cessation, not ADHD; NCT00330434 — pharmacokinetic mechanism study, withdrawn) were excluded from this table due to low relevance or absence of usable data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Bupropion for ADHD in adults: concludes bupropion is superior to placebo with a clinically meaningful effect; evidence quality rated moderate |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Network Meta-Analysis | The Lancet Psychiatry | Comparative efficacy and tolerability of ADHD medications across children, adolescents, and adults; bupropion demonstrates a measurable effect relative to placebo and active comparators |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Systematic Review & NMA | PLoS ONE | Pharmacological treatments for adult ADHD; network meta-analysis quantifying relative benefits and harms of bupropion versus methylphenidate, atomoxetine, and other agents |
| [38950507](https://pubmed.ncbi.nlm.nih.gov/38950507/) | 2024 | Bayesian NMA | Journal of Psychiatric Research | Efficacy and safety of monoamine reuptake inhibitors in ADHD based on 31 clinical trials; bupropion assessed for comparative ranking among non-stimulant agents |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Comparative Safety NMA | The Lancet Psychiatry | Cardiovascular safety of ADHD medications including bupropion; haemodynamic and ECG parameter effects quantified across age groups — directly relevant to prescribing decisions |
| [27813651](https://pubmed.ncbi.nlm.nih.gov/27813651/) | 2017 | Systematic Review | Journal of Child and Adolescent Psychopharmacology | Systematic review of bupropion for ADHD in children and adolescents; positive signal, positioned as second-line option when stimulants are unsuitable |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Review | Health Psychology Research | Comprehensive review of bupropion's pharmacokinetics, pharmacodynamics, and mechanisms across depression, ADHD, and smoking cessation; drug interactions addressed |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Review | Expert Review of Neurotherapeutics | Current non-stimulant medications for adult ADHD; bupropion positioned within the prescribing landscape alongside atomoxetine, viloxazine, and guanfacine |
| [27738872](https://pubmed.ncbi.nlm.nih.gov/27738872/) | 2017 | Multi-treatment Comparison | Molecular Neurobiology | Efficacy and safety comparison of ADHD medications in children and adolescents using ADHD-RS and CPRS rating scales; provides paediatric-specific effect size data |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Current Pharmaceutical Design | Psychopharmacology of ADHD including bupropion; mechanism of dopamine and norepinephrine reuptake inhibition reviewed in clinical context |

---

## UK Market Information

No MHRA marketing authorisation records were retrieved for bupropion in this evidence pack (0 licences on record). This is likely to reflect a data collection gap in the regulatory data pipeline rather than genuine market absence. Bupropion is commercially available in the United Kingdom — notably as **Zyban®** (sustained-release tablets, 150 mg) licensed for smoking cessation, and formulations for depression have historically been authorised in several EU/UK markets.

Healthcare professionals should verify current UK authorisation status directly via:
- **MHRA products database**: [https://products.mhra.gov.uk](https://products.mhra.gov.uk)
- **BNF** (British National Formulary): BNF section on antidepressants and smoking cessation
- **NICE guideline NG92** (Stop smoking interventions and services) and **NG87** (ADHD: diagnosis and management)

---

## Safety Considerations

Formal UK SmPC warnings, contraindications, and drug interaction data were not retrieved in this evidence pack. Key known safety considerations for bupropion from published literature and regulatory sources include:

- **Seizure risk**: Bupropion lowers the seizure threshold in a dose-dependent manner; contraindicated in patients with seizure disorders or those at elevated risk (eating disorders, abrupt alcohol withdrawal, concurrent seizurogenic medications)
- **Psychiatric effects**: Risk of agitation, anxiety, and — particularly in younger patients — suicidal ideation; consistent with MHRA guidance for antidepressants
- **CYP2D6 interactions**: Bupropion is a potent CYP2D6 inhibitor and may significantly increase plasma levels of co-administered CYP2D6 substrates (e.g., tricyclic antidepressants, antipsychotics, certain beta-blockers)
- **Cardiovascular**: Modest increases in heart rate and blood pressure reported; relevant to ADHD populations who may also be prescribed stimulants

Please refer to the current SmPC and BNF for complete and up-to-date safety information. Report suspected adverse reactions via the **Yellow Card Scheme** ([https://yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk)).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 double-blind RCT (NCT00048360), supported by Phase 2/3 and Phase 4 studies, a Cochrane systematic review (PMID 28965364), and multiple network meta-analyses in high-impact journals (Lancet Psychiatry, PLoS ONE) collectively constitute Level 1 evidence for bupropion's efficacy in ADHD. The mechanistic rationale — dual DAT/NET inhibition directly addressing the prefrontal dopaminergic and noradrenergic deficits underlying ADHD — is well characterised and pharmacologically coherent.

**To proceed, the following is needed:**

- **UK regulatory clarification**: Confirm current MHRA authorisation status and obtain full SmPC; assess whether an off-label use framework or formal variation is required for an ADHD indication
- **NICE alignment**: Review compatibility with NICE NG87 (ADHD: diagnosis and management), which currently recommends methylphenidate, lisdexamfetamine, dexamfetamine, and atomoxetine as first-line options; establish the clinical pathway position for bupropion as a non-stimulant second-line agent
- **Seizure risk assessment protocol**: Develop a patient-level risk stratification tool prior to initiation, given bupropion's dose-dependent seizure liability — particularly relevant in ADHD populations with frequent comorbidities (eating disorders, substance use, depression)
- **Drug interaction screening**: Systematic CYP2D6 interaction review for ADHD patients with co-prescriptions (especially antidepressants, antipsychotics, or stimulants)
- **Special population data**: Paediatric safety and dosing data specific to ADHD (existing evidence primarily from adult RCTs; paediatric evidence largely from comorbid or off-label settings)
- **Comparative effectiveness vs. UK standard of care**: Head-to-head or indirect comparison data versus atomoxetine and methylphenidate to support formulary decision-making and commissioning

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before any change in prescribing practice. All clinical decisions should be made in accordance with current NICE guidance, MHRA authorisations, and individual patient assessment.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

