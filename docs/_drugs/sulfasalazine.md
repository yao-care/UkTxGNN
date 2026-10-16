---
layout: default
title: Sulfasalazine
parent: Model Prediction Only (L5)
nav_order: 583
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sulfasalazine: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Sulfasalazine"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "osteoarthritis susceptibility", "congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "WHIM syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "spondyloarthropathy, susceptibility to", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
---

# Sulfasalazine
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

# Sulfasalazine: From Rheumatoid Arthritis and Inflammatory Bowel Disease to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Sulfasalazine is an anti-inflammatory drug originally used for rheumatoid arthritis, ulcerative colitis and other inflammatory bowel and joint conditions.
The TxGNN model's top-ranked prediction is **brachydactyly-syndactyly syndrome**, a congenital limb malformation, but **no clinical trials and no publications** support it.
A lower-ranked prediction, **osteoarthritis**, has preclinical support only (see the note under Literature Evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis; ulcerative colitis; inflammatory bowel disease; juvenile idiopathic arthritis; spondyloarthropathy |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Sulfasalazine is an anti-inflammatory disease-modifying drug, and its efficacy in inflammatory arthritis and inflammatory bowel disease is established. Its activity is generally linked to inhibition of NF-kB and of inflammatory mediators.

For brachydactyly-syndactyly syndrome, **no plausible mechanistic link has been identified**. This is a congenital limb malformation, and an anti-inflammatory agent is unlikely to alter a developmental disorder. The high TxGNN score reflects a knowledge-graph pattern only. It should be read as a hypothesis-generating signal, not as evidence of benefit.

The other top-10 predictions are similar. Most are rare hereditary or developmental conditions with no supporting studies. Two are exceptions:

- **Osteoarthritis** (rank 5, score 99.64%) has plausible preclinical biology. Sulfasalazine blocked proteoglycan and collagen release from cytokine-stimulated cartilage, reduced cartilage destruction in animal models, and affected prostaglandin and leukotriene release. All of this evidence is in vitro or in animals.
- **Spondyloarthropathy, susceptibility to** (rank 8) is already a listed original indication, so it is not a true repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for brachydactyly-syndactyly syndrome. None were found for osteoarthritis either.

---

## Literature Evidence

Currently no related literature available for brachydactyly-syndactyly syndrome.

**Note on the best-supported alternative (osteoarthritis):** the most relevant publications are preclinical.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Animal study | Int J Biol Macromol | Sulfasalazine-containing hyaluronic acid reduced inflammation and cartilage degradation in a rat osteoarthritis model |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Animal study | J Orthop Res | Sulfasalazine attenuated cartilage destruction after ACL transection and meniscectomy, via cystine/glutamate antiporter inhibition |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | In vitro | Rheumatology (Oxford) | Blocked proteoglycan and collagen release from cytokine-stimulated cartilage and down-regulated metalloproteinases |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | In vitro | Mod Rheumatol | Altered the protein profile of articular chondrocytes |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | In vitro | Wien Klin Wochenschr | Sulfasalazine and its metabolites affected prostaglandin and leukotriene release from human synovial tissue |

No human osteoarthritis trials were identified. Several other retrieved papers concern inflammatory arthritis generally or are unrelated.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0105010E0AAAAAA (BNF-style code as listed; PL number not available) | Sulfasalazine Tab 500mg | Tablet | Not stated in the data compiled |

One valid single-ingredient authorisation is recorded. Please check the current SmPC, the BNF and any relevant NICE guidance for authorised indications.

---

## Safety Considerations

- **Contraindications and cautions** (from knowledge-graph drug-disease associations, not label text):
  - Blood disorders: neutropenia, agranulocytosis, aplastic anaemia
  - Metabolic and enzyme conditions: G6PD deficiency, slow acetylator status, porphyria (including inherited porphyria and other porphyrin metabolism disorders), galactosemia, glycogen storage disease, cystinuria
  - Organ conditions: kidney disease, liver disease, gallbladder disease, urinary tract obstruction, pyoureter
  - Respiratory conditions: asthma (including intrinsic and allergic asthma)
- **Drug Interactions** (100 interactions recorded; the 20 reviewed are summarised here):
  - **Major:** methenamine, human immunoglobulin G (intravenous), prilocaine (topical)
  - **Moderate:** NSAIDs (ketorolac, ibuprofen, celecoxib), azathioprine, aciclovir, oestrogens (ethinylestradiol, estradiol), alpelisib, apalutamide, amphotericin B, amikacin, bacitracin, asparaginase and aminolevulinic acid (topical)
  - **Minor:** folic acid

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests only on a knowledge-graph score. It has no trials, no publications and no plausible mechanism, so it is not suitable for further development. Osteoarthritis is the only prediction with some biological support, but that support is limited to preclinical work and is indirect.

**To proceed, the following is needed:**
- Mechanism of action data for sulfasalazine
- For osteoarthritis, a formal review of the preclinical evidence, followed by an early-phase human study if the case holds up
- Label-based warnings and contraindications from the SmPC, to replace the knowledge-graph associations
- Confirmation of the UK marketing authorisation details (PL number, formulations and approved indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

