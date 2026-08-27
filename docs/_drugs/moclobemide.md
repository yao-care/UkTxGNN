---
layout: default
title: Moclobemide
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 2
---

# Moclobemide
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

# Moclobemide: From Depression to Agoraphobia

## One-Sentence Summary

Moclobemide is a reversible inhibitor of monoamine oxidase A (RIMA), historically used as an antidepressant. The TxGNN model predicts it may also be effective for **Agoraphobia**, with **no registered clinical trials** but **12 supporting publications**, including two randomised controlled trials in panic disorder with agoraphobia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (based on known pharmacological class information — not present in the supplied regulatory dataset) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory dataset. Based on known information drawn from the supporting literature, moclobemide is a **reversible inhibitor of monoamine oxidase A (RIMA)**, which raises synaptic concentrations of serotonin (5-HT), noradrenaline (NE) and dopamine (DA). Its antidepressant efficacy has been demonstrated in multiple placebo-controlled trials, and this same monoaminergic mechanism is the pharmacological basis for its use in anxiety-spectrum disorders.

Agoraphobia is, in clinical practice, most commonly diagnosed alongside panic disorder ("panic disorder with agoraphobia" in DSM classification) rather than as an isolated diagnosis. The monoamine dysregulation hypothesis underlying panic disorder and social anxiety disorder overlaps substantially with agoraphobia's presumed pathophysiology, and moclobemide's efficacy in panic disorder and social anxiety disorder is well documented in the literature below.

However, none of the identified studies use "agoraphobia" as the primary, isolated diagnostic entry — evidence instead comes from trials and reviews of panic disorder with agoraphobia as a co-occurring feature. This should therefore be regarded as **extrapolated evidence** rather than direct, indication-specific evidence, which is reflected in the L2 evidence grade.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448444](https://pubmed.ncbi.nlm.nih.gov/10448444/) | 1999 | RCT | The British Journal of Psychiatry | Randomised trial of moclobemide, cognitive-behavioural therapy, and their combination in panic disorder with agoraphobia |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | RCT | European Archives of Psychiatry and Clinical Neuroscience | Multicentre double-blind RCT (n=135) comparing moclobemide 450 mg/day vs clomipramine 150 mg/day in panic disorder with/without agoraphobia |
| [16850261](https://pubmed.ncbi.nlm.nih.gov/16850261/) | 2006 | Cohort/Comparative neuroimaging | Metabolic Brain Disease | SPECT study comparing citalopram vs moclobemide effects on resting brain perfusion in social anxiety disorder |
| [28867934](https://pubmed.ncbi.nlm.nih.gov/28867934/) | 2017 | Review | Dialogues in Clinical Neuroscience | Guideline-based review of pharmacological treatment for panic disorder/agoraphobia and other anxiety disorders |
| [32002937](https://pubmed.ncbi.nlm.nih.gov/32002937/) | 2020 | Review | Advances in Experimental Medicine and Biology | Review of current and novel psychopharmacological agents for panic disorder/agoraphobia, GAD and SAD |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of RIMAs (moclobemide, brofaromine, toloxatone); moclobemide antidepressant efficacy shown in 4 placebo-controlled trials |
| [2248064](https://pubmed.ncbi.nlm.nih.gov/2248064/) | 1990 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of MAOI efficacy in panic disorder with agoraphobia, social phobia and related conditions |
| [8313401](https://pubmed.ncbi.nlm.nih.gov/8313401/) | 1993 | Review | Clinical Neuropharmacology | Review of reversible MAO-A inhibitors (brofaromine, moclobemide) in panic disorder trials vs clomipramine |
| [1498904](https://pubmed.ncbi.nlm.nih.gov/1498904/) | 1992 | Review | Clinical Neuropharmacology | Review of reversible MAO-A inhibitors in panic disorder (abstract not available) |
| [7892341](https://pubmed.ncbi.nlm.nih.gov/7892341/) | 1995 | Case report | Psychiatrische Praxis | Treatment-refractory panic disorder with agoraphobia managed successfully with combined imipramine, moclobemide and behavioural therapy |

*Two further pending-classification records (PMID 12006898, 7954487) were excluded from this table in favour of the ten most clinically relevant entries.*

---

## UK Market Information

No UK marketing authorisations were identified for moclobemide in the supplied dataset (0 licenses; market status: Not Marketed). Any future UK use for this indication would require a full regulatory pathway assessment, as no MHRA-authorised product currently exists to reference for dosage form or approved wording.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level L2 is supported only by literature-derived RCTs in panic disorder with agoraphobia rather than trials targeting agoraphobia as a standalone diagnosis, and no clinical trials are currently registered for this specific indication.
- There is no UK marketing authorisation for moclobemide (0 licenses, Not Marketed status), and a **blocking data gap** exists for official product warnings/contraindications (DG001), which prevents progression to the S1 safety evaluation stage.

**To proceed, the following is needed:**
- Official product warning/contraindication data (e.g. TFDA or MHRA-equivalent SmPC), to resolve blocking data gap DG001
- Confirmed mechanism of action documentation from DrugBank or equivalent source (DG002)
- Clinical trials or studies enrolling agoraphobia specifically, rather than as a co-diagnosis with panic disorder
- A UK regulatory pathway assessment, given the current unlicensed status

*Note on secondary prediction:* The evidence pack also flags a lower-confidence signal for "benign paroxysmal torticollis of infancy" (TxGNN score 99.30%, Evidence Level L5, recommendation Hold). This prediction has no supporting clinical trials or literature and no plausible mechanistic link to moclobemide's RIMA activity; it should be treated as a low-priority model artefact and is not recommended for further investigation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

