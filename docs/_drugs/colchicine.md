---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 190
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Gout"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "familial Mediterranean fever, autosomal dominant", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Colchicine: From Gout and Familial Mediterranean Fever to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is an established anti-inflammatory drug, originally used to treat gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but there are **no registered clinical trials** and only **2 indirect laboratory publications**, neither of which tested colchicine against malaria. The prediction is therefore a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; familial Mediterranean fever (the UK authorisation data compiled for this report contain no indication text) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, colchicine binds tubulin and disrupts microtubule polymerisation. Its anti-inflammatory effects in gout and FMF are linked to reduced neutrophil chemotaxis and activation.

Microtubules are essential to the cytoskeleton and cell division of *Plasmodium* parasites, so an antiparasitic effect is plausible in principle. However, this link is unproven. The two publications retrieved are indirect: one shows that **curcumin** (not colchicine) disrupts *P. falciparum* microtubules, and the other examines *pfmdr1* expression in mammalian cells and chloroquine susceptibility. Neither shows colchicine efficacy against malaria.

The high TxGNN score is a computational prediction only. Colchicine also has a narrow therapeutic index and substantial toxicity at antiproliferative doses. This weighs against its use in an infectious disease where effective alternatives already exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro study | PLoS One | Curcumin (not colchicine) disrupts microtubules in *P. falciparum*; relevant only as indirect support for microtubules as a target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro study | Mol Cell Biol | Expression of the plasmodial *pfmdr1* gene in mammalian cells increased susceptibility to chloroquine; no colchicine efficacy data |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001040G0AAACAC | Colchicine Tab 500mcg | Tablet (500 microgram) | Not stated in the compiled data |

Only one authorisation record is available, and it carries no indication text or manufacturer. Please check the current MHRA authorisation and the BNF for the licensed indications.

## Cytotoxicity

Colchicine is an antimitotic (microtubule-disrupting) agent rather than a conventional anticancer drug, and it is not classed as antineoplastic here, so a formal cytotoxicity profile is not provided. Toxicity at higher doses is significant (see Safety Considerations). Please refer to the SmPC warnings and precautions.

## Safety Considerations

Label-derived warnings and contraindications are not available in the data compiled for this report. The following comes from knowledge-graph contraindication links (not label text) and from drug interaction data.

- **Contraindication links (knowledge graph):**
  - Liver failure and impaired renal function
  - Blood disorders, including thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including congenital forms), aplastic anaemia and cyclic haematopoiesis
  - Muscle disorders, including myopathy and rhabdomyolysis
  - Peptic ulcer disease and diarrhoeal disease
  - Acute urate nephropathy
- **Drug interactions:** 100 interactions were identified; the 20 listed in the data include:
  - **Major:** aprepitant, clarithromycin, cobicistat, deferiprone, eliglustat, rolapitant, rosuvastatin, simvastatin
  - **Moderate:** chloroquine, cimetidine, metronidazole, miconazole, ticagrelor, and others

  Colchicine combined with strong CYP3A4/P-glycoprotein inhibitors (such as clarithromycin and cobicistat) is a recognised risk for serious toxicity. The statin interactions raise myopathy concerns. The chloroquine interaction is notable given the predicted malaria indication.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Other Predicted Indications (for context)

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Familial Mediterranean fever, autosomal dominant | 99.38% | L4 | Not a true repurposing: colchicine is already first-line therapy for FMF. Only narrative reviews were retrieved, with no subtype-specific trials. Next step is to check whether the dominant-subtype label adds anything beyond the existing FMF indication. |
| Dermatofibrosarcoma protuberans | 99.37% | L5 | No trials or literature. Only a speculative antimitotic rationale, with no link to the COL1A1-PDGFB driver. Hold. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The malaria prediction rests on a model score and two indirect laboratory papers, with no trials and no evidence of colchicine activity against *P. falciparum*. Colchicine's narrow therapeutic index and interaction burden, together with the availability of effective antimalarials, argue against progressing without direct evidence.

**To proceed, the following is needed:**
- In vitro testing of colchicine against *P. falciparum* (including chloroquine-resistant strains), with selectivity versus human cell toxicity
- Detailed mechanism of action data and a comparison of parasite and human tubulin binding
- Label-derived warnings and contraindications from the SmPC and BNF
- Confirmation of the licensed indications for the UK authorisation record
- A review of the chloroquine and other antimalarial interactions if the work progresses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

