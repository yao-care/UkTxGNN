---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Diarrhoeal disease, dysentery"
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "serous conjunctivitis except viral", "conjunctival folliculosis", "chronic follicular conjunctivitis", "parasitic conjunctivitis", "Angelucci syndrome"]
---

# Loperamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Loperamide: From Diarrhoeal Disease to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a peripherally acting anti-motility agent, originally used to treat diarrhoeal disease and dysentery.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but there are **no clinical trials** and **no publications** supporting this prediction. It is a model output only, with no known biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhoeal disease, dysentery (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Loperamide is a peripherally acting mu-opioid receptor agonist that slows gut motility. Detailed mechanism of action data is not available in the data compiled for this report, so this description is based on general pharmacological knowledge.

The original indications (diarrhoeal disease and dysentery) are gastrointestinal conditions. Conjunctivitis is an eye condition. No ocular or anti-infective mechanism of loperamide is established. The very high score (99.97%) is most likely driven by associations within the knowledge graph rather than by biology, and the other top-ranked predictions are mostly conjunctivitis subtypes, which supports this interpretation.

In short, this prediction should be regarded as a computational hypothesis only, with no plausible mechanistic link identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For context, literature exists for other lower-ranked predictions, but it describes safety concerns rather than benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | Journal of Travel Medicine | Fulminant amoebic colitis with toxic megacolon in a patient with heavy loperamide use (amebic dysentery prediction). Suggests possible harm. |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case report | Cureus | Loperamide-induced respiratory depression in severe chemotherapy-related gastrointestinal inflammation (gastroduodenitis prediction). Suggests increased systemic exposure when the gut mucosa is compromised. |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | The American Journal of Medicine | General review of non-fluid therapy and chemoprophylaxis for acute diarrhoea. Not specific to amebic dysentery. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0104020L0AAAAAA | Loperamide HCl Capsules 2 mg | Capsule (inferred from product name) | Not available in the data compiled |

The identifier above is in the format of a BNF-style code rather than a standard MHRA PL number, so the authorisation details should be verified against the MHRA database.

## Safety Considerations

- **Contraindications (knowledge graph associations, not label text):** liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, diarrhoeal disease, infectious diarrhoeal disease, intestinal infectious disease.
- **Drug Interactions:** 100 interactions were recorded. Major-level examples include abiraterone, ranitidine, fosamprenavir and gemfibrozil. Moderate-level examples include codeine, dihydrocodeine, tramadol, ethanol and several antihistamines (chlorpheniramine, cetirizine, acrivastine).
- **Case-report safety signals:** worsening of invasive intestinal infection (toxic megacolon in amoebic colitis) and central opioid effects such as respiratory depression when gut inflammation increases systemic absorption.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score. There are no trials or publications, and no plausible mechanism links an anti-motility gut agent to conjunctivitis. Related predictions in the gastrointestinal area yielded safety warnings rather than supportive evidence.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis for an ocular effect, supported by preclinical data
- Mechanism of action data for loperamide
- Label warnings and contraindications from the SmPC and BNF
- Verification of the MHRA authorisation details, including approved indication and dosage form
- Evidence of a suitable ocular formulation or route, as none is currently identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

