---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 2
---

# Omeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Omeprazole: From Gastro-oesophageal Reflux Disease to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI), long established for gastro-oesophageal reflux disease (GERD), peptic ulcer disease and *Helicobacter pylori* eradication. The TxGNN model predicts it may be effective for **Duodenogastric Reflux**, with **1 clinical trial** and **20 publications** identified, most of which are observational, mechanistic or animal studies rather than dedicated efficacy RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (taiwan_regulatory.licenses and drug.original_indications are both empty). Omeprazole is generally known as a PPI used for GERD, peptic ulcer disease and *H. pylori* eradication. |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 (Observational/mechanistic studies; no completed RCT specific to this indication) |
| UK Market Status | Not marketed (per evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, omeprazole is a **proton pump inhibitor (PPI)** that irreversibly inhibits the H+/K+-ATPase in gastric parietal cells, reducing gastric acid secretion. Its established efficacy in GERD, peptic ulcer disease and acid-related upper GI conditions is mechanistically adjacent to duodenogastric reflux (DGR), a condition in which duodenal contents (bile, pancreatic enzymes) reflux into the stomach and oesophagus, often alongside acid reflux.

The rationale for repurposing is therefore mechanistic proximity: DGR frequently coexists with acid reflux and peptic ulcer disease, and PPIs are already used off-label in this clinical context to raise gastric pH and reduce mucosal irritation from mixed reflux. Several of the identified publications describe omeprazole being used specifically to study or manage bile/duodenal reflux in Barrett's oesophagus and paediatric populations, supporting biological plausibility.

However, a notable counter-signal exists in the preclinical literature: multiple animal studies (see Literature Evidence below) suggest that acid suppression with omeprazole in the presence of DGR may **potentiate mucosal growth stimulation and gastric carcinogenesis** in rodent models. This is an important mechanistic caveat that should be weighed against the therapeutic rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A | Completed | 157 | Evaluated endoscopic tri-modal imaging (NBI/AFI/WLI) to differentiate functional dyspepsia from reflux disease, including bile (duodenogastric) reflux — a diagnostic rather than interventional trial. |

*No dedicated interventional trial testing omeprazole specifically for duodenogastric reflux as a primary endpoint was identified.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Clinical study | Gut | Omeprazole 20 mg twice daily reduced duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's oesophagus. |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Clinical study | Scand J Gastroenterol | Omeprazole's effect on antral duodenogastric reflux in Barrett's oesophagus; suggests DGR may be reduced by omeprazole. |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Prospective study | J Pediatr Gastroenterol Nutr | Prospective study of omeprazole for oesophageal bile reflux in children. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Case series | Eur J Pediatr | Describes primary duodenogastric reflux in six paediatric patients, unresponsive to classical antacid therapy. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal study | Acta Cir Bras | Investigated omeprazole's role (protective vs. carcinogenic) in rat model of induced duodenogastric reflux. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal study | Dig Dis Sci | Gastric acid blockade with omeprazole promoted gastric carcinogenesis in a rat DGR model — safety signal. |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Animal study | Dig Dis Sci | DGR-induced foregut mucosal growth stimulation was potentiated by omeprazole-induced acid blockade. |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal study | Gastric Cancer | Related PPI (lansoprazole) promoted gastric carcinogenesis in rats with DGR — class-level safety signal. |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | Update on clinical use and pharmacokinetics of PPIs, including omeprazole, across acid-related disorders. |
| [3932137](https://pubmed.ncbi.nlm.nih.gov/3932137/) | 1985 | Clinical pharmacology study | Gut | Early dose-ranging study of omeprazole's effect on basal and stimulated gastric acid output. |

---

## UK Market Information

No UK marketing authorisation is recorded in this evidence pack (`market_status: Not marketed`, `total_licenses: 0`). This appears inconsistent with omeprazole's widespread global availability as a generic PPI, and should be verified directly against the MHRA product database before any regulatory conclusions are drawn — flagged as data gap **DG001** in this evidence pack (TFDA/MHRA SmPC not yet retrieved).

---

## Safety Considerations

Formal safety fields (key warnings, contraindications, drug interactions) are not populated in this evidence pack.

- **Mechanistic safety signal from literature**: Several animal studies (PMID 10389684, 8943968, 15052437) indicate that long-term acid suppression with omeprazole or related PPIs, in the presence of duodenogastric reflux, may potentiate foregut mucosal growth stimulation and gastric carcinogenesis in rodent models. This should be specifically assessed before considering long-term PPI use for a DGR indication.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting omeprazole for duodenogastric reflux is currently limited to observational/diagnostic studies and preclinical animal work, with no completed RCT targeting this indication. A blocking data gap exists around UK licensing status and SmPC safety information (DG001), and MOA confirmation is also outstanding (DG002). Preclinical data additionally raise an unresolved carcinogenesis signal specific to acid suppression under DGR conditions, which warrants dedicated review before any progression.

**To proceed, the following is needed:**
- MHRA SmPC/PIL retrieval to resolve DG001 (warnings, contraindications, licensing status)
- Confirmed mechanism of action data from DrugBank (DG002)
- Verification of actual UK market status (the "not marketed / 0 licenses" record appears anomalous for a generic PPI and should be reconciled)
- Targeted assessment of the preclinical carcinogenesis signal (PMID 10389684, 8943968, 15052437) before considering long-term use in DGR
- Search for any dedicated interventional trials or RCTs specifically evaluating PPI therapy for duodenogastric reflux as a primary endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

