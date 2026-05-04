---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Celecoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Celecoxib: From Inflammatory Arthritis to Inflammatory Spondylopathy

> **Research Use Only.** This report is intended for research and evaluation purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All prescribing decisions must be made by qualified healthcare professionals in accordance with current UK guidelines.

---

## One-Sentence Summary

Celecoxib is a selective cyclooxygenase-2 (COX-2) inhibitor used in clinical practice for the symptomatic treatment of osteoarthritis and rheumatoid arthritis.
The TxGNN model predicts it may be effective for **inflammatory spondylopathy** (encompassing ankylosing spondylitis and axial spondyloarthritis), with **19 clinical trials** and **20 publications** currently supporting this direction.
This is the highest-evidence prediction identified in a multi-indication screening (10 candidates evaluated), achieving Evidence Level **L1** — the strongest possible rating.

> **Note on report scope:** This evidence pack evaluated 10 predicted indications simultaneously. The report focuses on **rank 9 — inflammatory spondylopathy** as the primary indication, as it carries the highest evidence level (L1) and the only actionable recommendation ("Proceed with Guardrails") in this dataset. The remaining nine predictions are all rated L4–L5 with a "Hold" recommendation and are not detailed further here.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not mapped in current data — Celecoxib is a COX-2-selective NSAID; verify current approved indications via MHRA/emc |
| Predicted New Indication | Inflammatory Spondylopathy (incl. Ankylosing Spondylitis, Axial Spondyloarthritis) |
| TxGNN Prediction Score | 99.80% (Global rank: 2,564) |
| Evidence Level | L1 |
| UK Market Status | Not mapped in current dataset — see regulatory note below |
| Number of Marketing Authorisations | Not mapped in current dataset — see regulatory note below |
| Recommended Decision | Proceed with Guardrails |

> **Regulatory data note:** The UK marketing authorisation fields in this evidence pack returned no records for Celecoxib (market status listed as not marketed; 0 licences). This is almost certainly a pipeline data collection issue rather than a reflection of actual market status. Clinicians should verify directly via the **electronic Medicines Compendium (emc)** at medicines.org.uk or the **MHRA Products website**. Celecoxib (Celebrex®, 100 mg and 200 mg capsules) is known to hold MHRA marketing authorisation for the symptomatic treatment of osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis in adults; the BNF classifies it under Section 10.1.1 (Non-steroidal anti-inflammatory drugs). The UK regulatory data pipeline for this drug should be reviewed and corrected.

---

## Why Is This Prediction Reasonable?

Celecoxib works by selectively inhibiting the cyclooxygenase-2 (COX-2) enzyme, blocking the synthesis of prostaglandin E2 (PGE2) and related pro-inflammatory mediators. Its selectivity for COX-2 over COX-1 accounts for its more favourable gastrointestinal safety profile compared to non-selective NSAIDs. Detailed mechanism of action data was not returned by the DrugBank query in this evidence pack (data gap DG002); however, Celecoxib's pharmacology is extensively characterised in the clinical literature, including multiple studies within this evidence pack, and its mechanism is well understood in inflammatory musculoskeletal disease.

In inflammatory spondylopathy — encompassing ankylosing spondylitis (AS), non-radiographic axial spondyloarthritis (nr-axSpA), and related subtypes — COX-2 is highly expressed in inflamed spinal ligaments, entheses, and sacroiliac joints. Selective inhibition of COX-2 by Celecoxib directly reduces the local PGE2-driven inflammatory cycle responsible for the pain, morning stiffness, and progressive ankylosis that define these conditions. The mechanistic rationale is therefore direct and robust, explaining why multiple Phase 3 RCTs have already confirmed clinical benefit.

A particularly compelling finding is reported in a 2025 study (PMID 39757202), which proposes that Celecoxib may be the only NSAID capable of inhibiting radiographic bone progression in spondyloarthritis — potentially via modulation of the Wnt/BMP signalling pathway independently of COX inhibition per se. If confirmed, this would give Celecoxib a genuine disease-modifying role in inflammatory spondylopathy beyond symptom control, further strengthening this TxGNN prediction. The breadth and consistency of the clinical evidence base — spanning Phase 3 RCTs, large Phase 4 studies, national cohorts, and systematic reviews — makes this one of the most robustly supported drug–indication predictions possible from a repurposing analysis.

---

