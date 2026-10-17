---
layout: default
title: Clarithromycin
parent: Model Prediction Only (L5)
nav_order: 176
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Clarithromycin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial infections, including infectious otitis media…"
monitor_inn: "Clarithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
---

# Clarithromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Clarithromycin: From Respiratory and Streptococcal Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic, originally used for bacterial infections such as pneumonia, otitis media, sinusitis and streptococcal or staphylococcal infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are currently **no clinical trials** and **no publications** supporting this direction. The prediction rests on the computational score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including infectious otitis media, bacterial pneumonia, maxillary sinusitis, and streptococcal and staphylococcal infections (the MHRA licence record compiled for this report contains no indication text, so these come from the knowledge-graph indication data) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Clarithromycin is a macrolide antibiotic whose efficacy in respiratory and other bacterial infections is established. Macrolides are also known to have immunomodulatory and anti-inflammatory properties, such as effects on cytokine production and on B-cell and plasma-cell activity.

Polyclonal hyperviscosity syndrome arises from raised levels of immunoglobulins. In theory, an immunomodulatory effect on antibody-producing cells could be relevant. However, this link is **speculative**. No retrieved data support a direct mechanistic connection, and the high score is a network-based computational prediction only.

Other predictions for this drug are also weak:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Hyperamylasemia | 99.35% | L5 | A single case report of a *M. abscessus* lung infection with macroamylasemia; clarithromycin was likely used for the infection, not the enzyme abnormality |
| Congenital analbuminemia | 99.21% | L5 | A genetic defect in albumin synthesis; no plausible mechanism |
| Punctate epithelial keratoconjunctivitis | 99.11% | L4 | Plausible indirect link via the anti-inflammatory effects of macrolides in meibomian gland disease; no clarithromycin-specific evidence |
| Blood group incompatibility | 99.07% | L5 | No mechanistic link; interaction concerns with transplant immunosuppressants |

Of these, punctate epithelial keratoconjunctivitis has the most biologically coherent rationale and may merit a closer look as a research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

For the lower-ranked predictions, two publications were retrieved:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38472959](https://pubmed.ncbi.nlm.nih.gov/38472959/) | 2024 | Retrospective observational study | Diagnostics (Basel) | Features and treatment outcomes of keratoepitheliopathy in meibomitis-related keratoconjunctivitis (27 eyes, 18 patients); relevant to punctate epithelial keratoconjunctivitis, but clarithromycin-specific efficacy is not confirmed |
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case report | Nihon Kokyuki Gakkai Zasshi | *M. abscessus* lung infection complicated by primary macroamylasemia; relevant to hyperamylasemia only incidentally |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501050B0AAAAAA | Clarithromycin Tab 250 mg | Tablet | Not available in the compiled data |

This is a single-ingredient product with valid status. The identifier above is in a BNF-style code format rather than a standard PL number, so it should be verified against the MHRA register.

---

## Safety Considerations

**Contraindications and cautions from knowledge-graph data** (these come from drug-disease relationships, not product label text, and should be checked against the SmPC):

- **Cardiac:** long QT syndrome, torsades de pointes, ventricular tachycardia (including catecholaminergic polymorphic and incessant infant forms)
- **Hepatic and biliary:** liver failure, liver disease, cholestasis (including benign recurrent and familial intrahepatic forms), gallbladder disease
- **Metabolic:** porphyria (inherited porphyria and porphyrin metabolism disease)
- **Renal:** kidney disease, pyoureter
- **Neuromuscular:** myasthenia gravis (including adult-onset), neuromuscular junction disease
- **Gastrointestinal:** *Clostridium difficile* colitis, perinatal necrotising enterocolitis
- **Bone:** osteoporosis, postmenopausal osteoporosis, bone fracture
- **Infectious:** infectious mononucleosis, chronic Epstein-Barr virus infection syndrome

**Drug Interactions:** The interaction query returned 100 interactions in total. Examples of those rated **Major** include:
- Abemaciclib
- Fentanyl
- Acalabrutinib

Examples rated **Moderate** include paclitaxel, tramadol, famotidine, formoterol, nifedipine, adenosine, trastuzumab emtansine, flunisolide, afatinib, ethinylestradiol, hydrocortisone, abametapir (topical), abiraterone and acarbose. Minor interactions include dolutegravir, zidovudine and loratadine.

Clarithromycin is a strong CYP3A4 and P-gp inhibitor, which is the likely basis for many of these interactions.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome rests on a computational score alone (L5), with no trials, no literature and no supported mechanistic link. The other top-ranked predictions are similarly unsupported, and the extensive interaction and cardiac contraindication profile raises the bar for any new use.

**To proceed, the following is needed:**
- Mechanism of action data, to allow proper mechanistic analysis
- Product label information (indications, warnings, contraindications) for the UK authorisation, as the current record is incomplete
- A targeted literature search on macrolide immunomodulation in hypergammaglobulinaemic states
- Consideration of punctate epithelial keratoconjunctivitis as a separate research question, supported by clarithromycin-specific ocular data
- Preclinical or early-phase evidence before any clinical development is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

