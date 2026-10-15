---
layout: default
title: Nizatidine
parent: Model Prediction Only (L5)
nav_order: 452
evidence_level: L5
indication_count: 7
---

# Nizatidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Nizatidine: From Gastric Ulcer to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is a histamine H2-receptor antagonist, originally used to treat gastric and duodenal ulcers, peptic ulcer disease and gastro-oesophageal reflux disease.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **no registered clinical trials** but **19 publications** currently supporting this direction.
This prediction largely overlaps with the drug's existing uses, so it is better described as on-label confirmation than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis, dyspepsia, duodenal ulcer (UK licence text not available) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (provisional, see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, nizatidine is an H2-receptor antagonist. It blocks histamine at the parietal cell and so reduces basal, nocturnal and stimulated gastric acid secretion. The literature describes it as a potent inhibitor of acid secretion, and in animal studies it was more active than cimetidine on a weight-for-weight basis.

Acid suppression is the core mechanism for healing peptic ulcers. The predicted indication is therefore not a new use. It overlaps with the drug's established indications (gastric ulcer, duodenal ulcer and peptic ulcer disease). The literature includes randomised, placebo-controlled trials in active duodenal ulcer and benign gastric ulcer, as well as maintenance studies after healing.

**Note on the evidence level:** The L1 grade rests on publication titles and abstracts describing randomised trials. No registered clinical trial record (for example, an NCT number with a verified Phase 3 design) was available, so the grade should be treated as provisional.

**Other predictions in the ranked list**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Peptic ulcer perforation | 99.94% | L5 | Model prediction only. No evidence nizatidine prevents or treats perforation itself. |
| Gastrojejunal ulcer | 99.94% | L4 | Mechanistically plausible, but the literature is indirect. PPIs are generally preferred. |
| Duodenal obstruction | 99.86% | L5 | Model prediction only. No direct evidence of benefit. |
| Duodenogastric reflux | 99.85% | L5 | Mainly a bile and pancreatic secretion problem, which H2-receptor antagonists do not address. |
| Gastroduodenitis | 99.58% | L3 (provisional) | Small studies on NSAID-induced lesions. No randomised evidence for the condition itself. |
| Multiple endocrine neoplasia | 99.27% | L5 | Model prediction only. Any link is symptomatic control of acid hypersecretion, and PPIs have largely replaced H2-receptor antagonists. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | Eight-week, multicentre, double-blind comparison of nizatidine 150 mg twice daily and 300 mg at bedtime with placebo in healing active benign gastric ulcer |
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | Randomised, placebo-controlled trial | Clin Pharmacol Ther | Two-phase trial of nizatidine 150 mg twice daily versus placebo for healing and recurrence of active duodenal ulcer |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | Randomised, placebo-controlled trial | Isr J Med Sci | In 55 patients with active duodenal ulcer, nizatidine 300 mg at night versus placebo for 4 weeks, examining healing and mucosal inflammatory mediators |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | Randomised, double-blind study | Scand J Gastroenterol Suppl | One-year maintenance in 513 patients with healed duodenal ulcer. Cumulative recurrence at 12 months was 34% with nizatidine versus 64% with placebo |
| [7863254](https://pubmed.ncbi.nlm.nih.gov/7863254/) | 1994 | Open clinical study | Scand J Gastroenterol Suppl | Efficacy and quality-of-life effects of nizatidine maintenance therapy in healed duodenal ulcer |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Review of pharmacology, pharmacokinetics and therapeutic use of nizatidine in peptic ulcer disease. Notes potent inhibition of acid secretion and that published experience was limited at the time |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy for peptic ulcer disease. Describes the newer H2 blockers, including nizatidine, as safe and effective without new clinically important properties |
| [2892253](https://pubmed.ncbi.nlm.nih.gov/2892253/) | 1987 | Safety analysis | Scand J Gastroenterol Suppl | Safety assessment in about 3,800 nizatidine-treated individuals across US and European trials in ulcer disease |
| [15683433](https://pubmed.ncbi.nlm.nih.gov/15683433/) | 2005 | Randomised controlled study | J Gastroenterol Hepatol | Nizatidine compared with famotidine as maintenance therapy for erosive oesophagitis. The study explores the additional prokinetic effect of nizatidine |
| [26883979](https://pubmed.ncbi.nlm.nih.gov/26883979/) | 2016 | Animal study | Life Sci | Gastroprotective effects of several H2-receptor antagonists on ibuprofen-induced gastric ulcer in rats |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103010N0AAAAAA (BNF-style product code, not a PL number) | Nizatidine capsules 150 mg | Capsule | Indication text not available in the data compiled for this report |

Only one valid single-ingredient authorisation is recorded. The dosage form, manufacturer and approved indication wording were not available, so please check the current SmPC and BNF.

---

## Safety Considerations

**Contraindications (knowledge-graph associations, not label text)**

The knowledge graph links nizatidine to the following conditions. These should be checked against the SmPC.
- Liver disease
- Gallbladder disease
- Impaired renal function
- Gastric cancer and related gastric neoplasms (including gastric carcinoma, diffuse gastric adenocarcinoma and linitis plastica). Acid suppression can mask symptoms and delay diagnosis of gastric malignancy, so malignancy should be excluded before treatment.

**Drug Interactions**

The interaction screen returned 100 interacting drugs, and 20 are shown in the data compiled for this report. Examples by severity:
- **Major:** atazanavir, dasatinib. Acid suppression can reduce absorption of drugs that need an acidic environment.
- **Moderate:** acalabrutinib, bosutinib, brigatinib, ceritinib, dabrafenib, dacomitinib, cefditoren, cefpodoxime, cefuroxime, chlorpropamide
- **Minor:** ketorolac, ibuprofen, diclofenac, oxaprozin, alendronic acid, axitinib, cyanocobalamin, magnesium oxide

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction for active peptic ulcer disease is supported by randomised, placebo-controlled trials in gastric and duodenal ulcer. However, it is essentially on-label confirmation rather than new repurposing, and the evidence is largely from the 1980s and 1990s. No registered trial records were available. Among the other predictions, none beyond gastroduodenitis (provisional L3) has meaningful supporting evidence, and those should be held or treated only as research questions.

**To proceed, the following is needed:**
- Current UK SmPC and BNF text, including the approved indication, dosage form, warnings and contraindications
- Verified trial records (for example, NCT or ISRCTN identifiers) to confirm the evidence level
- Mechanism-of-action data from DrugBank
- Clinical review of the major interactions, particularly with drugs that need gastric acid for absorption
- Dose adjustment guidance in renal impairment, and exclusion of gastric malignancy before use
- A comparison with current standard care, as PPIs are generally preferred for many acid-related conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

