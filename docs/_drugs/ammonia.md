---
layout: default
title: Ammonia
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 6
---

# Ammonia
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ammonia: From No Established Indication to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Ammonia (NH₃) is a simple inorganic compound with no currently approved therapeutic indication registered in the UK; its historical uses in medicine have been largely superseded by safer alternatives.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans (ACA)**, a late-stage cutaneous manifestation of Lyme borreliosis, with a prediction score of **99.70%**.
However, this prediction is supported by **no clinical trials** and **no published literature**, placing it at the lowest evidence tier (**L5**); the mechanistic rationale is highly indirect and speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No established approved indication |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for Ammonia in a therapeutic context. Ammonia is a naturally occurring inorganic compound (NH₃) that exists endogenously in human physiology as a by-product of amino acid catabolism. In historical medical practice, dilute ammonia solutions were occasionally used as topical counter-irritants and in aromatic spirits of ammonia for vasovagal episodes, though these applications are now largely obsolete.

Acrodermatitis Chronica Atrophicans (ACA) is caused by persistent infection with *Borrelia burgdorferi sensu lato*, typically presenting as a chronic, progressive atrophic skin condition on the distal extremities. The standard of care is prolonged antibiotic therapy (e.g., oral doxycycline or amoxicillin). The TxGNN knowledge graph model may have generated this prediction based on spatial proximity between dermatological nodes in the graph, rather than a biologically meaningful mechanistic link. The theoretical basis suggested — that ammonia's alkaline pH (~11) could alter the skin microenvironment and inhibit bacterial colonisation — is highly indirect and lacks any clinical or preclinical validation.

Critically, ammonia's well-documented systemic toxicities (hepatic encephalopathy risk, respiratory mucosal irritation, direct tissue caustic injury) present a significant safety barrier for any therapeutic application, particularly for a chronic skin condition for which safe, effective antibiotic options already exist. This prediction is most likely an artefact of the knowledge graph topology and should not be interpreted as a biologically plausible repurposing opportunity at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Ammonia holds no MHRA marketing authorisations in the United Kingdom. It is not listed as an active medicinal ingredient in the British National Formulary (BNF) for any currently approved therapeutic indication. Historically, preparations such as Aromatic Ammonia Spirit have been withdrawn or discontinued.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme (https://yellowcard.mhra.gov.uk/).

> **Note for clinicians**: Ammonia is a recognised industrial and environmental hazard. Inhalation causes severe respiratory tract irritation, chemical pneumonitis, bronchospasm, and pulmonary oedema. Direct skin or mucosal contact with concentrated solutions causes caustic chemical burns. Systemic ammonia toxicity is associated with hepatic encephalopathy. These known toxicological properties are particularly relevant given that one of the model's top-ranked predicted indications (childhood interstitial lung disease, rank 4) involves a respiratory target organ that ammonia is known to damage acutely — a clear counter-indication signal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predicted indications are rated L5 (model prediction only), with zero supporting clinical trials or published literature across any indication; furthermore, ammonia's well-established toxicological profile (caustic tissue injury, respiratory toxicity, hepatic encephalopathy) presents fundamental safety barriers that are not reconcilable with the predicted therapeutic applications in their current form.

**To proceed, the following would be needed:**

- Formal mechanistic hypothesis validation: a plausible, peer-reviewed mechanistic pathway linking ammonia to ACA pathophysiology (e.g., *Borrelia* inhibition at concentrations achievable without tissue toxicity) would need to be established before any further evaluation.
- Preclinical safety and efficacy data: *in vitro* and *in vivo* studies demonstrating antimicrobial activity against *B. burgdorferi* at sub-toxic concentrations.
- Formulation feasibility assessment: any viable therapeutic application would need a specialised delivery system (e.g., buffered topical preparation) to mitigate caustic risk; a pharmaceutical formulation programme would be required.
- Regulatory and ethics review: given the known hazard profile of ammonia, any first-in-human proposal would require exceptional scientific justification and would face a high regulatory bar from the MHRA.
- Resolution of all data gaps: MHRA SmPC-equivalent safety data, full MOA characterisation, and drug–drug interaction profiling are all currently absent and would be required for any S1 safety pre-assessment.

> ⚠️ **Research use only.** This report is generated for research purposes and does not constitute medical advice. Drug repurposing candidates require full clinical validation before any therapeutic application. This report should not be used to guide clinical decision-making.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

