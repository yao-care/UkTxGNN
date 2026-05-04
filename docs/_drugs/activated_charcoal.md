---
layout: default
title: Activated Charcoal
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Activated Charcoal
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

# Activated Charcoal: From Acute Poisoning Management to Jeune Syndrome Situs Inversus

## One-Sentence Summary

Activated charcoal is a non-selective gastrointestinal adsorbent widely used in emergency medicine to reduce systemic absorption of ingested toxins and drugs in acute poisoning.
The TxGNN model predicts it may be effective for **Jeune Syndrome Situs Inversus** (a rare ciliopathy-associated skeletal dysplasia with visceral transposition),
however there are currently **no clinical trials** and **no publications** supporting this specific predicted indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal MHRA marketing authorisation on record; clinically used as an emergency gastrointestinal decontaminant in acute poisoning |
| Predicted New Indication | Jeune Syndrome Situs Inversus |
| TxGNN Prediction Score | 89.94% |
| Evidence Level | L5 |
| UK Market Status | Not currently marketed in the UK |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for activated charcoal from the DrugBank record in this evidence pack. Based on established pharmacological knowledge, activated charcoal is a non-selective gastrointestinal adsorbent. Its high surface area enables it to bind a broad range of drugs and toxins within the GI lumen, thereby preventing or reducing systemic absorption. It is principally recognised in UK emergency medicine for managing acute poisoning episodes, supported by TOXBASE guidance and the National Poisons Information Service (NPIS).

Jeune syndrome (asphyxiating thoracic dystrophy) is a rare autosomal recessive skeletal ciliopathy caused by mutations in cilia-associated genes such as IFT140 and DYNC2H1. These mutations disrupt intraflagellar transport, leading to impaired cilia function and resulting in a narrow thoracic cage with progressive respiratory compromise. The situs inversus variant reflects the visceral transposition that accompanies systemic cilia dysfunction.

There is no identified mechanistic intersection between activated charcoal's non-selective GI adsorption action and the molecular pathology of Jeune syndrome. Activated charcoal has no known targets relevant to ciliary biogenesis, skeletal development, or organ positioning. The TxGNN prediction in this instance almost certainly reflects a knowledge graph topology artefact—a false positive driven by indirect graph connections—rather than a biologically plausible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Activated charcoal currently holds no MHRA marketing authorisations in the United Kingdom and is not recorded as a marketed product in the UK regulatory dataset. Activated charcoal preparations are, however, used in UK clinical practice (emergency departments, intensive care) under the guidance of TOXBASE and the NPIS, though without formal product licences reflected in this dataset. Clinicians should refer to the BNF (Section: Emergency treatment of poisoning) and current NPIS guidance for approved uses.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no plausible mechanistic basis linking activated charcoal's gastrointestinal adsorption mechanism to Jeune syndrome situs inversus, a rare congenital ciliopathy involving skeletal dysplasia and visceral transposition. This prediction is assessed as a TxGNN knowledge graph false positive, with no supporting clinical trials, no relevant publications, no UK marketing authorisation, and no known biological pathway connecting the drug to the disease (Evidence Level L5).

**To proceed, the following is needed:**
- Identification of any biologically plausible mechanism connecting GI adsorption or charcoal-mediated toxin clearance to ciliopathy pathways or skeletal development
- Preclinical evidence (cell model or in vivo) demonstrating any effect of activated charcoal on cilia function, IFT signalling, or thoracic skeletal morphogenesis
- Retrieval of the full DrugBank MOA record and MHRA/NPIS SmPC to rule out any overlooked pharmacological activities
- Expert review by a clinical geneticist or rare disease specialist before any further investigation is contemplated
- If the broader candidate pipeline is of interest, note that **Heart Disease (rank 8)** represents a more scientifically grounded hypothesis within this evidence pack, supported by indirect mechanistic rationale (uremic toxin–cardiovascular axis, acute cardiotoxic drug ingestion) and a larger body of associated literature; this may warrant a separate focused evaluation

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content should be reviewed by a qualified healthcare professional before use in clinical decision-making.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

