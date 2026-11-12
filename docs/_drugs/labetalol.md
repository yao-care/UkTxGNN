---
layout: default
title: Labetalol
parent: Model Prediction Only (L5)
nav_order: 355
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Labetalol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "Labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Labetalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Labetalol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Labetalol is a combined alpha-1 and non-selective beta-adrenergic blocker, originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **no registered clinical trials** and **no directly relevant publications** supporting this prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (the approved indication text is not recorded in the licence data compiled for this report) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (19 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, labetalol combines alpha-1 and non-selective beta-adrenergic blockade. Its blood pressure lowering effect is established in hypertension and is used in hypertensive emergencies.

Malignant hypertensive renal disease is kidney injury driven by severely raised blood pressure. Controlling blood pressure is therefore mechanistically plausible as a way to limit further renal damage.

An important caveat: this predicted indication largely overlaps with the existing hypertension use rather than representing a truly distinct new indication. The high score is a computational prediction only, and the relationship to the original indication has not yet been formally assessed.

Two other predictions were also generated, and they are weaker:
- **Malignant renovascular hypertension** (score 0.9908): The only linked publication (PMID 7242419) is a 1981 case report of drug-induced vasculitis in which labetalol was used with minoxidil for initial blood pressure control. It does not evaluate labetalol for this indication. Beta-blockade may reduce renin, which is mechanistically relevant.
- **Pulmonary hypertension** (two predicted forms, score 0.9908): There is no supporting evidence. Beta-blockers are generally used cautiously in pulmonary hypertension because of the risk to right ventricular function, and non-selective beta-blockade may worsen bronchospasm in lung disease. The ten publications retrieved concern systemic or obstetric hypertension, beta-blocker overdose, and animal or unrelated studies, and appear to have been matched on keywords only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top predicted indication (malignant hypertensive renal disease), currently no related literature is available.

The only publication retrieved for a closely related predicted indication (malignant renovascular hypertension) is below. It is a low-tier case report and does not provide evidence of efficacy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | Med J Aust | Malignant hypertension in a young man after hallucinogenic drug use, with vasculitis responding to prednisone. Minoxidil and labetalol were used for initial blood pressure control. |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0204000I0AAANAN | Labetalol 1.5mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0AAACAC | Labetalol 100mg tablets | Labetalol hydrochloride |
| 0204000I0AAAAAA | Labetalol 100mg/20ml solution for injection ampoules | Labetalol hydrochloride |
| 0204000I0AAALAL | Labetalol 100mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0AAAMAM | Labetalol 10mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0AAADAD | Labetalol 200mg tablets | Labetalol hydrochloride |
| 0204000I0AAAJAJ | Labetalol 200mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0AAAKAK | Labetalol 25mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0AAAEAE | Labetalol 400mg tablets | Labetalol hydrochloride |
| 0204000I0AAABAB | Labetalol 50mg tablets | Labetalol hydrochloride |
| 0204000I0AAAPAP | Labetalol 50mg/10ml inj pre-filled syringes | Labetalol hydrochloride |
| 0204000I0AAAIAI | Labetalol 50mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0AAARAR | Labetalol 5mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0AAAQAQ | Labetalol 75mg/5ml oral liquid | Labetalol hydrochloride |
| 0204000I0BCABAC | Trandate 100mg tablets | Labetalol hydrochloride |
| 0204000I0BCAEAA | Trandate 100mg/20ml solution for injection ampoules | Labetalol hydrochloride |
| 0204000I0BCACAD | Trandate 200mg tablets | Labetalol hydrochloride |
| 0204000I0BCADAE | Trandate 400mg tablets | Labetalol hydrochloride |
| 0204000I0BCAAAB | Trandate 50mg tablets | Labetalol hydrochloride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The licence identifier is not in the standard MHRA "PL" format, so the number, form and indication should be verified against the MHRA records and the BNF before any decision relies on them.

<!-- review:begin uk-lic-20261106-labetalol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "One valid single-ingredient authorisation is recorded, with no cancelled authorisations. The licence identifier is not in the standard MHRA "PL" format, so the number, form and indication should be verified against the MHRA records and the BNF before any decision relies on them." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 19 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-labetalol-1 -->

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are drug-disease associations from the TxGNN knowledge graph, not label text, and should be confirmed against the SmPC):
- Cardiac and respiratory: atrioventricular block, pulmonary emphysema, bronchial disease, hypotensive disorder
- Hepatic: liver failure, liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease, pancreatitis, neonatal jaundice
- Renal and metabolic: kidney disease, anuria, diabetes mellitus, diabetic ketoacidosis, gout, hyperuricaemia, potassium deficiency, hypercalcaemia, hyperparathyroidism, nephrocalcinosis, phosphorus metabolism disease
- Other: systemic lupus erythematosus (including paediatric), anxiety and neurotic disorders, dysthymic disorder, pyoureter, intraoperative floppy iris syndrome

Several of these, particularly kidney disease and anuria, are directly relevant to a renal indication.

**Drug interactions** (100 interactions recorded; examples from the first 20 reviewed):
- **Major**: epinephrine, dolasetron
- **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine, dicyclomine), morphine, cimetidine, SGLT2 inhibitors (canagliflozin, dapagliflozin), chlorpropamide, calcium salts
- **Minor**: acetylsalicylic acid, magnesium oxide

Package insert warnings and contraindications could not be retrieved. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5), with no registered trials and no directly relevant publications. The predicted indication also largely overlaps with labetalol's existing hypertension use, so it is not a clearly new therapeutic direction.

**To proceed, the following is needed:**
- Retrieval of the SmPC and BNF warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data
- The licensed indication text and dosage form for the UK authorisation, verified against MHRA records
- A targeted literature search for labetalol in malignant hypertension with renal involvement, including NICE and BNF guidance on hypertensive emergencies
- Review of the knowledge-graph contraindications (notably kidney disease and anuria) against the SmPC for any renal use
- Clarification of whether this is a genuinely new indication or falls within the existing hypertension label
- No further investment is recommended for the pulmonary hypertension predictions unless supporting safety and efficacy data emerge

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One valid single-ingredient authorisation is recorded, with no cancelled authorisations" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

