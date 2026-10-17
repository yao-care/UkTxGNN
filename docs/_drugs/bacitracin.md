---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bacitracin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Keratitis, keratoconjunctivitis, blepharoconjunctivitis"
monitor_inn: "bacitracin"
predicted_indications: ["otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracin: From Keratitis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a topical antibacterial peptide, originally used for ocular surface infections such as keratitis, keratoconjunctivitis and blepharoconjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Keratitis, keratoconjunctivitis, blepharoconjunctivitis (the licence records compiled for this report contain no indication text, so these come from the knowledge-graph indication data) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, bacitracin is a topical polypeptide antibacterial, mainly active against Gram-positive organisms, and its use in bacterial infections of the ocular surface is established. Mechanistically it may be applicable to punctate epithelial keratoconjunctivitis only where a bacterial component is present.

The predicted condition is anatomically adjacent to the original indications, which probably explains the very high score. However, punctate epithelial keratoconjunctivitis is frequently viral (for example adenoviral) or non-infectious (for example toxic), and an antibacterial would be expected to give limited benefit in those cases. The score most likely reflects proximity to existing indications in the knowledge graph rather than a distinct mechanism, and this cannot be validated without mechanism data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For context, the literature retrieved relates to a lower-ranked prediction, otitis externa (evidence level L4, "Research Question"). It is indirect and does not support the lead indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Double-blind randomised study (151 patients) | Eur Arch Otorhinolaryngol | Polymyxin B + bacitracin ointment alone versus with hydrocortisone acetate in acute bacterial otitis externa; examines the added contribution of the steroid |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | In vitro study (veterinary) | Zentralbl Veterinarmed B | Antibiotic susceptibility of 46 bacterial isolates from chronic canine otitis externa; increasing resistance noted |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | Review / practice article | Md State Med J | Historical practical treatment of otitis externa |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | Historical clinical report | Z Laryngol Rhinol Otol | Local treatment of inflammatory ear conditions with a combination product (Nebacetin) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1310011W0BCAAAB | Polyfax Ointment | Not stated | Not stated |
| 1310011W0AAABAB | Polymyxin / Bacitracin Ointment | Not stated | Not stated |

Both authorisations are valid single-ingredient records. Dosage form and indication text were not available in the data compiled for this report, so please confirm the details against the MHRA product information and the BNF.

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from drug-disease relationships in the knowledge graph, not from label text, and should be verified against the SmPC). Those most relevant to topical ocular use include:
  - Eye infections: herpes simplex virus keratitis, viral eye infection, fungal eye infection, and conjunctivitis
  - Neuromuscular disease: myasthenia gravis and neuromuscular junction disease
  - Organ impairment: kidney disease and liver disease
  - Other recorded signals: open-angle glaucoma, ocular hypertension, epilepsy, diabetes, adrenocortical insufficiency, and heart block
- **Drug Interactions**: 84 interactions were recorded. The major-level ones include:
  - Aminoglycosides: kanamycin, neomycin and streptomycin
  - Deferasirox
  - Iodinated contrast agents: diatrizoate, iodipamide, iodixanol and iohexol

  Moderate-level interactions include mesalazine, balsalazide, olsalazine, sulfasalazine, exenatide, vancomycin and picosulfuric acid. These are mainly relevant to systemic exposure, and topical ocular exposure is likely to be much lower.
- **Other concerns**: bacitracin is nephrotoxic with systemic exposure, so use outside topical routes (for example urinary tract) is not supported.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no trials or literature, and the condition is often viral or non-infectious, where an antibacterial is unlikely to help. Most of the other top-ranked predictions are non-specific categories or immune-mediated conditions with no plausible mechanism, and are not actionable. Otitis externa is the only prediction with any supporting literature, but that evidence is indirect and mixes combination products.

**To proceed, the following is needed:**
- Mechanism of action data for bacitracin
- Licence indication text and dosage forms confirmed from MHRA product information
- Evidence that a bacterial component contributes to punctate epithelial keratoconjunctivitis, followed by clinical studies in that subgroup
- Verification of the knowledge-graph contraindication signals against the SmPC
- If otitis externa is pursued instead, direct bacitracin-specific clinical evidence and a review of safety with a perforated tympanic membrane
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

