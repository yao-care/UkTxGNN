---
layout: default
title: Formaldehyde
parent: Model Prediction Only (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-25
monitor_inn: "Formaldehyde"
predicted_indications: ["leishmaniasis, diffuse cutaneous", "cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency", "mucocutaneous leishmaniasis", "pyelonephritis", "streptococcal pneumonia", "X-linked lymphoproliferative syndrome", "trigonitis", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "Plasmodium falciparum malaria"]
description: "Formaldehyde: predicted new indication Leishmaniasis, diffuse cutaneous (evidence level L5). In the UK: 8 NHSBSA BNF presentation codes"
---

# Formaldehyde
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

## Formaldehyde: Leishmaniasis, diffuse cutaneous
{: .text-alpha }

## One-Sentence Summary

Formaldehyde is recorded in the TxGNN knowledge graph as linked to influenza (for example through its use in inactivating vaccine antigens), and is listed in the UK BNF prescribing codes as topical solutions and gels.
The TxGNN model predicts it may be effective for **diffuse cutaneous leishmaniasis**, but there are **no clinical trials** and **no related publications** supporting this prediction.
The score is a computational output only, and the available data point to safety concerns rather than benefit.

<!-- review:begin uk-lic-20261124b-formaldehyde-1 -->

> **Review correction (2026-11-24)**: Originally stated: "and is marketed in the UK as a topical gel." Corrected: the sentence described the drug as having a single UK form, strength or product, based on the older evidence pack; the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902) lists presentations of this drug in more than one dosage form or strength. See the Quick Overview and the BNF code table under UK Market Information. These are NHS prescribing codes, not MHRA licences. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124b-formaldehyde-1 -->

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Leishmaniasis, diffuse cutaneous |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (8 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Formaldehyde is a reactive, non-selective cross-linking and tissue-fixing agent with general antimicrobial activity. This is why it is used for disinfection, tissue fixation and the inactivation of vaccine antigens.

The link between influenza and diffuse cutaneous leishmaniasis is weak. One is a viral respiratory infection and the other is a chronic infection caused by an intracellular protozoan parasite. A general biocidal action does not translate into a safe systemic treatment for parasites that live inside host cells. Formaldehyde is also cytotoxic and carcinogenic, which argues strongly against systemic therapeutic use.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and there is no documented pharmacological rationale. Other top-ranked predictions for this drug (mucocutaneous leishmaniasis, a mitochondrial disorder, haemophagocytic syndromes) share the same limitation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for diffuse cutaneous leishmaniasis.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1307000C0AAALAL | Formaldehyde (Buffered) 4% solution | Formaldehyde |
| 1307000C0AAABAB | Formaldehyde 0.75% gel | Formaldehyde |
| 1307000C0AAAHAH | Formaldehyde 2% solution | Formaldehyde |
| 1307000C0AAAFAF | Formaldehyde 3% solution | Formaldehyde |
| 1307000C0AAADAD | Formaldehyde 5% solution | Formaldehyde |
| 1307000C0AAAXAX | Formaldehyde 6% solution | Formaldehyde |
| 1307000C0AAACAC | Formaldehyde solution | Formaldehyde |
| 1307000C0BBAAAB | Veracur 0.75% gel | Formaldehyde |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The codes shown are NHSBSA BNF presentation codes, not MHRA PL numbers. Please check the MHRA register for licence details before relying on them.

<!-- review:begin uk-lic-20261124d-formaldehyde-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The identifier above is as recorded in the compiled licence data and is not in the standard MHRA "PL" format. Please verify it against the MHRA register before relying on it." Corrected wording only: the text described this site's UK market data as MHRA licences, marketing authorisations, licence numbers or licence records, or rested on a UK licence status. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902): these are NHS prescribing codes, not MHRA licences, they carry no indication text, and MHRA licence status is not included. The wording was changed to BNF prescribing codes (or the unsupported premise was removed); the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124d-formaldehyde-1 -->

---

## Safety Considerations

- **Carcinogenicity signal:** Occupational studies and meta-analyses in the literature compiled for this report associate formaldehyde exposure with lymphohaematopoietic malignancy (including non-Hodgkin lymphoma and leukaemia) and with cancers of the nasopharynx and nasal cavity. This is a harm signal relevant to any systemic or prolonged-exposure use.
- **Drug interactions:** No interaction data were found.

For label-based warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5), with no trials and no relevant publications. The proposed mechanism is not plausible for an intracellular parasite, and formaldehyde's known toxicity and carcinogenicity argue against systemic repurposing.

**To proceed, the following is needed:**
- Any in vitro or in vivo evidence of activity against *Leishmania* at tolerable concentrations
- Mechanism of action data and a clear rationale for the route of administration (topical use would need separate justification)
- Complete safety information from the SmPC and BNF for the UK gel products, including contraindications and warnings
- A review of whether less toxic, established anti-leishmanial options already address the clinical need

<!-- review:begin uk-lic-20261125-formaldehyde-1 -->

> **Review correction (2026-11-25)**: Originally stated: "Complete safety information from the SmPC and BNF for the marketed gel, including contraindications and warnings" Corrected wording only: the text said the drug or product is marketed, available or sold in the UK. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902): a BNF presentation code shows that an NHS prescribing code exists, not that the product is currently marketed or on sale, and MHRA licence status is not included. The wording was changed to the UK BNF prescribing codes (or the unsupported premise was removed); forms named are those in the BNF code list, and the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261125-formaldehyde-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Corrected: "and is marketed in the UK as a topical gel." | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-24 | Corrected: "The identifier above is as recorded in the compiled licence data and is not in the standard MHRA "PL" format. Please verify it against the MHRA register before relying on it." | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-25 | Corrected: "Complete safety information from the SmPC and BNF for the marketed gel, including contraindications and warnings" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

