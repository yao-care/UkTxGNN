---
layout: default
title: Cefaclor
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Cefaclor
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

# Cefaclor: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefaclor is a second-generation oral cephalosporin antibiotic, used for the treatment of common bacterial infections of the respiratory tract, urinary tract, and skin.
The TxGNN model's highest-ranked prediction identifies **Hyperamylasemia** as a potential new indication (score: 97.70%); however, **no clinical trials or supporting literature** exist for this direction, and critical mechanistic analysis suggests the model may have misidentified an adverse drug reaction as a therapeutic signal.
A secondary finding worth noting is that **Gonococcal Urethritis** (rank 4) is supported by **6 published clinical studies**, though its contemporary relevance is substantially limited by modern antimicrobial resistance patterns.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (second-generation cephalosporin antibiotic) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 97.70% |
| Evidence Level | L5 (model prediction only — no supporting studies identified) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cefaclor is a second-generation oral cephalosporin antibiotic. Like all beta-lactam antibiotics, it acts by binding to penicillin-binding proteins (PBPs) on the bacterial cell membrane, inhibiting peptidoglycan cross-linking and disrupting cell wall synthesis, ultimately causing bacterial cell lysis. Its antimicrobial spectrum covers many Gram-positive cocci (such as *Streptococcus* spp. and methicillin-sensitive *Staphylococcus aureus*) and selected Gram-negative organisms (such as *Haemophilus influenzae* and *Moraxella catarrhalis*), making it suitable for community-acquired infections.

Hyperamylasemia — an elevation of serum amylase — is most commonly a biochemical marker of pancreatitis, salivary gland disease, or certain metabolic disorders. There is **no established pharmacological mechanism** by which a cephalosporin antibiotic would therapeutically lower elevated serum amylase. On the contrary, published case reports document that Cefaclor can cause a **serum sickness-like reaction (SSLR)** — a well-recognised adverse effect of this particular drug — which may occasionally be accompanied by raised amylase as part of the inflammatory response. It is therefore likely that the TxGNN knowledge graph has inadvertently interpreted a **drug–adverse effect association** (Cefaclor → amylase elevation) as a **drug–treatment relationship**, producing a high model score for a biologically implausible repurposing candidate.

This prediction is considered a **knowledge graph artefact**. The TxGNN score reflects structural proximity between "Cefaclor" and "hyperamylasemia" nodes within the knowledge graph, rather than any genuine mechanistic or clinical rationale. Healthcare professionals should be particularly cautious when a high-scoring TxGNN prediction involves a condition that closely resembles the drug's known adverse effect profile.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Cefaclor currently holds **no MHRA marketing authorisations** and is not commercially available in the United Kingdom. No licensed products, approved indications, or dosage forms are on record with the MHRA.

> **Note for prescribers:** As Cefaclor is not authorised in the UK, there is no UK Summary of Product Characteristics (SmPC) or MHRA-approved patient information leaflet available. If use were considered, reference would need to be made to authorisations held in other jurisdictions (e.g., the United States, European Union, or Japan) and appropriate unlicensed use procedures followed in accordance with MHRA guidance.

---

## Safety Considerations

Please refer to the SmPC from a relevant reference jurisdiction and the BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme (https://yellowcard.mhra.gov.uk/).

> **Known class-level caution:** Cefaclor is specifically associated with a higher rate of serum sickness-like reactions (SSLR) compared with other oral cephalosporins — a consideration of particular relevance to the hyperamylasemia prediction discussed above. This adverse effect profile is an important reason why Cefaclor has largely fallen out of routine clinical use in the UK.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (hyperamylasemia, L5) lacks any clinical or mechanistic foundation and almost certainly represents a knowledge graph error in which an adverse drug reaction has been misclassified as a therapeutic indication. With no supporting clinical trials or literature, no UK marketing authorisation, and a biologically implausible mechanism, there is no basis to proceed with this repurposing hypothesis.

**Overview of All Predicted Indications:**

Across the full set of 10 TxGNN predictions, only one — **Gonococcal Urethritis (rank 4)** — demonstrates any meaningful evidence base. This indication is supported by **6 published clinical studies** dating from 1979 to 1997 (evidence level L3), and the mechanistic rationale is coherent: *Neisseria gonorrhoeae* possesses a bacterial cell wall and was historically sensitive to beta-lactam antibiotics including Cefaclor. However, this repurposing direction faces a significant contemporary barrier: WHO now recommends dual therapy with third-generation cephalosporins (ceftriaxone) due to widespread beta-lactamase production and PBP mutations that have rendered Cefaclor clinically ineffective against modern gonococcal isolates. This prediction is therefore of **historical interest only** and is not recommended for further development.

The remaining 8 predictions (including polyclonal hyperviscosity syndrome, Ureaplasma urethritis, congenital analbuminemia, blood group incompatibility, monoclonal gammopathy, and others) all carry L5 evidence with no mechanistic plausibility and should be disregarded.

**To proceed with any future repurposing work on Cefaclor, the following would be required:**

- Obtain full mechanistic data (MOA) from DrugBank or primary literature to characterise Cefaclor's pharmacological profile comprehensively
- Verify MHRA regulatory pathway for any unlicensed use in the UK context
- Reassess TxGNN knowledge graph edges connecting Cefaclor to haematological and metabolic conditions to identify and correct adverse-effect-as-indication misclassifications
- If gonococcal urethritis is pursued as a historical research question, contemporary minimum inhibitory concentration (MIC) data for UK *N. gonorrhoeae* isolates would be essential to establish whether any clinical utility remains

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates identified by computational models require rigorous clinical validation before any clinical application. All content should be interpreted in conjunction with current clinical guidelines, the BNF, and applicable MHRA guidance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

