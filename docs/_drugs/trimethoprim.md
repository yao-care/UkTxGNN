---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 644
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Trimethoprim: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "Trimethoprim"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "conjunctivitis (disease)"]
---

# Trimethoprim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Trimethoprim: From Urinary Tract Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial originally used for urinary tract infections and several other bacterial infections, including eye infections such as conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so the evidence is model-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (the UK licence record has no indication text, so this comes from the drug's recorded indications, which also include infectious otitis media, pneumocystosis, shigellosis and bacterial conjunctivitis/blepharoconjunctivitis) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trimethoprim is a bacterial dihydrofolate reductase inhibitor. Its efficacy in bacterial infections, including ocular surface infections (often as a topical combination with polymyxin B), is established.

The high score most likely reflects network proximity to its known eye indications (conjunctivitis, acute contagious conjunctivitis, blepharoconjunctivitis) rather than independent evidence. Punctate epithelial keratoconjunctivitis is frequently viral or immune-mediated, for example adenoviral disease or Thygeson's superficial punctate keratitis. An antibacterial agent would not be expected to treat the underlying cause. The mechanistic link is therefore weak. It may apply only where a bacterial component or secondary infection is present, and that has not been verified.

The model also lists conjunctivitis as a prediction. That condition is already an original indication for trimethoprim, so it is not true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

The literature found for the broader condition of conjunctivitis (for example, trials of trimethoprim-polymyxin B eye drops in bacterial conjunctivitis) relates to the existing indication, not to this prediction.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501080W0AAADAD (product code as recorded; not a PL number) | Trimethoprim 100 mg tablets | Tablet | Not stated in the available record |

Only one single-ingredient authorisation is recorded, and it is valid. It is an oral tablet, so no topical ophthalmic route is documented. Route compatibility with the predicted eye indication has not been assessed. Check the BNF and current MHRA/NICE sources for authorised indications.

---

## Safety Considerations

- **Contraindications and conditions of concern (from the knowledge graph, not label text):** inherited porphyria and other porphyrias, kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, folic acid deficiency anaemia, and pyoureter.
- **Drug interactions:** 100 interactions were recorded, and the first 20 are summarised here.
  - *Major:* potassium citrate, potassium bicarbonate, potassium chloride and potassium gluconate. The usual concern with potassium-containing products is additive hyperkalaemia.
  - *Moderate:* metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid and sapropterin.
  - *Unspecified severity:* pantoprazole, omeprazole, doxycycline, clotrimazole, morphine, sucralfate, vancomycin, lactulose and simvastatin.

Label warnings are not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials or publications for this indication. The predicted condition is often viral or immune-mediated, so an antibacterial is unlikely to address its cause. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale for a role in non-bacterial or immune-mediated keratoconjunctivitis
- A literature search specific to punctate epithelial keratoconjunctivitis and trimethoprim, including any bacterial-aetiology subgroups
- An assessment of route compatibility, since the only recorded UK product is an oral tablet
- Label-based warnings and contraindications from the SmPC and BNF
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

