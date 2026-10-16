---
layout: default
title: Clofazimine
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Clofazimine: predicted new indication Pneumocystosis (evidence level L5). Approved use: Leprosy, multibacillary leprosy, pyoderma gangrenosum"
monitor_inn: "Clofazimine"
predicted_indications: ["pneumocystosis", "malaria", "gastrin secretion abnormality"]
---

# Clofazimine
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

# Clofazimine: From Leprosy to Pneumocystosis

## One-Sentence Summary

Clofazimine is an antimycobacterial drug, originally used to treat leprosy (including multibacillary leprosy) and pyoderma gangrenosum.
The TxGNN model predicts it may be effective for **Pneumocystosis**, but there are **no registered clinical trials** and **3 publications**, none of which test clofazimine against Pneumocystis.
This prediction rests on model output alone and is not supported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy, multibacillary leprosy, pyoderma gangrenosum (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clofazimine is an antimycobacterial agent with established use in leprosy and is also used within multidrug regimens for drug-resistant tuberculosis and non-tuberculous mycobacterial infections. A mechanistic route to Pneumocystosis cannot be built from the data compiled for this report.

The high TxGNN score (0.999) is a graph-based prediction only. Pneumocystis is a fungus, and clofazimine's known antimycobacterial activity does not extend to fungi. The retrieved literature appears to link the two conditions through co-occurrence in patients with AIDS, who commonly develop both Pneumocystis pneumonia and mycobacterial infections, not through any therapeutic effect of clofazimine on Pneumocystis.

For context, two other predictions were generated for this drug:
- **Malaria** (score 99.60%, evidence level L4): only indirect in vitro data on clofazimine analogues showing antiplasmodial activity (PMID 29026393). There are no clinical trials and no human efficacy data, and analogue findings cannot be assumed to apply to clofazimine itself.
- **Gastrin secretion abnormality** (score 99.57%, evidence level L5): no trials, no publications and no mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Randomised open-label trial | J Infect Dis | Clofazimine as prophylaxis for disseminated *Mycobacterium avium* complex infection in 110 HIV patients (recent Pneumocystis pneumonia or CD4 ≤100/mm³). It does not test clofazimine against Pneumocystis. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case report | Infection | AIDS patient with *M. kansasii* lung disease complicated by Pneumocystis pneumonia. Recovered on a multidrug regimen including clofazimine, with trimethoprim-sulfamethoxazole added for Pneumocystis. The recovery from Pneumocystis cannot be attributed to clofazimine. |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | General update on opportunistic infections; no abstract available. |

None of these publications provides evidence that clofazimine treats Pneumocystosis.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501100C0AAAAAA | Clofazimine Capsules 100 mg | Capsule (per product name) | Not available in the data compiled for this report |

The manufacturer, dosage form field and indication text are not recorded for this authorisation. Please confirm the details against the MHRA register and the BNF.

---

## Safety Considerations

**Contraindication-related conditions (knowledge graph, not label text):** liver disease, gallbladder disease, diarrhoeal disease, active peptic ulcer disease, digestive system disease, intestinal disease, splenic infarction, splenic disease and hypersplenism.

**Drug Interactions:** 100 interactions were identified. Examples:
- **Major:** cisapride, dolasetron
- **Moderate:** clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, famotidine, loperamide, and a range of laxatives (bisacodyl, picosulfuric acid, lactulose, lactitol, macrogols, magnesium salts, castor oil, glycerin, mineral oil)
- **Minor:** metronidazole

The interaction with QT-prolonging agents (such as cisapride and dolasetron) warrants particular attention.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Pneumocystosis prediction has no clinical trials and no publications testing clofazimine against the organism, and no credible mechanistic link. The very high TxGNN score reflects graph association only. Malaria shows only preclinical analogue data, and gastrin secretion abnormality has no evidence.

**To proceed, the following is needed:**
- Mechanism of action data for clofazimine
- In vitro or in vivo evidence of activity against *Pneumocystis jirovecii*
- Complete UK authorisation details (dosage form, manufacturer, approved indication) and SmPC warnings and contraindications
- Review of the QT-related interaction risk before any new use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

