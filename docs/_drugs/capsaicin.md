---
layout: default
title: Capsaicin
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Capsaicin
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

# Capsaicin: From Neuropathic Pain to Otitis Externa

---

## One-Sentence Summary

Capsaicin is a naturally occurring TRPV1 (Transient Receptor Potential Vanilloid 1) receptor agonist, widely used internationally as a topical analgesic for neuropathic pain, though no UK marketing authorisation is recorded in this Evidence Pack.
The TxGNN model assigns its highest prediction score of **98.76%** to **Otitis Externa** as a candidate repurposing indication; however, **no supporting clinical trials or published literature** have been identified for this specific application, placing it at the lowest evidence level (L5) and warranting a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK marketing authorisation on record; internationally recognised for topical neuropathic pain management |
| Predicted New Indication | Otitis Externa |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L5 (model prediction only — no clinical studies identified) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, capsaicin is the principal pungent component of *Capsicum* peppers and a potent, selective agonist at the TRPV1 (Transient Receptor Potential Vanilloid 1) receptor. On initial exposure, TRPV1 activation causes intense sensory neuronal depolarisation and the release of neuropeptides including Substance P and CGRP. With sustained or repeated exposure, this progresses to receptor desensitisation and Substance P depletion, ultimately attenuating nociceptive signalling in the treated tissue. This desensitisation mechanism underlies capsaicin's established clinical role in chronic neuropathic pain.

The theoretical rationale for the otitis externa prediction is that TRPV1 receptors are expressed on sensory neurones innervating the external ear canal. In principle, local capsaicin-mediated desensitisation could attenuate otalgia. This is the mechanistic pathway the TxGNN knowledge graph is most likely following.

However, clinical plausibility is very limited. Otitis externa is primarily an infectious and inflammatory condition — most commonly caused by *Pseudomonas aeruginosa*, *Staphylococcus aureus*, or fungal organisms — and requires antimicrobial therapy directed at the underlying pathogen. Capsaicin has no known direct antibacterial, antifungal, or disease-modifying anti-inflammatory activity relevant to this pathology. Applying a potent chemical irritant to acutely inflamed, potentially macerated ear canal skin also raises serious tolerability and safety concerns. This prediction is most likely driven by broad TRPV1 expression annotation in the knowledge graph rather than a genuine therapeutic mechanistic link. It is worth noting that among all ten predictions in this pack, **post-infectious syndrome** (rank 5, score 98.66%) carries substantially stronger mechanistic support — gut TRPV1 sensitisation in post-infectious IBS is directly corroborated by published clinical and translational literature (PMID [33023902](https://pubmed.ncbi.nlm.nih.gov/33023902/), [29051514](https://pubmed.ncbi.nlm.nih.gov/29051514/)) — and represents the more scientifically credible repurposing candidate in this dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for otitis externa.

---

## Literature Evidence

Currently no related literature available for otitis externa.

---

## UK Market Information

No MHRA marketing authorisations for capsaicin are recorded in this Evidence Pack (0 licences on file; market status: not marketed).

Clinicians should independently verify current UK licensing status via the [MHRA Product Licence Database](https://products.mhra.gov.uk/) and the British National Formulary (BNF), as capsaicin-containing preparations (such as high-concentration cutaneous patches for peripheral neuropathic pain) may hold authorisations not captured in this dataset. Any suspected adverse reactions to capsaicin products should be reported via the **Yellow Card Scheme**.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (98.76%), the proposed use of capsaicin in otitis externa is entirely unsupported by clinical trial or published literature evidence (L5), and the mechanistic basis for treating an infectious ear condition with a TRPV1-desensitising agent is extremely weak — capsaicin addresses nociception, not the underlying antimicrobial or inflammatory aetiology of otitis externa.

**To proceed, the following is needed:**

- Retrieve full capsaicin MOA data from DrugBank to formally document TRPV1 pharmacology in the evidence pack
- Obtain and review the UK SmPC (or MHRA equivalent) to establish the complete safety profile, including any contraindications relevant to otic or mucosal use
- Commission or identify preclinical (in vitro / in vivo) studies demonstrating analgesic benefit in external ear canal models; without at least L4 evidence, the hypothesis cannot be scientifically justified for progression
- Conduct a feasibility assessment for otic capsaicin formulation development, including tolerability modelling for inflamed mucosa (route compatibility currently pending)
- **Strongly consider redirecting the primary repurposing focus to post-infectious syndrome (rank 5)**, which has an L4 evidence base (3 clinical trials, 4 publications including mechanistic TRPV1 data) and a mechanistic rationale rated as the highest-fidelity among all ten predictions in this dataset

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

