---
layout: default
title: Glucagon
parent: Model Prediction Only (L5)
nav_order: 316
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Glucagon: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Not stated in the UK licence data compiled for this report"
monitor_inn: "Glucagon"
predicted_indications: ["irritable bowel syndrome"]
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Glucagon: From Hypoglycaemia Management to Irritable Bowel Syndrome
{: .text-alpha }

## One-Sentence Summary

Glucagon is a pancreatic peptide hormone, supplied in the UK as an injection (powder plus diluent). The TxGNN model predicts it may be effective for **irritable bowel syndrome (IBS)**. However, the supporting evidence is indirect: **2 clinical trials** and **20 publications** were identified, but the trials tested GLP-1 analogues rather than glucagon.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK licence data compiled for this report |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 (model prediction only; no study has tested glucagon in IBS) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for glucagon is not available in the data compiled for this report. Glucagon acts on the glucagon receptor (GCGR) and is used clinically to raise blood glucose and, during gastrointestinal procedures, as an antispasmodic that relaxes gut smooth muscle.

A plausible but indirect link to IBS exists. Glucagon and GLP-1 come from the same proglucagon precursor, and both influence gut motility. GLP-1 and its analogue ROSE-010 have been reported to slow gastrointestinal motility and reduce pain during IBS attacks.

This link has an important limit: GLP-1 acts through a different receptor (GLP-1R) from glucagon (GCGR). Findings from GLP-1 studies cannot be directly extrapolated to glucagon, and no trial has tested glucagon in IBS patients. The high TxGNN score reflects network-based association, not clinical proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analogue) and GI motor function in women with constipation-predominant IBS. Relevant population, but not glucagon. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 versus ROSE-010 on upper GI motility in humans, with supplementary in vitro work. Not an IBS population and not glucagon. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic review / meta-analysis | Front Endocrinol | GLP-1 receptor agonists and IBS; GLP-1 and ROSE-010 reduce GI motility in IBS patients |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Cross-analysis of clinical study data | Scand J Gastroenterol | ROSE-010 reduced pain during IBS attacks; exploratory analysis to identify suitable subpopulations |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Role of GLP-1 and L-cells in IBS pathophysiology |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Prescription and discontinuation patterns of GLP-1 receptor agonists in IBS patients |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic review | J Headache Pain | GLP-1 receptor agonists in headache and pain disorders |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolised GLP-1 for diabetes and IBS |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | Investigational drugs for constipation-predominant IBS |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Clinical study | Front Nutr | Circulating GLP-1 rose after a low FODMAP diet in IBS patients |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cell Mol Gastroenterol Hepatol | Brain-gut-microbiome axis interactions |
| [41974246](https://pubmed.ncbi.nlm.nih.gov/41974246/) | 2026 | Review | Clin Gastroenterol Hepatol | Care gaps in IBS and future therapies targeting visceral afferents |

Almost all of these publications concern GLP-1 or general IBS biology; none evaluates glucagon itself as an IBS treatment.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0601040H0AAAEAE (BNF-style product code) | Glucagon injection (powder for reconstitution) 1 mg vial with diluent | Injection (powder and diluent) | Not stated in the data compiled |

This is a single valid, single-ingredient product. The BNF section reference implied by the product code (0601, drugs used in diabetes) is consistent with glucagon's use in severe hypoglycaemia.

---

## Safety Considerations

- **Drug Interactions:** 25 interactions were identified; the 20 listed in the data are all classed as **Minor**. They are mainly with beta-blockers (for example atenolol, bisoprolol, carvedilol, metoprolol, propranolol, sotalol, labetalol, nadolol, pindolol, esmolol, and ophthalmic timolol, betaxolol, carteolol, levobunolol and metipranolol) and with **warfarin**.

Warning and contraindication text from the label was not available in the data compiled. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the evidence is indirect. The trials and most publications concern GLP-1 analogues acting on a different receptor, and no study has tested glucagon in IBS. The evidence level is therefore L5, and label safety data is incomplete.

**To proceed, the following is needed:**
- Mechanistic evidence on whether glucagon (GCGR) signalling affects gut motility or visceral pain in IBS
- Any direct clinical or well-designed preclinical study of glucagon in IBS
- The glucagon mechanism of action and the UK licensed indication text
- Label warnings and contraindications from the SmPC and BNF, to allow safety screening
- An assessment of route and dosing feasibility, as the current product is an injection and chronic IBS use would need a different approach
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

