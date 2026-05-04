---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist with an established clinical role in managing muscle spasticity, particularly in conditions such as multiple sclerosis and spinal cord injury. The TxGNN model ranks **Attention Deficit-Hyperactivity Disorder (ADHD)** as its top repurposing candidate (score: 99.32%), supported by **no registered clinical trials** and **10 publications** that are predominantly preclinical or review in nature. A second high-ranking prediction — **Nicotine Dependence** (99.19%) — carries substantially stronger clinical evidence, including a completed Phase 2 trial and 20 publications, and is presented in full alongside the primary indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Muscle spasticity (note: UK regulatory data not retrieved — see data note below) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| UK Market Status | Not retrieved (data gap — see note) |
| Number of Marketing Authorisations | 0 (data gap — see note) |
| Recommended Decision | Hold |

> **⚠ Data Note on UK Market Status:** The evidence pack returns zero UK marketing authorisations for baclofen. This is almost certainly a data pipeline issue rather than a true regulatory absence. Baclofen (e.g., Lioresal® and multiple generic preparations) is a long-established MHRA-authorised medicine widely available in the UK for spasticity. Regulatory status must be verified directly via the [MHRA Products database](https://products.mhra.gov.uk/) or the [Electronic Medicines Compendium (eMC)](https://www.medicines.org.uk/emc) before drawing any conclusions.

---

## Why is This Prediction Reasonable?

Baclofen acts as a selective GABA-B receptor agonist, activating inhibitory receptors at pre- and post-synaptic sites throughout the central nervous system. Although formal MOA documentation is absent from the UK regulatory data in this evidence pack, baclofen's pharmacology is extensively characterised in the wider literature: it suppresses the release of excitatory neurotransmitters — principally dopamine, norepinephrine, and glutamate — from presynaptic terminals in limbic, cortical, and spinal pathways. This underpins its established efficacy in reducing muscle tone and spasm.

The predicted link to ADHD is mechanistically indirect but not implausible. ADHD is characterised by dysregulated catecholamine (dopamine and norepinephrine) neurotransmission in the prefrontal cortex (PFC) and striatum, leading to impaired inhibitory control, sustained attention, and impulse regulation. GABA-B agonism could theoretically modulate downstream catecholamine release in these circuits, attenuating hyperactivity and impulsivity. Lending limited biological plausibility, the spontaneously hypertensive rat (SHR) — the canonical animal model for ADHD — shows measurable alterations in GABAergic tone, and baclofen has been shown to produce EEG changes in this model consistent with cortical inhibition.

However, this mechanistic pathway is acknowledged by the evidence pack itself to be a "highly indirect inference lacking direct human validation." The ADHD-relevant literature identified here largely concerns Tourette syndrome and autism spectrum disorder — conditions frequently comorbid with ADHD — rather than directly testing baclofen in ADHD patients or ADHD-specific paradigms. No human clinical data exists for this specific indication. This remains an early-stage hypothesis.

---

## Clinical Trial Evidence

Currently no clinical trials related to Baclofen in ADHD are registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal model (preclinical) | Brain Research | EEG responses to GABAergic and other neurotransmitter agonists in SHR (ADHD model) and kainate-treated rats; altered frontal cortex and hippocampal baseline activity observed — directly relevant to ADHD neurobiology |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal model (preclinical) | Neuropsychopharmacology | Dissociable roles of anterior cingulate cortex and basolateral amygdala in effortful cognitive decision-making; impaired effortful choice is a hallmark of ADHD executive dysfunction |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal model (preclinical) | Psychopharmacology | α2A-adrenergic stimulation in ventral hippocampus reduces impulsive decision-making in rats; contextualises adrenergic–GABAergic interactions relevant to ADHD impulsivity |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal model (preclinical) | European Journal of Neuroscience | Habenula integrity required for social play in rats; links GABAergic modulation to monoaminergic circuits relevant to ADHD-associated social deficits |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Behavioural interventions, antipsychotics, and alpha agonists for tic disorders in Tourette syndrome; ADHD highlighted as the most prevalent and impactful comorbidity |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | International Review of Neurobiology | Emerging treatment strategies for Tourette syndrome, including management of ADHD comorbidity; pipeline assessment noting need for novel GABAergic agents |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | Journal of Child Neurology | 450-patient case series: baclofen and botulinum toxin A in tics/Tourette syndrome; improvement on Yale Global Tic Severity Scale reported — the only identified article directly linking baclofen to a neurodevelopmental condition |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clinical Neuropharmacology | Mood stabilisers in children and adolescents with autism spectrum disorders; attention deficit identified as a key comorbid symptom domain requiring pharmacological management |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Tourette syndrome clinical characteristics and pharmacotherapy; dopamine antagonists as first-line, with ADHD comorbidity management discussed |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical article | L'Encéphale | Off-label methylphenidate prescribing in adult ADHD in France; documents the broader landscape of unlicensed prescribing in ADHD as context for potential baclofen use |

---

## Second-Ranked Prediction: Nicotine Dependence

This candidate (TxGNN rank 2, score 99.19%) carries substantially stronger clinical and preclinical evidence than the top ADHD prediction. It is presented here in full given its greater near-term translational potential.

### Evidence Overview

| Item | Content |
|------|---------|
| Predicted Indication | Nicotine Dependence |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L3 |
| Number of Clinical Trials | 3 (1 completed Phase 2, 2 terminated Phase 2) |
| Number of Publications | 20 |
| Recommended Decision | Research Question |

### Mechanistic Rationale

The mechanistic case for nicotine dependence is more direct and better supported than for ADHD. Baclofen's GABA-B agonism inhibits dopaminergic neuron firing in the ventral tegmental area (VTA), thereby reducing dopamine release in the nucleus accumbens — the critical site of nicotine's rewarding and reinforcing effects via the mesolimbic pathway. In parallel, baclofen inhibits presynaptic glutamate release, which may attenuate the excitatory components of nicotine withdrawal. This dual mechanism has been validated in multiple independent animal nicotine self-administration models (PMIDs 18682277, 19250803, 24553576, 23500668), representing one of the best-characterised mechanistic rationales in baclofen repurposing research.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | Perfusion fMRI study examining baclofen's effects on brain and behavioural responses to smoking cues in active cigarette smokers; uses dopaminergic polymorphisms as moderators — the only completed Phase 2 trial and the highest-quality clinical evidence in this pack |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Baclofen vs placebo to reduce smoking urge, withdrawal, and reinforcement in moderate-to-heavy smokers; near-complete enrolment at termination suggests administrative/funding rather than safety reasons — partial data likely available |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Testing the GABAergic hypothesis of nicotine dependence; terminated very early with only 6 participants — minimal clinical data generated, though title confirms mechanistic interest |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Clinical abstract / Pilot RCT | Neuropsychopharmacology | Baclofen as pharmacotherapy for concurrent alcohol and nicotine dependence; double-blind, placebo-controlled, randomised design — direct human evidence for this repurposing hypothesis |
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Animal study (preclinical) | Psychopharmacology | Baclofen attenuates nicotine rewarding properties and physical withdrawal manifestations in rodents; strong preclinical efficacy signal |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Animal study (preclinical) | European Neuropsychopharmacology | Baclofen prevents drug-induced reinstatement of nicotine-seeking behaviour and conditioned place preference in rats — models relapse prevention |
| [23500668](https://pubmed.ncbi.nlm.nih.gov/23500668/) | 2013 | Animal study (preclinical) | Progress in Neuro-Psychopharmacology & Biological Psychiatry | Baclofen prevents mecamylamine-precipitated nicotine withdrawal; α4β2 nicotinic receptor density changes characterised — mechanistic depth |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Animal study (preclinical) | Neuroscience Letters | Baclofen selectively reduces nicotine-induced conditioned place preference and nicotine discrimination in rats without abolishing food-reinforced behaviour |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Review | Neuropharmacology | GABA-B receptors as therapeutic targets across multiple substance use disorders; positive allosteric modulators (PAMs) as safer alternatives to direct agonism reviewed |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Current and emerging pharmacotherapies for tobacco cessation; baclofen identified as an investigational agent with mechanistic plausibility |
| [17338593](https://pubmed.ncbi.nlm.nih.gov/17338593/) | 2007 | Review | CNS Drugs | Pharmacotherapy of dual substance abuse; baclofen discussed for co-occurring alcohol and nicotine dependence — clinically relevant for comorbid populations |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Review | International Review of Neurobiology | Drug repurposing for alcohol use disorder; baclofen cited as approved for AUD in some jurisdictions (e.g., France), with cross-dependency implications for nicotine |
| [36258248](https://pubmed.ncbi.nlm.nih.gov/36258248/) | 2022 | Adaptive clinical trial (Phase 1/2) | Trials | FORWARDS-1: baclofen safety and PK/PD characterisation in opioid-dependent patients on methadone; safety data relevant across addiction indications |

---

## UK Market Information

No UK marketing authorisations for Baclofen were retrieved in this evidence pack, which is inconsistent with the drug's known availability in the UK. The pipeline data gap should be remediated before any regulatory assessment.

Please consult the following authoritative sources directly:

| Source | Purpose | URL |
|--------|---------|-----|
| MHRA Products database | Confirm current UK product licences | https://products.mhra.gov.uk/ |
| Electronic Medicines Compendium (eMC) | Access approved SmPCs and PILs | https://www.medicines.org.uk/emc |
| BNF Online | Prescribing guidance and classification | https://bnf.nice.org.uk/ |
| NICE Evidence Search | Any technology appraisals or guidelines | https://www.evidence.nhs.uk/ |

---

## Safety Considerations

Safety data (warnings, contraindications, and drug interactions) was not available in this evidence pack. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at https://yellowcard.mhra.gov.uk/.

---

## Conclusion and Next Steps

### Primary Indication — ADHD

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, the evidence base for baclofen in ADHD is currently limited to preclinical animal models and literature concerning comorbid neurodevelopmental conditions (Tourette syndrome, ASD). No clinical trials in ADHD patients have been conducted, and the mechanistic pathway — though biologically coherent — remains speculative and indirect.

**To proceed, the following is needed:**
- Targeted ADHD-specific preclinical studies with baclofen in validated animal models (SHR, DAT knockdown rodents) measuring core ADHD behavioural phenotypes (hyperactivity, impulsivity, sustained attention)
- A systematic review or meta-analysis synthesising GABAergic involvement in ADHD neurobiology across existing literature
- Assessment of baclofen's tolerability in paediatric populations, given the predominantly childhood-onset nature of ADHD
- Expert input from a paediatric neurologist or child and adolescent psychiatry specialist before any clinical study design

---

### Second-Ranked Indication — Nicotine Dependence

**Decision: Research Question (Proceed to Study Design)**

**Rationale:**
A completed Phase 2 trial (NCT01821560), multiple independent preclinical self-administration studies, and a coherent, direct mechanistic rationale collectively justify moving this to a structured research proposal. The evidence is insufficient to support routine clinical use but is sufficient to design and fund a well-powered efficacy trial.

**To proceed, the following is needed:**
- Full published results from NCT01821560 (completed June 2017) — if unpublished, data should be requested from the investigators
- A meta-analysis of existing preclinical dose-response data to inform Phase 2b dosing (likely 40–80 mg/day range based on alcohol use disorder literature)
- Phase 2b/3 RCT design with CO-verified continuous 12-week smoking abstinence as the primary endpoint, in collaboration with NHS Stop Smoking Services
- MHRA pre-submission scientific advice — given baclofen's existing UK licence for spasticity, a line extension via a Type II variation may offer a more efficient pathway than a new marketing authorisation
- Safety monitoring plan addressing sedation, respiratory depression, and withdrawal risk, particularly in patients with concurrent alcohol use disorder

> **Disclaimer:** This report is intended for research and evaluation purposes only. It does not constitute medical advice, a prescribing recommendation, or a regulatory opinion. All drug repurposing candidates require prospective clinical validation before clinical application. This analysis was generated using the TxGNN model and does not replace independent clinical or regulatory assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

