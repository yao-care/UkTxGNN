---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Flurbiprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "Flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
---

# Flurbiprofen
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

# Flurbiprofen: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatic conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
There are currently **no clinical trials** and **no publications** supporting this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from knowledge-graph indication data; no indication text is recorded for the UK authorisation) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Flurbiprofen is an NSAID of the phenylalkanoic acid class. As a class, NSAIDs inhibit cyclo-oxygenase (COX) enzymes and reduce prostaglandin-mediated inflammation and pain. This is the basis of its use in inflammatory and degenerative joint disease.

The predicted condition is different in nature. Acromesomelic dysplasia, Hunter-Thompson type, is a congenital skeletal dysplasia affecting limb development. It has no recognised inflammatory driver that COX inhibition would be expected to modify. The high score most likely reflects proximity in the knowledge graph, such as shared skeletal or joint-related genes or phenotypes, rather than a pharmacological link.

At most, a purely symptomatic role (for example, joint pain relief) can be imagined. No data support even this, and there is no plausible disease-modifying mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010I0AAACAC (as recorded; not in standard MHRA PL format, so verify against the MHRA register) | Flurbiprofen Tab 100 mg | Tablet (inferred from product name) | Not stated in the data compiled |

The data show one valid single-ingredient authorisation. Indication text, manufacturer and dosage-form fields are not populated, and no NICE-appraised indication information was available. Check the BNF and the current SmPC for the licensed indications.

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
The prediction has no supporting trials or publications, and no plausible mechanistic link. The condition is a congenital skeletal dysplasia with no inflammatory target for flurbiprofen, so the high score likely reflects knowledge-graph proximity.

**To proceed, the following is needed:**
- Mechanism of action data, and any biological rationale linking COX inhibition to this condition
- Preclinical or clinical evidence in this disorder (none currently exists)
- Full safety data from the SmPC and BNF, given the cardiovascular, gastrointestinal, renal and hepatic cautions above
- Complete UK authorisation details (indication text, dosage form, valid licence number)

**Note on other predictions:** Among the other predicted indications for flurbiprofen, only **ankylosing spondylitis** (rank 8) has supporting literature. This includes several randomised, double-blind comparisons with indomethacin, phenylbutazone and naproxen from the 1970s and 1980s (for example [PMID 4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) and [PMID 3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/)). It sits at evidence level L3 and is better viewed as an extension within the NSAID class than as novel repurposing. It would be the more productive direction to evaluate, and its evidence should not be transferred to the indication reported here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

