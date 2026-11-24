---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 346
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Itraconazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Fungal infections (oesophageal candidiasis, candidaemia…"
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
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

## Itraconazole: From Fungal Infections to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Itraconazole is an azole antifungal, originally used for fungal infections such as candidiasis, histoplasmosis, aspergillosis and blastomycosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the data compiled for this report show **no registered clinical trials** and **20 publications**, none of which show that itraconazole treats *Pneumocystis*.
The prediction is best regarded as a model artefact rather than a credible repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (oesophageal candidiasis, candidaemia, histoplasmosis, aspergillosis, blastomycosis, coccidioidomycosis, sporotrichosis, fusariosis and others); no approved indication text is available for the UK products |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (8 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 8 |
| Recommended Decision | Hold |

<!-- review:begin uk-lic-20261124c-itraconazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Original Indication / Fungal infections (oesophageal candidiasis, candidaemia, histoplasmosis, aspergillosis, blastomycosis, coccidioidomycosis, sporotrichosis, fusariosis and others); no approved indication text is available for the UK product" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-itraconazole-1 -->

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for itraconazole: "In vitro studies have demonstrated that itraconazole inhibits the cytochrome P450-dependent synthesis of ergosterol, which is a vital component of fungal cell membranes." ([DailyMed: Sporanox (itraconazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a4d555fa-787c-40fb-bb7d-b0d4f7318fd0), label version 2026-07-13; accessed 2026-11-19.) From general pharmacology, itraconazole inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane. This underlies its activity against moulds and endemic fungi such as *Aspergillus* and *Histoplasma*.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as other fungal infections, not biological evidence. It probably does not reflect a true mechanistic fit. *Pneumocystis jirovecii* lacks ergosterol in its cell membrane and uses cholesterol instead, so azole antifungals are not expected to be effective. Co-trimoxazole (trimethoprim-sulfamethoxazole) remains the standard of care for both treatment and prophylaxis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications retrieved are mainly general reviews and case reports on opportunistic infections in HIV, transplant and neutropenic patients. In these, itraconazole appears as an agent against moulds or endemic fungi, not as a *Pneumocystis* therapy. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Phase III RCT (placebo-controlled) | HIV Medicine | Itraconazole capsules as prophylaxis against deep fungal infections in HIV-infected patients; the data compiled do not show a *Pneumocystis* outcome |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Pulmonary epithelial lining fluid penetration of antifungals; pharmacokinetic data only, not efficacy against *Pneumocystis* |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis of opportunistic infections in HIV |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clinical Infectious Diseases | Antimicrobial prophylaxis in febrile neutropenia; co-trimoxazole is highly effective against *Pneumocystis* pneumonia |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *Pneumocystis carinii* |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Infection after lung transplantation |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Invasive fungal infections after kidney transplantation (single centre) |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Case series | Medicine | Disseminated histoplasmosis in AIDS: clinical findings, diagnosis and treatment |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report with review | Frontiers in Immunology | *Talaromyces marneffei* and *Pneumocystis jirovecii* coinfection in a child with a STAT1 mutation |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0502010C0AAAAAA | Itraconazole 100mg capsules | Itraconazole |
| 0502010C0AAACAC | Itraconazole 50mg/5ml oral liquid | Itraconazole |
| 0502010C0AAABAB | Itraconazole 50mg/5ml oral solution sugar free | Itraconazole |
| 0502010C0AAADAD | Itraconazole 250mg/25ml concentrate and solvent for inf amp | Itraconazole |
| 0502010C0BBAAAA | Sporanox 100mg capsules | Itraconazole |
| 0502010C0BBACAB | Sporanox 50mg/5ml oral solution | Itraconazole |
| 0502010C0BBADAD | Sporanox I.V. 250mg/25ml inf ampoules and diluent | Itraconazole |
| 0502010C0BBABAA | Sporanox-Pulse 100mg capsules | Itraconazole |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

BNF classification code 0502010C relates to itraconazole within the antifungal drugs section (BNF chapter 5, infections).

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug-disease network links, not from the product label, and need confirmation against the SmPC):

- Cardiac: long QT syndrome, torsades de pointes, congestive heart failure, heart failure, cardiomyopathy, myocardial ischaemia, coronary artery disease, heart valve disease
- Hepatic and renal: liver disease, drug-induced liver injury, kidney disease, impaired renal function
- Respiratory: chronic obstructive pulmonary disease
- Neurological and sensory: peripheral neuropathy, vision disorder, hearing loss
- Metabolic: potassium deficiency, hypercalcaemia, nephrocalcinosis, achlorhydria

**Drug Interactions:** 100 interactions were identified; the main ones are listed below.

- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole (acid-reducing agents may reduce absorption of the capsule), hydrocortisone, dexamethasone, betamethasone, alosetron, aprepitant
- **Minor:** metformin, pioglitazone, chlorpropamide, amphotericin B

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L4 evidence). *Pneumocystis* lacks ergosterol, so the azole mechanism is not expected to work, and no trial or publication shows efficacy. Co-trimoxazole is the established standard of care. Itraconazole also carries notable cardiac and interaction risks.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or animal) of itraconazole activity against *Pneumocystis*, with a plausible non-ergosterol mechanism
- Mechanism of action data and SmPC-based warnings and contraindications for the UK products
- A clear clinical niche (for example, co-trimoxazole intolerance) before any clinical study is considered

<!-- review:begin uk-lic-20261124c-itraconazole-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Mechanism of action data and SmPC-based warnings and contraindications for the UK product" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-itraconazole-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sporanox (itraconazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a4d555fa-787c-40fb-bb7d-b0d4f7318fd0) |
| 2026-11-24 | Corrected: "&#124; Original Indication &#124; Fungal infections (oesophageal candidiasis, candidaemia, histoplasmosis, aspergillosis, blastomycosis, coccidioidomycosis, sporotrichosis, fusariosis and others); no approved indication text is available for the UK product &#124;" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-24 | Corrected: "Mechanism of action data and SmPC-based warnings and contraindications for the UK product" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

