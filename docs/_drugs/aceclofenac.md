---
layout: default
title: Aceclofenac
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Aceclofenac
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

# Aceclofenac: From Musculoskeletal Pain and Inflammation to Brachyolmia-Amelogenesis Imperfecta Syndrome

---

## One-Sentence Summary

Aceclofenac is a non-steroidal anti-inflammatory drug (NSAID) approved internationally for the management of pain and inflammation in conditions such as rheumatoid arthritis, osteoarthritis, and ankylosing spondylitis, though it does not currently hold a marketing authorisation in the United Kingdom.
The TxGNN model predicts it may be effective for **Brachyolmia-Amelogenesis Imperfecta Syndrome**, however there are **no clinical trials** and **no publications** currently supporting this direction, and the prediction carries a high risk of being a false positive driven by knowledge graph topology rather than genuine therapeutic applicability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK marketing authorisation; approved internationally for rheumatoid arthritis, osteoarthritis, and ankylosing spondylitis |
| Predicted New Indication | Brachyolmia-Amelogenesis Imperfecta Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Aceclofenac in this Evidence Pack. Based on established pharmacological knowledge, Aceclofenac is a phenylacetic acid-derived NSAID that exerts its effects primarily through inhibition of cyclooxygenase (COX-1 and COX-2) enzymes, reducing prostaglandin E2 synthesis and thereby producing analgesic and anti-inflammatory effects. It also downregulates pro-inflammatory cytokines including IL-1β and TNF-α, which underpins its efficacy in inflammatory joint disease such as rheumatoid arthritis and ankylosing spondylitis.

Brachyolmia-amelogenesis imperfecta syndrome is an extremely rare congenital disorder characterised by two co-occurring features: skeletal dysplasia causing short-trunk dwarfism (due to vertebral abnormalities, i.e. brachyolmia) and defective tooth enamel formation (amelogenesis imperfecta). The condition is driven by mutations in genes such as *TRPV4* or *SLC26A2*, which cause structural abnormalities in bone and cartilage through developmental, non-inflammatory pathways unrelated to prostaglandin signalling.

There is no established mechanistic link between COX inhibition and the genetic pathogenesis of this syndrome. The TxGNN model's high prediction score (99.89%) most likely reflects shared skeletal and cartilage tissue co-occurrence features within the knowledge graph rather than a genuine therapeutic relationship — a pattern recognised as a common source of false positives in graph-based prediction models. Aceclofenac might theoretically provide non-specific symptomatic pain relief in patients with skeletal dysplasia, but this is a class effect of all NSAIDs and does not constitute a meaningful repurposing opportunity for disease modification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Aceclofenac does not currently hold a marketing authorisation in the United Kingdom and is not listed in the British National Formulary (BNF). There are no MHRA-approved products for this drug, and it has no history of NICE technology appraisal in this indication or any other.

For reference, Aceclofenac has received regulatory approval in several other jurisdictions — including Spain (originally via a European mutual recognition procedure), South Korea, and India — where it is indicated for musculoskeletal inflammatory conditions including rheumatoid arthritis, osteoarthritis, and ankylosing spondylitis. Any future UK application would require a full MHRA submission and would not benefit from a grandfathered authorisation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.89%), brachyolmia-amelogenesis imperfecta syndrome is a purely genetic skeletal developmental disorder with no inflammatory aetiology. The COX-inhibition mechanism of Aceclofenac has no plausible connection to *TRPV4* or *SLC26A2* gene dysfunction, and there is a complete absence of supporting clinical trial or published literature evidence. This prediction is assessed as a high-probability false positive.

**To proceed, the following is needed:**
- Formal mechanistic review by a rare disease specialist or clinical geneticist to confirm or definitively exclude any theoretical link between prostaglandin/COX pathways and *TRPV4*/*SLC26A2* function
- Retrieval of the full Aceclofenac SmPC (from a jurisdiction where it is authorised, e.g. Spain or South Korea) to complete the safety and MOA profile
- Review of MHRA authorisation requirements and feasibility prior to any UK development pathway
- Separate evaluation of the rank 8 predicted indication — **Inflammatory Spondylopathy (L3 evidence, "Proceed with Guardrails")** — which represents a substantially more clinically plausible repurposing direction for Aceclofenac, supported by 3 disease-relevant clinical trials and a recognised NSAID mechanism in ankylosing spondylitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

