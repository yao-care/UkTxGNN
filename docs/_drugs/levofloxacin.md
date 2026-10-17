---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections (streptococcal, staphylococcal, pneumonia…"
monitor_inn: "Levofloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibacterial, originally used for infections such as bacterial pneumonia, sinusitis, conjunctivitis and pyelonephritis.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis**, but it is supported by **no clinical trials** and **1 publication** (an outbreak report that does not support efficacy).
Of the ten predictions reviewed, the best-supported direction is **infection prophylaxis in myeloma (monoclonal gammopathy spectrum)**, backed by a Phase 3 RCT (TEAMM).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal, staphylococcal, pneumonia, sinusitis, conjunctivitis, pyelonephritis, anthrax) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis (rank 1); see the note on other predictions below |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (rank 1 prediction); L1 for the monoclonal gammopathy/myeloma prophylaxis prediction (rank 7) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails for myeloma infection prophylaxis |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Levofloxacin belongs to the fluoroquinolone class, which is known to kill bacteria by inhibiting DNA gyrase and topoisomerase IV. Its efficacy in bacterial conjunctivitis is established, so ocular surface use is plausible.

For the rank 1 prediction, the link is weak. The only retrieved paper describes an outbreak of microsporidial keratoconjunctivitis linked to swimming pool water in Taiwan. Microsporidia are not meaningfully susceptible to fluoroquinolones, so this paper offers no support for efficacy. The high TxGNN score remains a model prediction only.

Among the other predictions, two have a more credible rationale:

- **Monoclonal gammopathy / myeloma (rank 7):** Levofloxacin acts as an antibacterial prophylactic, not a disease-modifying agent. The evidence supports preventing infection in symptomatic myeloma, not treating MGUS or the underlying gammopathy.
- **Septicaemic plague (rank 9):** Levofloxacin is active against *Yersinia pestis*. The evidence is mostly from animal models, and the plague indication is closer to an extension of its existing antibacterial use than a novel repurposing.

The remaining predictions (polyclonal hyperviscosity syndrome, hyperamylasaemia, congenital analbuminaemia, blood group incompatibility, premalignant haematological disease, haematological disease with peripheral neuropathy, congenital haematological disorder) have no plausible mechanistic link or only anecdotal evidence. For hyperamylasaemia and neuropathy-related disease, the known safety profile of fluoroquinolones points in the opposite direction.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the rank 1 prediction.

For the rank 7 prediction (myeloma infection prophylaxis), no registered trials were retrieved in the data compiled for this report, but the following published randomised trial is relevant:

| Trial | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| TEAMM (published in PMID [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/)) | Phase 3 | Published | Not stated | Multicentre, double-blind, placebo-controlled trial of levofloxacin prophylaxis in newly diagnosed myeloma; reduced febrile episodes and deaths in the first 12 weeks |

---

## Literature Evidence

**Rank 1: punctate epithelial keratoconjunctivitis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | Am J Ophthalmol | Microsporidial keratoconjunctivitis outbreak from swimming pool water in Taiwan; no evidence for levofloxacin efficacy |

