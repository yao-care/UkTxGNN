---
layout: default
title: Sucralfate
parent: Model Prediction Only (L5)
nav_order: 540
evidence_level: L5
indication_count: 2
---

# Sucralfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Sucralfate: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

> Sucralfate is a cytoprotective agent historically used for peptic ulcer and gastritis management, as reflected in the literature evidence within this pack.
> The TxGNN model predicts it may be effective for **Duodenogastric Reflux**,
> with **no registered clinical trials** but **13 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the regulatory pack; literature evidence describes sucralfate as a treatment for peptic/duodenal ulcer and gastritis (e.g. PMID 2186496, 3838414) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L3 (published randomised and comparative studies; no registered clinical trials) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record. However, the literature within this pack itself provides mechanistic clues: sucralfate is repeatedly described as having "cytoprotective features in addition to its known antipepsin and antacid effects" (PMID 3838414), forming a protective barrier over damaged mucosa — a mechanism well suited to conditions involving mucosal injury from refluxed gastric or duodenal contents.

Duodenogastric reflux involves retrograde flow of alkaline, bile-containing duodenal contents into the stomach, causing mucosal irritation and "alkaline reflux gastritis" (PMID 6372664). Because sucralfate's original use appears closely tied to peptic ulcer and gastritis management, and its mucosal-protective mechanism is not acid-dependent, it is mechanistically plausible that the same barrier effect would also reduce symptoms and mucosal damage from bile-mediated reflux rather than acid-mediated injury alone.

This rationale is further supported by direct clinical literature: several controlled studies specifically tested sucralfate in alkaline/bile reflux gastritis (e.g. PMID 3839973, 12923369, 3475771, 3616071), lending real-world plausibility to the TxGNN prediction beyond pure mechanistic extrapolation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | The American Journal of Medicine | Randomised, double-blind study of sucralfate 6g/day vs placebo in 23 patients with alkaline reflux gastritis post-gastric surgery |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | European Journal of Gastroenterology & Hepatology | Randomised trial of sucralfate vs rabeprazole vs no treatment for post-cholecystectomy alkaline reactive gastritis |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | RCT | Scandinavian Journal of Gastroenterology, Supplement | Prospective randomised trial comparing sucralfate with placebo in symptomatic/macroscopic gastritis including duodenogastric reflux |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Comparative study | Minerva Gastroenterologica e Dietologica | Compared cisapride vs sucralfate for dyspeptic symptoms in duodenogastric reflux gastritis (18 patients) |
| [3616071](https://pubmed.ncbi.nlm.nih.gov/3616071/) | 1987 | Case series | Revista Espanola de las Enfermedades del Aparato Digestivo | Evaluation of 50 cases of postsurgical biliary reflux gastritis treated with sucralfate |
| [2186496](https://pubmed.ncbi.nlm.nih.gov/2186496/) | 1990 | Case series | Terapevticheskii Arkhiv | 72 patients with erosive/ulcerous gastroduodenal lesions treated with sucralfate; beneficial effect on pain and healing |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Review | The American Journal of Gastroenterology | ACG Committee review of sucralfate's cytoprotective, nonulcer uses including gastritis |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Current Treatment Options in Gastroenterology | Review of duodenogastric reflux-induced (alkaline) oesophagitis and its medical/surgical management |
| [17285081](https://pubmed.ncbi.nlm.nih.gov/17285081/) | 2006 | Review | Journal de Chirurgie | Review of duodenogastric and gastroesophageal bile reflux pathophysiology, diagnosis and therapy |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annual Review of Medicine | Review of alkaline reflux (bile) gastritis and oesophagitis pathophysiology and management |

---

## UK Market Information

No UK marketing authorisations are recorded in this evidence pack (market status: **Not Marketed**, total licences: **0**).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists — SmPC-level warnings and contraindications are unavailable, so a safety initial assessment (S1) cannot be completed. Combined with missing mechanism of action data, zero UK marketing authorisations, and no registered clinical trials for duodenogastric reflux, the evidence base — while mechanistically and historically plausible from older literature — is not yet sufficient to progress.

**To proceed, the following is needed:**
- SmPC/product labelling warnings and contraindications (resolves DG001, currently Blocking)
- Mechanism of action data via DrugBank (resolves DG002)
- Confirmation of UK regulatory pathway/licensing status for sucralfate
- Registered clinical trial evidence specifically for duodenogastric reflux
- Drug-drug interaction (DDI) data, currently not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

