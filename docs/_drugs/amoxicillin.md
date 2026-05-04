---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Amoxicillin is a broad-spectrum penicillin antibiotic widely prescribed for bacterial infections including respiratory tract, urinary tract, and skin infections.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, with **no clinical trials** and **no published literature** currently supporting this specific indication.
This prediction warrants particular caution, as Amoxicillin is itself a recognised cause of drug-induced pancreatitis and elevated serum amylase — raising a significant reverse causality concern.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum penicillin antibiotic; no MHRA licence data retrieved) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| UK Market Status | No MHRA authorisation data retrieved |
| Number of Marketing Authorisations | 0 (data not retrieved) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Amoxicillin is a broad-spectrum aminopenicillin that exerts its bactericidal activity by irreversibly binding to penicillin-binding proteins (PBPs), thereby disrupting peptidoglycan cross-linking in the bacterial cell wall. This leads to osmotic instability and cell lysis. It is active against a wide range of Gram-positive and selected Gram-negative organisms and is used clinically across respiratory, urinary, gastrointestinal, and skin infections.

Hyperamylasemia — defined as an elevation of serum amylase above the normal reference range — is most commonly a laboratory finding secondary to acute pancreatitis, parotitis, or pancreatic duct obstruction. There is no established pharmacological mechanism by which a β-lactam antibiotic would directly suppress or regulate serum amylase concentrations. The mechanistic bridge between Amoxicillin's antibacterial action and serum enzyme modulation is not biologically credible on current evidence.

Critically, there is a **significant reverse causality concern**: Amoxicillin has itself been documented to cause drug-induced pancreatitis, which is associated with elevated serum amylase as an adverse effect. This raises a plausible explanation for the TxGNN prediction — the model may have identified a clinical co-occurrence pattern (the drug appearing alongside the laboratory finding) rather than a genuine therapeutic signal. This prediction is best regarded as a potential knowledge graph artefact unless independent biological validation can be provided.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amoxicillin in hyperamylasemia.

---

## Literature Evidence

Currently no related literature available for Amoxicillin in hyperamylasemia.

---

## UK Market Information

No MHRA marketing authorisation records were retrieved for Amoxicillin in this Evidence Pack, with market status recorded as not marketed and zero licences returned. This appears to be a data retrieval gap: Amoxicillin is a well-established licensed medicine in the United Kingdom, marketed under numerous brand names (including Amoxil) and classified in BNF Chapter 5.1 (Antibacterial drugs — Penicillins). Clinicians should consult the current BNF and the relevant Summary of Product Characteristics (SmPC) for full prescribing information pending correction of the MHRA data feed.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently no clinical or preclinical evidence supporting the use of Amoxicillin as a treatment for hyperamylasemia, and the biological plausibility of the prediction is fundamentally undermined by Amoxicillin's own known association with drug-induced pancreatitis — a condition in which hyperamylasemia is itself a cardinal feature.

**To proceed, the following is needed:**
- Independent biological investigation of the mechanistic basis for this TxGNN prediction, including assessment of whether the knowledge graph co-occurrence reflects an adverse drug reaction signal rather than a therapeutic one
- Pharmacovigilance review of Amoxicillin-associated pancreatitis cases via the Yellow Card database and published adverse event reports
- Retrieval and reconciliation of full MHRA marketing authorisation data to correct the current data gap
- Full SmPC review, including warnings and precautions relating to gastrointestinal and pancreatic adverse effects
- Consultation with a clinical pharmacologist before this hypothesis is considered for any further development

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

