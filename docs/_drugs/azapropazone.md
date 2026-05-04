---
layout: default
title: Azapropazone
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Azapropazone
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

# Azapropazone: From Inflammatory Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Azapropazone is a pyrazolone-class non-steroidal anti-inflammatory drug (NSAID) historically used in the management of inflammatory rheumatic conditions — including ankylosing spondylitis and rheumatoid arthritis — though it is no longer authorised in the United Kingdom.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare autosomal recessive skeletal dysplasia, achieving a prediction score of **99.77%**.
However, **no clinical trials or published literature** currently support this specific direction; the strongest contextual evidence in this pack relates to the rank-10 prediction, inflammatory spondylopathy, which is backed by **6 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not listed in UK regulatory data; historically used for ankylosing spondylitis and inflammatory arthritis |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, azapropazone is a pyrazolone-class NSAID with anti-inflammatory, analgesic, and uricosuric properties. Its efficacy in inflammatory musculoskeletal conditions — particularly ankylosing spondylitis and psoriatic arthropathy — has been demonstrated in controlled clinical trials (see literature section below). The drug inhibits prostaglandin synthesis and may modulate inflammatory cascades relevant to connective tissue and joint disease.

Acromesomelic dysplasia, Hunter-Thompson type is caused by loss-of-function mutations in the *CDMP1* (GDF5) gene, which encodes cartilage-derived morphogenetic protein 1, a bone morphogenetic protein (BMP) family member critical for skeletal patterning and chondrogenesis. The hypothetical mechanistic link between NSAID activity and this genetic skeletal dysplasia is not immediately apparent from first principles; the TxGNN model likely reflects shared network-level molecular signatures within the knowledge graph rather than a direct therapeutic mechanism.

Notably, all 10 top-ranked TxGNN predictions for azapropazone cluster within musculoskeletal, skeletal, and rheumatological disease categories — including rheumatoid vasculitis, polyarticular juvenile rheumatoid arthritis, inflammatory spondylopathy, and Kümmell disease — which is broadly consistent with its established anti-inflammatory pharmacological profile. This clustering strengthens biological plausibility for the drug class, even if the evidence for the specific top-ranked rare disease indication remains preclinical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No published literature was identified for the top-ranked indication (Acromesomelic Dysplasia, Hunter-Thompson Type).

---

**Supplementary: Literature for Rank 10 — Inflammatory Spondylopathy**

The following publications were retrieved in the evidence search for **inflammatory spondylopathy** (TxGNN rank 10; score 99.52%). They provide direct evidence of azapropazone's activity in inflammatory spinal disease, which informs mechanistic plausibility across the broader cluster of musculoskeletal predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4604141](https://pubmed.ncbi.nlm.nih.gov/4604141/) | 1974 | Controlled trial | *Rheumatology and Rehabilitation* | Azapropazone in ankylosing spondylitis: controlled clinical trial demonstrating therapeutic benefit |
| [770082](https://pubmed.ncbi.nlm.nih.gov/770082/) | 1976 | RCT (crossover) | *Current Medical Research and Opinion* | Double-blind crossover: azapropazone 1,200 mg/day vs indomethacin 100 mg/day in psoriatic arthritis (n=34) and Reiter's disease (n=16) — no significant overall difference in efficacy |
| [369020](https://pubmed.ncbi.nlm.nih.gov/369020/) | 1978 | Review/Commentary | *Terapevticheskii Arkhiv* | Drug therapy of ankylosing spondyloarthritis (Bechterew's disease), includes azapropazone |
| [7282105](https://pubmed.ncbi.nlm.nih.gov/7282105/) | 1980 | RCT | *Zeitschrift für Rheumatologie* | Double-blind trial: azapropazone vs indomethacin in 60 patients with ankylosing spondylitis — comparable therapeutic effect; azapropazone numerically favoured on chest expansion and patient preference |
| [6999577](https://pubmed.ncbi.nlm.nih.gov/6999577/) | 1980 | Clinical study | *Reumatologia* | Clinical evaluation of NSAIDs in rheumatoid arthritis and ankylosing spondylitis, including azapropazone comparator arm |
| [11208503](https://pubmed.ncbi.nlm.nih.gov/11208503/) | 2001 | Case report | *Medical Science Monitor* | Ankylosing spondylitis with peripheral arthritis refractory to conventional therapy (including azapropazone); successfully controlled with cyclosporine |

---

## UK Market Information

Azapropazone does not currently hold a marketing authorisation granted by the MHRA and is not listed in the BNF as an available product.

> **Historical context:** Azapropazone was previously marketed in the United Kingdom under the brand name **Rheumox®**. Following recommendations from the Committee on Safety of Medicines (CSM), its licence was substantially restricted in 1994 and the product was subsequently withdrawn from the UK market due to a disproportionate risk of serious adverse gastrointestinal events and clinically significant interactions with anticoagulants (particularly warfarin). It is not available via NHS prescription.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Additional context:** No current UK SmPC exists, as the product is not authorised. Clinicians should note that azapropazone — as a pyrazolone-class NSAID — carries risks characteristic of this drug class: upper gastrointestinal haemorrhage and ulceration, renal impairment, fluid retention, and cardiovascular risk. Azapropazone also has a documented pharmacokinetic interaction with **warfarin** (potentiates anticoagulant effect), which contributed significantly to its UK market withdrawal. Any research use would require prospective safety data collection.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or published literature evidence supports azapropazone for acromesomelic dysplasia, Hunter-Thompson type (the top-ranked TxGNN prediction), and this rare genetic skeletal dysplasia lacks a clear mechanistic connection to azapropazone's known anti-inflammatory pharmacology. Furthermore, azapropazone is not authorised in the UK, and its previous market withdrawal on safety grounds represents a substantial barrier to clinical development without a well-defined risk mitigation strategy.

**To proceed, the following is needed:**

- **Mechanism of action data** — full MOA characterisation (DrugBank, primary literature) to identify whether azapropazone interacts with BMP/GDF5 signalling pathways relevant to acromesomelic dysplasia
- **Preclinical evidence** — in vitro or animal model studies investigating any effect of azapropazone on chondrogenesis or skeletal patterning
- **Safety reassessment** — a formal benefit–risk analysis for the target rare disease population, with particular attention to the GI toxicity and warfarin interaction profile that led to withdrawal
- **Regulatory pathway clarification** — a new MHRA marketing authorisation application (MAA) or consideration of orphan medicinal product designation (given the rarity of the target condition) would be required before any clinical use in the UK
- **Clinical expert consultation** — input from skeletal dysplasia specialists and paediatric rheumatologists on biological plausibility and unmet need

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

