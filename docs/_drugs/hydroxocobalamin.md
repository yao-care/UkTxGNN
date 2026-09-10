---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Hydroxocobalamin
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

# Hydroxocobalamin: From Vitamin B12 Deficiency to Esophageal Varices Without Bleeding

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, established for the treatment of cobalamin deficiency. The TxGNN model's top-ranked prediction suggests possible efficacy in **esophageal varices without bleeding**, but this candidate currently has **no clinical trials and no published literature** supporting it, and the model's own mechanistic review found no plausible biological link between B12 metabolism and variceal disease. This evidence pack also screened nine further candidate indications for this drug; none reached a credible repurposing signal (see Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 (cobalamin) deficiency — no formal UK licence text on file, but confirmed elsewhere in this evidence pack as the drug's established use |
| Predicted New Indication | Esophageal Varices Without Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the information present, hydroxocobalamin is a vitamin B12 (cobalamin) analogue, used for correcting cobalamin deficiency and as a cyanide-detoxifying agent; neither of these established roles has a known biochemical connection to oesophageal variceal disease.

Esophageal varices arise from portal hypertension — dilated submucosal veins secondary to increased portal venous pressure, typically from cirrhosis. This pathology involves vascular and haemodynamic mechanisms entirely distinct from cobalamin/cyanide metabolism. The evidence pack's own repurposing rationale for this candidate states explicitly that there is "no mechanistic support" and that the TxGNN score likely reflects a spurious knowledge-graph link rather than a genuine pharmacological relationship.

Given the complete absence of clinical trials or literature for this specific drug-disease pair, and the reviewer-flagged mechanistic implausibility, this prediction should be treated as a low-confidence model artefact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Hydroxocobalamin currently holds no marketing authorisation on record in this dataset (market status: **Not marketed**, 0 licences). No product, dosage form, or approved-indication information is available to tabulate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: TFDA/MHRA labelling data — including key warnings and contraindications — is marked as a Blocking data gap and must be resolved before any safety evaluation can proceed; see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature evidence, and the mechanistic rationale explicitly contradicts a plausible drug-disease link between hydroxocobalamin and esophageal varices. The high TxGNN score alone is insufficient to support progression.

**To proceed, the following is needed:**
- Resolve the Blocking data gap on TFDA/MHRA warnings, contraindications, and SmPC content before any safety-stage review can begin
- Obtain mechanism of action (MOA) data from DrugBank to properly assess mechanistic plausibility
- If this prediction is to be pursued further, seek independent pharmacological or preclinical rationale, since none currently exists in the source data

**Additional note on this evidence pack:** nine further TxGNN-predicted indications were screened alongside this one (varicose disease, several autoimmune myopathies, congenital prothrombin deficiency, and vitamin deficiency disorder). All were rated **Hold** or lacked genuine repurposing value — the only one with substantial evidence (vitamin deficiency disorder, L2, 50 trials, 20 publications) reflects hydroxocobalamin's already-established use as a B12 replacement therapy, not a novel indication. No candidate in this pack currently supports progression beyond Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

