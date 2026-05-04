---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cimetidine: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is a histamine H2-receptor antagonist, widely recognised for its pioneering role in the treatment of peptic ulcer disease and gastric acid hypersecretory conditions. The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**, a chronic mast cell disorder characterised by excessive histamine release. Currently **no registered clinical trials** or **dedicated publications** were identified for this specific indication, though the mechanistic rationale is supported by NCCN and expert consensus recommending H2-blocker use in mastocytosis symptom management.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease, gastric acid hypersecretory conditions |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (Mechanism-based, expert consensus) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Cimetidine was the first clinically available histamine H2-receptor antagonist. It works by competitively blocking H2 receptors on gastric parietal cells, thereby reducing basal and stimulated gastric acid secretion. This mechanism made it a landmark treatment for duodenal and gastric ulcers when it was introduced in the late 1970s. Beyond acid suppression, cimetidine has documented weak anti-androgenic activity (via androgen receptor competition and cytochrome P450 inhibition) and possible immunomodulatory properties.

In smouldering systemic mastocytosis (SSM), abnormally proliferating mast cells release excessive histamine into the circulation. Histamine acting via H2 receptors drives increased gastric acid production, leading to peptic ulceration, diarrhoea, and other gastrointestinal symptoms — which are prominent features of SSM. Cimetidine, by blocking H2 receptors, can directly reduce this excessive acid secretion and alleviate histamine-mediated gastrointestinal disturbance.

This application is well-recognised in clinical practice: NCCN guidelines and expert consensus documents recommend the combination of H1 and H2 receptor antagonists as first-line symptomatic therapy in systemic mastocytosis. Although cimetidine has largely been superseded by newer H2-blockers (ranitidine, famotidine) in general peptic ulcer management, its mechanism is directly relevant to symptom control in histamine-driven mast cell disorders, making the TxGNN prediction pharmacologically sound.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the specific indication of smouldering systemic mastocytosis with cimetidine.

> **Note:** The absence of registered trials reflects the well-established nature of H2-blocker use in mastocytosis (predating modern trial registries) rather than a lack of clinical experience. Guideline recommendations are based on decades of clinical practice.

---

## Literature Evidence

Currently no related literature available specifically linking cimetidine to smouldering systemic mastocytosis in the evidence search.

> **Note:** The use of H2-blockers in mastocytosis is documented in textbooks, NCCN guidelines, and expert consensus statements, which may not be indexed as primary research publications in PubMed under this specific disease term.

---

## UK Market Information

Cimetidine does not currently hold any active MHRA marketing authorisations identified in this dataset.

> **Note:** Cimetidine was historically widely available in the UK (e.g., Tagamet). Healthcare professionals should verify current availability through the BNF and MHRA product registry. The absence of active authorisations in this dataset may reflect market withdrawal of branded products rather than a safety concern.

---

## Additional Predicted Indications

The TxGNN model identified eight further candidate indications for cimetidine. A summary is provided below to give a complete picture of the repurposing landscape:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------------------|-------------|----------------|--------|-------------|----------------|
| 1 | Smouldering systemic mastocytosis | 99.80% | L4 | 0 | 0 | Research Question |
| 2 | Active peptic ulcer disease | 99.79% | L1 | 1 | 18 | Proceed with Guardrails |
| 3 | Gastrojejunal ulcer | 99.77% | L2 | 0 | 20 | Proceed with Guardrails |
| 4 | Peptic ulcer perforation | 99.77% | L4 | 0 | 0 | Hold |
| 5 | Lymphoadenopathic mastocytosis with eosinophilia | 99.76% | L5 | 0 | 0 | Hold |
| 6 | Duodenogastric reflux | 99.49% | L3 | 0 | 8 | Proceed with Guardrails |
| 7 | Duodenal obstruction | 99.44% | L3 | 0 | 11 | Proceed with Guardrails |
| 8 | Acne (disease) | 99.33% | L4 | 0 | 3 | Research Question |
| 9 | Abnormality of glucagon secretion | 99.14% | L5 | 0 | 1 | Hold |

