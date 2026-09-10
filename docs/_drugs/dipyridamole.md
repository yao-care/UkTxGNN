---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Dipyridamole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dipyridamole: From Antiplatelet/Coronary Vasodilator Therapy to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is a phosphodiesterase inhibitor and antiplatelet agent (detailed original indication and MOA are not yet confirmed in UK regulatory data). The TxGNN model assigns it a very high score (**99.99%**) for **Prinzmetal Angina**, but the underlying evidence actually describes dipyridamole **provoking** coronary vasospasm during diagnostic stress testing rather than treating it — no clinical trials and only mechanistic/case-level literature (15 publications) support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — no UK marketing authorisation; evidence pack literature describes the drug generically as an antiplatelet / coronary vasodilator agent |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for dipyridamole is not available in this evidence pack (flagged as data gap DG002). Based on the literature retrieved, dipyridamole is known as a phosphodiesterase inhibitor and adenosine-reuptake blocker with antiplatelet and coronary vasodilator properties, and it is widely used as a pharmacologic "stress agent" for myocardial perfusion imaging.

This is precisely where the mechanistic link to Prinzmetal (variant) angina breaks down. Prinzmetal angina is caused by focal coronary artery **vasospasm**. The retrieved literature does not show dipyridamole being used therapeutically to prevent or treat this spasm — instead, multiple papers (e.g. PMID 3421166, 16630456) describe dipyridamole-induced coronary vasodilation **triggering or unmasking** vasospastic episodes during diagnostic testing, which is closer to an adverse pharmacological interaction than a therapeutic effect.

In other words, the TxGNN model's very high similarity score appears to be driven by dipyridamole's strong association with the general "coronary/angina" disease neighbourhood in the knowledge graph, rather than by a genuine treatment signal for this specific vasospastic condition. No completed or ongoing clinical trial in this evidence pack tests dipyridamole as therapy for Prinzmetal angina.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review | Japanese Circulation Journal | In patients with rest angina (including Prinzmetal's variant), dipyridamole 50 mg was among several agents tested for effect on attacks; propranolol worsened attacks in Prinzmetal cases. |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Case report/Mechanistic | American Journal of Cardiology | Aminophylline-terminated dipyridamole stress can trigger coronary vasospasm in variant angina — an adverse provocation, not a treatment effect. |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Case series | Zhonghua xin xue guan bing za zhi | Compared clinical features of typical vs. atypical coronary artery spasm; dipyridamole testing used diagnostically. |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Observational | Journal of the American College of Cardiology | Echocardiographic changes in transiently asynergic myocardium during ischaemic episodes induced by various pharmacologic mechanisms, including dipyridamole. |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Study (unclassified) | British Heart Journal | Reproducibility of exercise testing in patients with different responses to the dipyridamole test; diagnostic, not therapeutic, use. |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Study (unclassified) | Japanese Circulation Journal | Dipyridamole-loading thallium myocardial imaging increased diagnostic sensitivity for coronary artery disease when combined with exercise testing. |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Study (unclassified) | Revista Portuguesa de Cardiologia | 3-year prognosis of patients with suspected CAD and normal thallium-dipyridamole scintigraphy. |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Study (unclassified) | Circulation | Reviews pathophysiological basis of noninvasive functional stress testing methods, including dipyridamole, for coronary stenosis. |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Study (unclassified) | Clinical Nuclear Medicine | Case report on "cardiac migraine," noting documented variant angina and vasoactive disorders in the differential. |
| [2221701](https://pubmed.ncbi.nlm.nih.gov/2221701/) | 1990 | Study (unclassified) | Annals of the New York Academy of Sciences | Discusses ECG diagnosis of transient myocardial ischaemia, sensitivity/specificity relevant to pharmacologic provocation testing. |

---

## UK Market Information

No UK marketing authorisation is currently on record for dipyridamole in this evidence pack (market status: **Not marketed**, 0 licences). Collection of the TFDA/MHRA-equivalent product label (warnings, contraindications) is flagged as a **blocking data gap (DG001)** and must be resolved before any safety review can proceed.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications, and DDI data were not available in this evidence pack — see DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the very high TxGNN similarity score, the actual literature evidence for Prinzmetal angina consists entirely of diagnostic-context, mechanistic, and case-level reports (L4) describing dipyridamole **inducing** coronary vasospasm during stress testing — not treating it. There are zero registered clinical trials testing dipyridamole as a therapy for this condition, and the proposed mechanism may be directly contrary to the pathology it would need to treat.

**To proceed, the following is needed:**
- TFDA/MHRA product label (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action (DG002)
- A preclinical or mechanistic study specifically distinguishing dipyridamole's provocative (diagnostic) vs. any potential protective (therapeutic) effect on coronary vasospasm, before this candidate can move beyond S1

---

**Note on other candidates in this evidence pack:** This report evaluates only the top-ranked TxGNN prediction (Prinzmetal angina). The same evidence pack contains substantially stronger candidates for dipyridamole — notably **stroke** and **transient ischaemic attack** (both L1, "Proceed with Guardrails," supported by large Phase 3/4 RCTs including ESPRIT (n=4,500) and PRoFESS (n=20,332), and Cochrane meta-analyses) — reflecting dipyridamole's established combination use with aspirin for secondary stroke prevention. These may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

