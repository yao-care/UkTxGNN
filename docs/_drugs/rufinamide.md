---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Rufinamide
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

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

---

## One-Sentence Summary

Rufinamide is a structurally novel triazole-derivative antiseizure medication (Inovelon®), approved by both the EMA and US FDA for adjunctive treatment of seizures associated with Lennox-Gastaut Syndrome (LGS) in children and adults.
The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**, a devastating, neuroinflammation-driven form of super-refractory status epilepticus.
Currently, **no registered clinical trials** and **no direct publications** specifically addressing this indication have been identified; the high TxGNN prediction score of **99.57%** most likely reflects the close topological proximity between FIRES and LGS in the underlying biomedical knowledge graph rather than independent clinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Adjunctive treatment of seizures associated with Lennox-Gastaut Syndrome (LGS) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 (mechanistic plausibility; anecdotal case-level evidence not captured in current dataset) |
| UK Market Status | No marketing authorisation on record |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Rufinamide (1-[2,6-difluorobenzyl]-1H-1,2,3-triazole-4-carboxamide) is a pharmacologically unique compound whose principal mechanism of action is the prolongation of the inactive state of voltage-gated sodium channels. By limiting the frequency of sodium-dependent neuronal action potentials, it produces a broad membrane-stabilising anticonvulsant effect that is mechanistically unrelated to any other antiseizure medication currently available. This mechanism has been validated in three randomised placebo-controlled trials demonstrating significant reduction in total seizures and drop attacks in LGS — a severe, childhood-onset developmental and epileptic encephalopathy characterised by multiple refractory seizure types, abnormal slow spike-and-wave electroencephalographic features, and profound cognitive impairment.

FIRES is an ultra-rare catastrophic epilepsy condition defined by a febrile illness prodrome followed by abrupt onset of super-refractory status epilepticus (SRSE), frequently lasting weeks to months, with severe neuroinflammation as its central pathological driver. While FIRES and LGS are pathophysiologically distinct entities, they share a constellation of clinically salient features: extreme seizure burden, profound multi-drug treatment refractoriness, childhood onset, and long-term neurodevelopmental sequelae. In the biomedical knowledge graph underpinning TxGNN, this phenotypic and clinical overlap likely positions FIRES and LGS as closely connected nodes — a relationship that plausibly explains the exceptionally high prediction score of 0.9957.

From a pharmacological standpoint, sustained sodium channel hyperactivation contributes to the perpetuation of ictal discharge during SRSE. Rufinamide's mechanism of action could theoretically attenuate this activity by reducing neuronal excitability during the acute FIRES phase. Sporadic clinical reports of Rufinamide being incorporated into polytherapy regimens for paediatric SRSE and FIRES do exist in the broader literature, although none are captured in the current evidence dataset. The mechanistic rationale is therefore plausible, but must be interpreted with appropriate caution in the absence of any controlled evidence; FIRES management also necessitates concurrent anti-inflammatory strategies such as the ketogenic diet, corticosteroids, and intravenous immunoglobulin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Rufinamide in febrile infection-related epilepsy syndrome.

---

## Literature Evidence

Currently no related literature directly addressing Rufinamide in febrile infection-related epilepsy syndrome is available in the current dataset.

---

## UK Market Information

No MHRA marketing authorisation for Rufinamide is recorded in this Evidence Pack. Clinicians should verify the current UK licensing position via the MHRA product licence database and the electronic Medicines Compendium (eMC) before considering prescribing.

> **Important note for clinicians:** Rufinamide is marketed as **Inovelon®** and holds a valid EMA marketing authorisation (EU/1/07/393) for adjunctive treatment of seizures associated with Lennox-Gastaut Syndrome in patients aged ≥1 year. Following the UK's departure from the EU, the MHRA separately maintains Great Britain product licences; clinicians should confirm current GB and Northern Ireland licensing status directly with the MHRA. Any use outside the licensed indication constitutes off-label prescribing and requires appropriate governance approval and informed patient/carer consent, in accordance with NICE guidance and GMC Good Practice standards.

---

## Safety Considerations

Please refer to the Summary of Product Characteristics (SmPC) and the British National Formulary (BNF) for full prescribing and safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at [https://yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The TxGNN model assigns a high prediction score (99.57%) for Rufinamide in FIRES, but no clinical trials or targeted published evidence exist for this specific indication at the data cut-off date (April 2026), placing this at Evidence Level L4. The prediction appears principally driven by knowledge graph topology shared with LGS rather than direct clinical validation, and no controlled evidence currently supports a clinical development decision.

**To proceed, the following is needed:**

- **Systematic case-level review:** Identify and collate published case reports and case series describing Rufinamide use in FIRES and paediatric SRSE — anecdotal clinical use exists but is not captured in this dataset
- **Registry and observational data:** Collaborate with international FIRES/SRSE registries (e.g., pSERG — paediatric Status Epilepticus Research Group; the EpiCARE European Reference Network) to quantify the frequency and outcomes of Rufinamide use in FIRES patients
- **Mechanistic research:** Investigate whether sodium channel dysfunction contributes to sustained ictal activity in neuroinflammation models of FIRES, and whether Rufinamide modulates neuronal excitability under inflammatory conditions
- **UK prescribing governance:** Confirm current MHRA GB licensing status and, if proceeding with off-label use, establish an appropriate institutional off-label prescribing framework and patient registry
- **Full safety dossier:** Obtain complete SmPC safety data including contraindications, pharmacokinetic interactions, and monitoring requirements relevant to critically ill paediatric patients receiving polytherapy in an intensive care setting

---

> *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates identified by TxGNN require prospective clinical validation before any clinical application. Healthcare professionals should consult the SmPC, BNF, and relevant NICE guidance before making prescribing decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

