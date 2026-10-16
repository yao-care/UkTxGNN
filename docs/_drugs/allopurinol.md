---
layout: default
title: Allopurinol
parent: Model Prediction Only (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L5). Approved use: Gout"
---

# Allopurinol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Allopurinol: From Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor, originally used to treat gout, hyperuricaemia and acute urate nephropathy.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but there are currently **no registered clinical trials** and only **2 publications** (a hypothesis paper and a rat study), neither of which tests allopurinol in patients with porphyria.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; hyperuricaemia; acute urate nephropathy |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, allopurinol is a xanthine oxidase inhibitor that lowers uric acid production, and its efficacy in gout and hyperuricaemia is well established.

The link to hepatic porphyria is indirect. Allopurinol has been reported to interact with haem biosynthesis, including degradation of hepatic cytochrome P450 haem and altered ALA synthase activity in animal studies. The retrieved literature consists of a hypothesis paper on metabolic targeting of 5-aminolevulinate synthase and a rat study on carbamazepine and haem metabolism. Neither tests allopurinol in people with porphyria.

The direction of effect is uncertain. Depending on the porphyria type, depleting haem could be harmful or beneficial, and some drugs that affect haem metabolism are known to be porphyrinogenic. The link is therefore plausible but unproven.

The other nine predictions (including idiopathic copper-associated cirrhosis, hepatopulmonary syndrome, and immune-mediated necrotizing myopathy) have scores of 99.85% to 99.94% but no clinical evidence, so they are not pursued here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes targeting liver 5-ALAS, via tryptophan or inhibition of tryptophan 2,3-dioxygenase, as a therapy for acute hepatic porphyrias; allopurinol is not tested |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal study (rat) | Biochemical Pharmacology | Carbamazepine, at a very small dose, exacerbated porphyria by depleting haem in rat liver; not a study of allopurinol |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001040C0AAAAAA | Allopurinol Tab 100 mg | Tablet (not specified in the data) | Not specified in the data |

The data compiled for this report list one valid single-ingredient authorisation. The identifier is not in standard MHRA PL format, and the indication text is not available. Please check the current SmPC, the BNF classification and any relevant NICE guidance directly.

## Safety Considerations

- **Contraindications and cautions from the knowledge graph** (these are model-derived associations, not label text): liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis, and anti-glomerular basement membrane disease. Liver disease is directly relevant to the proposed hepatic indication.
- **Drug Interactions**: The interaction query returned 100 records, of which 20 are listed in the data compiled for this report.
  - Moderate: aluminium hydroxide, attapulgite, kaolin, magaldrate and sucralfate.
  - Minor: amoxicillin and chlorpropamide.
  - Unknown severity: calcitriol, vitamin A, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole, acarbose, morphine, metformin, omeprazole, rosiglitazone and palonosetron.
- **Porphyria-specific concern**: Because some drugs that alter haem metabolism can precipitate porphyric attacks, any use in porphyria would need careful specialist assessment.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is a model prediction only. There are no clinical trials, and the two publications are a hypothesis paper and a rat study of another drug. The mechanism is indirect and its direction of effect is uncertain, with a potential risk of worsening porphyria.

**To proceed, the following is needed:**
- Mechanism of action data, and a focused review of allopurinol's effects on haem biosynthesis and ALA synthase in porphyria models
- Preclinical studies testing allopurinol directly in acute and non-acute hepatic porphyria models
- A porphyrinogenicity assessment, using established drug safety databases for porphyria
- Full SmPC warnings and contraindications, which are currently missing from the data and would be needed before any safety screening
- Confirmation of the UK authorisation details (licence number format, dosage form and approved indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