### Rank 2: Active Peptic Ulcer Disease (Strongest Evidence)

This prediction represents the most robustly supported indication, reflecting cimetidine's original therapeutic use.

**Selected Clinical Trial Evidence:**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|--------------|-------|--------|-----------|--------------|
| [NCT01757275](https://clinicaltrials.gov/study/NCT01757275) | Phase 3 | Completed | 239 | Compared high-dose esomeprazole vs cimetidine IV for prevention of rebleeding after endoscopic haemostasis in bleeding peptic ulcer (China). Cimetidine used as active comparator. |

**Selected Literature Evidence:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [73792](https://pubmed.ncbi.nlm.nih.gov/73792/) | 1976 | RCT | Lancet | Landmark trial: 90% ulcer healing with cimetidine vs 36% placebo at 6 weeks in duodenal/prepyloric ulcers |
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 67% healing at 3 weeks with cimetidine 1 g/day vs 25% placebo in duodenal/prepyloric ulcers |
| [3092659](https://pubmed.ncbi.nlm.nih.gov/3092659/) | 1986 | RCT (pooled) | Am J Med | Pooled analysis of 4 European RCTs comparing enprostil vs cimetidine 400 mg BD in duodenal ulcer (n=348) |
| [3299677](https://pubmed.ncbi.nlm.nih.gov/3299677/) | 1987 | Cohort | Scand J Gastroenterol | Multinational maintenance trial (n=1,842): cimetidine 400 mg nocte effective for up to 4 years |
| [2979263](https://pubmed.ncbi.nlm.nih.gov/2979263/) | 1988 | Cohort | Aliment Pharmacol Ther | Six years of continuous cimetidine treatment — efficacy and safety confirmed (UK/Ireland) |
| [6990861](https://pubmed.ncbi.nlm.nih.gov/6990861/) | 1980 | RCT | Ann Clin Res | 82.6% healing with cimetidine vs 48% placebo at 4 weeks; poor correlation between healing and symptoms |
| [8057210](https://pubmed.ncbi.nlm.nih.gov/8057210/) | 1994 | Cohort | J Pediatr Gastroenterol Nutr | Paediatric efficacy: 94.7% gastric ulcer and 87.0% duodenal ulcer healing at 8 weeks |
| [6367680](https://pubmed.ncbi.nlm.nih.gov/6367680/) | 1984 | Review | Arch Intern Med | Tricyclic antidepressants compared with cimetidine for ulcer healing — both effective |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | Review of prostaglandins and H2-receptor antagonists in peptic ulcer pathophysiology |
| [8736619](https://pubmed.ncbi.nlm.nih.gov/8736619/) | 1996 | Drug Review | Drugs | Ebrotidine review — antisecretory potency approximately 10-fold greater than cimetidine |

### Rank 3: Gastrojejunal Ulcer

**Mechanistic rationale:** Gastrojejunal ulcers at surgical anastomosis sites arise from acid exposure to vulnerable jejunal mucosa. H2 blockade by cimetidine reduces acid output, directly addressing the pathogenic mechanism. This is mechanistically identical to duodenal/gastric ulcer treatment.

**Selected Literature Evidence:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6103209](https://pubmed.ncbi.nlm.nih.gov/6103209/) | 1980 | RCT | Lancet | Somatostatin vs cimetidine in severe peptic ulcer haemorrhage — sequential RCT over 2.5 years |
| [7082957](https://pubmed.ncbi.nlm.nih.gov/7082957/) | 1982 | Case Series | Br J Surg | 15-year review: cimetidine reduced elective peptic ulcer surgery by 45% and perforations by 10% |
| [6375965](https://pubmed.ncbi.nlm.nih.gov/6375965/) | 1984 | Clinical Study | Crit Care Med | Cimetidine effective for stress-ulcer prophylaxis, comparable to titrated antacid dosing |
| [10310799](https://pubmed.ncbi.nlm.nih.gov/10310799/) | 1984 | Pharmacoeconomic | Eff Health Care | Cimetidine introduction in the Netherlands reduced hospital costs for peptic ulcer treatment |

### Rank 6: Duodenogastric Reflux

**Mechanistic rationale:** Cimetidine does not directly prevent bile reflux, but reduces gastric acid secretion, thereby mitigating the synergistic mucosal damage caused by acid and bile. Direct pharmacological evidence exists (PMID 4018640).

**Selected Literature Evidence:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [4018640](https://pubmed.ncbi.nlm.nih.gov/4018640/) | 1985 | Mechanistic Study | Gut | Direct demonstration of cimetidine's effects on gastric secretion and duodenogastric reflux in ulcer patients |
| [2294793](https://pubmed.ncbi.nlm.nih.gov/2294793/) | 1990 | Clinical Study | Am J Surg | Cimetidine altered intragastric bile acid composition postoperatively (RCT, n=52) |
| [3080289](https://pubmed.ncbi.nlm.nih.gov/3080289/) | 1986 | Comparative Study | Dig Dis Sci | Misoprostol vs cimetidine on coffee-induced gastric secretion in healthy subjects |

### Rank 8: Acne (Disease)

**Mechanistic rationale:** Cimetidine possesses weak anti-androgenic activity — it competitively binds androgen receptors and inhibits dihydrotestosterone (DHT) binding. Since androgen-driven sebum overproduction contributes to acne pathogenesis, this mechanism could theoretically improve acne. However, cimetidine's anti-androgenic potency is substantially weaker than spironolactone or cyproterone acetate.

**Selected Literature Evidence:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6130053](https://pubmed.ncbi.nlm.nih.gov/6130053/) | 1982 | Review | Der Hautarzt | H2-antagonists in dermatology: controversial effects reported in acne and psoriasis |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Clinical Review | Pol Tyg Lek | Anti-androgen treatment approaches for PCOS-related acne and hirsutism |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology | Cimetidine mentioned among systemic acne treatments with anti-androgenic properties |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Key pharmacological considerations for prescribers:**
> - Cimetidine is a potent inhibitor of cytochrome P450 enzymes (particularly CYP1A2, CYP2C9, CYP2D6, and CYP3A4), resulting in clinically significant drug interactions with warfarin, theophylline, phenytoin, and many other drugs
> - Weak anti-androgenic effects (gynaecomastia, impotence) have been reported, particularly at higher doses or with prolonged use
> - Dose adjustment is required in renal impairment
> - Detailed safety data (SmPC warnings, contraindications) were not available in this evidence pack — this represents a data gap requiring remediation

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN prediction for cimetidine in smouldering systemic mastocytosis is mechanistically well-founded — H2-receptor blockade directly addresses the histamine-mediated gastrointestinal symptoms that characterise this condition. NCCN guidelines already endorse H1+H2 blocker combination therapy for symptom control in systemic mastocytosis. However, formal clinical trial evidence specifically for cimetidine in SSM is lacking in modern registries, and the drug does not currently hold UK marketing authorisation. The strongest evidence in this evaluation relates to cimetidine's well-established efficacy in peptic ulcer disease (L1 evidence, rank 2 prediction), which is mechanistically contiguous with the mastocytosis indication.

**To proceed, the following is needed:**
- Verification of current UK availability of cimetidine (MHRA product registry / BNF check)
- Detailed mechanism of action data and SmPC safety information (remediate data gap DG001/DG002)
- Systematic literature search specifically for "H2 receptor antagonists AND mastocytosis" (broader search terms than "cimetidine AND smouldering systemic mastocytosis")
- Review of current NICE and BSH (British Society for Haematology) guidelines on mastocytosis management
- Assessment of whether famotidine (currently more widely available H2-blocker) would be a more practical therapeutic option in the same indication
- If pursuing a clinical study, a formal protocol for cimetidine as adjunctive therapy in SSM with defined GI symptom endpoints

---

*This report was generated on 5 April 2026. Results are for research purposes only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

