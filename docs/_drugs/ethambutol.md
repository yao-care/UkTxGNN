---
layout: default
title: Ethambutol
parent: Moderate Evidence (L3-L4)
nav_order: 260
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-15
description: "Ethambutol: predicted new indication Epiglottitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
---

# Ethambutol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Ethambutol: From Pulmonary Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is an anti-mycobacterial drug originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **epiglottitis**, but there are **no registered clinical trials** and only **1 publication** (a case series on laryngeal tuberculosis) supporting this direction. The prediction most likely reflects tuberculous involvement of the epiglottis rather than a genuinely new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, ethambutol is an anti-mycobacterial agent that inhibits arabinosyl transferase (embCAB), disrupting arabinogalactan synthesis in the mycobacterial cell wall. Its efficacy in pulmonary tuberculosis is well established.

The only supporting literature concerns laryngeal tuberculosis, in which the epiglottis can be affected. Ethambutol is used there as one component of standard multi-drug anti-tuberculous regimens. Any benefit would therefore be limited to tuberculous involvement of the epiglottis, which is essentially the existing indication at a different anatomical site.

The prediction should not be read as support for typical bacterial epiglottitis (for example, *Haemophilus influenzae*), against which ethambutol has no expected activity. The high TxGNN score probably reflects the drug's strong association with tuberculosis in the knowledge graph rather than a distinct mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Case series | European Respiratory Journal | 41 cases of laryngeal tuberculosis (1975–1985); the epiglottis was the second most frequently affected site. All patients had current or earlier pulmonary TB. Treatment was with standard anti-TB drugs including isoniazid, rifampicin and ethambutol. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501090H0AAABAB | Ethambutol HCl Tab 100mg | Not stated | Not stated |

Only one single-ingredient authorisation is recorded, and its status is valid. Approved indication text and dosage form were not available in the compiled data. Please check the current SmPC and BNF entry for ethambutol for the licensed indications.

## Safety Considerations

**Contraindications and conditions flagged in the knowledge graph** (these come from drug–disease relationships in the TxGNN knowledge graph, not from product label text, and should be checked against the SmPC):
- Kidney disease
- Pyoureter
- Gout
- Diabetic retinopathy
- Diabetic cataract
- Optic neuritis

**Drug Interactions:** 100 interactions were identified. The main ones listed are:
- **Moderate:** metronidazole, picosulfuric acid, naltrexone, rosuvastatin, simvastatin, tinidazole, aluminium hydroxide
- **Unknown severity:** clotrimazole, pantoprazole, morphine, omeprazole, lansoprazole, vancomycin, prednisone, nystatin, hydrocortisone, potassium chloride, sulfasalazine, prednisolone, ranitidine

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is a single case series on laryngeal tuberculosis, where ethambutol is part of standard anti-TB therapy. This is not a new repurposing opportunity. There is no evidence for non-tuberculous epiglottitis, and ethambutol would not be expected to work against the usual bacterial causes.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Warnings and contraindications from the current SmPC and BNF (the safety review cannot proceed without these)
- Approved indication and dosage form for the UK authorisation
- Clinical evidence that ethambutol adds value in epiglottitis beyond its existing anti-tuberculosis use, which is unlikely given the biology

**Other predictions reviewed (all Hold):**
- **Laryngitis** (score 99.71%, L4): the evidence is limited to case reports of laryngeal TB and non-tuberculous mycobacterial infection, with several off-topic papers. This is the existing anti-TB indication at another site.
- **Meningococcal infection** (99.63%, L5): no evidence. *Neisseria meningitidis* lacks the ethambutol target, so this is likely a knowledge-graph artefact.
- **Peritonitis** (99.20%, L4): the literature relates to tuberculous peritonitis, where ethambutol is part of standard combination therapy. There is no support for non-tuberculous peritonitis.
- **Infectious otitis media** (99.06%, L5): no evidence, and the common causative bacteria are not ethambutol targets.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

