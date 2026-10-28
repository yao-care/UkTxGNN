---
layout: default
title: Ampicillin
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 9
monitor_inn: "Ampicillin"
predicted_indications: ["laryngitis", "Ureaplasma urethritis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "gingivitis", "paranasal sinus neoplasm (disease)", "bacterial arthritis", "conjunctivitis", "pericoronitis"]
last_modified_at: 2026-10-27
description: "Ampicillin: predicted new indication Laryngitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ampicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ampicillin: Aminopenicillin beta-lactam antibiotic → Laryngitis
{: .text-alpha }

## One-Sentence Summary

Ampicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis.
The TxGNN model predicts it may be relevant to **laryngitis**, but **no clinical trials** and only **indirect literature** (mostly case reports, reviews and retrospective series on related bacterial laryngeal infections such as epiglottitis) currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ampicillin is a beta-lactam that inhibits bacterial cell wall synthesis, so it is plausibly relevant to bacterial infections of the larynx, such as epiglottitis and laryngeal or deep neck abscess.

The prediction has important limits:

- Most laryngitis is viral, so a benefit for the general indication is not supported.
- Epiglottitis is largely a *Haemophilus influenzae* disease, and ampicillin is no longer reliable for it because of beta-lactamase production.
- The retrieved publications are about related conditions (epiglottitis, laryngeal abscess, croup, deep neck infections) and do not study laryngitis itself as a treatment target for ampicillin.

For these reasons the evidence level is L5 (model prediction without a directly relevant study).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications is a randomised trial of ampicillin in laryngitis. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesthesia and Intensive Care | Review of 161 children with acute epiglottitis; 45 complications and 5 deaths; airway management emphasised |
| [3026014](https://pubmed.ncbi.nlm.nih.gov/3026014/) | 1986 | Not classified | Reviews of Infectious Diseases | Sulbactam/ampicillin in paediatric epiglottitis, prompted by ampicillin-resistant *H. influenzae* type b |
| [3290661](https://pubmed.ncbi.nlm.nih.gov/3290661/) | 1988 | Not classified | Monatsschrift Kinderheilkunde | 27 children with epiglottitis; emerging ampicillin resistance of *H. influenzae* type b changed therapy |
| [6881564](https://pubmed.ncbi.nlm.nih.gov/6881564/) | 1983 | Not classified | Anesthesia and Analgesia | 23 children with epiglottitis treated with ampicillin or chloramphenicol; study of intubation duration |
| [3322611](https://pubmed.ncbi.nlm.nih.gov/3322611/) | 1987 | Not classified | Clinical Otolaryngology | 19 adult epiglottitis cases; bacteriology and treatment principles |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Review | Western Journal of Medicine | 9 adults with acute epiglottitis; intubation needed in 4 |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case report/Review | Ann Otol Rhinol Laryngol | Spontaneous laryngeal abscess case and review of reported cases |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Cohort | Otolaryngol Head Neck Surg | Perioperative antibiotic choice in laryngectomy and complications |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | Cohort | Eur Arch Otorhinolaryngol | Microbiology and antibiotic selection in neck abscesses in diabetes |
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Not classified | CoDAS | Quality assessment of clinical guidelines for laryngitis and pharyngitis (AGREE II) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501013E0AAAAAA | Ampicillin Cap 250mg | Not recorded | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 61 interactions are recorded. Moderate-level interactions include doxycycline, minocycline, tetracycline, kanamycin, balsalazide, lansoprazole, dexlansoprazole and picosulfuric acid. Clarithromycin is rated minor. Others (for example omeprazole, pantoprazole, morphine, vancomycin, prednisolone) are of unknown level.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the retrieved literature concerns related bacterial conditions rather than laryngitis itself. Most laryngitis is viral, and ampicillin is unreliable against the main bacterial cause of the closest related condition (epiglottitis). The high model score is not matched by supporting clinical evidence.

**To proceed, the following is needed:**
- Controlled clinical data in a defined bacterial laryngeal infection population
- Local resistance data (particularly beta-lactamase-producing *H. influenzae*)
- Mechanism of action data and product-level safety information from the SmPC
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

