---
layout: default
title: Dactinomycin
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 9
---

# Dactinomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dactinomycin: From Standard Rhabdomyosarcoma Therapy to Site-Specific Sarcoma Extensions

## One-Sentence Summary

Dactinomycin (Actinomycin D, DrugBank DB00970) is a cytotoxic DNA-intercalating antibiotic that already forms part of the VAC regimen (vincristine, dactinomycin, cyclophosphamide) used in paediatric rhabdomyosarcoma. TxGNN's single highest-scoring prediction — **relapsing-remitting multiple sclerosis** (score 99.58%) — has no supporting trials, literature, or plausible mechanism, and is assessed in this evidence pack as a likely model false positive (**Hold**). The clinically meaningful signal instead lies among the next eight ranked candidates, which largely confirm dactinomycin's established role across further anatomical and histological subtypes of rhabdomyosarcoma-family sarcomas — most strongly for **parameningeal embryonal rhabdomyosarcoma**, supported by a completed Phase 3 Children's Oncology Group RCT (L1 evidence).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paediatric rhabdomyosarcoma / Wilms tumour, as part of the VAC chemotherapy regimen (established use referenced throughout the evidence base; not captured as a discrete field in this pack) |
| Top TxGNN-Ranked Prediction | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level (top-ranked prediction) | L5 (model prediction only, no trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision (top-ranked prediction) | **Hold** |

The highest raw TxGNN score does not correspond to the best-evidenced candidate. The table below summarises all nine ranked predictions; the strongest genuine signal is **parameningeal embryonal rhabdomyosarcoma** (L1, Proceed with Guardrails).

**All Predicted Indications at a Glance**

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Relapsing-remitting multiple sclerosis | 99.58% | L5 | S0 | Hold |
| 2 | Botryoid-type embryonal rhabdomyosarcoma (vagina) | 99.54% | L4 | S1 | Research Question |
| 3 | Extrahepatic bile duct rhabdomyosarcoma | 99.49% | L4 | S1 | Research Question |
| 4 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.48% | L4 | S1 | Research Question |
| 5 | Parameningeal embryonal rhabdomyosarcoma | 99.48% | L1 | S3 | Proceed with Guardrails |
| 6 | Prostate embryonal rhabdomyosarcoma | 99.46% | L3 | S2 | Research Question |
| 7 | Liver sarcoma | 99.42% | L3 | S2 | Research Question |
| 8 | Upper aerodigestive tract neoplasm | 99.16% | L3 | S1 | Research Question |
| 9 | Head and neck cancer | 99.16% | L3 | S2 | Research Question |

## Why is This Prediction Reasonable?

Dactinomycin is a DNA-intercalating transcription inhibitor with broad, non-selective cytotoxicity. This mechanism underlies its well-established role in the VAC regimen for rhabdomyosarcoma and related paediatric sarcomas — a use reflected repeatedly across the rationale for candidates 2–9. Because rhabdomyosarcoma is classified in disease ontologies by anatomical site (vagina, bile duct, prostate, parameningeal region, head and neck, etc.), TxGNN's mid-ranked predictions largely represent the model correctly recovering an **already-established indication at finer anatomical granularity**, rather than genuinely novel repurposing. This is reassuring for model validity but means most of these "predictions" carry limited new clinical value — they confirm existing standard-of-care use rather than open a new therapeutic avenue.

The **top-ranked prediction, relapsing-remitting multiple sclerosis, sits outside this pattern entirely**. RRMS is a chronic, inflammatory, demyelinating autoimmune disease requiring long-term, comparatively low-toxicity immunomodulation. Dactinomycin's toxicity profile (myelosuppression, hepatotoxicity, veno-occlusive disease) and mechanism (non-selective DNA intercalation) offer no plausible therapeutic rationale for this indication, and no trials or publications support it. This is best interpreted as a knowledge-graph artefact rather than a genuine repurposing signal.

The only candidate combining a distinct anatomical subtype **and** prospective controlled trial evidence is parameningeal embryonal rhabdomyosarcoma (rank 5), where a completed Phase 3 COG trial directly evaluated dactinomycin-containing VAC therapy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Relevant Indication | Key Findings |
|---------|------|------|------|------|---------|
| [NCT00002611](https://clinicaltrials.gov/study/NCT00002611) | Phase 3 | Completed | 3,031 | Liver sarcoma | National Wilms Tumor Study-5; compared chemotherapy ± radiotherapy in childhood kidney cancer. Graded low relevance (C) — targets Wilms tumour, not liver sarcoma directly |
| [NCT03382158](https://clinicaltrials.gov/study/NCT03382158) | N/A | Recruiting | 3,400 | Head and neck cancer | International PPB/DICER1 registry — an observational registry, not a treatment trial; graded low relevance (C) |

No trial in this pack directly and specifically evaluates dactinomycin in relapsing-remitting multiple sclerosis, parameningeal rhabdomyosarcoma, or the other anatomical subtypes; the strongest supporting evidence for those indications comes from the literature below.

## Literature Evidence

| PMID | Year | Type | Journal | Relevant Indication | Key Findings |
|------|-----|------|------|------|---------|
| [19770373](https://pubmed.ncbi.nlm.nih.gov/19770373/) | 2009 | RCT (Phase 3, COG D9803) | J Clin Oncol | Parameningeal embryonal rhabdomyosarcoma | Compared standard VAC to VAC alternating with vincristine/topotecan/cyclophosphamide in intermediate-risk RMS; VAC (with dactinomycin) remains standard |
| [10856103](https://pubmed.ncbi.nlm.nih.gov/10856103/) | 2000 | Cohort/Trial (IRS-IV) | J Clin Oncol | Parameningeal & prostate embryonal rhabdomyosarcoma | Intensified therapy including dactinomycin improved failure-free survival in local/regional embryonal RMS |
| [12586800](https://pubmed.ncbi.nlm.nih.gov/12586800/) | 2003 | Cohort/Trial (IRS III/IV) | J Clin Oncol | Head and neck rhabdomyosarcoma | Outcomes of localised non-orbital, non-parameningeal head and neck RMS treated with dactinomycin-containing regimens |
| [11408506](https://pubmed.ncbi.nlm.nih.gov/11408506/) | 2001 | Cohort/Trial (IRS-IV) | J Clin Oncol | Upper aerodigestive tract / head and neck | Risk-based surgery, radiotherapy and chemotherapy regimens (incl. dactinomycin) in non-metastatic RMS |
| [21671362](https://pubmed.ncbi.nlm.nih.gov/21671362/) | 2011 | Retrospective Cohort | Pediatr Blood Cancer | Liver sarcoma (safety) | Dactinomycin/vincristine toxicity review from the Children's Oncology Group; evidence-based dosing guidance is lacking |
| [15143082](https://pubmed.ncbi.nlm.nih.gov/15143082/) | 2004 | Retrospective | J Clin Oncol | Liver sarcoma (safety) | Age identified as a risk factor for VAC-induced hepatopathy |
| [5563889](https://pubmed.ncbi.nlm.nih.gov/5563889/) | 1971 | Case Report | J Pediatr Surg | Extrahepatic bile duct rhabdomyosarcoma | Sarcoma botryoides of the bile ducts with survival — the only direct literature for this indication |
| [34900598](https://pubmed.ncbi.nlm.nih.gov/34900598/) | 2022 | Case Report/Review | Urology Case Reports | Prostate embryonal rhabdomyosarcoma | Adult prostatic embryonal RMS treated with dactinomycin/vincristine/cyclophosphamide; poor outcome despite multimodal therapy |
| [35267106](https://pubmed.ncbi.nlm.nih.gov/35267106/) | 2022 | Mechanistic/Basic Research | Apoptosis | Upper aerodigestive tract neoplasm | p53-dependent apoptosis induction by actinomycin D in aerodigestive tract cancer cell lines; supports mechanistic plausibility but is preclinical |

Currently no related clinical trials or literature are registered for relapsing-remitting multiple sclerosis, embryonal extrahepatic bile duct rhabdomyosarcoma, or botryoid-type embryonal rhabdomyosarcoma of the vagina.

## UK Market Information

Dactinomycin holds **no current UK marketing authorisation** in this evidence pack (0 licenses; market status: Not marketed). Where used in UK oncology practice, dactinomycin is typically supplied via specials/named-patient routes for paediatric sarcoma protocols and would fall under BNF Chapter 8.1.3 (Cytotoxic antibiotics). No product-specific licence numbers, brand names, or dosage forms are available to report.

## Cytotoxicity

Dactinomycin is a conventional cytotoxic antineoplastic agent (DNA-intercalating antitumour antibiotic), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — DNA-intercalating antitumour antibiotic |
| Myelosuppression Risk | High — retrospective Children's Oncology Group data (PMID 21671362) describe significant dactinomycin/vincristine toxicity, and evidence-based dosing guidance is described as lacking |
| Hepatotoxicity Signal | Notable — multiple reports of veno-occlusive disease of the liver following dactinomycin-containing VAC regimens (PMID 9191535, 7700188, 15143082), with age identified as a risk factor |
| Emetogenicity Classification | Moderate to high — antiemetic prophylaxis should follow local chemotherapy protocols |
| Monitoring Items | FBC with differential, liver function tests (including monitoring for veno-occlusive disease), renal function, extravasation site if given intravenously |
| Handling Protection | Requires handling under UK cytotoxic drug handling and COSHH regulations (closed-system transfer devices, trained personnel, appropriate PPE) |

## Safety Considerations

Formal warnings, contraindications, and drug interaction data for dactinomycin are not available in this evidence pack (DDI search returned no results). Based on the literature identified above, veno-occlusive liver disease and myelosuppression are recurring safety signals with dactinomycin-containing regimens and warrant clinical attention pending formal SmPC review.

Please refer to the SmPC and BNF for complete safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold** (on the TxGNN top-ranked signal); the broader rhabdomyosarcoma-subtype cluster is more appropriately framed as **Research Question / confirmatory evidence** rather than novel repurposing.

**Rationale:**
- The highest-scoring prediction (relapsing-remitting multiple sclerosis) has no mechanistic, trial, or literature support and conflicts with dactinomycin's cytotoxic safety profile; it should not be pursued.
- Most other ranked candidates reflect TxGNN correctly recognising dactinomycin's existing standard use in rhabdomyosarcoma-family sarcomas at finer anatomical granularity, not a new therapeutic opportunity. Only parameningeal embryonal rhabdomyosarcoma reaches L1 evidence via a completed Phase 3 RCT, and this reflects confirmation of established therapy rather than repurposing.
- Two data gaps block a full safety evaluation: MHRA/SmPC warnings and contraindications (Blocking), and a formal, sourced mechanism-of-action record (High).

**To proceed, the following is needed:**
- Formal SmPC/product labelling data (warnings, contraindications) to close the Blocking data gap (DG001)
- A DrugBank-sourced, structured mechanism-of-action record to close the High-severity gap (DG002)
- If any further work on relapsing-remitting multiple sclerosis is considered, an independent mechanistic rationale, since none currently exists in this evidence pack
- Anatomical-subtype-specific prospective data (beyond case reports) for bile duct, vaginal, and prostatic rhabdomyosarcoma before treating these as anything beyond off-label extensions of existing VAC practice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

