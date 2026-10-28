---
layout: default
title: Mexiletine
parent: Model Prediction Only (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
monitor_inn: "Mexiletine"
predicted_indications: ["hypertrichosis (disease)", "nephrogenic syndrome of inappropriate antidiuresis", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "migraine disorder", "isolated genetic hair shaft abnormality", "pulmonary hypertension", "migraine with brainstem aura", "headache disorder"]
description: "Mexiletine: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Mexiletine
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

## Mexiletine: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Mexiletine is a class IB sodium channel blocker, used as an antiarrhythmic drug. The original indication text is not recorded in the data compiled for this report.
The TxGNN model ranks **hypertrichosis** highest by score, but the best-supported prediction is **headache disorder** (which includes trigeminal autonomic cephalalgias and refractory chronic daily headache).
It has **no registered clinical trials** and **5 publications**, all small observational or case-series reports, so evidence is limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 (observational studies and case series) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold (research question only) |

**Note on the choice of indication:** The top-ranked predictions by score (hypertrichosis, nephrogenic syndrome of inappropriate antidiuresis, Ambras syndrome and others) have no supporting studies and no plausible mechanism. Headache disorder and migraine have the only direct clinical literature, so this report focuses on headache disorder.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Mexiletine is a known class IB antiarrhythmic that blocks voltage-gated sodium channels. It is also used in clinical practice for neuropathic pain and myotonia.

Trigeminal autonomic cephalalgias and refractory daily headache involve neuronal hyperexcitability and ectopic discharge in trigeminal pathways. Blocking sodium channels could plausibly dampen this activity. A published review suggests that response to intravenous lidocaine (another class IB agent) may help predict response to mexiletine in trigeminal autonomic cephalalgias.

The link to classical migraine is more indirect, because the available studies concern refractory chronic daily headache and SUNCT/SUNA rather than migraine itself. For the other high-scoring predictions (hypertrichosis, congenital malformation syndromes, hair shaft abnormalities, nephrogenic syndrome of inappropriate antidiuresis), no mechanistic link to sodium channel blockade could be identified. These scores likely reflect network artefacts in the model rather than a therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective open-label study with single-arm meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT and SUNA, conditions where evidence-based recommendations are lacking |
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Case series / observational review | Curr Pain Headache Rep | Intravenous lidocaine and mexiletine (class 1B sodium channel blockers) used in trigeminal autonomic cephalalgias |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case series (9 cases) | Headache | Mexiletine used in a refractory chronic daily headache population |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Early clinical report | N Z Med J | Mexiletine in vascular headaches |
| [40197813](https://pubmed.ncbi.nlm.nih.gov/40197813/) | 2025 | Cochrane review | Cochrane Database Syst Rev | Drug treatment for myotonia (indirect relevance to headache) |

Other predictions have little or no relevant literature. For pulmonary hypertension, a 2026 preclinical study ([41518899](https://pubmed.ncbi.nlm.nih.gov/41518899/)) tested lidocaine, not mexiletine, as a TMEM16A channel blocker. A 1991 study ([1724233](https://pubmed.ncbi.nlm.nih.gov/1724233/)) concerned ventricular arrhythmias and does not support a pulmonary hypertension use.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0203020P0AAABAB (BNF-style code) | Mexiletine HCl capsules 200 mg | Capsule | Not stated in the data |

The BNF section code in the identifier (0203, "Drugs for arrhythmias") is consistent with an antiarrhythmic classification. The indication text, dosage form and manufacturer details were not available.

---

## Safety Considerations

- **Contraindications flagged by the TxGNN knowledge graph** (not taken from label text): epilepsy, liver disease, gallbladder disease, hypotensive disorder, myocardial infarction, coronary thrombosis, hemoglobinopathy, atrioventricular block, sick sinus syndrome and familial sick sinus syndrome. These should be checked against the SmPC.
- **Drug interactions:** 100 interactions were identified in total. Among those listed, bupropion is classed as **Major**. Moderate interactions include alosetron, morphine, lorcaserin, eliglustat, obeticholic acid, rolapitant, glycerol phenylbutyrate, potassium citrate, picosulfuric acid, sodium sulfate and polyethylene glycol with electrolytes. Ascorbic acid is classed as Minor. The interactions with omeprazole, sucralfate, vancomycin, nizatidine, simvastatin, potassium chloride and prednisolone have unknown severity.
- **Additional considerations noted in the literature review:** cardiac proarrhythmic risk and CYP2D6/CYP1A2-related interactions need evaluation before any headache use.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring predictions have no supporting evidence or plausible mechanism. The one credible direction, headache disorder (particularly trigeminal autonomic cephalalgias and refractory daily headache), rests only on small case series and open-label data, with no randomised trials and with notable cardiac and interaction risks. It is best treated as a research question rather than a candidate for clinical adoption.

**To proceed, the following is needed:**
- Mechanism of action data and the licensed indication text from the SmPC
- Full SmPC warnings and contraindications (currently unavailable, which blocks safety screening)
- Randomised, controlled evidence for mexiletine in trigeminal autonomic cephalalgias or refractory chronic headache
- A cardiac safety and drug interaction monitoring plan (ECG, CYP2D6/1A2 interacting drugs) for any headache study
- Confirmation of dosage form and route for the UK-authorised product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

