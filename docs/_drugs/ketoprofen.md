---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
description: "Ketoprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Ketoprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ketoprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and other arthropathies.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Ketoprofen is a non-selective cyclooxygenase (COX) inhibitor, and its efficacy in inflammatory and degenerative joint disease is well established. It works by reducing prostaglandin synthesis.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia caused by loss of function of the *GDF5* (CDMP1) gene. Ketoprofen has no established mechanism for correcting this defect. At most it could offer symptomatic pain relief, which is not a disease-modifying rationale. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should therefore be treated as a hypothesis only.

Other predicted indications were also screened. Most are rare developmental or genetic disorders with no plausible COX-related mechanism. Two stand out as research questions:

- This is class-level evidence that overlaps with ketoprofen's existing indications, so it is probably not true repurposing.
- **Juvenile arthritis due to defect in LACC1** (score 0.9974): NSAIDs are commonly used for symptom control in juvenile arthritis, but this monogenic autoinflammatory-type disease usually needs biologic therapy, so ketoprofen would be adjunctive at best.

Pseudoachondroplasia (score 0.9995) has a plausible indirect link, as early-onset joint pain and osteoarthritis are common, but this is symptomatic use only and no data were supplied.

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
| 100302010AAAAAA | Ketoprofen Gel 2.5% | Not specified | Not specified |

Only one authorisation is recorded, for a topical gel. The authorisation number in the compiled data does not follow the usual MHRA "PL" format, so it should be verified against the MHRA register. Dosage form and indication text are missing and should be confirmed against the current SmPC and BNF.

---

## Safety Considerations

- **Contraindications and conditions of concern (from the knowledge graph, not label text):** hypertension, liver failure, kidney disease, peptic ulcer disease (including active disease), blood coagulation disease, myocardial infarction and coronary thrombosis, cardiovascular and heart disease, and haemoglobinopathy. These are consistent with the known NSAID class risks (gastrointestinal, cardiovascular, renal and bleeding). They must be verified against the SmPC.
- **Drug Interactions:** the interaction screen returned 100 interacting drugs. Examples from the 20 retrieved entries:
  - *Moderate:* corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aspirin (acetylsalicylic acid), metformin, glimepiride and chlorpropamide, mesalazine and balsalazide, naltrexone, potassium citrate and bicarbonate, and the bowel preparations picosulfuric acid and polyethylene glycol with electrolytes.
  - *Minor:* famotidine, ranitidine, cimetidine and linaclotide.

Label warnings and contraindications were not available for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no publications and no plausible mechanism linking COX inhibition to a *GDF5*-related skeletal dysplasia. The same applies to most of the other top-ranked predictions. Only the spondyloarthropathy and LACC1-related juvenile arthritis predictions merit follow-up as research questions, and these largely reflect existing NSAID class use.

**To proceed, the following is needed:**
- Ketoprofen-specific clinical or literature evidence for any chosen indication, with priority on spondyloarthropathy and juvenile arthritis
- Mechanism of action data
- Label warnings and contraindications from the SmPC and BNF
- Confirmation of the UK authorisation details (number, dosage form, approved indication)
- Assessment of route compatibility, as only a topical gel is recorded in the UK data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

