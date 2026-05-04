---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a selective neurokinin-1 (NK1) receptor antagonist established for the prevention of chemotherapy-induced nausea and vomiting (CINV) and post-operative nausea and vomiting (PONV).
The TxGNN model predicts it may have potential activity against **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, with **no clinical trials** and **no published literature** currently supporting this direction.
Evidence is presently limited to computational model prediction alone, and the mechanistic rationale for this specific indication is considered weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (CINV) and post-operative nausea and vomiting (PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | No records found in this dataset (possible retrieval error — verify against MHRA register) |
| Number of Marketing Authorisations | 0 (data not retrieved) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not recorded in this Evidence Pack. Based on the prediction rationale and well-established pharmacology, Aprepitant acts as a selective, high-affinity antagonist at the NK1 (neurokinin-1) receptor. It blocks substance P (SP) binding at NK1 receptors in the central nervous system — principally the nucleus tractus solitarius and area postrema — thereby suppressing both the acute and delayed phases of chemotherapy-induced emesis. This mechanism differs fundamentally from the dopamine D2 blockade employed by older antiemetics and represents a neurochemically distinct approach to antiemesis.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare, X-linked genetic disorder caused by constitutively activating mutations in the *AVPR2* gene, which encodes the renal vasopressin V2 receptor. Constitutive V2 receptor signalling drives persistent Aquaporin-2 (AQP-2) expression and water reabsorption in the renal collecting duct, producing dilutional hyponatraemia despite low or undetectable plasma arginine vasopressin (AVP) levels.

The proposed mechanistic link rests on the possibility that substance P / NK1 signalling may indirectly modulate AQP-2 expression or downstream cyclic AMP (cAMP) regulation. However, no direct molecular evidence currently supports this connection. NSIAD is a genetically determined disease in which the primary defect — constitutive AVPR2 receptor activation — lies outside the pharmacological reach of NK1 antagonism. The biological plausibility for Aprepitant's efficacy in NSIAD is considered weak, and the high TxGNN prediction score most likely reflects indirect network linkages within the knowledge graph rather than a genuine therapeutic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Aprepitant in nephrogenic syndrome of inappropriate antidiuresis on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

Currently no related literature available for Aprepitant in nephrogenic syndrome of inappropriate antidiuresis.

---

## UK Market Information

No marketing authorisation records for Aprepitant were returned by this dataset's retrieval process. This appears inconsistent with known MHRA product licensing: Aprepitant is marketed in the United Kingdom as **Emend** (MSD) for the prevention of CINV associated with highly and moderately emetogenic chemotherapy regimens, and has been evaluated by NICE (Technology Appraisal TA213, 2012). The fixed-dose combination netupitant/palonosetron (Akynzeo) represents a related NK1/5-HT₃ combination product also authorised in the UK.

Prescribers should verify the current marketing authorisation status, approved indications, and licensed dosage forms via the [MHRA Products register](https://products.mhra.gov.uk/) and the BNF (Chapter 4.6: Drugs used in nausea and labyrinth disorders).

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting Aprepitant for nephrogenic syndrome of inappropriate antidiuresis, and the mechanistic connection between NK1 receptor antagonism and constitutive V2 receptor activation is speculative. As an essentially genetic condition, NSIAD is unlikely to be amenable to NK1-targeted therapy without compelling mechanistic or empirical data to justify further investigation.

**To proceed, the following is needed:**
- Preclinical studies (in vitro or animal models of NSIAD) demonstrating a functional role for SP/NK1 signalling in AVPR2-mediated AQP-2 upregulation or renal water handling
- Direct molecular evidence linking substance P to downstream cAMP regulation in renal collecting duct epithelial cells
- Formal mechanism of action data retrieved from DrugBank (data gap DG002)
- Complete UK SmPC safety data including MHRA-approved warnings and contraindications (data gap DG001)
- Correction of UK market status — MHRA product licence records for Aprepitant should be retrieved and validated for this dataset

---

> **Analyst note — alternative indication of interest:** Of the ten predicted indications in this Evidence Pack, the strongest mechanistic rationale belongs to **subarachnoid haemorrhage (rank 9, score 99.85%)**. Substance P is released in large quantities into the cerebrospinal fluid following SAH, and NK1 receptor-mediated neurogenic inflammation, blood-brain barrier disruption, and delayed cerebral ischaemia (DCI) provide a more plausible biological framework than any other prediction in this set. Aprepitant's favourable lipophilicity and potential CNS penetration are further enabling properties. A targeted literature search and pilot study review for this indication is recommended as the higher-priority research question from this prediction batch.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

