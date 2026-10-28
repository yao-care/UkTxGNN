---
layout: default
title: Cimetidine
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 4
monitor_inn: "Cimetidine"
predicted_indications: ["peptic ulcer perforation", "duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
last_modified_at: 2026-10-27
description: "Cimetidine: predicted new indication peptic ulcer perforation (evidence level L5). Approved use: Not recorded in the local data"
---

# Cimetidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Cimetidine: Histamine H2-receptor antagonist → peptic ulcer perforation
{: .text-alpha }

## One-Sentence Summary

Cimetidine is a histamine H2-receptor antagonist (acid-suppressing medicine). The TxGNN model predicts it may be relevant to **peptic ulcer perforation**, but this prediction is supported by **no registered clinical trials** and **20 publications**, none of which show that cimetidine treats perforation. Several of them are case reports of perforation occurring during cimetidine therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | peptic ulcer perforation |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Cimetidine is known as an H2-receptor antagonist that reduces gastric acid secretion, and it has long been used in acid-related upper gastrointestinal disease.

Perforation, however, is an acute surgical complication of peptic ulcer disease, not a condition treated by acid suppression. The publications retrieved include case reports and series of perforation occurring *during* cimetidine treatment (PMIDs 3967139, 6743974, 7082957). These point to a safety or non-protective signal rather than a therapeutic benefit. Cimetidine may lower long-term ulcer risk, but nothing here shows it treats perforation itself. The high score most likely reflects the disease's close relationship to peptic ulcer in the model's network, rather than a direct therapeutic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Of the 20 publications retrieved, the most relevant are listed below. None is a randomised trial of cimetidine in peptic ulcer perforation. The retrieved abstracts were incomplete for several entries.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8364140](https://pubmed.ncbi.nlm.nih.gov/8364140/) | 1993 | Review of controlled trials | Aliment Pharmacol Ther | Continuous H2-antagonist therapy reduces ulcer recurrence; relapse rates vary with study design |
| [7082957](https://pubmed.ncbi.nlm.nih.gov/7082957/) | 1982 | Case report/Commentary | Br J Surg | After cimetidine became available, elective ulcer operations fell 45%, perforations only about 10% |
| [6743974](https://pubmed.ncbi.nlm.nih.gov/6743974/) | 1984 | Case report | Br J Surg | Nine duodenal ulcer perforations occurred while on cimetidine; all eventually needed vagotomy and drainage |
| [3967139](https://pubmed.ncbi.nlm.nih.gov/3967139/) | 1985 | Case report | Br J Surg | Perforation occurring on cimetidine |
| [922364](https://pubmed.ncbi.nlm.nih.gov/922364/) | 1977 | Report | Br Med J | Perforation of peptic ulcer after withdrawal of cimetidine |
| [6861858](https://pubmed.ncbi.nlm.nih.gov/6861858/) | 1983 | Epidemiological/Cohort | Eur J Clin Pharmacol | Peptic ulcer-related hospital discharges were about 10% lower once cimetidine was generally available |
| [6649737](https://pubmed.ncbi.nlm.nih.gov/6649737/) | 1983 | Surgical audit | Z Gastroenterol | Operated patients fell 35% after cimetidine; elective operations for uncomplicated ulcer fell 51% |
| [1975090](https://pubmed.ncbi.nlm.nih.gov/1975090/) | 1990 | Review | Minerva Chir | Reviews medical and surgical ulcer therapy before and after cimetidine |
| [6113521](https://pubmed.ncbi.nlm.nih.gov/6113521/) | 1981 | Commentary/Review | Lancet | Commentary on cimetidine and peptic ulcer |
| [80675](https://pubmed.ncbi.nlm.nih.gov/80675/) | 1978 | Case report | Lancet | Candida peritonitis associated with cimetidine |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103010D0AAAAAA | Cimetidine Tab 200mg | Not recorded | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. Those listed include moderate interactions with paclitaxel, fentanyl, acalabrutinib, lidocaine, acebutolol, dihydrocodeine, codeine, tramadol, nifedipine and alfentanil. Minor interactions include dolutegravir, zidovudine, paracetamol, ketorolac, ibuprofen, ethinylestradiol, albendazole, alcohol and alendronic acid. Cimetidine inhibits several CYP enzymes, so a full interaction check is needed before use.

Please also refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study directly shows a benefit of cimetidine in peptic ulcer perforation, and the case reports suggest perforation can occur despite treatment. The high TxGNN score of 0.9977 is not supported by clinical evidence, so the evidence level is L5.

**To proceed, the following is needed:**
- Controlled clinical data on cimetidine in perforated peptic ulcer, or a clear rationale for why it would be tested as an adjunct to surgery
- Mechanism of action data
- Licence indication text, dosage form and warnings and contraindications from the SmPC and BNF
- A review of the interaction profile for the likely patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

