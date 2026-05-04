---
layout: default
title: Cholesterol
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Cholesterol
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

# Cholesterol: From No Approved Therapeutic Indication to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Cholesterol (DB04540) is an endogenous lipid molecule with no approved therapeutic indication in any jurisdiction.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
however all **50 clinical trials** and **20 publications** identified relate to drugs that *lower* cholesterol in HoFH — directly contradicting the hypothesis of administering cholesterol as a treatment. This prediction represents a **classic reverse false positive** driven by strong pathological (not therapeutic) associations in the knowledge graph.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None — cholesterol is an endogenous biological molecule with no approved therapeutic use |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L5 (Model prediction only; no supportive therapeutic evidence) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

**It is not.** This prediction is a well-characterised failure mode of knowledge-graph-based drug repurposing models. Cholesterol is the central pathological molecule in HoFH — the disease is defined by the inability to clear LDL cholesterol from the bloodstream due to bi-allelic mutations in the LDL receptor pathway. TxGNN has identified the exceptionally strong *association* between cholesterol and HoFH within its knowledge graph, but it has mistakenly interpreted this pathological relationship as a potential therapeutic one.

All clinical evidence points in the opposite direction: every registered clinical trial for HoFH aims to *reduce* cholesterol levels (via PCSK9 inhibitors, ANGPTL3 antibodies, MTP inhibitors, antisense oligonucleotides, CETP inhibitors, or LDL apheresis). Administering exogenous cholesterol to patients with HoFH would be expected to worsen the disease, not treat it.

Furthermore, cholesterol has no established mechanism of action as a therapeutic agent. It is not formulated as a medicine, holds no marketing authorisation in the UK or any other regulatory jurisdiction, and has no SmPC or BNF entry. The remaining nine predicted indications in this evidence pack (multiple endocrine neoplasia, HIV, platelet disorders, HER2+ breast cancer, and several veterinary diseases) are similarly implausible, with several representing animal diseases entirely inapplicable to human medicine.

## Clinical Trial Evidence

