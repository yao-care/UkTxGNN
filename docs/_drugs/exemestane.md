---
layout: default
title: Exemestane
parent: Model Prediction Only (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Exemestane: predicted new indication Antithrombin deficiency type 2 (evidence level L5). Approved use: Not available in the UK authorisation data compiled for this report (…"
monitor_inn: "Exemestane"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura", "acne (disease)", "migraine with or without aura, susceptibility to", "breast fibrocystic disease"]
---

# Exemestane
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

## Exemestane: From Hormone-Receptor-Positive Breast Cancer to Antithrombin Deficiency Type 2
{: .text-alpha }

## One-Sentence Summary

Exemestane is a steroidal, irreversible aromatase inhibitor that lowers oestrogen levels. The TxGNN model's top-ranked prediction is **antithrombin deficiency type 2**, but there are **0 clinical trials** and **0 publications** for this indication, so the prediction rests on model output alone. Across all ten predictions, only one (amenorrhoea) has any literature, and that literature does not support exemestane as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the UK authorisation data compiled for this report (exemestane is generally used in oestrogen-receptor-positive breast cancer in postmenopausal women) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, exemestane is a steroidal irreversible aromatase inhibitor that lowers circulating oestrogen. Its efficacy in hormone-receptor-positive breast cancer is established.

For antithrombin deficiency type 2, **no plausible mechanistic link was identified**. This condition is a hereditary SERPINC1 defect that affects thrombin-binding or heparin-binding function. Lowering oestrogen is not known to correct antithrombin function. The high score appears to reflect proximity in the knowledge graph rather than a genuine therapeutic relationship.

The other predictions follow the same pattern:

- **Thrombosis-related predictions** (factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, thrombophilia): there is no mechanism by which exemestane would act on the coagulation cascade. They probably share network neighbours in the graph. Oestrogen modulation can also affect thrombotic risk, so any use in a thrombophilic population would need separate safety consideration.
- **Amenorrhoea**: this is a pharmacological effect of oestrogen lowering, not a treatment target. Using an oestrogen-suppressing drug to treat amenorrhoea is mechanistically contradictory, and the association probably reflects an adverse-effect link in the graph.
- **Migraine (three entries)**: oestrogen withdrawal is a recognised migraine trigger in some women, so oestrogen lowering is more likely to worsen than relieve migraine.
- **Acne**: aromatase inhibition raises the androgen-to-oestrogen ratio and could worsen acne.
- **Breast fibrocystic disease**: this is the most biologically plausible candidate, because fibrocystic changes are oestrogen-responsive and exemestane already acts on breast tissue in cancer. However, no supporting studies were found, and the risk-benefit balance (bone loss, menopausal symptoms) is unfavourable for a benign condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (antithrombin deficiency type 2), or for any of the other nine predicted indications.

---

## Literature Evidence

No literature was found for antithrombin deficiency type 2. The only predicted indication with retrieved publications is amenorrhoea (rank 2). These papers are shown for transparency; they concern amenorrhoea as a context or side effect in breast cancer care, not exemestane as a treatment for it.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohort | Annals of Oncology | Ovarian function recovery in breast cancer patients with chemotherapy-induced amenorrhoea who switched from tamoxifen to exemestane; aromatase inhibitors may promote ovarian function recovery |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Review | Oncology (Williston Park) | Role of ovarian suppression in premenopausal women with hormone-receptor-positive early breast cancer |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Review | Journal of Clinical Oncology | Grand Rounds discussion of whether oestradiol monitoring is needed during ovarian suppression for breast cancer |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Review | Recenti Progressi in Medicina | Current role of LHRH analogues in premenopausal breast cancer; chemotherapy-induced amenorrhoea correlates with reduced recurrence risk |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Review | Klinicka Onkologie | Aromatase inhibitor treatment in postmenopausal breast cancer and management of side effects; aromatase inhibitors are contraindicated in women with functional ovaries |

Study types are tentative because abstracts were truncated.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0803041C0AAAAAA | Exemestane Tab 25mg | Not specified | Not specified |

One valid single-ingredient authorisation is recorded. Dosage form and approved indication text were not available in the data compiled for this report, so please check the MHRA record, SmPC and BNF classification directly.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (aromatase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Low |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the SmPC warnings and precautions (bone mineral density, and liver and renal function are commonly considered) |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Drug interactions:** An interaction screen returned 100 interacting drugs, of which only two are graded. Most others have no assigned severity.

- **Moderate:** dexamethasone, troglitazone
- **Severity unknown:** pantoprazole, omeprazole, lansoprazole, rabeprazole, ranitidine, famotidine, metformin, simvastatin, rosuvastatin, morphine, ondansetron, metronidazole, aspirin, and others

Further points relevant to the predictions:

- Oestrogen modulation can affect thrombotic risk, so use in thrombophilic populations would need separate safety assessment.
- Bone loss and menopausal symptoms are known consequences of oestrogen deprivation and weigh heavily against use in benign conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, antithrombin deficiency type 2, has no clinical, literature or mechanistic support. The high TxGNN score appears to reflect graph proximity only. None of the ten predictions has trial evidence, and the only literature retrieved (amenorrhoea) describes a pharmacological effect rather than a therapeutic benefit.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a documented rationale linking aromatase inhibition to the target condition
- Complete UK authorisation details (dosage form and approved indication) and SmPC safety data, including warnings and contraindications
- For any candidate to be taken forward (breast fibrocystic disease is the most plausible), preclinical or early clinical data, and a risk-benefit assessment covering bone health and menopausal symptoms
- For thrombosis-related candidates, a dedicated thrombotic safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

