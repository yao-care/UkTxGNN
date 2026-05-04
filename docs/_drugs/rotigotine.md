---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Parkinson's Disease to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Rotigotine is a non-ergoline dopamine agonist delivered via transdermal patch, established for the treatment of Parkinson's Disease and Restless Legs Syndrome.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**, with a prediction score of **99.997%**,
but **no clinical trials** and **no supporting publications** have been identified — this prediction currently rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's Disease; Restless Legs Syndrome |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per available data — see note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack (data gap DG002). Based on established pharmacology, Rotigotine is a broad-spectrum dopamine receptor agonist with activity across D1–D5 subtypes, with particular affinity for D3 and D2 receptors. Delivered via a once-daily transdermal patch, it provides continuous dopaminergic stimulation — a pharmacokinetic profile designed to avoid the peaks and troughs of oral therapy. Its proven efficacy in Parkinson's Disease and Restless Legs Syndrome reflects its core mechanism: compensating for reduced dopaminergic tone in nigrostriatal and mesolimbic pathways.

ADHD is associated with reduced dopaminergic (and noradrenergic) signalling in the prefrontal cortex, particularly via D1 receptors — the so-called "prefrontal D1 receptor hypothesis." On this theoretical basis, Rotigotine's D1/D2 agonist activity could augment prefrontal dopamine tone, which represents the mechanistic premise behind the TxGNN prediction. The model's high score likely reflects strong network proximity in the knowledge graph between dopamine receptor nodes and ADHD disease nodes.

However, there are critical caveats that weaken this hypothesis clinically. Standard ADHD pharmacotherapy (methylphenidate, lisdexamfetamine) acts via dopamine and noradrenaline reuptake inhibition, producing transient, activity-dependent increases at the synapse. Rotigotine's continuous, direct receptor agonism — particularly at D2/D3 — may over-activate striatal circuits, potentially worsening hyperactivity or inducing stereotyped behaviours. Furthermore, dopamine agonist class effects (impulse control disorders, compulsive behaviours) documented in existing Parkinson's use are of particular concern in a patient population where impulsivity is already a core feature. The prediction is mechanistically plausible in outline but diverges materially from established pharmacological strategy, and no clinical evidence currently supports it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No MHRA marketing authorisations are recorded in the data available for this evidence pack.

> **Verification required**: This finding should be confirmed against the MHRA product licence register directly. Rotigotine (Neupro® transdermal patch, UCB Pharma) is understood to hold regulatory approval for Parkinson's Disease and Restless Legs Syndrome within the European and UK regulatory framework; the absence of records here is likely a data sourcing gap rather than a true reflection of UK market status. Healthcare professionals should consult the current **BNF** (Section 4.9.1 — Dopaminergic drugs used in Parkinson's disease) and the **MHRA medicines search** at [products.mhra.gov.uk](https://products.mhra.gov.uk) for authoritative and up-to-date authorisation information.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Class-level alert**: As a dopamine agonist, Rotigotine carries a well-characterised class risk of **impulse control disorders** (pathological gambling, hypersexuality, binge eating, compulsive spending). This risk is of heightened concern when considering use in ADHD, where impulsivity is a core symptom. Full safety data from MHRA-approved SmPC (data gap DG001) must be reviewed before any further assessment proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.997%), the evidence base is entirely absent — no registered clinical trials, no observational studies, and no published literature specifically addressing Rotigotine in ADHD — placing this squarely at evidence Level L5 (model prediction only). The mechanistic rationale contains an inherent pharmacological contradiction: the same D2/D3 agonism that underpins Rotigotine's established efficacy could plausibly worsen impulsivity and hyperactivity in an ADHD population. Until preclinical data resolve this question, proceeding to clinical investigation would be premature.

**To proceed, the following is needed:**

- **Verify UK market status**: Confirm MHRA authorisation status directly via the MHRA product licence register and retrieve the current SmPC (resolves data gap DG001)
- **Retrieve full MOA data**: Query DrugBank API for receptor binding profiles and pharmacodynamic data (resolves data gap DG002)
- **Preclinical evidence**: Identify or commission animal model studies examining dopamine D1–D3 agonism in validated ADHD models (e.g., spontaneously hypertensive rat model)
- **Safety review for target population**: Formally assess the impulse control disorder risk profile in the context of ADHD and evaluate whether the transdermal continuous-delivery route is compatible with ADHD treatment in children and adolescents
- **Mechanistic disambiguation**: Conduct a systematic review of prodopaminergic agents in ADHD (note: a related systematic review exists for schizophrenia negative symptoms — PMID [31688399](https://pubmed.ncbi.nlm.nih.gov/31688399/) — which may provide indirect mechanistic context)
- **Regulatory landscape review**: Assess whether any off-label use or compassionate use data exists for dopamine agonists in ADHD within NICE-appraised treatment pathways

---

> *This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions should be interpreted in conjunction with a qualified healthcare professional.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

