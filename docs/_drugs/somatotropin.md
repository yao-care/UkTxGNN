---
layout: default
title: Somatotropin
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Somatotropin: predicted new indication Middle ear neuroendocrine tumour (evidence level L5). Approved use: Pituitary dwarfism, isolated congenital growth hormone deficiency…"
---

# Somatotropin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Somatotropin: From Pituitary Dwarfism to Middle Ear Neuroendocrine Tumour

## One-Sentence Summary

Somatotropin (recombinant human growth hormone) was originally used for growth-related conditions such as pituitary dwarfism, congenital growth hormone deficiency, Turner syndrome and Prader-Willi syndrome.
The TxGNN model predicts it may be effective for **middle ear neuroendocrine tumour** (top-ranked prediction), but there are currently **no clinical trials** and **no publications** supporting this direction.
The mechanism also raises a theoretical safety concern, so this prediction should be treated with caution.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pituitary dwarfism, isolated congenital growth hormone deficiency, Turner syndrome, monosomy X, gonadal dysgenesis, Prader-Willi syndrome, Noonan syndrome (from the knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Middle ear neuroendocrine tumour |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Somatotropin replaces or supplements endogenous growth hormone, acting through the GH/IGF-1 axis to promote linear growth and metabolic effects. Its use in growth disorders is established, but no data compiled for this report link it to neuroendocrine tumour treatment.

The high TxGNN score (0.968) is a computational prediction only. Growth hormone signalling is mitogenic, so it could theoretically promote proliferation of neuroendocrine tissue. This points to a potential **safety concern** rather than a therapeutic rationale.

The same pattern appears in the other top-ranked oncology predictions (malignant cutaneous granular cell tumour, ectomesenchymoma, human herpesvirus 8-related tumour and rhabdoid tumour). All are prediction-only with no supporting data, and growth-promoting effects may be counterproductive.

Three lower-ranked predictions are biologically coherent because they are closely related to existing indications:
- **Mixed gonadal dysgenesis** (score 95.58%): overlaps with the Turner phenotype, but cases with a Y chromosome carry a gonadal tumour risk.
- **Mosaic monosomy X** (score 95.06%): a Turner syndrome variant with the same short-stature mechanism.
- **Turner syndrome due to structural X chromosome anomalies** (score 95.02%): a subtype of an approved indication.

These are closer to extensions of existing indications than true repurposing, and no trials or literature were provided for them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0605010S0AABHBH | Somatropin (Rmc) Inj 24u Pfs Cart | Prefilled cartridge (injection) | Not stated in the available data |

The identifier above appears to be a BNF-style product code rather than a standard MHRA Product Licence (PL) number. The licence number should be verified against the MHRA register.

## Safety Considerations

**Drug Interactions:** 100 interactions were identified. The 20 listed in the compiled data are all rated Moderate:
- **Corticosteroids:** hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- **Antidiabetic agents:** acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, metformin, pioglitazone
- **Proton pump inhibitors:** omeprazole, rabeprazole
- **Others:** aprepitant, clarithromycin, dolasetron, dronabinol

Growth hormone can reduce insulin sensitivity, so glycaemic control should be monitored with antidiabetic agents. Corticosteroids may blunt the growth-promoting effect.

**Theoretical oncological concern:** Because of the mitogenic GH/IGF-1 pathway, use in malignant or endocrine-tumour settings needs careful safety justification. Lentiginosis syndromes may be associated with endocrine tumours (for example Carney complex with GH excess), so GH supplementation could be inappropriate there.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5), with no trials, no publications and no established mechanism. The theoretical proliferative risk of the GH/IGF-1 axis in tumours argues against pursuing the oncology predictions.

**To proceed, the following is needed:**
- Mechanism of action data and a documented mechanistic link to neuroendocrine tumour biology
- A systematic literature search and trial registry search for the predicted indication
- A formal safety assessment of GH/IGF-1 mitogenic risk in tumour settings
- Verification of the UK licence record, including approved indications, dosage form and manufacturer
- Complete SmPC/BNF warnings and contraindications
- For the Turner-related predictions (mixed gonadal dysgenesis, mosaic monosomy X, structural X anomalies): confirm whether they are already covered by the existing Turner syndrome indication. These are better handled as research questions than as new repurposing candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

