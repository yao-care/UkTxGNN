---
layout: default
title: Lactulose
parent: Model Prediction Only (L5)
nav_order: 358
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Lactulose: predicted new indication Obstructive jaundice (evidence level L5). Approved use: Hepatic encephalopathy, hepatic coma, constipation"
monitor_inn: "Lactulose"
predicted_indications: ["acute urate nephropathy", "nephrolithiasis", "obstructive jaundice", "bile duct disease", "biliary tract disease", "hyperphosphatemia (disease)", "exercise-induced malignant hyperthermia", "bile duct neoplasm"]
---

# Lactulose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Lactulose: From Hepatic Encephalopathy to Obstructive Jaundice
{: .text-alpha }

## One-Sentence Summary

Lactulose is a non-absorbable disaccharide, originally used to treat hepatic encephalopathy, hepatic coma and constipation.
The TxGNN model predicts it may be useful for **obstructive jaundice** (mainly to reduce complications such as endotoxaemia and postoperative renal dysfunction), with **no registered clinical trials** but **20 publications** retrieved, most of them small, older or preclinical studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma, constipation (the UK licence record carries no indication text) |
| Predicted New Indication | Obstructive jaundice (top-ranked prediction, acute urate nephropathy, has no supporting evidence; see note below) |
| TxGNN Prediction Score | 0.9953 (obstructive jaundice); 0.9989 for the top-ranked acute urate nephropathy |
| Evidence Level | L5 (obstructive jaundice) |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold (research question; no registered trials, evidence limited to small, older or preclinical studies) |

**Note on selection:** The highest-scoring prediction, acute urate nephropathy (0.9989), has no trials or literature and no plausible mechanism (L5). This report therefore focuses on obstructive jaundice, the highest-ranked prediction with meaningful literature (L3). Other predictions are summarised at the end.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Lactulose is widely understood to be a non-absorbable sugar that is fermented in the colon. This lowers colonic pH, reduces ammonia absorption and has an osmotic laxative effect. This is the basis of its use in hepatic encephalopathy and constipation.

In obstructive jaundice, bile no longer reaches the gut. This is associated with impaired intestinal barrier function, bacterial translocation and systemic endotoxaemia, which contribute to postoperative complications, especially renal dysfunction. Lactulose may reduce gut endotoxin load and bacterial overgrowth, which provides a plausible link. The retrieved literature describes this hypothesis, but it does not establish a clinical benefit. A 1997 review noted that a renoprotective effect "has not been shown conclusively" in clinical studies. A rat study (1989) found that lactulose did not prevent bile infarction or transaminase elevation.

