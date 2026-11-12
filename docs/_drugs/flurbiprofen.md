---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 300
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
monitor_inn: "Flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
description: "Flurbiprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Flurbiprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Flurbiprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatic conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
There are currently **no clinical trials** and **no publications** supporting this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (17 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Flurbiprofen is an NSAID of the phenylalkanoic acid class. As a class, NSAIDs inhibit cyclo-oxygenase (COX) enzymes and reduce prostaglandin-mediated inflammation and pain. This is the basis of its use in inflammatory and degenerative joint disease.

The predicted condition is different in nature. Acromesomelic dysplasia, Hunter-Thompson type, is a congenital skeletal dysplasia affecting limb development. It has no recognised inflammatory driver that COX inhibition would be expected to modify. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

At most, a purely symptomatic role (for example, joint pain relief) can be imagined. No data support even this, and there is no plausible disease-modifying mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1104020G0AAACAC | Flurbiprofen 0.03% eye dps 0.4ml unit dose preservative free | Flurbiprofen sodium |
| 1001010I0AAAAAA | Flurbiprofen 100mg suppositories | Flurbiprofen |
| 1001010I0AAACAC | Flurbiprofen 100mg tablets | Flurbiprofen |
| 1001010I0AAADAD | Flurbiprofen 200mg modified-release capsules | Flurbiprofen |
| 1001010I0AAABAB | Flurbiprofen 50mg tablets | Flurbiprofen |
| 1203010F0AAABAB | Flurbiprofen 2.92mg/actuation oromucosal spray sugar free | Flubiprofen |
| 1203010F0AAAAAA | Flurbiprofen 8.75mg lozenges | Flubiprofen |
| 1203010F0AAACAC | Flurbiprofen 8.75mg lozenges sugar free | Flubiprofen |
| 1001010I0BBACAA | Froben 100mg suppositories | Flurbiprofen |
| 1001010I0BBABAC | Froben 100mg tablets | Flurbiprofen |
| 1001010I0BBAAAB | Froben 50mg tablets | Flurbiprofen |
| 1001010I0BBADAD | Froben SR 200mg capsules | Flurbiprofen |
| 1104020G0BBABAC | Ocufen 0.03% eye drops 0.4ml unit dose | Flurbiprofen sodium |
| 1203010F0BBACAB | Strefen Direct 8.75mg oromucosal spray | Flubiprofen |
| 1203010F0BBAEAC | Strefen Eucalyptus and Manuka Honey 8.75mg lozenges | Flubiprofen |
| 1203010F0BBAAAA | Strefen Honey and Lemon 8.75mg lozenges | Flubiprofen |
| 1203010F0BBADAC | Strefen Orange 8.75mg lozenges sugar free | Flubiprofen |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Indication text, manufacturer and dosage-form fields are not populated, and no NICE-appraised indication information was available. Check the BNF and the current SmPC for the licensed indications.

<!-- review:begin uk-lic-20261106-flurbiprofen-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data show one valid single-ingredient authorisation. Indication text, manufacturer and dosage-form fields are not populated, and no NICE-appraised indication information was available." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 17 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-flurbiprofen-1 -->

## Safety Considerations

- **Contraindications (knowledge-graph-derived, not label text)**: The knowledge graph links flurbiprofen with contraindications in these conditions:
  - Cardiovascular: hypertension, myocardial infarction, coronary thrombosis, heart disease, cardiovascular disease
  - Gastrointestinal and hepatic: peptic ulcer disease (including active), liver disease, gallbladder disease
  - Renal: kidney disease, pyoureter
  - Haematological: blood coagulation disease, haemoglobinopathy
  - Other: substance abuse/dependence

  These reflect the usual NSAID class cautions and must be confirmed against the SmPC.
- **Drug Interactions**: The interaction query returned 100 interacting drugs; the 20 reviewed here are mostly moderate-level.
  - Moderate interactions include acetylsalicylic acid, the corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, the sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, aprepitant, and several bowel preparations and potassium salts.
  - Minor interactions include famotidine, cimetidine and linaclotide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and no plausible mechanistic link. The condition is a congenital skeletal dysplasia with no inflammatory target for flurbiprofen. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanism of action data, and any biological rationale linking COX inhibition to this condition
- Preclinical or clinical evidence in this disorder (none currently exists)
- Full safety data from the SmPC and BNF, given the cardiovascular, gastrointestinal, renal and hepatic cautions above
- Complete UK authorisation details (indication text, dosage form, valid licence number)

This includes several randomised, double-blind comparisons with indomethacin, phenylbutazone and naproxen from the 1970s and 1980s (for example [PMID 4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) and [PMID 3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/)). It sits at evidence level L3 and is better viewed as an extension within the NSAID class than as novel repurposing. It would be the more productive direction to evaluate, and its evidence should not be transferred to the indication reported here.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data show one valid single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

