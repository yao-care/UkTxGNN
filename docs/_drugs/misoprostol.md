---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 2
---

# Misoprostol
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

# Misoprostol: From Peptic Ulcer Prevention to Amenorrhea

## One-Sentence Summary

Misoprostol is a synthetic prostaglandin E1 (PGE1) analogue, originally licensed for the prevention of NSAID-induced gastric and duodenal ulcers and long established (in combination with mifepristone) in obstetric practice for medical management of miscarriage and pregnancy termination. The TxGNN model predicts it may be effective for **Amenorrhea**, with **no registered clinical trials** and **7 supporting publications**, though the mechanistic link is indirect and evidence quality is currently limited to mechanism-based reasoning (L4).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of NSAID-induced gastric/duodenal ulcers (established use; no UK licence record available in this evidence pack) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data for misoprostol is not present in the structured drug record of this evidence pack, but the model's own rationale for this candidate supplies the relevant pharmacology: misoprostol is a PGE1 analogue acting on EP2/EP3 receptors in the myometrium, where it induces uterine contraction and cervical softening. Clinically, it is used together with mifepristone in the management of missed abortion and anembryonic pregnancy (embryonic demise), conditions that present with secondary amenorrhea because the pregnancy has failed to progress.

The mechanistic bridge to amenorrhea is therefore real but narrow: misoprostol promotes expulsion of retained products of conception, which allows a normal menstrual cycle to resume — it does not act directly on the hypothalamic-pituitary-ovarian axis or endometrium in the way a treatment for primary or endocrine-driven amenorrhea (e.g. PCOS, hypothalamic amenorrhea) would need to. In other words, the drug resolves a specific obstetric cause of amenorrhea rather than treating amenorrhea as a general condition.

This distinction matters for interpreting the TxGNN score. The very high prediction score (99.64%) most likely reflects the proximity, within the knowledge graph, of the "amenorrhea" disease node to "missed abortion"/"pregnancy termination" nodes, rather than a direct pharmacological relationship to amenorrhea in its broader clinical sense. The prediction should therefore be read as **mechanistically plausible only in the specific context of pregnancy-related amenorrhea**, not as evidence for a general amenorrhea indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging RCT (n=2,500) of mifepristone (50–150 mg) plus oral misoprostol 200 µg for termination of ultra-early pregnancy (amenorrhea ≤35 days); establishes efficacy/safety of lower-dose regimens for medical abortion, not a trial of amenorrhea treatment per se |
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | Cohort | Reproductive Sciences | 744 women with ultra-early pregnancy (amenorrhea ≤35 days) comparing self-administered vs hospital-administered low-dose mifepristone + misoprostol for medical abortion |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort | Human Reproduction | Evaluated low-dose mifepristone combined with misoprostol taken before expected menstruation to prevent/interrupt unintended pregnancy |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohort | J Obstet Gynaecol Res | Self-administered low-dose mifepristone + misoprostol for early medical abortion; reports efficacy and safety outcomes |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Review of endometrial ablation for abnormal uterine bleeding; provides gynaecological background only and does not evaluate misoprostol |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review/Case series | BMJ | Early description of medical management of missed abortion and anembryonic pregnancy using prostaglandin-based protocols |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Case of acute fatty liver of pregnancy presenting with amenorrhea; a differential-diagnosis case report, not a misoprostol treatment study |

**Note:** the majority of this literature concerns medical management of failed/unwanted pregnancy in which amenorrhea is an inclusion criterion or presenting feature, rather than trials of misoprostol as a treatment for amenorrhea itself.

---

## UK Market Information

No UK marketing authorisation records are available in this evidence pack, consistent with the reported "Not Marketed" status (0 licences on file).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Additional Model Signal (Lower Priority, Not Recommended for Action)

The evidence pack also contains a second TxGNN prediction for misoprostol: **atypical coarctation of aorta** (score 99.30%, rank 6347, Evidence Level L5, decision stage S0, recommendation Hold). This rationale is purely theoretical — it draws an analogy to alprostadil (another PGE1 analogue used to maintain ductal patency in ductal-dependent congenital heart disease) rather than any direct evidence for misoprostol. There are **zero clinical trials and zero publications** supporting this candidate, and misoprostol's pharmacokinetics (oral, short half-life) differ substantially from alprostadil's requirement for continuous intravenous infusion. This candidate should be treated as a structural knowledge-graph artefact rather than a genuine repurposing signal, and no further action is warranted at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhea candidate is supported only by mechanism-based reasoning (L4) and literature that addresses a related but distinct clinical scenario (medical management of missed abortion/pregnancy termination) rather than amenorrhea treatment directly. No clinical trials evaluate misoprostol for amenorrhea, and a Blocking data gap (missing MHRA/SmPC warnings and contraindications) currently prevents a safety (S1) assessment.

**To proceed, the following is needed:**
- UK SmPC/BNF safety data — warnings, contraindications, and drug interactions (Blocking gap)
- Confirmed mechanism-of-action documentation from DrugBank
- Clarification of target population: this mechanism supports secondary amenorrhea due to retained products of conception, not primary/endocrine amenorrhea — the intended clinical use case needs to be defined before further evaluation
- Dedicated studies evaluating misoprostol specifically for amenorrhea, rather than relying on pregnancy-termination literature as a proxy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

