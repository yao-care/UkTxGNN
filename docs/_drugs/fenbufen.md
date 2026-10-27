---
layout: default
title: Fenbufen
parent: Model Prediction Only (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fenbufen: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not recorded in the data compiled for this report"
monitor_inn: "Fenbufen"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "pseudoachondroplasia", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "rheumatoid arthritis", "gout", "arthropathy"]
---

# Fenbufen
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

## Fenbufen: From Musculoskeletal Pain and Inflammation to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Fenbufen is a non-steroidal anti-inflammatory drug (NSAID) that is currently marketed in the UK, and the data compiled for this report do not record a specific approved indication for it.
The TxGNN model predicts it may be effective for **osteoarthritis**, with **no registered clinical trials** but **20 publications** (including several randomised, double-blind comparisons) supporting this direction.
Osteoarthritis is already an established use of fenbufen, so this is better described as confirmation of a known use than as true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L1 (as assigned in the compiled data; see the note under Literature Evidence) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fenbufen is not available in the compiled data. However, fenbufen is an NSAID and a prodrug. Its main active metabolite is felbinac (biphenylacetic acid). The pharmacology literature indicates that fenbufen itself has no intrinsic effect on cyclooxygenase (COX), whereas felbinac is a potent inhibitor. Through COX-1 and COX-2 inhibition, it reduces prostaglandin-driven pain and inflammation in affected joints.

Osteoarthritis is a painful, partly inflammatory joint condition, and symptom relief with NSAIDs is a well-established approach. Fenbufen was widely studied in osteoarthritis and rheumatoid arthritis in the 1970s and 1980s, so the model's prediction is consistent with existing clinical knowledge.

Other predictions in the list need to be treated more cautiously. Rheumatoid arthritis has similar trial support, again for symptom relief only. Gout and "arthropathy" have only indirect evidence. The rare skeletal dysplasias (pseudoachondroplasia, brachyolmia, Hunter-Thompson acromesomelic dysplasia and similar), myosclerosis and "osteoarthritis susceptibility" have no plausible mechanistic link or clinical evidence. These high scores most likely reflect proximity to osteoarthritis in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table lists the most relevant publications for osteoarthritis, prioritising randomised trials.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7051052](https://pubmed.ncbi.nlm.nih.gov/7051052/) | 1982 | RCT (short-term, double-blind, placebo-controlled) | Pharmacology | Fenbufen versus placebo in osteoarthritis; no abstract available |
| [7044804](https://pubmed.ncbi.nlm.nih.gov/7044804/) | 1982 | RCT (long-term, double-blind) | Eur J Rheumatol Inflamm | Fenbufen versus indomethacin in 110 osteoarthritis patients, comparing long-term efficacy and safety |
| [377471](https://pubmed.ncbi.nlm.nih.gov/377471/) | 1979 | RCT (crossover) | Scand J Rheumatol Suppl | Fenbufen 600 mg versus aspirin 3.6 g daily in 53 patients with knee or hip osteoarthritis; both produced significant improvement |
| [331427](https://pubmed.ncbi.nlm.nih.gov/331427/) | 1977 | Comparative trial | Rev Med Chil | Fenbufen compared with acetylsalicylic acid in osteoarthritis; no abstract available |
| [367713](https://pubmed.ncbi.nlm.nih.gov/367713/) | 1978 | RCT (crossover) | Curr Med Res Opin | Fenbufen versus indomethacin and placebo in 20 patients; fenbufen was significantly better than placebo on two assessment indices |
| [6242958](https://pubmed.ncbi.nlm.nih.gov/6242958/) | 1981 | Single-blind crossover | Eur J Rheumatol Inflamm | Fenbufen 600 mg versus piroxicam 20 mg at night in osteoarthritis |
| [6356911](https://pubmed.ncbi.nlm.nih.gov/6356911/) | 1983 | Review | Am J Med | Overview of 155 trials (102 in RA, 53 in OA); all 12 pivotal protocols were double-blind and controlled, six of them in OA |
| [7009135](https://pubmed.ncbi.nlm.nih.gov/7009135/) | 1981 | Review | Drugs | Fenbufen 600 mg daily was comparable to aspirin 3.6 g or indomethacin in efficacy, generally with fewer side effects |
| [7111386](https://pubmed.ncbi.nlm.nih.gov/7111386/) | 1982 | Clinical study | Pharmacology | Fenbufen in osteoarthritis of the hip |
| [7601178](https://pubmed.ncbi.nlm.nih.gov/7601178/) | 1994 | Critical review | Eur J Rheumatol Inflamm | Topical felbinac was equivalent to oral ibuprofen or fenbufen in mild to moderate osteoarthritis |

**Note:** The evidence is old (1977 to 1994, apart from one 2022 paper on immunomodulatory and toxic potential) and uses older comparators such as aspirin and indomethacin. The L1 grade reflects the number of randomised trials found, but none of these is a registered Phase 3 trial, so the grade should be read with caution.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010F0AAACAC | Fenbufen Tab 450mg | Not recorded | Not recorded |

This is a single valid product containing fenbufen alone. The compiled data do not include the dosage form, manufacturer or approved indication text, and the number shown is a BNF-style product code rather than a standard PL number. Please check the current MHRA product information and BNF entry to confirm the authorised indications.

---

## Safety Considerations

No warnings, contraindications or drug interaction data were available in the compiled data. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

The literature retrieved for this report also describes some reactions associated with fenbufen:
- Rash and pulmonary eosinophilia (BMJ, 1990)
- Pure red cell aplasia in a patient with rheumatoid arthritis (J Rheumatol, 1987)

These are individual reports and should be weighed against the usual NSAID class risks (gastrointestinal, cardiovascular and renal).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomised, double-blind trials support symptomatic benefit of fenbufen in osteoarthritis, and the drug is already marketed in the UK. However, the trials are decades old, there are no registered clinical trials, and safety and labelling data are missing from the compiled data. This is a confirmation of an existing use, not a new repurposing opportunity.

**To proceed, the following is needed:**
- Confirmation of the authorised indication, dosage form and manufacturer from the current MHRA product information and SmPC
- Complete safety data (warnings, contraindications and interactions) from the SmPC and BNF
- Comparison with current NICE-recommended osteoarthritis treatments, as the evidence uses older comparators
- Mechanism of action data (COX inhibition via the active metabolite felbinac) confirmed from DrugBank
- Clarification of the other predicted indications before further work: gout and "arthropathy" need subtype-specific evidence, and the rare skeletal dysplasias and "osteoarthritis susceptibility" should remain on hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

