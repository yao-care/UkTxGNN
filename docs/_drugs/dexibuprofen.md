---
layout: default
title: Dexibuprofen
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Dexibuprofen
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

# Dexibuprofen: From Rheumatoid Arthritis and Osteoarthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Dexibuprofen (the S-enantiomer of ibuprofen) is an NSAID originally used for arthritic and inflammatory conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model's top-ranked prediction is **brachydactyly-syndactyly syndrome**, but there are **no clinical trials and no publications** supporting it.
The only prediction with any supporting literature in the data compiled for this report is **ankylosing spondylitis**, and that literature is general rather than disease-specific.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy and related conditions (the UK authorisation record contains no indication text) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome (top-ranked) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known pharmacology, dexibuprofen is a cyclooxygenase (COX) inhibitor. It reduces prostaglandin-mediated inflammation and pain, and its efficacy in inflammatory and degenerative joint disease is established.

For the top-ranked prediction, there is **no credible mechanistic link**. Brachydactyly-syndactyly syndromes are congenital limb malformations of developmental genetic origin, which an NSAID would not be expected to modify. The high score is a computational output only, with no trials or literature behind it.

The same applies to most of the other top-ten predictions, which are rare genetic or developmental conditions:

| Predicted Condition | Score | Assessment |
|------|------|------|
| Brachydactyly-syndactyly syndrome | 99.87% | No credible mechanism |
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.85% | No plausible mechanism |
| Acromesomelic dysplasia, Hunter-Thompson type | 99.84% | Caused by GDF5 loss of function; no COX link |
| Brachyolmia-amelogenesis imperfecta syndrome | 99.83% | No credible mechanism |
| Myosclerosis | 99.82% | At most hypothetical symptomatic relief |
| Brachyolmia | 99.80% | No COX link to genetic cause |
| Pseudoachondroplasia | 99.74% | Possible symptomatic relief of secondary joint pain only; no disease-modifying rationale |
| Spondyloarthropathy, susceptibility to | 99.73% | Overlaps an existing original indication; not a new opportunity |
| Ankylosing spondylitis | 99.70% | Biologically plausible (see below) |
| WHIM syndrome | 99.68% | CXCR4 gain-of-function; no COX link |

**Ankylosing spondylitis** is the one biologically plausible candidate. NSAIDs are first-line symptomatic therapy, and dexibuprofen is already used in related arthritic conditions, so this would be largely an extension within the labelled class. No dexibuprofen-specific trials in ankylosing spondylitis were identified.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other nine predictions.

## Literature Evidence

No literature is available for the top-ranked prediction. The only supporting publications relate to ankylosing spondylitis (rank 9) and are general reviews rather than disease-specific studies:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11771569](https://pubmed.ncbi.nlm.nih.gov/11771569/) | 2001 | Review | Clinical Rheumatology | Overview of dexibuprofen clinical data: eight GCP trials (1,463 patients), including double-blind comparisons with placebo, racemic ibuprofen and diclofenac, plus a tolerability meta-analysis |
| [9013382](https://pubmed.ncbi.nlm.nih.gov/9013382/) | 1996 | Review | Journal of Clinical Pharmacology | Reevaluation of double-blind randomised studies of dexibuprofen in inflammatory and degenerative diseases, including rheumatoid arthritis, gonarthrosis and ankylosing spondylitis |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review | Critical Reviews in Therapeutic Drug Carrier Systems | Microencapsulation as a drug-delivery approach for NSAIDs in arthritis, including ankylosing spondylitis |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010AMAAAAAA | Dexibuprofen Tab 300mg | Not recorded | Not recorded |

The data compiled for this report show one valid single-ingredient authorisation. Its dosage form and indication details are incomplete, and the number does not follow the usual MHRA PL format, so it should be verified against the MHRA register and the BNF.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, brachydactyly-syndactyly syndrome, has no trials, no literature and no credible mechanism, so it is effectively a model artefact. Of the ten predictions reviewed, only ankylosing spondylitis is biologically plausible (L4, flagged as a research question), and even there the evidence is general review literature.

**To proceed, the following is needed:**
- Verified SmPC and BNF safety data (warnings, contraindications and interactions), which are currently missing and block safety screening
- Mechanism of action data, for example from DrugBank
- Complete UK authorisation details (dosage form, approved indications, manufacturer)
- For ankylosing spondylitis: a focused literature search and, if warranted, comparison with established NSAIDs, since it is an extension of existing NSAID use rather than a distinct repurposing opportunity
- No further investment in the rare genetic and developmental predictions unless new mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

