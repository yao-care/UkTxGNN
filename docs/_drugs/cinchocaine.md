---
layout: default
title: Cinchocaine
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 7
---

# Cinchocaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cinchocaine: From Local Anaesthesia to Bronchitis

## One-Sentence Summary

Cinchocaine (also known as dibucaine) is a potent amide-type local anaesthetic primarily used for topical and spinal anaesthesia.
The TxGNN model predicts it may be effective for **Bronchitis**,
however there are currently **no clinical trials** and **no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia (topical and spinal) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (Model prediction only) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacology, cinchocaine is a potent local anaesthetic belonging to the amide class. It acts primarily by blocking voltage-gated sodium channels, thereby inhibiting nerve impulse conduction. It has historically been used for surface anaesthesia, spinal anaesthesia, and in topical preparations for haemorrhoidal and anorectal conditions.

The mechanistic link between cinchocaine and bronchitis is considered very weak. While there is limited evidence that inhaled local anaesthetics (notably lidocaine) can suppress the cough reflex via airway nerve blockade, cinchocaine has a significantly higher systemic toxicity profile than lidocaine, making such an application impractical. Sodium channel blockade does not address the underlying pathology of bronchitis, which involves airway infection, inflammation, and mucus hypersecretion.

Furthermore, cinchocaine lacks anti-inflammatory, anti-infective, or mucolytic properties that would be relevant to bronchitis treatment. The high TxGNN prediction score (99.77%) likely reflects structural or network-level associations in the knowledge graph rather than a genuine therapeutic mechanism. Without any supporting clinical or preclinical evidence, this prediction should be interpreted with considerable caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

*Searches were conducted on ClinicalTrials.gov and the WHO ICTRP on 26 March 2026 for cinchocaine in combination with all seven predicted indications. No results were returned.*

## Literature Evidence

Currently no related literature available.

*PubMed searches were conducted on 26 March 2026 for cinchocaine paired with each predicted indication. No relevant publications were identified.*

## UK Market Information

Cinchocaine currently holds no MHRA marketing authorisations in the United Kingdom. No licensed products were identified in the evidence pack.

## Additional Predicted Indications

The TxGNN model generated six further predictions beyond bronchitis. All share the same evidence profile (L5, no clinical or literature support) and a **Hold** recommendation:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Plausibility |
|------|---------------------|-------------|--------------------------|
| 2 | Acrodermatitis chronica atrophicans | 99.76% | None — requires antibiotic treatment for *Borrelia burgdorferi* infection |
| 3 | Neonatal dermatomyositis | 99.72% | None — autoimmune inflammatory myopathy; sodium channel blockade has no immunomodulatory effect |
| 4 | Secondary interstitial lung disease in childhood (connective tissue disease-associated) | 99.72% | None — requires antifibrotic or immunosuppressive therapy |
| 5 | Acne keloid | 99.67% | Very weak — local anaesthetics may assist procedurally but have no intrinsic anti-scarring activity |
| 6 | Hydroa vacciniforme, familial | 99.66% | None — rare photosensitivity disorder linked to EBV; requires photoprotection and immunotherapy |
| 7 | Amyopathic dermatomyositis | 99.65% | None — autoimmune skin disease requiring hydroxychloroquine or immunosuppressants |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Key warnings, contraindications, and drug interaction data were not available in the evidence pack. Prescribers should consult the BNF monograph for cinchocaine and relevant product SmPCs before considering any off-label use.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predicted indications are supported solely by computational modelling (TxGNN), with no clinical trials, no published literature, and no mechanistic plausibility to substantiate repurposing. Cinchocaine is a potent local anaesthetic with a narrow therapeutic index and significant systemic toxicity, and it currently holds no MHRA marketing authorisation in the UK. The absence of any corroborating evidence, combined with weak-to-absent mechanistic links across all predictions, does not justify progression at this time.

**To proceed, the following would be needed:**
- Detailed mechanism of action data and pharmacokinetic profiling relevant to the predicted indications
- Preclinical studies demonstrating activity of cinchocaine (or sodium channel blockade more broadly) in bronchitis or inflammatory airway models
- Identification of a viable route of administration with an acceptable safety margin
- UK regulatory pathway assessment, given the absence of a current marketing authorisation
- Safety data including SmPC warnings, contraindications, and drug–drug interactions

---

*This report was generated on 5 April 2026 based on evidence collected up to 5 April 2026. Results are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

