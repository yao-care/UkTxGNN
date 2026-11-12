---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 127
evidence_level: L5
indication_count: 1
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach"]
last_modified_at: 2026-11-12
description: "Capecitabine: predicted new indication Gastric adenocarcinoma and proximal polyposis of the stomach (evidence level L5). Approved use: Metastasis from malignant tumour of colon"
---

# Capecitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Capecitabine: From Gastric Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach
{: .text-alpha }

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine chemotherapy, recorded in the knowledge graph for colon cancer metastasis and gastric cancer.
The TxGNN model predicts it may be useful for **gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS)**, but the data compiled for this report contain **no clinical trials and no publications** for this condition, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastasis from malignant tumour of colon; gastric cancer (relations recorded in the knowledge graph; no licence indication text is available) |
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (5 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Capecitabine is generally understood to be a prodrug of 5-fluorouracil, which inhibits thymidylate synthase and disrupts DNA synthesis in rapidly dividing cells. This general pharmacology is not confirmed by the supplied data.

GAPPS is a rare hereditary syndrome (associated with APC promoter 1B mutations) with a gastric adenocarcinoma component. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

No GAPPS-specific evidence for capecitabine was supplied. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0801030V0AAABAB | Capecitabine 150mg tablets | Capecitabine |
| 0801030V0AAACAC | Capecitabine 300mg tablets | Capecitabine |
| 0801030V0AAAAAA | Capecitabine 500mg tablets | Capecitabine |
| 0801030V0BBABAB | Xeloda 150mg tablets | Capecitabine |
| 0801030V0BBAAAA | Xeloda 500mg tablets | Capecitabine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier is not in the usual MHRA "PL" format and should be verified against the MHRA register.

<!-- review:begin uk-lic-20261106-capecitabine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data list one single-ingredient authorisation with valid status. The identifier is not in the usual MHRA "PL" format and should be verified against the MHRA register." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 5 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-capecitabine-1 -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions. The knowledge graph records neutropenia, thrombocytopenia, agranulocytosis and anaemia as contraindication-related conditions. |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC. Given the recorded relations, full blood count, liver function and renal function are relevant. |
| Handling Protection | Follow local cytotoxic drug handling procedures |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph relations, not label text):** liver disease, gallbladder disease, thrombocytopenia, infectious disease, neutropenia, agranulocytosis, coronary artery disease, anaemia, macrocytic anaemia, hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome, impaired renal function, sudden cardiac arrest, heart conduction disease, necrotising enterocolitis, stomatitis, and dihydropyrimidine dehydrogenase deficiency.
- **Drug Interactions:** 100 interactions were found in total; the first 20 are shown in the data compiled for this report. Moderate interactions: metronidazole and tinidazole. Minor interactions: aluminium hydroxide, levofloxacin, magaldrate, magnesium carbonate, magnesium hydroxide and magnesium oxide. Interactions of unknown severity include pantoprazole, omeprazole, lansoprazole, glimepiride, doxycycline, morphine, metformin, atropine, prednisone, simvastatin, hydrocortisone and dolasetron.

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-derived only (L5), with no trials or publications on GAPPS. Capecitabine's likely use in the gastric adenocarcinoma component of GAPPS overlaps with existing gastric cancer practice, so it offers little new repurposing information.

**To proceed, the following is needed:**
- GAPPS-specific clinical or observational evidence for capecitabine
- Mechanism-of-action data
- Label-based warnings, contraindications and the approved indication text for the UK authorisation
- Confirmation of the authorisation details against the MHRA register

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data list one single-ingredient authorisation with valid status" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