All identified trials investigate drugs that *lower* cholesterol in HoFH patients. None investigate cholesterol itself as a therapeutic agent.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05611528](https://clinicaltrials.gov/study/NCT05611528) | Phase 3 | Completed | 10 | Evinacumab (anti-ANGPTL3) real-world safety/efficacy in HoFH in Canada |
| [NCT03851705](https://clinicaltrials.gov/study/NCT03851705) | Phase 3 | Completed | 56 | ORION-5: Inclisiran (PCSK9 siRNA) safety/tolerability/efficacy in HoFH |
| [NCT04659863](https://clinicaltrials.gov/study/NCT04659863) | Phase 3 | Completed | 13 | ORION-13: Inclisiran in adolescents with HoFH |
| [NCT03156621](https://clinicaltrials.gov/study/NCT03156621) | Phase 3 | Completed | 69 | Alirocumab (anti-PCSK9) vs placebo in HoFH — LDL-C reduction at 12 weeks |
| [NCT00607373](https://clinicaltrials.gov/study/NCT00607373) | Phase 3 | Completed | 51 | Mipomersen (apoB antisense) as add-on therapy in HoFH |
| [NCT00730236](https://clinicaltrials.gov/study/NCT00730236) | Phase 3 | Completed | 29 | Lomitapide (MTP inhibitor) long-term LDL-C lowering in HoFH |
| [NCT04034485](https://clinicaltrials.gov/study/NCT04034485) | Phase 3 | Completed | 65 | LIB003 vs evolocumab cross-over in HoFH |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | Completed | 20 | Rosuvastatin in children/adolescents with HoFH |
| [NCT00263081](https://clinicaltrials.gov/study/NCT00263081) | Phase 3 | Terminated | 44 | TAK-475 (squalene synthase inhibitor) — programme terminated |
| [NCT01841684](https://clinicaltrials.gov/study/NCT01841684) | Phase 3 | Terminated | 2 | Anacetrapib (CETP inhibitor) in HoFH — terminated, only 2 enrolled |

**Key interpretation:** Every trial listed above tests a cholesterol-*lowering* intervention. The therapeutic direction is diametrically opposite to administering cholesterol.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32813947](https://pubmed.ncbi.nlm.nih.gov/32813947/) | 2020 | RCT | N Engl J Med | Evinacumab significantly reduced LDL-C in HoFH patients including those with null-null LDLR variants |
| [37860863](https://pubmed.ncbi.nlm.nih.gov/37860863/) | 2024 | Clinical Trial | Circulation | Evinacumab efficacy and safety in paediatric HoFH patients |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | Clinical Trial | Circulation | ORION-5: Inclisiran produced durable LDL-C reduction in HoFH |
| [40391436](https://pubmed.ncbi.nlm.nih.gov/40391436/) | 2025 | Clinical Trial | Circulation | ORION-13: Inclisiran in adolescents with genetically confirmed HoFH |
| [38695169](https://pubmed.ncbi.nlm.nih.gov/38695169/) | 2024 | Outcomes Study | Arterioscler Thromb Vasc Biol | Evinacumab demonstrated durable LDL-C response and improved CV outcomes |
| [37130090](https://pubmed.ncbi.nlm.nih.gov/37130090/) | 2023 | Consensus Statement | Eur Heart J | EAS 2023 update: pragmatic recommendations for HoFH diagnosis and treatment |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | Review of novel LDL-C lowering pharmacotherapies for HoFH |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Retrospective Cohort | Lancet | Worldwide HoFH experience: clinical, genetic characteristics and outcomes |
| [38353972](https://pubmed.ncbi.nlm.nih.gov/38353972/) | 2024 | Cohort Study | JAMA Cardiol | Sex differences in HoFH diagnosis, treatment, and CV outcomes |
| [27246162](https://pubmed.ncbi.nlm.nih.gov/27246162/) | 2016 | Consensus Statement | Lancet Diabetes Endocrinol | IAS panel defining severe FH and implications for management |

**Key interpretation:** All publications concern the *disease* HoFH and its management via cholesterol-lowering strategies. None provide evidence supporting cholesterol as a therapeutic agent.

## UK Market Information

Cholesterol holds no marketing authorisation in the United Kingdom. There are no MHRA-licensed products, no NICE technology appraisals, and no BNF entries for cholesterol as a therapeutic agent.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

As cholesterol has no marketing authorisation, no SmPC exists. Exogenous cholesterol administration would be expected to elevate serum LDL-C levels and could accelerate atherosclerotic cardiovascular disease, particularly in patients with pre-existing lipid metabolism disorders.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is a classic reverse false positive. Cholesterol is the causative pathological molecule in HoFH, not a treatment for it. The TxGNN knowledge graph correctly identifies the strong association between cholesterol and HoFH but incorrectly interprets this pathological relationship as a therapeutic one. All 50 clinical trials and 20 publications identified in the evidence pack concern drugs designed to *lower* cholesterol — the opposite therapeutic direction. Additionally, cholesterol is not a licensed medicine in any jurisdiction, has no established mechanism of action as a therapeutic agent, and 4 of the 10 predicted indications are veterinary diseases (infectious bovine rhinotracheitis, malignant catarrh, feline AIDS, simian immunodeficiency virus) inapplicable to human medicine.

**This candidate should not proceed further in the evaluation pipeline.**

**If future review is warranted, the following would be needed:**
- Fundamental re-evaluation of TxGNN scoring methodology to distinguish pathological associations from therapeutic relationships
- Implementation of a "directionality filter" to flag cases where the drug is a known causative factor for the predicted disease
- Exclusion of veterinary diseases from the predicted indications output
- Verification that candidate molecules hold at least one marketing authorisation as a therapeutic agent before entering the evaluation pipeline

---

> *Disclaimer: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before any therapeutic application. Report suspected adverse reactions via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

