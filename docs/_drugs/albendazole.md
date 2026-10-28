---
layout: default
title: Albendazole
parent: High Evidence (L1-L2)
nav_order: 29
evidence_level: L2
indication_count: 3
monitor_inn: "Albendazole"
predicted_indications: ["alveolar echinococcosis", "coenurosis", "Cestode infectious disease"]
last_modified_at: 2026-10-28
description: "Albendazole: predicted new indication alveolar echinococcosis (evidence level L2). Approved use: Not recorded in the local data"
---

# Albendazole
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

## Albendazole: benzimidazole anthelmintic (β-tubulin inhibitor) → alveolar echinococcosis
{: .text-alpha }

## One-Sentence Summary

Albendazole is a benzimidazole anthelmintic that acts on parasite tubulin.
The TxGNN model predicts it may be effective for **alveolar echinococcosis**, with **3 clinical trials** and **20 publications** compiled for this direction. Only one of those trials (a Phase 2 study) directly tests albendazole in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | alveolar echinococcosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L2 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Albendazole is a benzimidazole that binds parasite β-tubulin, inhibiting microtubule polymerisation and impairing glucose uptake in the parasite. Detailed mechanism of action data was not available in the data compiled for this report, so this description reflects the general pharmacology of the drug class.

Alveolar echinococcosis is caused by the larval stage of *Echinococcus multilocularis*, which is closely related to *E. granulosus*, the cause of cystic echinococcosis. Because the two parasites are closely related, the same tubulin-targeting mechanism is expected to apply. Albendazole is already the guideline-recommended benzimidazole for alveolar echinococcosis. It is used mainly as long-term parasitostatic therapy, and as an adjunct to surgery. This prediction is therefore close to existing clinical practice rather than a wholly new repurposing opportunity. Reviews note that albendazole does not appear to kill the parasite in vivo (it is parasitostatic, not parasiticidal) and can cause severe adverse effects, so better options are being sought.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Albendazole treatment of early-stage alveolar echinococcosis found by ultrasound screening in Kyrgyzstan; directly tests the drug in this disease. No results summarised in the data. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | Not applicable | Completed | 50 | Parasite viability and new follow-up markers in hepatic alveolar echinococcosis treated with albendazole, to guide timing of treatment withdrawal. Not a controlled efficacy trial. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | Not applicable | Unknown | 24 | Randomised trial of adjuvant albendazole versus placebo after pulmonary hydatid cyst resection. Concerns cystic disease, so only indirectly relevant. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Review (expert consensus) | Acta Trop | Consensus on diagnosis, treatment and follow-up of cystic and alveolar echinococcosis |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clin Microbiol Rev | 21st-century advances in echinococcosis diagnosis and treatment |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | Tidsskr Nor Laegeforen | Alveolar echinococcosis; surgery combined with prolonged antiparasitic treatment |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Review | Semin Liver Dis | Hepatic alveolar echinococcosis overview |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Management of liver echinococcosis; surgery is the cornerstone |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Observational study | J Antimicrob Chemother | 35 patients on mebendazole or albendazole, followed for an average of 39 months |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Review | Parasitology | Albendazole is not parasiticidal and can cause severe adverse effects; drug repurposing (pyronaridine) explored |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Preclinical (rat model) | Antimicrob Agents Chemother | Solubilised albendazole formulations to improve bioavailability in a hepatic alveolar echinococcosis model |

## UK Market Information

Albendazole is marketed in the UK, and one valid single-ingredient licence record is held in the local data. No licence number, dosage form or indication text is recorded for it, so no licence table is shown. The product is listed as albendazole 400 mg chewable tablets. Please check the BNF and the current SmPC for authorised indications.

## Safety Considerations

- **Conditions flagged as contraindications in related drug-disease data (not label text):** liver disease, gallbladder disease, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pancytopenia, aplastic anaemia.
- **Drug Interactions:** 96 interactions were identified. Examples:
  - Moderate: aprepitant, cobicistat, deferasirox, fostamatinib, alemtuzumab, amprenavir, anagrelide, apalutamide, bendamustine, bexarotene, binimetinib, boceprevir, bosentan, radioiodine (I-123 and I-131), topical abametapir
  - Minor: cimetidine, dexamethasone, lidocaine, armodafinil

Consult the SmPC and BNF for full safety information. The haematological and hepatic concerns above suggest baseline and periodic blood counts and liver function tests during long-term therapy. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (n=194) directly studies albendazole in early-stage alveolar echinococcosis, and guidelines already support its use as parasitostatic therapy. Evidence is mostly guideline and review level, and the available data lack controlled efficacy results.

**To proceed, the following is needed:**
- Published results of NCT07182305
- Label-based warnings and contraindications from the current SmPC and BNF
- A monitoring plan for long-term use (full blood count, liver function)
- Detailed mechanism of action data
- UK licence details (indication text and dosage form)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

