---
layout: default
title: Fidaxomicin
parent: Model Prediction Only (L5)
nav_order: 287
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Fidaxomicin"
predicted_indications: ["staphylococcal scalded skin syndrome", "bullous impetigo", "inhalational botulism", "impetigo", "toxin-mediated infectious botulism", "vulvovaginal candidiasis", "hordeolum", "staphylococcus aureus pneumonia", "punctate epithelial keratoconjunctivitis"]
description: "Fidaxomicin: predicted new indication Staphylococcal scalded skin syndrome (evidence level L5). In the UK: 4 NHSBSA BNF presentation codes"
---

# Fidaxomicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Fidaxomicin: Staphylococcal scalded skin syndrome
{: .text-alpha }

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum antibacterial, originally used to treat *Clostridium difficile* colitis.
The TxGNN model predicts it may be effective for **staphylococcal scalded skin syndrome**,
but there are currently **no clinical trials** and **no relevant publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Staphylococcal scalded skin syndrome |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for fidaxomicin: "Fidaxomicin is an antibacterial drug. […] Fidaxomicin is a fermentation product obtained from the Actinomycete Dactylosporangium aurantiacum. Fidaxomicin is a macrolide antibacterial drug that inhibits RNA synthesis by binding to RNA polymerases. Fidaxomicin is bactericidal against C. difficile in vitro, and demonstrates a post-antibiotic effect vs. C. difficile of 6-10 hrs." ([DailyMed: Dificid (fidaxomicin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb), label version 2024-10-16; accessed 2026-11-19.) Based on general knowledge, fidaxomicin is a narrow-spectrum macrocyclic antibacterial that inhibits bacterial RNA polymerase. Its efficacy in *C. difficile* colitis is established, and it may show in vitro activity against some Gram-positive organisms, including *Staphylococcus aureus*.

That in vitro activity is the only link to the predicted indication, and it is a weak one. Staphylococcal scalded skin syndrome is a toxin-mediated skin disease caused by *S. aureus*. Fidaxomicin has minimal systemic absorption, so it is unlikely to reach effective concentrations in skin or blood. The high TxGNN score probably reflects similarity between anti-infective agents and infections rather than a demonstrated pharmacological rationale.

Other top-ranked predictions (bullous impetigo, impetigo, inhalational botulism, toxin-mediated infectious botulism, vulvovaginal candidiasis, hordeolum, *S. aureus* pneumonia and punctate epithelial keratoconjunctivitis) also have scores of 0.9902 to 0.9970. None has trial or supporting literature evidence, and several lack any plausible mechanism (for example, an antibacterial for a fungal infection or a preformed neurotoxin). The only conceivable link for toxin-mediated infectious botulism is gut-localised activity against *Clostridium* species, which is indirect reasoning only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication of staphylococcal scalded skin syndrome.

For completeness, one publication was retrieved for the lower-ranked prediction of *S. aureus* pneumonia: [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) (2019, Review, *Journal of Hospital Medicine*), a general hospital medicine literature update noting that vancomycin or fidaxomicin are first-line treatments for *C. difficile* infection. It is not specific to *S. aureus* disease and is not supporting evidence.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0501070ACAAAAAA | Fidaxomicin 200mg tablets | Fidaxomicin |
| 0501070ACAAABAB | Fidaxomicin 40mg/ml oral suspension sugar free | Fidaxomicin |
| 0501070ACBBAAAA | Dificlir 200mg tablets | Fidaxomicin |
| 0501070ACBBABAB | Dificlir 40mg/ml oral suspension | Fidaxomicin |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The BNF code suggests a position in BNF chapter 5 (infections), but the data compiled for this report do not include the product's dosage form field, manufacturer or approved indication text.

## Safety Considerations

**Drug Interactions**

The interaction screen returned 79 interacting drugs in total; the first 20 are summarised here.

- **Major:** *Vibrio cholerae* CVD 103-HgR strain live antigen (live vaccine).
- **Moderate:** alpelisib, apalutamide, binimetinib, picosulfuric acid.
- **Minor:** nifedipine, amiodarone, brigatinib, cabozantinib, capmatinib, diltiazem, spironolactone, clarithromycin, verapamil, cyclosporine, daclatasvir, dronedarone, erythromycin, elagolix, ivacaftor.

Please refer to the SmPC and BNF for warnings and contraindications, which are not available in the data compiled for this report. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no trials or relevant publications. Fidaxomicin's minimal systemic absorption makes efficacy in a toxin-mediated systemic skin disease implausible, and established treatments already exist.

**To proceed, the following is needed:**
- Mechanism of action data and a clear pharmacological rationale for staphylococcal scalded skin syndrome
- Preclinical data on activity against toxin-producing *S. aureus* strains and on skin or tissue exposure
- Confirmation of whether a topical or systemic formulation could achieve effective concentrations
- Warnings and contraindications from the SmPC and BNF, so that safety screening can be completed
- Approved indication text and product details for the UK products

<!-- review:begin uk-lic-20261124c-fidaxomicin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Approved indication text and product details for the UK authorisation" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-fidaxomicin-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Dificid (fidaxomicin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb) |
| 2026-11-24 | Corrected: "Approved indication text and product details for the UK authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

