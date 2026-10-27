---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Teriparatide: predicted new indication Duodenal ulcer (evidence level L5). Approved use: Postmenopausal osteoporosis / osteoporosis"
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Teriparatide: From Postmenopausal Osteoporosis to Duodenal Ulcer
{: .text-alpha }

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34), originally used to treat osteoporosis in patients at high risk of fracture.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Teriparatide is the active fragment (1-34) of human parathyroid hormone. Pharmacology data show it acts on the PTH1 receptor (and is also listed against the PTH2 receptor). In osteoporosis it works as a bone-building (anabolic) agent, stimulating osteoblast-driven bone formation. Detailed mechanism-of-action data were not available beyond these receptor targets.

On the data compiled for this report, **no plausible mechanistic link** between anabolic PTH signalling and duodenal ulcer healing is evident. Osteoporosis is a skeletal disease, whereas duodenal ulcer is a mucosal disease of the upper gastrointestinal tract. No shared pathway, supporting study or clinical observation connects them.

The high model score probably reflects network-level associations in the knowledge graph rather than a biological rationale that can be tested. It should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0606010U0AAACAC (BNF-style product code, not a PL number) | Teriparatide injection 250 micrograms/mL, 2.4 mL pre-filled pen | Injection (pre-filled pen) | Not specified in the listing |

The listing is a single marketed single-ingredient product. It carries no approved indication text, so the indication should be confirmed against the SmPC and BNF.

---

## Safety Considerations

- **Contraindication signals (knowledge-graph derived, not label text):** hypercalcaemia, hyperparathyroidism, bone osteosarcoma, bone Paget disease (including juvenile Paget disease), osteomalacia, rickets, renal osteodystrophy, osteitis fibrosa, nephrocalcinosis, urolithiasis, phosphorus metabolism disease and hypotensive disorder. These should be verified against the SmPC.
- **Drug Interactions (8 records, including 2 receptor-target entries):**
  - *Moderate:* digoxin, digitoxin, topical calcitriol, topical calcipotriol. Teriparatide can raise serum calcium, which is relevant to digitalis glycosides and to vitamin D analogues.
  - *Minor:* hydrochlorothiazide, furosemide.

Label warnings and contraindication text were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction has a high model score but no trials, no literature and no apparent mechanistic rationale (Evidence Level L5). Teriparatide's known safety signals, such as hypercalcaemia and its effects on calcium handling, add caution without any offsetting evidence of benefit.

**To proceed, the following is needed:**
- A biologically plausible mechanism linking PTH1 receptor signalling to gastroduodenal mucosal healing, supported by preclinical data
- Any preclinical or clinical signal in peptic ulcer disease
- Confirmation of the SmPC-based safety profile, including calcium-related risks and interactions with digoxin
- A clear justification for pursuing this over established ulcer therapy, since teriparatide is a daily injection

**Note on other predictions:** In the same output, **pregnancy-associated osteoporosis** (rank 8, score 99.55%) is much better supported, at Evidence Level L3. It has about 20 publications, including a systematic review and meta-analysis, teriparatide cohort studies and a 2026 position statement. The evidence is observational, with no RCT identified, and it is essentially an off-label extension of the existing osteoporosis use. It is a more realistic research question than duodenal ulcer.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

