---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Rivaroxaban: predicted new indication Rheumatoid arthritis (evidence level L4). Approved use: Not stated in the licence data compiled for this report (the product…"
monitor_inn: "Rivaroxaban"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Rivaroxaban: From Venous Thromboembolism Prophylaxis and Treatment to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Rivaroxaban is an oral direct Factor Xa inhibitor (anticoagulant). The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this rests on the model score alone: **no clinical trials** and only **4 publications**, none of which tests rivaroxaban as a treatment for the condition, were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (the product is a 20 mg tablet, an anticoagulant) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Rivaroxaban is known to be a direct Factor Xa inhibitor used for anticoagulation, and this is the basis for the discussion below.

The link to rheumatoid arthritis (RA) is indirect. RA involves chronic inflammation with a prothrombotic state, and thrombin generation is altered in autoimmune disease (PMID 34175144). This could support a role in thromboprophylaxis for RA patients. It does not support disease-modifying activity. The very high TxGNN score is not backed by any clinical trial of rivaroxaban in RA.

Other predicted indications (gout, HIV infectious disease, sclerosing cholangitis, systemic mastocytosis and several rare syndromes) have even weaker support. Their evidence is either absent or concerns anticoagulation in patients who already have the condition, or drug interactions, rather than treatment of the condition itself.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower extremity venous thromboembolism; DVT incidence is 88 to 112 per 100,000 person-years and rises with age. Not specific to RA. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de medecine interne | Thrombin generation assay can assess hypercoagulability in autoimmune disease. Supports a thrombotic-risk rationale only. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Adherence to rivaroxaban versus apixaban in non-valvular atrial fibrillation. Not relevant to RA treatment. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | Embolic events despite anticoagulation in an 88-year-old woman with chronic kidney disease taking steroids for RA. Anecdotal. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0208020Y0AAACAC (BNF-style product code, not a PL number) | Rivaroxaban Tab 20mg | Tablet (not specified in the data) | Not specified in the data compiled for this report |

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** liver failure, kidney disease, pyoureter, liver disease, gallbladder disease and blood coagulation disease. These come from drug-disease contraindication links in the TxGNN knowledge graph and must be checked against the SmPC.
- **Drug Interactions:** 100 interactions were identified in total, and 20 are listed in the data compiled for this report. Major interactions include:
  - Acetylsalicylic acid
  - Cobicistat
  - Deferasirox
  - Ibritumomab tiuxetan
  - Tositumomab (I-131)

  Moderate interactions include aprepitant, dexamethasone, cimetidine, clarithromycin, eliglustat, miconazole, clotrimazole, dexfenfluramine, fenfluramine, rolapitant, sibutramine, troglitazone, iodide I-131, iodide I-123 and sugammadex.
- RA patients commonly take NSAIDs, aspirin and corticosteroids. The interactions with aspirin and dexamethasone are therefore directly relevant to this population, particularly for bleeding risk.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No trials exist, and the available literature supports at most a thromboprophylaxis rationale rather than any effect on RA itself. The licence data are also incomplete, and RA patients often take drugs that interact with rivaroxaban.

**To proceed, the following is needed:**
- Licence details for the UK product (PL number, dosage form, approved indications) and the SmPC warnings and contraindications
- Mechanism of action data
- Preclinical or clinical evidence that Factor Xa inhibition affects RA disease activity, or a clearly defined thromboprophylaxis question in RA
- A bleeding and drug-interaction risk assessment for RA patients taking NSAIDs, aspirin or corticosteroids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

