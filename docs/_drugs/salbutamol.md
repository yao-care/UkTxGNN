---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: From Bronchial Asthma to Papillary Conjunctivitis

## One-Sentence Summary

Salbutamol (albuterol) is a selective short-acting β2-adrenoceptor agonist, widely established as a first-line bronchodilator for the relief of bronchospasm in asthma and reversible obstructive airways disease. The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**, with **no registered clinical trials** and **no supporting publications** currently available for this indication. The prediction rests entirely on AI graph-based pattern recognition and carries an Evidence Level of L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchial asthma; relief of reversible airways obstruction (bronchodilator) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.9964% |
| Evidence Level | L5 |
| UK Market Status | No marketing authorisation data found in this dataset (likely data gap — see note below) |
| Number of Marketing Authorisations | 0 (data gap) |
| Recommended Decision | Hold |

> **Data Note:** Salbutamol (e.g., Ventolin®, Salamol®) is a well-established medicine in the United Kingdom with multiple MHRA-authorised products. The absence of licence data in this evidence pack represents a system data gap rather than a true absence of UK authorisation. Please consult the MHRA Product Licence Register and BNF Section 3.1.1 (Adrenoceptor Agonists) for confirmed prescribing information.

---

## Why is This Prediction Reasonable?

Detailed pharmacological mechanism of action data was not populated in this evidence pack. Based on information contained within the evidence pack's clinical rationale sections, Salbutamol is a selective β2-adrenoceptor agonist. Its canonical mechanism involves β2-AR activation → adenylyl cyclase stimulation → intracellular cAMP elevation → protein kinase A (PKA) activation → inhibition of myosin light-chain kinase (MLCK) phosphorylation → airway smooth muscle relaxation and bronchodilation. This is the established mechanistic basis for its use in asthma and obstructive lung disease.

In the context of papillary conjunctivitis, a theoretical link could be drawn through β2-adrenoceptor-mediated mast cell stabilisation: β2 agonists may suppress localised conjunctival mast cell degranulation, thereby reducing the release of histamine and other inflammatory mediators that drive papillary formation. Papillary conjunctivitis — in particular giant papillary conjunctivitis (GPC) — is typically triggered by mechanical irritation (e.g., contact lens wear) or allergen exposure, and characterised by upper tarsal papillae, mucous discharge, and pruritus.

However, the mechanistic case for Salbutamol in this condition is not established. The primary pathology of GPC involves mechanical friction and IgE/mast cell-mediated inflammation of the tarsal conjunctiva — a setting for which β2 agonism has no validated pharmacological role, and for which no clinical or preclinical data exist. The TxGNN score of 99.9964% reflects the model's graph-level pattern recognition; without corroborating evidence, it holds no independent clinical significance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No MHRA marketing authorisation records were returned for Salbutamol in this dataset. This is a data gap. Salbutamol holds multiple UK product licences across inhaler (pressurised metered-dose inhaler, dry powder inhaler), nebuliser solution, oral tablet, oral solution, and intravenous formulations. Authorised indications include acute and chronic bronchospasm in asthma, COPD, and exercise-induced bronchospasm.

For comprehensive and up-to-date authorisation details, please refer to:
- **MHRA Products database**: https://products.mhra.gov.uk/
- **BNF** (Section 3.1.1 — Short-acting beta2 agonists): https://bnf.nice.org.uk/

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is a complete absence of clinical and preclinical evidence for Salbutamol in papillary conjunctivitis, and the proposed mechanistic link between β2-adrenoceptor agonism and the tarsal conjunctival inflammatory pathology of this condition remains speculative and unvalidated. An L5 AI prediction alone is insufficient to justify progression.

**To proceed, the following is needed:**
- Preclinical studies (in vitro conjunctival cell models and/or animal models) to confirm β2-adrenoceptor expression and functional mast cell stabilisation activity in tarsal conjunctival tissue
- Formal mechanism of action (MOA) review via DrugBank API to characterise Salbutamol's anti-inflammatory receptor profile beyond bronchodilation
- Ocular safety assessment: review of published data and SmPC for any existing ocular adverse effects or contraindications relevant to a conjunctival route of administration
- Regulatory feasibility consultation with the MHRA regarding development of a novel ophthalmic indication for an established systemic/inhaled medicine
- Comparison with established mast cell stabilisers (e.g., sodium cromoglicate, nedocromil) and antihistamine eye drops already approved for allergic conjunctivitis, to define a differentiation hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

