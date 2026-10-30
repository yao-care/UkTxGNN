---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Pyrazinamide: predicted new indication Infectious otitis media (evidence level L5). Approved use: Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis"
monitor_inn: "Pyrazinamide"
predicted_indications: ["infectious otitis media", "middle ear disease", "otosalpingitis", "chronic otitis media", "suppurative otitis media", "non-suppurative otitis media", "middle ear cholesterol granuloma", "allergic otitis media", "Lyme disease", "infectious otitis interna"]
---

# Pyrazinamide
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

## Pyrazinamide: From Tuberculosis to Infectious Otitis Media
{: .text-alpha }

## One-Sentence Summary

Pyrazinamide is an antimycobacterial drug originally used to treat pulmonary and meningeal tuberculosis.
The TxGNN model predicts it may be effective for **infectious otitis media**, but **no clinical trials and no publications** currently support this specific prediction. The literature found for related middle ear diagnoses consists of case reports of tuberculous otitis media, which fall under the existing TB indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis (the UK licence record contains no indication text) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pyrazinamide is an antimycobacterial agent used as part of multi-drug anti-tuberculosis regimens. Its activity depends on conversion to pyrazinoic acid by mycobacterial pyrazinamidase, a mechanism specific to *Mycobacterium tuberculosis*.

The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (tuberculosis-related infectious diseases and ear infections), not biological evidence. Common causes of bacterial otitis media (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*) are not susceptible to pyrazinamide. The only plausible link is the rare tuberculous otitis media, which is already covered by the existing TB indication and is not true repurposing.

The other top-ranked predictions are all ear-related (middle ear disease, otosalpingitis, chronic, suppurative, non-suppurative and allergic otitis media, middle ear cholesterol granuloma, infectious otitis interna). Lyme disease is also predicted, but with no mechanistic support. None has a credible mechanism beyond tuberculous involvement.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publications were found for infectious otitis media itself. The most relevant items come from closely related predicted diagnoses (middle ear disease, chronic and suppurative otitis media):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case report | Int J Mycobacteriol | Nasal and middle ear TB in a 55-year-old woman, treated for 9 months with rifampicin, isoniazid and pyrazinamide. No recurrence at one year. |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | Am J Kidney Dis | Tuberculous otitis media in a renal transplant recipient, after recurrent chronic otitis media was treated repeatedly with empiric antibiotics. |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | Tuberculous otitis media presenting as otorrhoea; rare and often diagnosed late in low-prevalence regions. |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Clinical observation | Laryngo-Rhino-Otologie | 12 patients with TB first found in the head and neck, including one with middle ear involvement. |
| [21439219](https://pubmed.ncbi.nlm.nih.gov/21439219/) | 2011 | Animal study (mouse) | J Am Assoc Lab Anim Sci | Torticollis in mice infected with *M. tuberculosis*, including those given pyrazinamide-containing regimens. Indirect relevance only. |

These reports describe pyrazinamide as one component of standard anti-TB therapy for tuberculosis at an unusual site. They do not show benefit in non-tuberculous otitis media.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501090N0AAAAAA (BNF-style code, not a PL number) | Pyrazinamide Tablets 500 mg | Tablet | Indication text not available in the data compiled for this report |

The single authorisation is a valid single-ingredient product. The BNF classification code suggests section 5.1.9 (antituberculosis drugs). Please confirm the licensed indication and PL number against the MHRA record and SmPC.

---

## Safety Considerations

- **Contraindications and risk conditions (not from label text):** liver failure, acute liver failure, liver disease, hepatitis, inherited porphyria, porphyrin metabolism disease, porphyria, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, gout, peripheral nervous system disease, peripheral neuropathy, substance abuse/dependence, and slow acetylator status. These should be verified against the SmPC.
- **Drug Interactions:** 56 interactions were identified. Those rated Moderate are picosulfuric acid and naltrexone. Others, listed without a severity grade, include pantoprazole, omeprazole, lansoprazole, mesalazine, morphine, vancomycin, prednisone, prednisolone, amphotericin B, potassium chloride, sulfasalazine, ranitidine, famotidine, metronidazole, acetylsalicylic acid, glyburide, amoxicillin and streptomycin.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no direct literature, and no plausible mechanism for common otitis media. The only supporting reports are case reports of tuberculous otitis media, which are already covered by the existing TB indication. Exposing patients to a hepatotoxic agent without a rationale is not justified.

**To proceed, the following is needed:**
- Microbiological evidence that a non-tuberculous otitis media pathogen is susceptible to pyrazinamide (currently none)
- Mechanism of action data and licensed indication text for the UK product
- Verified SmPC warnings and contraindications (the label-based safety data were unavailable)
- If of interest, clarify whether the aim is simply to support anti-TB therapy in confirmed tuberculous otitis media, which needs no new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