**Rank 7: monoclonal gammopathy / myeloma (most relevant publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT (Phase 3) | Lancet Oncol | TEAMM: levofloxacin prophylaxis in newly diagnosed myeloma |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | RCT (summary) | Health Technol Assess | UK TEAMM report; notes concern over healthcare-associated infections such as *C. difficile* |
| [32172361](https://pubmed.ncbi.nlm.nih.gov/32172361/) | 2020 | Review | Curr Hematol Malig Rep | Supportive care in myeloma, including infection management |
| [37573150](https://pubmed.ncbi.nlm.nih.gov/37573150/) | 2023 | Cohort | Transpl Infect Dis | Infectious complications after autologous transplant in myeloma, with or without levofloxacin prophylaxis |
| [29080369](https://pubmed.ncbi.nlm.nih.gov/29080369/) | 2018 | Retrospective cohort | Clin Transplant | Ciprofloxacin vs levofloxacin prophylaxis in autologous transplant for myeloma (297 patients) |
| [26150022](https://pubmed.ncbi.nlm.nih.gov/26150022/) | 2015 | Cohort | Biol Blood Marrow Transplant | Levofloxacin prophylaxis and bloodstream infection or fever in neutropenic myeloma patients |
| [25212681](https://pubmed.ncbi.nlm.nih.gov/25212681/) | 2014 | Study | Int J Hematol | Levofloxacin prophylaxis in myeloma patients on bortezomib regimens |
| [32007199](https://pubmed.ncbi.nlm.nih.gov/32007199/) | 2020 | Correspondence | Lancet Oncol | Commentary on TEAMM |
| [32007198](https://pubmed.ncbi.nlm.nih.gov/32007198/) | 2020 | Correspondence | Lancet Oncol | Commentary on TEAMM |
| [25591868](https://pubmed.ncbi.nlm.nih.gov/25591868/) | 2016 | Case report | J Oncol Pharm Pract | Acute kidney injury from crystal nephropathy with pomalidomide and levofloxacin |

**Rank 9: septicaemic plague (most relevant publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Animal study (primate) | PLoS Negl Trop Dis | Levofloxacin cured experimental pneumonic plague in African green monkeys |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal study (primate) | Clin Infect Dis | Effect of delayed treatment on ciprofloxacin and levofloxacin efficacy |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Review | Clin Infect Dis | African green monkey model and FDA approval under the Animal Rule |
| [17517837](https://pubmed.ncbi.nlm.nih.gov/17517837/) | 2007 | In vitro model | Antimicrob Agents Chemother | Streptomycin vs levofloxacin for plague, including resistance selection |
| [21574421](https://pubmed.ncbi.nlm.nih.gov/21574421/) | 2010 | Animal study (mouse) | Antibiot Khimioter | Levofloxacin ineffective against nalidixic acid-resistant plague strains |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Animal study (mouse) | Antibiot Khimioter | Levofloxacin effective in mice against FI+ and FI- *Y. pestis* strains |

No human RCT exists for plague.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501120X0AAAAAA | Levofloxacin Tab 500mg | Tablet (not specified in the data) | Not specified in the data |

One valid single-ingredient authorisation is recorded. Please check the current SmPC and BNF (fluoroquinolone antibacterials) for the full licensed indications.

---

## Safety Considerations

**Contraindications and cautions from the knowledge graph** (these are drawn from drug-disease links, not from label text, and should be verified against the SmPC):

- **Cardiac:** long QT syndrome (including familial), torsades de pointes, myocardial ischaemia, coronary artery disease
- **Neurological and neuromuscular:** epilepsy, myasthenia gravis (including adult-onset), neuromuscular junction disease, peripheral neuropathy and peripheral nervous system disease
- **Musculoskeletal:** tendinitis, periarthritis, rhabdomyolysis
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- **Hepatic, gastrointestinal and renal:** liver disease, drug-induced liver injury, gallbladder disease, *Clostridium difficile* colitis, impaired renal function
- **Haematological:** thrombocytopenia, leukopenia, pancytopenia, anaemia

**Drug interactions:** 100 interactions were identified. Examples include:

- **Major:** tramadol, hydrocortisone
- **Moderate:** abiraterone, acarbose, famotidine, formoterol, ketorolac, adenosine, ibuprofen, ethinylestradiol, salbutamol, alfuzosin, alogliptin, metformin, pioglitazone, amifampridine, albiglutide
- **Minor:** paclitaxel, aldesleukin, altretamine

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold (rank 1, punctate epithelial keratoconjunctivitis); Proceed with Guardrails for infection prophylaxis in myeloma**

**Rationale:**
- The top-ranked prediction rests on a model score alone. Its single publication concerns a microsporidial outbreak, and microsporidia are not susceptible to fluoroquinolones.
- The most robust finding is the TEAMM Phase 3 RCT, which supports infection prevention in symptomatic myeloma. This is supportive care, not treatment of the gammopathy itself, and it must be weighed against antibiotic resistance, *C. difficile* risk and adverse effects.

**To proceed, the following is needed:**
- Mechanism of action data and the full SmPC warnings and contraindications for the UK product
- Licensed indication and dosage form details for the UK authorisation
- For ocular use: evidence of in vitro or clinical activity against the causative pathogens of punctate epithelial keratoconjunctivitis, and a suitable ophthalmic formulation
- For myeloma prophylaxis: review of NICE and UK haematology guidance in light of TEAMM, with a stewardship and resistance monitoring plan and a QT and tendon risk assessment
- For plague: confirmation of whether the existing licence already covers this use, given that the evidence is largely from animal models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

