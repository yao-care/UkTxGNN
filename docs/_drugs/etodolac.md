---
layout: default
title: Etodolac
parent: Model Prediction Only (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etodolac: predicted new indication Ankylosing spondylitis (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
monitor_inn: "Etodolac"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "spondyloarthropathy, susceptibility to", "brachyolmia", "ankylosing spondylitis", "pseudoachondroplasia", "hypermobility of coccyx", "inflammatory spondylopathy"]
---

# Etodolac
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

# Etodolac: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Etodolac is a COX-2-preferential non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis and related joint conditions.
The TxGNN model's highest-ranked prediction is a rare skeletal dysplasia with no supporting evidence; the most clinically meaningful candidate is **ankylosing spondylitis**, which has **no registered clinical trials** and **8 publications** (indirect evidence, mainly reviews and surveillance reports).

## Quick Overview

The first-ranked prediction (acromesomelic dysplasia, Hunter-Thompson type) has no supporting evidence and no plausible mechanism, so this report focuses on ankylosing spondylitis (ranked 6th), the best-supported candidate.

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy (UK licence text not available) |
| Predicted New Indication | Ankylosing spondylitis (rank 6); rank 1 prediction was acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.93% (ankylosing spondylitis); 99.97% (rank 1) |
| Evidence Level | L4 (ankylosing spondylitis); L5 for rank 1 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold (rank 1 prediction); Research Question for ankylosing spondylitis |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on the published literature, etodolac is an NSAID whose main anti-inflammatory action is a selective effect on cyclo-oxygenase-2 (COX-2), reducing prostaglandin-mediated inflammation and pain.

For ankylosing spondylitis, NSAIDs are guideline-recommended first-line symptomatic therapy, and prostaglandin suppression plausibly explains relief of inflammatory back pain and stiffness. Etodolac is already used in related rheumatic conditions (rheumatoid arthritis, osteoarthritis, spondyloarthropathy), so this is largely an extension within the drug's existing class and use rather than a novel repurposing. Note that NSAIDs relieve symptoms; they are not shown to modify the disease.

The other top-ranked predictions should be treated with caution:
- **Rare skeletal and connective tissue disorders** (acromesomelic dysplasia Hunter-Thompson type, brachyolmia, brachyolmia-amelogenesis imperfecta syndrome, pseudoachondroplasia, myosclerosis): these are genetic conditions with no known link to COX inhibition. The high scores probably reflect proximity in the knowledge graph to arthropathy terms rather than biology. At most, etodolac might ease secondary pain.
- **Spondyloarthropathy, susceptibility to**: overlaps with an existing indication and is effectively a relabelling, not repurposing.
- **Rheumatoid vasculitis**: requires immunosuppression; NSAIDs do not treat vasculitis, and renal and cardiovascular risks may be unfavourable.
- **Hypermobility of coccyx**: NSAIDs are sometimes used for coccydynia, which gives a plausible symptomatic rationale, but there is no direct evidence.
- **Inflammatory spondylopathy**: overlaps with ankylosing spondylitis and relies on the same literature, so it is not independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these is an etodolac-specific controlled trial in ankylosing spondylitis, so the evidence is indirect. The same set supports inflammatory spondylopathy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | Review | Drugs | Etodolac is effective in rheumatoid arthritis, osteoarthritis and ankylosing spondylitis, and appears at least as effective as other NSAIDs |
| [2146130](https://pubmed.ncbi.nlm.nih.gov/2146130/) | 1990 | Review | Eur J Rheumatol Inflamm | Overview of randomised, double-blind studies comparing etodolac with standard NSAIDs or placebo in rheumatoid arthritis, osteoarthritis and ankylosing spondylitis |
| [17694363](https://pubmed.ncbi.nlm.nih.gov/17694363/) | 1997 | Review | Inflammopharmacology | Clinical review of etodolac as an analgesic; acts via selective COX-2 effect; used in inflammatory arthritides including ankylosing spondylitis |
| [22071858](https://pubmed.ncbi.nlm.nih.gov/22071858/) | 2011 | Review (Cochrane) | Cochrane Database Syst Rev | Safety of NSAIDs alongside methotrexate in inflammatory arthritis, including ankylosing spondylitis |
| [2525800](https://pubmed.ncbi.nlm.nih.gov/2525800/) | 1989 | Observational (open-label) | Rev Med Interne | Open trial of 4,947 patients (rheumatoid arthritis, ankylosing spondylitis, osteoarthritis) assessing efficacy and tolerability |
| [2150569](https://pubmed.ncbi.nlm.nih.gov/2150569/) | 1990 | Open-label safety trial | Rheumatol Int | Two large French open-label studies confirming efficacy and safety of etodolac |
| [2150568](https://pubmed.ncbi.nlm.nih.gov/2150568/) | 1990 | Postmarketing surveillance | Rheumatol Int | Surveillance in 8,334 patients (Italy, Switzerland, UK, France) showing a favourable safety profile |
| [20829199](https://pubmed.ncbi.nlm.nih.gov/20829199/) | 2011 | Guideline/Recommendation | Ann Rheum Dis | ASAS recommendations for collecting and reporting NSAID intake in axial spondyloarthritis studies (methodological, not efficacy data) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010E0AAADAD | Etodolac tablets 600 mg modified-release | Modified-release tablet | Not available in the data compiled |

Only one valid single-ingredient authorisation was identified. Please check the current MHRA record, the SmPC and the BNF for licensed indications and dosing.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease associations, not label text): hypertension, kidney disease, liver disease, gallbladder disease, active peptic ulcer disease, blood coagulation disease, myocardial infarction, coronary thrombosis, other cardiovascular and heart disease, and haemoglobinopathy. These are consistent with the known class risks of NSAIDs (gastrointestinal, cardiovascular and renal) and must be checked against the SmPC.
- **Drug Interactions** (100 interactions identified; selected examples):
  - Moderate: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, glimepiride, repaglinide, chlorpropamide, mesalazine, balsalazide, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
  - Minor: famotidine, ranitidine, cimetidine, linaclotide

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked rare skeletal and connective tissue predictions). Ankylosing spondylitis is a **Research Question**.

**Rationale:**
The highest-scoring predictions are rare genetic disorders with no trials, no literature and no biological rationale, so the scores likely reflect knowledge-graph artefacts. Ankylosing spondylitis is clinically plausible, but it falls within established NSAID use and rests only on indirect evidence, with no etodolac-specific controlled trial.

**To proceed, the following is needed:**
- Licensed indication text and dosage form for the UK authorisation (SmPC/MHRA)
- Mechanism of action data confirmed from DrugBank
- Warnings and contraindications from the SmPC and BNF
- For ankylosing spondylitis: a comparison with NICE-recommended NSAID options and, if warranted, a controlled study
- A gastrointestinal, cardiovascular and renal risk assessment for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

