---
layout: default
title: Tigecycline
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tigecycline: predicted new indication Disorder of tyrosine metabolism (evidence level L5). Approved use: Streptococcal pneumonia"
monitor_inn: "Tigecycline"
predicted_indications: ["disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria", "disorder of phenylalanine metabolism", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy"]
---

# Tigecycline
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

# Tigecycline: From Streptococcal Pneumonia to Disorder of Tyrosine Metabolism

## One-Sentence Summary

Tigecycline is a glycylcycline antibiotic, originally used for streptococcal pneumonia.
The TxGNN model predicts it may be effective for **disorder of tyrosine metabolism**, but there are **no registered clinical trials** and only **4 publications** (all preclinical or commentary, none directly relevant to tyrosine metabolism), so the prediction is supported by model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal pneumonia (from the knowledge graph; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Disorder of tyrosine metabolism |
| TxGNN Prediction Score | 95.76% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, tigecycline is a tetracycline-class (glycylcycline) antibiotic that inhibits bacterial protein synthesis. Its efficacy in bacterial infection such as streptococcal pneumonia is the basis of its original use.

No direct link to tyrosine metabolism has been established. The retrieved literature concerns tigecycline's inhibition of mitochondrial translation and oxidative phosphorylation in cancer stem cells and leukaemia cells, and its effects on human melanocytes and fibroblasts. Melanin is synthesised from tyrosine, so the melanocyte study offers a tenuous, indirect connection, but it does not examine tyrosine metabolic disorders.

The high TxGNN score is a computational prediction without clinical support. It should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41009505](https://pubmed.ncbi.nlm.nih.gov/41009505/) | 2025 | In vitro study | Int J Mol Sci | Effects of tigecycline on human epidermal melanocytes and fibroblasts; tetracyclines are linked to pigmentary disorders and phototoxicity, possibly through affinity for melanin |
| [31765940](https://pubmed.ncbi.nlm.nih.gov/31765940/) | 2020 | Preclinical | Neoplasia | Targeting SIRT1 and mitochondrial oxidative phosphorylation in EGFR TKI-resistant lung adenocarcinoma stem cells (tigecycline not the main focus in the available abstract) |
| [28920959](https://pubmed.ncbi.nlm.nih.gov/28920959/) | 2017 | Preclinical | Nature Medicine | Targeting mitochondrial oxidative phosphorylation, with tigecycline plus imatinib, eradicated therapy-resistant chronic myeloid leukaemia stem cells |
| [29404396](https://pubmed.ncbi.nlm.nih.gov/29404396/) | 2018 | Commentary | Mol Cell Oncol | Auto-commentary on the above: tigecycline plus imatinib prevented relapse in preclinical models |

None of these publications addresses tyrosine metabolism disorders.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501030Y0AAAAAA (BNF-style product code; not a PL number) | Tigecycline powder for injection, 50 mg vial | Powder for injection | Not available in the data compiled for this report |

The BNF section code 0501030Y0 places the product among the tetracycline-class antibacterials (BNF chapter 5, Infections). The data compiled for this report did not include an MHRA PL number or approved indication text.

---

## Safety Considerations

- **Contraindications and associated conditions (knowledge graph, not label text)**: liver failure, hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, pancreatitis.
- **Drug Interactions**: 30 interactions were identified, most with unclassified severity. Those graded **Moderate** include warfarin, dicoumarol (anticoagulant effect; monitor coagulation), picosulfuric acid, methoxsalen and tacrolimus. Others with unclassified severity include vancomycin, metronidazole, clarithromycin, proton pump inhibitors (omeprazole, lansoprazole, pantoprazole), morphine, prednisone, simvastatin, clopidogrel, heparin, ondansetron, metoclopramide, potassium chloride and acetylcysteine.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials, and the retrieved literature does not address tyrosine metabolism. Several knowledge-graph contraindications (liver failure, hyperbilirubinaemia, pancreatitis) would also be relevant in a population with metabolic disease.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between tigecycline and the tyrosine metabolic pathway
- Targeted preclinical studies (for example, in relevant enzyme or cell models) before any clinical consideration
- MHRA licence details (PL number, approved indications) and the SmPC safety information, including warnings and contraindications
- Review of safety in the target population, given the hepatic and pancreatic signals

**Other predictions reviewed:** None of the other nine predicted indications (ranks 2-10) supports repurposing. Several are better explained as adverse-event associations (teratogenic Pierre Robin syndrome, hyperamylasaemia) or have no evidence. The only one with preclinical data is monoclonal gammopathy (L4, Research Question): tigecycline showed antitumour activity in myeloma cell lines, but one study reported that it opposes the effect of bortezomib, which raises an antagonism concern with standard therapy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

