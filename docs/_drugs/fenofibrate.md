---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 282
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-12
description: "Fenofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia…"
---

# Fenofibrate
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

## Fenofibrate: From Hypertriglyceridaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug used for hypertriglyceridaemia and related hyperlipidaemias.
The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**, but the supporting evidence is limited to **0 clinical trials** and **3 preclinical or mechanistic publications**, none of which studies the disease directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia, hypoalphalipoproteinaemia (relations recorded in the knowledge graph; the licence text in the data compiled for this report is empty) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (15 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fenofibrate is generally known as a PPARα agonist, and the mechanistic link described here is drawn from the supporting literature. In mice, fenofibrate raises HDL cholesterol and lowers triglycerides, partly by increasing apoA-I/apoA-II expression and inducing the phospholipid transfer protein (PLTP) gene, which enlarges HDL particles.

CETP deficiency is characterised by markedly raised HDL cholesterol and altered reverse cholesterol transport. Fenofibrate acts on overlapping lipoprotein pathways (HDL remodelling, PLTP induction, and, in preclinical models, combined CETP inhibition with PPARα agonism). However, the link is indirect and biologically ambiguous. CETP deficiency is already a high-HDL state, so there is no clear therapeutic reason to raise HDL further.

The high TxGNN score probably reflects network proximity of lipid-metabolism genes rather than a validated treatment opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclinical | J Cardiovasc Pharmacol Ther | In human ApoB100/CETP transgenic mice, CETP inhibition (torcetrapib) and PPARα agonism (fenofibrate) were studied for effects on lipid profiles, including HDL and LDL cholesterol |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Preclinical | J Biol Chem | Fenofibrate induced the PLTP gene, accounting for the enlarged, cholesteryl ester-rich HDL seen in treated mice |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Preclinical / mechanistic | Front Physiol | Plasma HDL cholesterol did not correlate with faecal cholesterol excretion or cholesterol efflux capacity, suggesting HDL function matters more than HDL level |

None of these studies addresses CETP deficiency in patients.

<!-- review:begin uk-lic-20261106-fenofibrate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The list contains one single-ingredient authorisation." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 15 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-fenofibrate-1 -->

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0212000P0AAAGAG | Fenofibrate 160mg/5ml oral solution | Fenofibrate |
| 0212000P0AAAFAF | Fenofibrate 200mg capsules | Fenofibrate |
| 0212000P0AAAEAE | Fenofibrate micronised 160mg tablets | Fenofibrate |
| 0212000P0AAABAB | Fenofibrate micronised 200mg capsules | Fenofibrate |
| 0212000P0AAADAD | Fenofibrate micronised 267mg capsules | Fenofibrate |
| 0212000P0AAACAC | Fenofibrate micronised 67mg capsules | Fenofibrate |
| 0212000AJBBAAAA | Cholib 145mg/20mg tablets | Fenofibrate/simvastatin |
| 0212000AJBBABAB | Cholib 145mg/40mg tablets | Fenofibrate/simvastatin |
| 0212000AJAAAAAA | Fenofibrate 145mg / Simvastatin 20mg tablets | Fenofibrate/simvastatin |
| 0212000AJAAABAB | Fenofibrate 145mg / Simvastatin 40mg tablets | Fenofibrate/simvastatin |
| 0212000P0BDAAAF | Fenogal 200mg capsules | Fenofibrate |
| 0212000P0BBABAB | Lipantil Micro 200 capsules | Fenofibrate |
| 0212000P0BBADAD | Lipantil Micro 267 capsules | Fenofibrate |
| 0212000P0BBACAC | Lipantil Micro 67 capsules | Fenofibrate |
| 0212000P0BCAAAE | Supralip 160mg tablets | Fenofibrate |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver failure and liver disease, pancreatitis, gallbladder disease and cholelithiasis, myopathy and rhabdomyolysis, thrombocytopenia, anaemia, impaired renal function, and leukopenia, agranulocytosis and neutropenia (including congenital forms).
- **Drug interactions:** the interaction screen returned 100 records. The entries listed are all Moderate severity: sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), many insulin preparations, chenodeoxycholic acid and esomeprazole. Glucose-lowering therapy warrants attention when co-prescribed.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies fenofibrate in CETP deficiency itself, so the evidence level is L5. The mechanistic link is indirect, and raising HDL further in a condition that already has high HDL has no clear therapeutic basis.

**To proceed, the following is needed:**
- A clear clinical rationale showing that fenofibrate would benefit people with CETP deficiency, beyond HDL modulation
- Disease-specific preclinical or clinical studies in CETP deficiency
- Mechanism of action data and the licence indication and warning text from the SmPC
- A safety review of the contraindications and interactions above for this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The list contains one single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

