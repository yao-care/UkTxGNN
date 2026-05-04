---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline: From Bronchospasm to Migraine Disorder

## One-Sentence Summary

Aminophylline is a well-established methylxanthine bronchodilator used in the management of bronchospasm and apnea of prematurity, although no MHRA marketing authorisation is currently recorded in this evidence pack.
The TxGNN model predicts it may be effective for **Migraine Disorder**, driven by its pharmacological role as a non-selective adenosine receptor antagonist acting on pathways increasingly implicated in migraine pathogenesis.
Current evidence comprises **no registered clinical trials** and **6 publications**, placing this prediction at an **L4 (mechanistic/preclinical) evidence level** — warranting further evaluation before clinical progression.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchospasm; apnea of prematurity (established clinical use; no UK marketing authorisation currently on record) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (no MHRA marketing authorisation on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, aminophylline is a soluble salt of theophylline (combined with ethylenediamine to improve solubility). It exerts its effects primarily through two complementary mechanisms: non-selective competitive antagonism at adenosine receptors (A1, A2A, A2B, A3 subtypes), and inhibition of phosphodiesterase (PDE) enzymes leading to elevated intracellular cyclic AMP (cAMP). The structurally related methylxanthine caffeine is routinely incorporated into migraine combination analgesics (e.g., alongside aspirin and paracetamol), providing clinically validated mechanistic precedent for this drug class in headache.

The biological rationale for aminophylline in migraine rests on the adenosine hypothesis of migraine. Accumulating evidence suggests that pathologically elevated adenosine levels during a migraine attack activate A2A and A2B receptors on pial and dural blood vessels, precipitating vasodilation and stimulating the trigeminovascular pain pathway. By competitively blocking these receptors, aminophylline may theoretically interrupt this cascade. Indirect clinical evidence supports this: the selective A2A agonist regadenoson has been documented to trigger migraine attacks (PMID 34308528), which were subsequently reversed by aminophylline — a real-world proof-of-mechanism observation. Furthermore, aminophylline's efficacy in relieving post-dural puncture headache, another adenosine-mediated headache syndrome, has been observed in clinical practice and reviewed in the literature (PMID 38059379).

Despite the plausibility of the mechanism, aminophylline has a narrow therapeutic index and a distinct adverse effect profile compared with caffeine, carrying risks of tachyarrhythmia, hypokalaemia, and seizures at supratherapeutic concentrations. These considerations mean that any repurposing programme would require independent pharmacokinetic and safety characterisation in migraine populations, including careful assessment of appropriate dose and administration route.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for aminophylline in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Narrative Review | Pain Management | Proposes that migraine is driven by impaired brain energy metabolism and high adenosine levels; reviews evidence that aminophylline (as an adenosine receptor antagonist) provides strong relief in pain and post-dural headache; includes data from a published observational case series demonstrating therapeutic benefit |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case Report | Journal of Nuclear Cardiology | Reports a case of hemiplegic migraine triggered by regadenoson, a selective A2A adenosine receptor agonist used for myocardial perfusion imaging; aminophylline used to reverse adverse neurological effects — directly supports adenosine pathway involvement in migraine |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | In Vitro Basic Science | Stroke | Demonstrates that adenosine and adenine nucleotides markedly dilate feline and human pial arteries in vitro (particularly against a raised vascular tone), whilst sparing extracranial vessels; discusses this selectivity as a possible mechanism of migraine headache |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case Report | Canadian Journal of Cardiology | Documents a case of syndrome X presenting as "myocardial migraine without ischaemia"; severe chest pain and ST changes induced by dipyridamole were attributed to excessive adenosine activity, consistent with aminophylline's mechanistic rationale |
| [5540199](https://pubmed.ncbi.nlm.nih.gov/5540199/) | 1971 | Historical Clinical | The Practitioner | Historical article on suppository formulations including aminophylline; abstract not available; limited direct relevance to current clinical practice |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Case Series | Aggiornamenti Clinicoterapeutici | Early Italian clinical case series on medical management of headaches; abstract not available; primarily of historical interest |

---

## UK Market Information

No MHRA marketing authorisation for aminophylline is currently recorded in this evidence pack (market status: not marketed; 0 authorisations on record). This most likely represents a **data gap** in the evidence collection process rather than the true regulatory position, as aminophylline is a long-established compound listed in the **British National Formulary (BNF Section 3.1.3 — Theophylline)** and is available in UK hospitals for intravenous use in acute severe asthma and neonatal apnoea. Oral modified-release theophylline preparations (e.g., Nuelin SA, Slo-Phyllin) are also licensed in the UK.

Clinicians should consult the BNF and the relevant Summary of Product Characteristics (SmPC) for current prescribing, dosing, and monitoring guidance. The MHRA product licence register should be queried directly to confirm current authorisation status.

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at [https://yellowcard.mhra.gov.uk/](https://yellowcard.mhra.gov.uk/).

> **Clinical note for context:** Although formal safety data was not available in this evidence pack, aminophylline carries a well-recognised **narrow therapeutic index**. Theophylline plasma concentrations above 20 mg/L are associated with serious toxicity including ventricular arrhythmias, hypokalaemia, and generalised seizures. Routine therapeutic drug monitoring (target range 10–20 mg/L) is standard practice. Numerous pharmacokinetic interactions are documented (e.g., accelerated clearance in hyperthyroidism and with enzyme inducers; reduced clearance with ciprofloxacin, erythromycin, and cimetidine). These considerations are particularly relevant when evaluating any new indication in an unselected migraine population.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The adenosine receptor antagonism hypothesis linking aminophylline to migraine is biologically coherent and supported by indirect clinical observations and a recent narrative review (PMID 38059379); however, no prospective clinical trial evidence exists, and the current evidence base does not yet support a formal repurposing development decision. The narrow therapeutic index and potential for serious adverse effects at supratherapeutic concentrations add further complexity.

**To proceed, the following is needed:**

- **Confirm MOA and safety data:** Retrieve full mechanism of action and contraindication data from DrugBank API and the current MHRA SmPC; close Data Gap DG001 (MHRA warnings/contraindications) and DG002 (MOA) before formal safety screening (Stage S1)
- **Define the target research question precisely:** Distinguish between (a) acute migraine abortive therapy, (b) prevention, or (c) a specific subgroup such as post-dural puncture headache — for which observational evidence appears strongest
- **Conduct a prospective observational or Phase 2 proof-of-concept study:** With pre-specified primary endpoints (e.g., pain-free rate at 2 hours), therapeutic drug monitoring, and robust safety monitoring including cardiac rhythm assessment
- **Assess route-of-administration feasibility:** IV administration is impractical for outpatient migraine management; oral bioavailability, target plasma concentrations, and patient acceptability must be characterised for any community-based indication
- **Review drug interaction profile:** Particularly relevant in migraine patients who frequently use triptans, NSAIDs, and prophylactic agents (beta-blockers, topiramate, amitriptyline)
- **Engage with MHRA via Scientific Advice:** Given the novel indication and narrow therapeutic index, early regulatory dialogue is advisable before committing to a full development programme

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates identified by TxGNN require clinical validation before any therapeutic application. This report has been prepared in accordance with YMYL (Your Money or Your Life) content standards; clinicians should always refer to authoritative sources including the BNF, MHRA SmPC, and NICE guidance when making prescribing decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

