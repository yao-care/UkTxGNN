---
layout: default
title: Chenodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 5
---

# Chenodeoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Chenodeoxycholic Acid: From Cerebrotendinous Xanthomatosis to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Chenodeoxycholic acid (CDCA) is a primary bile acid used in the treatment of cerebrotendinous xanthomatosis (CTX), a rare inherited disorder of bile acid synthesis. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolaemia (HoFH)**, with **0 clinical trials** and **1 publication** currently supporting this direction — evidence is confined to a single narrative review of a related lipid disorder, and the mechanistic link to HoFH remains indirect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cerebrotendinous xanthomatosis (CTX) |
| Predicted New Indication | Homozygous Familial Hypercholesterolaemia (HoFH) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| UK Market Status | Not currently marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established biochemistry, CDCA is a primary bile acid and a weak agonist of the Farnesoid X receptor (FXR). FXR activation upregulates the biliary cholesterol efflux transporters ABCG5 and ABCG8, theoretically increasing cholesterol secretion into bile and reducing systemic cholesterol burden. This represents an indirect but biologically coherent connection to disorders of cholesterol metabolism.

The knowledge graph model's prediction likely derives from an ontological pathway linking CTX to lipid metabolism, and from there to HoFH. This is plausible at the disease taxonomy level: CTX (the established indication for CDCA) presents with a hypercholesterolaemia phenotype driven by defective bile acid synthesis via CYP27A1 mutations, accumulating cholestanol in tissues. Both CTX and HoFH involve dysfunctional cholesterol handling, providing an apparent biological neighbourhood in the graph.

However, the mechanistic disconnect is significant and must be clearly stated. The defining pathology of HoFH is loss-of-function mutation in the LDL receptor (LDLR), resulting in severely impaired clearance of LDL-cholesterol from the circulation. CDCA does not act on the LDLR pathway. Its bile acid–FXR mechanism addresses cholesterol excretion at the level of the biliary canaliculus, not receptor-mediated hepatic LDL uptake. The TxGNN prediction most likely reflects shared metabolic ontology rather than direct pharmacological relevance, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Chenodeoxycholic acid in homozygous familial hypercholesterolaemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Narrative Review | *Orphanet Journal of Rare Diseases* | Comprehensive review of CTX pathogenesis (CYP27A1 mutation, cholestanol accumulation, hypercholesterolaemia phenotype) and CDCA's established role as the standard treatment. Not a direct study of CDCA in HoFH; relevance is mechanistic and contextual only. |

---

## UK Market Information

No marketing authorisations for Chenodeoxycholic acid are currently recorded in this dataset for the United Kingdom, and the drug does not hold an active MHRA licence according to the data available at the time of this report.

> **Note for clinicians:** Healthcare professionals should independently verify current MHRA and NICE guidance. CDCA formulations used in the management of CTX (e.g., as an orphan medicinal product) may be available in the UK through named-patient supply, Specials, or hospital exemption arrangements, and the authorisation landscape for orphan drugs can change. Please consult the MHRA product database and BNF/BNFc for the most up-to-date licensing position.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme at [https://yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The core pathology of HoFH — loss of LDLR function — is mechanistically distinct from CDCA's bile acid–FXR pathway, and there are no clinical trials or direct efficacy studies in this indication. The single supporting publication is a narrative review of CTX, a related but distinct disease; it does not provide direct evidence for CDCA in HoFH. At L4 evidence with no clinical data specific to HoFH, this candidate does not yet meet the threshold for further development without additional mechanistic justification.

**To proceed, the following is needed:**

- **Mechanism of action clarification:** Formal review of DrugBank and primary pharmacology literature to confirm whether CDCA has any direct or indirect action on LDLR expression, LDL-C clearance, or PCSK9 regulation
- **MHRA SmPC and BNF review:** Confirm current UK licensing status, approved indications, and full safety profile (warnings, contraindications, drug interactions)
- **Preclinical evidence:** In vitro studies in LDLR-deficient cell lines or HoFH animal models to assess whether CDCA produces any measurable LDL-lowering effect through an LDLR-independent mechanism
- **Expert lipidology opinion:** Specialist input on the biological plausibility of a bile acid–based approach in HoFH, particularly given the availability of established LDL-lowering therapies (LDL apheresis, lomitapide, evinacumab, PCSK9 inhibitors)
- **Systematic literature search:** Broader PubMed search covering CDCA + familial hypercholesterolaemia, bile acids + LDLR, and FXR agonists + LDL to identify any overlooked mechanistic or clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

