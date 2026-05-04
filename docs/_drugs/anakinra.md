---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Rheumatoid Arthritis to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra (Kineret) is a recombinant interleukin-1 receptor antagonist (IL-1Ra), established in clinical practice for rheumatoid arthritis and autoinflammatory conditions including Familial Mediterranean Fever and neonatal-onset multisystem inflammatory disease (NOMID).
The TxGNN model ranks **Extracutaneous Mastocytoma** as its top novel indication with a prediction score of 99.93%; however, this prediction is supported by **no clinical trials and no published literature**, placing it at evidence level L5.
Across the full top-10 predictions, the strongest clinically supported candidate is **Autosomal Recessive Familial Mediterranean Fever** (rank 3, L2 evidence, 20 publications), which carries substantially more actionable evidence and a direct mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis; autoinflammatory conditions (no UK licence records retrieved — see note below) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | No marketing authorisation on record |
| Number of Marketing Authorisations | 0 (on record) |
| Recommended Decision | Hold |

> **Note on UK market data:** This evidence pack retrieved zero marketing authorisations for Anakinra in the UK. This almost certainly reflects a data collection gap rather than genuine absence of approval, as Kineret (anakinra) holds MHRA authorisation for rheumatoid arthritis and NOMID/CINCA. Clinicians should verify directly via the [MHRA product licence register](https://products.mhra.gov.uk/). A separate search against MHRA Public Assessment Reports is also recommended.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established clinical knowledge, anakinra is a recombinant, non-glycosylated form of the human IL-1 receptor antagonist (IL-1Ra) that competitively inhibits both IL-1α and IL-1β from binding to the interleukin-1 type I receptor (IL-1R1). By blocking this receptor, anakinra suppresses downstream NF-κB activation and the pro-inflammatory cytokine cascades that drive fever, joint destruction, serositis, and systemic autoinflammation.

Extracutaneous mastocytoma is a rare, benign mast cell proliferation occurring at extra-cutaneous sites, for which surgical excision remains the primary treatment. Mast cells do produce IL-1β and express IL-1 receptors, creating a theoretical topological connection within the TxGNN knowledge graph. However, the dominant pathological driver of mastocytoma — and of systemic mastocytosis more broadly — is an activating KIT mutation (D816V), which is entirely independent of the IL-1 signalling axis. There is currently no preclinical or clinical evidence that IL-1 blockade influences mast cell neoplasm growth or disease course. The high TxGNN prediction score most likely reflects an indirect graph-topology association between mast cells and IL-1, rather than a validated mechanistic pathway.

It is important for context that several other indications within the top-10 predictions carry considerably stronger mechanistic and clinical support. **Autosomal Recessive Familial Mediterranean Fever** (rank 3, L2) is driven by MEFV gene mutations that cause pyrin inflammasome over-activation and excessive IL-1β secretion — precisely the pathway that anakinra blocks. The AIRTRIP Phase 3 RCT (NCT02059291) has demonstrated efficacy in colchicine-resistant FMF, although this trial was not captured in the current data pull (a known database coverage gap). **Pyogenic Autoinflammatory Syndrome** (PAPA/PASH/PAPASH spectrum, rank 9, L3) similarly involves PSTPIP1-driven IL-1β overproduction, and a scoping review and multiple case series directly report anakinra efficacy in this population. These two indications represent considerably more clinically actionable repurposing opportunities than the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No marketing authorisation records for Anakinra were retrieved in this data pull. This is likely a data gap rather than a genuine absence of UK approval. Healthcare professionals should consult the following authoritative sources directly:

- **MHRA Product Licence Register:** [https://products.mhra.gov.uk/](https://products.mhra.gov.uk/)
- **BNF classification:** Musculoskeletal diseases → Cytokine modulators (section 10.1.3)
- **NICE Technology Appraisal TA195:** Anakinra for the treatment of rheumatoid arthritis (2009, guidance not recommended as routine use in RA; relevant for off-label NOMID/autoinflammatory indications)
- **Kineret SmPC:** Available via the electronic medicines compendium (emc) at [https://www.medicines.org.uk/emc](https://www.medicines.org.uk/emc)

Based on publicly available information, Kineret is MHRA-authorised for: (1) rheumatoid arthritis in adults, in combination with methotrexate, in patients with inadequate response to DMARDs alone; and (2) neonatal-onset multisystem inflammatory disease (NOMID/CINCA). These records should be verified and retrieved to complete the evidence pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme ([https://yellowcard.mhra.gov.uk/](https://yellowcard.mhra.gov.uk/)).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top prediction for anakinra — extracutaneous mastocytoma — is grounded solely in knowledge graph topology, with no clinical trials, no supporting literature, and no established IL-1 mechanistic rationale specific to this rare benign mast cell tumour. This prediction cannot be meaningfully actioned at the current evidence level.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or in vivo) demonstrating a functional, non-redundant role for IL-1 signalling in extracutaneous mastocytoma pathogenesis
- MOA data retrieval from DrugBank (data gap DG002) to enable a structured mechanistic plausibility assessment
- Correction of the UK marketing authorisation data gap — verify Kineret's full MHRA licence status and retrieve approved indication text for the evidence pack
- MHRA warnings and contraindications (data gap DG001) must be retrieved before any safety screening stage can be completed
- **Priority recommendation:** Redirect investigative effort towards better-supported predictions — in particular, **Autosomal Recessive FMF** (rank 3, L2, *Proceed with Guardrails*) and **Pyogenic Autoinflammatory Syndrome** (rank 9, L3, *Proceed with Guardrails*) — both of which have strong mechanistic justification and existing clinical evidence; the FMF indication would benefit from retrieval of the AIRTRIP Phase 3 trial (NCT02059291) not captured in this data pull
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