## Clinical Trial Evidence

| Trial | Phase | Status | Enrolment | Key Findings |
|-------|-------|--------|-----------|--------------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week comparison of Celecoxib 200 mg once daily, 200 mg twice daily, and diclofenac 75 mg SR twice daily in AS; primary confirmatory trial of Celecoxib's symptomatic efficacy and safety in AS |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Celecoxib 200 mg once daily vs diclofenac 75 mg SR once daily in Chinese patients with AS (6-week RCT + 6-week extension at 400 mg); broadens generalisability of Phase 3 evidence to non-Western populations |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: Celecoxib added to golimumab (TNF inhibitor) vs golimumab monotherapy over 2 years in radiographic axial SpA; assesses whether continuous NSAID use retards structural spinal damage progression |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | Celecoxib 200 mg once daily vs 400 mg once daily vs diclofenac three times daily in AS over 12 weeks; 12-week confirmatory study extending the results of a prior 6-week Phase 3 trial |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Multi-centre open-label RCT: etanercept 50 mg weekly vs Celecoxib 200 mg twice daily vs combination over 54 weeks in active AS; primary endpoint is MRI SPARCC score of sacroiliac joints |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Phase 2 | Unknown | 300 | Registry study: adalimumab with NSAIDs vs adalimumab alone in AS; provides real-world data on Celecoxib use patterns in combination with biologic therapy |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | Double-blind active-controlled RCT: Naxozol (naproxen + esomeprazole) vs Celecoxib in OA/RA/AS; compares gastroprotective effect and pain relief between the two approaches |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Multi-centre prospective RCT: standard-dose vs reduced-dose TNF inhibitor in stable AS; NSAIDs including Celecoxib used as background therapy |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trial series comparing selective COX-2 inhibitors vs non-selective NSAIDs in axial SpA; terminated early but provides proteomic biomarker and individualised response data |
| [NCT01709656](https://clinicaltrials.gov/study/NCT01709656) | N/A | Completed | 120 | Prospective open-label trial: human mesenchymal stem cells vs NSAIDs (NSAID arm includes Celecoxib) in active AS; provides mechanistic and gene expression profiling data on disease pathophysiology |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematic Review | BMB Reports | Celecoxib is the only NSAID shown to inhibit radiographic bone progression in spondyloarthritis; proposed COX-2–independent mechanism involves modulation of bone formation pathways, potentially Wnt/BMP signalling |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Comparative Cohort | Scandinavian Journal of Rheumatology | Nationwide retrospective cohort in AS: cardiovascular disease and GI bleeding risk is comparable between Celecoxib and non-selective NSAIDs, supporting Celecoxib as a viable long-term option |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella Review | Drugs | Systematic synthesis of meta-analyses reporting on Celecoxib safety in chronic musculoskeletal disorders; provides the most comprehensive current safety signal assessment for this drug class |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT | Annals of the Rheumatic Diseases | CONSUL trial report: Celecoxib added to golimumab did not significantly reduce radiographic spinal progression vs golimumab alone at 2 years in r-axSpA, though exploratory findings support disease activity benefits |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Randomised, double-blind, placebo-controlled trial of iguratimod combined with Celecoxib in active axSpA; assesses combination therapy efficacy and safety |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT | Clinical Rheumatology | Celecoxib vs imrecoxib in axSpA: analyses changes in bone metabolism markers and angiogenesis related to sacroiliac joint inflammation, linking treatment response to mechanistic biomarkers |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Randomised trial (n=51 completers) of imrecoxib vs Celecoxib 200 mg twice daily in axSpA; MRI SPARCC scores and serum DKK-1 levels used to correlate imaging and clinical response |
| [25623277](https://pubmed.ncbi.nlm.nih.gov/25623277/) | 2015 | Population Cohort | Arthritis Care & Research | Swedish national cohort: comparative rates of GI, renovascular, and cardiovascular adverse events for etoricoxib, Celecoxib, and non-selective NSAIDs specifically in AS/SpA patients — key long-term safety reference |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Systematic Review | Drugs | Comprehensive systematic review of Celecoxib efficacy and tolerability in OA, RA, and AS; summarises the clinical evidence base that supports current MHRA-approved indications |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | Clinical Study | Journal of Rheumatology | Evaluates efficacy and safety of Celecoxib in patients with AS; an early foundational study demonstrating significant clinical benefit that supported original AS indication approval |

---

## UK Market Information

Current data in this evidence pack contains no marketing authorisation records for Celecoxib in the United Kingdom. This is a known pipeline data collection gap (see metadata DG001) and does not reflect the actual regulatory status of this drug.

Clinicians should consult the following authoritative UK sources directly:

- **Electronic Medicines Compendium (emc)**: [medicines.org.uk](https://www.medicines.org.uk) — search "Celebrex" for full SmPC
- **MHRA Products**: [products.mhra.gov.uk](https://products.mhra.gov.uk) — marketing authorisation records
- **BNF Online**: [bnf.nice.org.uk](https://bnf.nice.org.uk) — Section 10.1.1 for Celecoxib prescribing guidance
- **NICE Guidance**: NG65 — Spondyloarthritis in over 16s: diagnosis and management

> **Action required for the UK TxGNN data pipeline**: The MHRA authorisation matching process for Celecoxib (Celebrex®) should be reviewed and corrected. The drug holds a valid UK marketing authorisation and should appear in future evidence packs with complete licence and approved indication data.

---

## Safety Considerations

Specific UK SmPC safety data — including formalised warnings, contraindications, and drug interaction data — is not available in this evidence pack (pipeline data gap DG001; DDI query returned no results).

Please refer to the **Celebrex® SmPC** (available on emc) and **BNF Section 10.1.1** for full prescribing information, contraindications, and monitoring requirements before any clinical use. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

The literature evidence within this pack highlights several safety considerations specifically relevant to Celecoxib use in inflammatory spondylopathy:

- **Cardiovascular risk**: A 2025 nationwide cohort study (PMID 40028763) and a Swedish national registry (PMID 25623277) both examined cardiovascular and GI outcomes with Celecoxib in AS/SpA patients — these should be reviewed alongside the SmPC cardiovascular warnings
- **Long-term renal and hepatic monitoring**: A 2024 prospective cohort study (PMID 39315555) assessed liver and kidney function in AS patients on long-term continuous NSAIDs; monitoring guidance is available therein
- **Concomitant methotrexate**: A Cochrane review (PMID 22071858) specifically assessed NSAID safety in patients receiving methotrexate for inflammatory arthritis; consult before co-prescribing
- **Comprehensive safety synthesis**: A 2025 umbrella review (PMID 40911151) systematically synthesises safety evidence across meta-analyses of Celecoxib in chronic musculoskeletal conditions and is the most current overall safety reference

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (including NCT00648141, n=458 and NCT00762463, n=240) directly confirm Celecoxib's efficacy in ankylosing spondylitis — a core subtype of inflammatory spondylopathy — and emerging 2025 systematic evidence (PMID 39757202) suggests Celecoxib may uniquely inhibit radiographic bone progression in spondyloarthritis beyond symptom control, potentially representing a meaningful disease-modifying advantage over other NSAIDs.

**To proceed, the following is needed:**

- **Regulatory pipeline fix (priority):** Update the UK MHRA data collection pipeline to correctly capture Celecoxib's existing marketing authorisation; confirm whether an additional label extension to non-radiographic axial SpA (nr-axSpA) would be clinically and commercially warranted
- **SmPC and contraindication data (DG001 — Blocking):** Retrieve full SmPC warnings and contraindications text to complete the S1 safety screening step; this is currently a blocking data gap
- **Drug interaction data:** Re-run a targeted DDI query (the current query returned 0 results, which is implausible for a widely prescribed NSAID); prioritise interactions with TNF inhibitors, methotrexate, aspirin, and anticoagulants relevant to the spondyloarthritis patient population
- **MOA data confirmation (DG002):** Obtain complete DrugBank mechanism of action data to formally characterise the proposed Wnt/BMP pathway interaction and support any future label extension submission or NICE appraisal
- **NICE NG65 alignment:** Map Celecoxib's evidence base against the current NICE axial spondyloarthritis guideline (NG65) to confirm its positioning in the UK treatment pathway and identify whether a technology appraisal update is appropriate
- **Paediatric population:** Consider a separate evaluation for RF-positive polyarticular juvenile idiopathic arthritis (JIA; prediction rank 8 in this pack, Evidence Level L4), given historical FDA paediatric JIA supplemental data referenced in the evidence; this may represent a viable extension route through the MHRA's paediatric investigation plan process
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

