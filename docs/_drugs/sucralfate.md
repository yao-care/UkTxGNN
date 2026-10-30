---
layout: default
title: Sucralfate
parent: High Evidence (L1-L2)
nav_order: 579
evidence_level: L2
indication_count: 2
last_modified_at: 2026-10-30
description: "Sucralfate: predicted new indication Duodenogastric reflux (evidence level L2). Approved use: Duodenal ulcer"
monitor_inn: "Sucralfate"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction"]
---

# Sucralfate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **2** 
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

## Sucralfate: From Duodenal Ulcer to Duodenogastric Reflux
{: .text-alpha }

## One-Sentence Summary

Sucralfate is a mucosal-protective agent, originally used to treat duodenal ulcer.
The TxGNN model predicts it may be effective for **duodenogastric reflux** (alkaline reflux gastritis), with **no registered clinical trials** but **11 publications**, including **2 randomised controlled trials**, currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duodenal ulcer |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 0.9937 |
| Evidence Level | L2 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, sucralfate binds to damaged gastric mucosa and forms a protective barrier. It is also thought to adsorb bile acids and pepsin.

Duodenogastric reflux means bile and other duodenal contents flow back into the stomach and can injure the mucosa, causing alkaline reflux gastritis and sometimes oesophagitis. Sucralfate's established mucosal-protective action in peptic ulcer disease could plausibly reduce this bile-related injury. The link rests on general knowledge of the drug rather than on mechanism data in the supplied record.

A note on the second prediction in the data: **duodenal obstruction** (TxGNN score 0.9930) has no credible mechanistic link and no supporting evidence. Sucralfate protects ulcerated mucosa but does not relieve mechanical obstruction. The high score probably reflects network proximity to duodenal ulcer, of which obstruction is a complication. It is not discussed further, and its recommendation is **Hold** (L5).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Double-blind trial in 23 patients with alkaline reflux gastritis symptoms after gastric surgery. Sucralfate 6 g/day vs placebo for 6 weeks, followed by 6 weeks of open-label sucralfate. |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | Sucralfate vs rabeprazole vs no treatment for post-cholecystectomy alkaline reactive gastritis, assessing dyspeptic symptoms and endoscopic/histological signs. |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Clinical study | Minerva Gastroenterol Dietol | 18 patients with duodenogastric reflux gastritis given cisapride 30 mg/day or sucralfate 4 g/day for two months; compares a prokinetic with a cytoprotective agent. |
| [3616071](https://pubmed.ncbi.nlm.nih.gov/3616071/) | 1987 | Cohort | Rev Esp Enferm Apar Dig | Evaluation of 50 cases of gastritis from postsurgical biliary reflux treated with sucralfate (no abstract available). |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | Review | Scand J Gastroenterol Suppl | Half-year randomised placebo-controlled trial of sucralfate in symptomatic gastritis, discussed alongside gastro-oesophageal and duodenogastric reflux. |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Duodenogastric reflux-induced (alkaline) oesophagitis; best medical treatment is proton-pump inhibitors, and treatment can be difficult. |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Alkaline reflux gastritis and oesophagitis: causes, diagnostic features and pathophysiology of bile-induced mucosal injury. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Review/Cohort | Eur J Pediatr | Six children and adolescents with primary duodenogastric reflux and excessive bile exposure on 24-hour gastric bilimetry. |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Review | Am J Gastroenterol | Non-ulcer uses of sucralfate; role in gastritis and oesophagitis is promising but not clearly established. |
| [10228771](https://pubmed.ncbi.nlm.nih.gov/10228771/) | 1999 | Surgical series | Hepatogastroenterology | Duodenal switch operation for pathological duodenogastric reflux. Not drug-related; useful for disease context only. |

The abstracts available in the data do not report outcome results, so efficacy conclusions cannot be drawn from this table alone.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103030S0AAAAAA | Sucralfate Tab 1 g | Tablet | Not available |

This is the only authorisation in the data compiled for this report (single-ingredient, valid). The identifier is not in the usual PL format, and dosage form and indication text are not recorded, so please verify the entry against the MHRA register and the BNF.

---

## Safety Considerations

- **Disease-level contraindication signals** (from the TxGNN knowledge graph, not from label text): hyperglycaemia, chronic kidney disease, chronic renal failure and end-stage renal failure. These should be checked against the SmPC.
- **Drug Interactions**: 100 interactions were identified; the 20 shown in the data include:
  - **Major**: dolutegravir, bictegravir
  - **Moderate**: tetracycline, doxycycline, alendronic acid, risedronic acid, ibandronate, acarbose, pioglitazone, alogliptin, albiglutide, allopurinol, ascorbic acid, calcifediol, baloxavir marboxil
  - **Minor**: beta-blockers (acebutolol, atenolol, betaxolol, bisoprolol) and anagrelide

  Many of these likely reflect reduced absorption when taken together with sucralfate, so dose separation may be needed.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two small randomised trials and several smaller clinical studies examine sucralfate in alkaline reflux gastritis, and the mechanism is plausible. However, the trials are small and old, no trials are registered, the results are not reported in the available abstracts, and the UK licence record is incomplete. This supports further investigation, not a change in practice.

**To proceed, the following is needed:**
- Review of the full texts of the two RCTs (PMIDs 3839973 and 12923369) for outcomes and effect sizes
- Mechanism of action data (currently missing)
- SmPC and BNF warnings and contraindications, particularly for renal impairment and diabetes or hyperglycaemia
- A verified MHRA licence record with dosage form and approved indication
- A plan for managing interactions, including dose separation from interacting drugs
- Any new trial would need a defined patient group (for example, post-gastric surgery or post-cholecystectomy) and clear symptom and histological endpoints
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

