---
layout: default
title: Scopolamine
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 6
---

# Scopolamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Scopolamine: From Motion Sickness to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine (hyoscine) is a naturally occurring antimuscarinic alkaloid with established clinical use in motion sickness prevention, pre-operative sedation, and nausea management.
The TxGNN model predicts potential utility in **Cauda Equina Syndrome**, with a prediction score of 99.99%; however, there are currently **no registered clinical trials and no published literature** to support this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No MHRA marketing authorisation records identified in this dataset |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not identified in dataset |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available for this assessment. Based on established pharmacology, Scopolamine is a competitive antagonist at muscarinic acetylcholine receptors — principally M1 and M3 subtypes — belonging to the belladonna alkaloid class. Its well-recognised clinical applications include prevention of motion sickness (transdermal patch), reduction of pre-operative secretions, and management of postoperative nausea and vomiting.

Cauda Equina Syndrome (CES) is a neurosurgical emergency arising from compression of the lumbosacral nerve roots within the spinal canal, for which urgent surgical decompression remains the definitive intervention. The TxGNN model's high prediction score most plausibly reflects an **indirect knowledge graph pathway**: CES frequently produces secondary neurogenic bladder dysfunction, and antimuscarinic agents — the pharmacological class to which scopolamine belongs — are used to suppress involuntary detrusor contractions, a common sequela of CES. The model appears to have identified a class-level association via the neurogenic bladder node rather than any direct mechanistic link to CES itself.

This connection concerns symptomatic management of a secondary complication, not disease modification of CES. More bladder-selective antimuscarinics — oxybutynin, tolterodine, and solifenacin — are already established first-line agents for neurogenic detrusor overactivity, offering superior receptor selectivity and a more favourable systemic side-effect profile compared to scopolamine. The biological plausibility for scopolamine as a targeted treatment directed at cauda equina syndrome is therefore considered **low**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or published literature evidence supports scopolamine for cauda equina syndrome, and the mechanistic rationale is indirect — the TxGNN prediction most likely reflects a knowledge graph association routed through neurogenic bladder rather than a direct therapeutic target in CES; established and more selective agents already address the implicated complication.

**To proceed, the following is needed:**

- Retrieve mechanism of action data from the DrugBank API to enable formal mechanistic plausibility assessment (data gap DG002, currently High severity)
- Conduct a full MHRA product licence search to reconcile the dataset status: Scopoderm TTS (transdermal patch) and Kwells (oral tablets) are known UK-marketed scopolamine products; the current dataset records zero MHRA authorisations, which is likely a search gap rather than true market absence
- Review published literature on anticholinergic use specifically in CES-associated neurogenic detrusor overactivity to determine whether any clinical signal exists for this drug in this context
- Evaluate whether a bladder-selective antimuscarinic (rather than scopolamine) would constitute a more appropriate and differentiated repurposing candidate for neurogenic bladder as a CES complication
- Assess clinical meaningfulness and competitive landscape versus current standard of care before committing to further evidence generation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