The relationship between the original and new indications is therefore indirect. Both involve liver disease and gut-derived toxins, but the new use would be supportive perioperative care rather than disease modification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Selected from the retrieved publications, prioritising human studies. Study types are as classified in the compiled data; several were not classified, and findings are based on titles and abstract excerpts only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/) | 1991 | Prospective randomised multicentre study | Br J Surg | 102 patients with obstructive jaundice randomised to preoperative lactulose (n=35), sodium deoxycholate (n=32) or no treatment, assessing postoperative renal dysfunction. Outcome not available in the data |
| [3768644](https://pubmed.ncbi.nlm.nih.gov/3768644/) | 1986 | Clinical/experimental study | Br J Surg | 24 surgical patients (12 lactulose, 12 controls); endotoxaemia was significantly reduced in the lactulose group |
| [12957136](https://pubmed.ncbi.nlm.nih.gov/12957136/) | 2003 | Mechanistic study (rabbit model) | J Surg Res | Evaluated lactulose for preventing bacterial translocation and endotoxaemia after bile duct ligation |
| [23297639](https://pubmed.ncbi.nlm.nih.gov/23297639/) | 2012 | Clinical study | Zh Mikrobiol Epidemiol Immunobiol | Bile duct decompression combined with lactulose; assessed intestinal microecology in obstructive jaundice |
| [15782993](https://pubmed.ncbi.nlm.nih.gov/15782993/) | 2005 | Review | Hepato-gastroenterology | Argues for adequate hydration and lactulose to prevent postoperative renal dysfunction in acute obstructive jaundice |
| [9145459](https://pubmed.ncbi.nlm.nih.gov/9145459/) | 1997 | Review/commentary | Scand J Gastroenterol Suppl | Renoprotective effect of lactulose not conclusively shown in clinical studies |
| [12598962](https://pubmed.ncbi.nlm.nih.gov/12598962/) | 2002 | Animal study | Pediatr Surg Int | Melatonin and lactulose tested on liver and kidney in rats with obstructive jaundice |
| [2614579](https://pubmed.ncbi.nlm.nih.gov/2614579/) | 1989 | Experimental study (rats) | J Pathol | Lactulose, polymyxin B and neomycin did not prevent bile infarction or transaminase rise |
| [8944448](https://pubmed.ncbi.nlm.nih.gov/8944448/) | 1996 | Clinical and experimental study | Br J Surg | Intestinal barrier dysfunction in obstructive jaundice, reversed by internal biliary drainage (not lactulose-specific) |
| [29428098](https://pubmed.ncbi.nlm.nih.gov/29428098/) | 2018 | Review | Hepatobiliary Pancreat Dis Int | Pathophysiology and perioperative management of obstructive jaundice |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0106040G0AAAAAA (BNF-style code, not a PL number) | Lactulose oral solution 3.1–3.7 g/5 ml | Oral solution | Not stated in the compiled data |

Only one authorisation record is available. The BNF classification code (section 1.6.4, osmotic laxatives) is consistent with its use as a laxative. Please check the current SmPC and BNF for the licensed indications and NICE guidance.

---

## Safety Considerations

**Contraindications (from the knowledge graph, not label text):** diabetes mellitus, diabetic ketoacidosis, appendicitis, galactosemia, glycogen storage disease, G6PD deficiency, cystinuria and glucose-galactose malabsorption. These should be verified against the SmPC.

**Drug interactions:** 100 interactions were identified, nearly all graded Moderate in the compiled data (a few Minor, e.g. sodium citrate). Examples include:
- Diuretics and electrolyte-affecting drugs: acetazolamide, hydrochlorothiazide, amiloride
- QT-prolonging or arrhythmia-related drugs: amiodarone, amisulpride, arsenic trioxide, lumefantrine, asenapine, anagrelide
- Corticosteroids and beta-agonists: hydrocortisone, triamcinolone, salbutamol
- Others: tramadol, abiraterone, apalutamide, apomorphine, alfuzosin, atomoxetine, propofol

A plausible shared concern is electrolyte disturbance (e.g. hypokalaemia) from diarrhoea, but the data do not state the mechanisms.

Please refer to the SmPC and BNF for full warnings. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for obstructive jaundice is limited to small, older clinical studies and animal experiments, with no registered trials. One review found no conclusive renoprotective effect, and one rat study found no benefit. The mechanistic hypothesis (reduced endotoxaemia) is reasonable but unproven, and the UK licence record carries no indication text.

**To proceed, the following is needed:**
- Full-text review of the 1991 randomised multicentre study (PMID 2032107) and the 1986 study to confirm outcomes
- A systematic review of lactulose for preventing postoperative renal dysfunction in obstructive jaundice
- Mechanism of action data and UK licence indication wording
- Safety review against the SmPC, including electrolyte monitoring and the knowledge-graph contraindications (notably diabetes)
- If pursued, a modern, adequately powered randomised trial in the context of current biliary drainage practice

**Other predicted indications (for reference):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Acute urate nephropathy | 0.9989 | L5 | No data; no plausible mechanism. Hold |
| Nephrolithiasis | 0.9978 | L5 | No data; computational only. Hold |
| Bile duct disease | 0.9947 | L4 | Mostly indirect or preclinical; overlaps with obstructive jaundice. Research question |
| Biliary tract disease | 0.9938 | L5 | Indirect (bile composition, SIBO, endotoxaemia). Research question |
| Hyperphosphatemia | 0.9937 | L5 | Only a review of constipation in CKD; no evidence of phosphate lowering. Hold |
| Exercise-induced malignant hyperthermia | 0.9914 | L5 | No data; no plausible mechanism. Hold |
| Bile duct neoplasm | 0.9912 | L5 | Indirect perioperative gut-barrier literature only. Research question |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

