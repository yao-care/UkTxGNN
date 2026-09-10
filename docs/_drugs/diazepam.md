---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety and Seizure Disorders to Insomnia

## One-Sentence Summary

Diazepam is a long-established benzodiazepine, classically used for anxiety, seizure disorders, muscle spasm and alcohol withdrawal (the formal original-indication and MOA fields are not populated in this dataset). The TxGNN model predicts it may also be effective for **Insomnia**, with **24 clinical trials** and **18 publications** currently retrieved for this pairing — though, as detailed below, most of this evidence concerns benzodiazepine *discontinuation* rather than new efficacy for insomnia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the regulatory dataset (see Safety Considerations). Diazepam is classically an anxiolytic/sedative-hypnotic, anticonvulsant and skeletal muscle relaxant. |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.9997% (rank 9 of all candidates) |
| Evidence Level | L1 |
| UK Market Status | Not marketed (per current dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug-level record (MOA field flagged as a data gap, DG002). However, the prediction's own rationale supplies the pharmacological link: Diazepam is a positive allosteric modulator of the GABA-A receptor, enhancing inhibitory GABAergic transmission to produce sedative/hypnotic effects. This is a long-established mechanism for benzodiazepines generally, not a novel finding.

This is an important caveat for interpretation: the model's rationale explicitly notes that diazepam-for-insomnia is **not a novel repurposing hypothesis** — it reflects pharmacology that has been known for decades (diazepam already has real-world use as a short-term hypnotic). The "new" value of this signal is therefore limited; the KG/GNN model is essentially confirming class-level knowledge rather than surfacing an unexpected therapeutic link.

Consistent with this, the supporting evidence collected is dominated by studies about *tapering off* benzodiazepine hypnotics (including diazepam) in patients already dependent on them, rather than trials establishing diazepam's efficacy as a treatment for insomnia. This shifts the practical value of the evidence toward safety/dependence management rather than a new treatment opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244711](https://clinicaltrials.gov/study/NCT01244711) | Phase 4 | Terminated | 1 | Pilot study substituting quetiapine for chronic benzodiazepine use in treatment-refractory anxiety/depression with insomnia; terminated early with only 1 participant enrolled. |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, not recruiting | 260 | Randomised trial comparing blinded vs. open-label hypnotic tapering combined with CBT-I to improve discontinuation rates of sedative-hypnotics (including benzodiazepines). |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Behavioural-mechanism intervention to help older adults discontinue long-term sleeping pill (hypnotic) use. |
| [NCT03405493](https://clinicaltrials.gov/study/NCT03405493) | N/A | Completed | 60 | UK community-based sleep therapy/light-box trial for depression; not a diazepam efficacy study. |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for treatment of benzodiazepine dependence; addresses withdrawal rather than diazepam's hypnotic efficacy. |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | Recruiting | 93 | Baclofen used to assist benzodiazepine dose-tapering in patients with benzodiazepine dependence. |
| [NCT04205682](https://clinicaltrials.gov/study/NCT04205682) | Early Phase 1 | Unknown | 52 | RCT of cannabidiol for alcohol withdrawal symptoms; diazepam is not the study drug. |
| [NCT00678691](https://clinicaltrials.gov/study/NCT00678691) | Phase 4 | Completed | 55 | Armodafinil augmentation for fibromyalgia-related fatigue; unrelated to diazepam. |
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | Unknown | 58 | Antioxidant therapy combined with Adepsique® (amitriptyline, perphenazine, diazepam) for chronic tinnitus, assessing inflammatory/oxidative markers. |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Placebo-controlled trial of ramelteon combined with benzodiazepine/non-benzodiazepine hypnotics to assist dose reduction in chronic insomnia. |

**Note:** none of the trials above directly test diazepam's efficacy as a first-line insomnia treatment; the majority concern discontinuation or dose-reduction of hypnotics in dependent populations.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | Double-blind comparison of lormetazepam vs. diazepam (5 mg) in 100 outpatients with insomnia; lormetazepam showed some superiority in sleep onset/duration, but diazepam was an effective active comparator. |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | Reviews small-molecule GABA-A receptor modulators, citing diazepam as a well-known positive allosteric modulator effective for insomnia, anxiety, epilepsy and depression. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica (Zagreb) | Meta-analysis of tranquilizer use in elderly patients with chronic disease, assessing optimal dosing and adverse effects across benzodiazepine-class agents. |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clinical/mechanistic | Cell Mol Biol Lett | Reports that long-term use of benzodiazepines (including diazepam) and Z-drugs is associated with exacerbated breast cancer risk, with proposed molecular mechanisms. |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Review | Frontiers in Pharmacology | Reviews Chinese herbal (Suanzaoren) formulae for insomnia, referencing benzodiazepines including diazepam as standard comparators. |
| [40896345](https://pubmed.ncbi.nlm.nih.gov/40896345/) | 2025 | Review | Integrative Medicine Research | Scoping review of herbal medicine/acupuncture for insomnia comorbid with chronic pain, discussing pharmacological hypnotics as current standard treatment. |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Cohort/Preclinical | Nature Neuroscience | Long-term diazepam treatment enhances microglial synaptic pruning and impairs cognitive performance via mitochondrial TSPO, in mice — a mechanistic safety signal for chronic use. |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Preclinical | J Pharm Biomed Anal | Metabolomic study of Naoling Pian for insomnia in a rat model, using diazepam as the positive control comparator. |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Preclinical | China J Chinese Materia Medica | Ziziphi Spinosae Semen extract tested against depression/insomnia-like behaviour in mice, with diazepam (2 mg/kg) as the positive control drug. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Reviews the pharmacokinetics of anxiolytic drugs, a class that includes diazepam. |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: key warnings, contraindications and drug-interaction data are currently unavailable in this dataset — this is flagged as a Blocking data gap, DG001, that prevents a formal S1 safety pre-screen.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Diazepam's GABA-A mechanism plausibly supports a hypnotic effect, and one historical RCT (6113175) directly compares it to another benzodiazepine hypnotic in insomnia patients — but this reflects an already-established, decades-old use rather than a genuinely novel repurposing signal.
- The bulk of the current evidence base concerns tapering/discontinuation of benzodiazepine hypnotics rather than confirming diazepam's efficacy for insomnia, and long-term-use safety signals (cognitive impairment, cancer association) argue for caution around any new indication for chronic use.

**To proceed, the following is needed:**
- Resolution of the Blocking data gap (DG001): TFDA/UK product label (SmPC) warnings and contraindications, required before any S1 safety pre-screen can proceed.
- Formal mechanism-of-action documentation (DG002) from DrugBank or equivalent, to support a rigorous mechanistic-link analysis.
- Confirmation of actual UK marketing status and licence details, since the current dataset shows zero licences despite diazepam being a long-marketed medicine — this discrepancy should be verified before any market-status conclusions are drawn.
- If pursued, restriction to short-term/limited use given known dependence, tolerance and cognitive-impairment risks with chronic benzodiazepine use for insomnia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

