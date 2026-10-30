---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
monitor_inn: "Ofloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-30
description: "Ofloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Ofloxacin
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

## Ofloxacin: Polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial.
The TxGNN model predicts it may be useful for **septicaemic plague**. The supporting evidence is **11 publications** (mostly animal and laboratory studies) and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

The evidence level is L5 because no cited study directly examines septicaemic plague in humans. The retrieved publications are animal and in vitro studies of *Yersinia pestis* (the cause of plague). The pipeline's own preliminary grading was L4, but under the ceiling rule L5 applies.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ofloxacin is a fluoroquinolone, a class that inhibits bacterial DNA gyrase and topoisomerase IV, enzymes needed for bacterial DNA replication. This is general class knowledge rather than data from the compiled record.

The relationship to the original uses is straightforward. Ofloxacin is already used against a range of bacterial infections, and plague is also a bacterial infection. *Yersinia pestis* is susceptible to fluoroquinolones in laboratory testing. Plague is therefore a biologically plausible target, unlike the other high-scoring predictions for this drug (such as hyperviscosity syndrome or congenital analbuminemia), which have no credible mechanism.

An important caveat is that the support is indirect. Other fluoroquinolones, such as ciprofloxacin and levofloxacin, are better characterised for plague. Ofloxacin would need to be positioned relative to them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Eleven publications were retrieved for plague. The most relevant are listed below (animal studies first, then in vitro studies). No human trials or RCTs were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal study | Antibiotiki i khimioterapiia | Ofloxacin in experimental plague in mice. In vitro MIC was 0.08 mg/L, and it was more active than pefloxacin and nalidixic acid. Prophylaxis efficacy was lower against strains lacking fraction I and mouse toxin |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Ofloxacin was active in vitro and was compared with beta-lactams, aminoglycosides and doxycycline in a mouse model of systemic *Y. pestis* infection |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal study | Antimicrob Agents Chemother | Mouse model of pneumonic plague comparing streptomycin with antibiotics that have little or no clinical experience |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal study | Antibiotiki i khimioterapiia | Fluoroquinolones including ofloxacin interfered with post-vaccination immunity in mice. A quinolone-resistant vaccine strain avoided this |
| [11871319](https://pubmed.ncbi.nlm.nih.gov/11871319/) | 2001 | Animal study | Antibiotiki i khimioterapiia | Experimental bubonic plague model in baboons for assessing new antibacterials |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | 78 *Y. pestis* strains. Ceftriaxone and ciprofloxacin were most active, followed by ofloxacin and ampicillin |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | 100 human isolates from southern Africa. Ofloxacin and levofloxacin were highly active (MIC90 below 0.03 µg/mL) |
| [18644132](https://pubmed.ncbi.nlm.nih.gov/18644132/) | 2008 | In vitro / molecular | BMC Microbiol | Screening for antibiotic resistance determinants in *Y. pestis* |
| [13677133](https://pubmed.ncbi.nlm.nih.gov/13677133/) | 2003 | In vitro / microbiology | Antibiotiki i khimioterapiia | Plague mutants resistant to rifampicin and nalidixic acid arose at low frequency |

Two further retrieved papers concern *Burkholderia* and *Vibrio cholerae* rather than plague and are not relevant to this prediction.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501120P0AAABAB | Ofloxacin 400 mg tablets | Tablet | Not stated in the licence record |

This is a single-ingredient product with a valid status. The listed number appears to be a product code rather than a standard PL number.

---

## Safety Considerations

**Knowledge-graph contraindication relations** (not taken from label text) include:
- **Cardiac:** long QT syndrome, familial long QT syndrome, torsades de pointes
- **Neurological and neuromuscular:** epilepsy, myasthenia gravis, peripheral neuropathy
- **Musculoskeletal:** tendinitis, rhabdomyolysis
- **Hepatic and renal:** liver failure, liver disease, drug-induced liver injury, kidney disease, impaired renal function
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- **Blood and gut:** thrombocytopenia, anaemia, leukopenia, *Clostridium difficile* colitis

**Drug interactions:** 100 interactions were found. Examples flagged as **Major** include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), bupropion and chlorpropamide. Many **Moderate** interactions involve antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, canagliflozin), as well as famotidine, loperamide, aspirin, and calcium and potassium salts.

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Septicaemic plague is a biologically plausible target, but the evidence is limited to animal and laboratory studies, with no human trials. Better-characterised fluoroquinolones are available for plague. The other nine predictions have no credible mechanism or evidence and should also be held.

**To proceed, the following is needed:**
- Clinical data in human plague, or a rationale for choosing ofloxacin over ciprofloxacin or levofloxacin
- Mechanism of action data and the licensed indication text from the SmPC
- Label-based warnings and contraindications, with particular attention to QT prolongation, tendon, neuropathy and CNS risks
- Review of the interaction profile, notably with corticosteroids, and of dosing in renal impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

