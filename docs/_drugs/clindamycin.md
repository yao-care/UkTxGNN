---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clindamycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections (streptococcal…"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis", "superior limbic keratoconjunctivitis", "visual snow syndrome", "keratomalacia", "ophthalmia nodosa"]
---

# Clindamycin
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

## Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Clindamycin is an antibacterial originally used for bacterial infections such as staphylococcal and streptococcal infections, anaerobic infections, bacterial vaginosis and acne.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal, staphylococcal and anaerobic infections), bacterial vaginosis, acne, aspiration pneumonia (from the knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Clindamycin is a lincosamide antibacterial that is generally understood to inhibit bacterial protein synthesis by binding to the 50S ribosomal subunit. It is mainly active against Gram-positive and anaerobic bacteria.

The link between the original and predicted indications is weak. Punctate epithelial keratoconjunctivitis is often viral or non-infectious, so a plausible antibacterial mechanism has not been established. The high score is therefore best treated as a model-generated hypothesis rather than a mechanistically supported finding.

Other predictions in the list show similar problems. For example, visual snow syndrome (neurological), epidemic keratoconjunctivitis (adenoviral) and ophthalmia nodosa (inflammatory reaction to caterpillar hairs) have no obvious antibacterial rationale. Exposure keratitis has some indirect plausibility, since Gram-positive organisms such as *Staphylococcus aureus* can cause secondary bacterial keratitis. However, the retrieved papers cover bacterial keratitis in general and do not show that clindamycin works.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (punctate epithelial keratoconjunctivitis).

For context, the second-ranked prediction (exposure keratitis) has limited, indirect literature. None of it assesses clindamycin efficacy in that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective cohort | PLoS One | Hospital case review of *S. aureus* keratitis, comparing MRSA and MSSA isolates |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective cohort | PLoS One | Prevalence, clinical features and antibiotic susceptibility of ocular MRSA vs MSSA infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis linked to a contaminated lens case |
| [42763505](https://pubmed.ncbi.nlm.nih.gov/42763505/) | 2026 | Case report | IDCases | Foveal ocular toxoplasmosis diagnosed by intraocular fluid sequencing (a different pathogen) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501060D0AAABAB | Clindamycin HCl capsules 150 mg | Capsule | Not stated in the data compiled for this report |

The number shown appears to be a BNF-style product code rather than an MHRA "PL" number, so the MHRA licence details should be confirmed directly.

## Safety Considerations

- **Contraindication and disease-association signals (knowledge graph, not label text):** liver failure, inflammatory bowel disease (including Crohn's disease, Crohn's colitis and ulcerative colitis), *Clostridium difficile* colitis, diarrhoeal disease, perinatal necrotising enterocolitis, atopic eczema and other dermatitis (including exfoliative dermatitis), sunburn, and vulvovaginal candidiasis.
- **Drug Interactions:** 100 interactions were identified. Those graded Moderate were balsalazide, clarithromycin, picosulfuric acid, attapulgite and kaolin. Other listed interactions had no assigned severity, including amphotericin B, acetylsalicylic acid, amoxicillin, bupropion, pantoprazole, glimepiride, doxycycline, clotrimazole, morphine, metformin, omeprazole, sucralfate, rosiglitazone, lansoprazole and vancomycin.
- **Safety signal for consideration:** Clindamycin is a recognised risk factor for *C. difficile* infection. This is a harm signal, not a therapeutic one.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. The proposed mechanism is also doubtful, since the condition is often viral or non-infectious. The data compiled for this report also lack mechanism of action and label safety data.

**To proceed, the following is needed:**
- Mechanism of action data and SmPC/BNF warnings and contraindications
- Confirmation of the MHRA licence number, dosage form and approved indications
- Evidence of an infectious, clindamycin-sensitive component in punctate epithelial keratoconjunctivitis, or direct preclinical or clinical data
- Assessment of whether an ocular (topical) route is feasible, since only an oral capsule is listed
- If a ophthalmic infection hypothesis is pursued, consider exposure keratitis (secondary Gram-positive infection) as a more biologically plausible target than the top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

