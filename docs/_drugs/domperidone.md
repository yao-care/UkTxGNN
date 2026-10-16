---
layout: default
title: Domperidone
parent: Model Prediction Only (L5)
nav_order: 236
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Domperidone: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the UK licence data compiled for this report (pharmacol…"
---

# Domperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Domperidone: From Upper Gastrointestinal Symptoms to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist used to manage nausea, vomiting, dyspepsia and related upper gastrointestinal symptoms.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this direction; it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK licence data compiled for this report (pharmacology sources describe use in nausea, vomiting, dyspepsia and heartburn) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology sources identify domperidone as an antagonist at the dopamine D2 and D3 receptors (DRD2, DRD3). It acts mainly outside the central nervous system and is used for dyspepsia, heartburn, epigastric pain, nausea and vomiting.

NSIAD is a rare condition caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*), with some cases linked to GNAS-related signalling. The V2 receptor is constitutively active, which leads to inappropriate water retention and hyponatraemia. A mechanistic link to domperidone is not apparent. A plausible but unverified hypothesis is that dopaminergic modulation influences renal water handling or vasopressin signalling. However, domperidone is not known to act on V2 receptor activity, which is the core defect in NSIAD.

The high score may reflect network proximity in the knowledge graph rather than a true biological relationship. This prediction should be treated as a hypothesis requiring independent validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000J0AAACAC | Domperidone oral suspension 5 mg/5 ml, sugar-free | Oral suspension | Not stated in the data compiled |

The record shows one valid single-ingredient product. The identifier shown is in a BNF-style product code format rather than a standard PL number, so the authorisation details should be confirmed against the MHRA register. Domperidone is classified in BNF chapter 1 (gastrointestinal system), under drugs affecting gastrointestinal motility.

## Safety Considerations

- **Conditions linked to domperidone by the knowledge graph** (from drug–disease contraindication links in the TxGNN knowledge graph, not from label text and so to be verified against the SmPC): long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease.
- **Pharmacological targets:** dopamine D2 and D3 receptors (DRD2, DRD3). No drug–drug interaction entries with specific named drugs were identified in the data compiled.
- Regulators have reviewed the benefit-risk balance of domperidone-containing medicines (the EMA review began in March 2013). Prescribers should consult the current SmPC and BNF for warnings, contraindications and cardiac risk guidance.

Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score. There are no clinical trials or publications, the mechanistic link to NSIAD is not evident, and the knowledge graph flags QT-related and hepatic safety concerns. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible, testable pathway linking dopamine D2/D3 antagonism to vasopressin V2 receptor signalling or renal water handling
- Preclinical studies (for example, cell-based *AVPR2* gain-of-function models) to test any effect
- Review of UK SmPC warnings and contraindications, with a cardiac (QT) and hepatic risk assessment
- Confirmation of the UK licensed indication and authorisation details with the MHRA
- A literature and trial registry search specific to NSIAD, which is a very rare condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

