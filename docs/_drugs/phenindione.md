---
layout: default
title: Phenindione
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 1
---

# Phenindione
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Phenindione: From Vitamin K Antagonist Anticoagulation to Thrombotic Disease

## One-Sentence Summary

Phenindione is an indandione-class vitamin K antagonist (VKA); however, this evidence pack contains no recorded original indication, mechanism-of-action text, or UK marketing authorisation for the drug. TxGNN predicts efficacy for **Thrombotic Disease**, but this is not a genuinely novel repurposing signal — thrombotic disease is the prototype indication for the VKA drug class itself — and it is supported by only **1 indirect clinical trial** and **20 publications**, most of which are older case reports and reviews rather than direct trial evidence for phenindione.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorisation or original indication text on file for this drug |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L3 (observational/review-level evidence) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Phenindione is not available in structured form. However, the evidence pack's own repurposing rationale indicates that Phenindione belongs to the indandione class of vitamin K antagonists (VKA), acting by inhibiting hepatic synthesis of clotting factors II, VII, IX and X — the same mechanism shared by warfarin, acenocoumarol and fluindione.

This means the predicted indication, thrombotic disease, is pharmacologically self-evident rather than a novel discovery: it is the class-defining indication for any VKA. The TxGNN model has essentially identified the drug's own established pharmacological category rather than surfacing a new therapeutic hypothesis. This significantly limits the value of the prediction for repurposing purposes.

A further important caveat: Phenindione is not currently marketed in the UK (0 licences on file), and historical literature in this evidence pack (e.g. PMID 13162792, "Severe drug sensitivity reaction to phenindione", 1954) points to known hypersensitivity concerns associated with this specific agent — consistent with why indandione-class VKAs (including phenindione) were withdrawn from most markets in favour of coumarin derivatives such as warfarin. Any evaluation of this drug should first establish why it is not marketed in the UK before considering any indication-level decision.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05646394](https://clinicaltrials.gov/study/NCT05646394) | N/A | Recruiting | 150 | Observational registry of antithrombotic regimens (VKA ± aspirin, or dual antiplatelet therapy) in antiphospholipid syndrome patients with a recent arterial thrombotic event. Not a direct interventional trial of phenindione; relevance graded C (indirect, disease-area background only). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13307153](https://pubmed.ncbi.nlm.nih.gov/13307153/) | 1956 | Historical report | J Med Assoc Georgia | Early clinical evaluation naming phenindione ("phenylindanedione") as an effective oral anticoagulant (title only; abstract not available). |
| [13162792](https://pubmed.ncbi.nlm.nih.gov/13162792/) | 1954 | Case report | JAMA | Documents a severe drug sensitivity reaction to phenindione itself — an early signal underlying the drug's later withdrawal from most markets (title only; abstract not available). |
| [41177211](https://pubmed.ncbi.nlm.nih.gov/41177211/) | 2025 | Systematic review | Contraception | Updated systematic review of contraceptive safety in women on anticoagulant (VKA) therapy, addressing bleeding and recurrent thrombosis risk. |
| [24889788](https://pubmed.ncbi.nlm.nih.gov/24889788/) | 2014 | Cohort (case-control) | J Mal Vasc | Identifies risk factors for thrombotic or bleeding events in patients treated with vitamin K antagonists. |
| [21531328](https://pubmed.ncbi.nlm.nih.gov/21531328/) | 2011 | Review | Adv Chronic Kidney Dis | Reviews nephrotoxic syndromes including drug-induced thrombotic microangiopathy, relevant to VKA-class renal safety. |
| [17176918](https://pubmed.ncbi.nlm.nih.gov/17176918/) | 2006 | Case report | Clin Nephrol | Acute immuno-allergic interstitial nephritis caused by fluindione, another indandione-class VKA structurally related to phenindione. |
| [8037888](https://pubmed.ncbi.nlm.nih.gov/8037888/) | 1994 | Review | Drug Safety | Reviews clinically significant drug interactions with oral anticoagulants, including coumarin and indandione derivatives. |
| [12503504](https://pubmed.ncbi.nlm.nih.gov/12503504/) | 2002 | Case series | Arch Pediatr | Use of acenocoumarol and fluindione in 150 paediatric patients following cardiac surgery. |
| [14714343](https://pubmed.ncbi.nlm.nih.gov/14714343/) | 2003 | Cohort | Ann Cardiol Angeiol | Evaluates an education programme for patients undergoing oral anticoagulation therapy. |
| [4338821](https://pubmed.ncbi.nlm.nih.gov/4338821/) | 1972 | Case report | Ann Surg | Femoral neuropathy associated with anticoagulant therapy (title only; abstract not available). |

---

## UK Market Information

No marketing authorisations are currently held for Phenindione in the UK (0 licences on file; market status: Not marketed). No product name, dosage form, or approved indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: no structured warnings, contraindications, or drug–drug interaction data were returned for this drug. However, literature in this evidence pack (PMID 13162792) flags a historical hypersensitivity reaction specifically to phenindione, and a related indandione-class VKA (fluindione) has documented cases of immuno-allergic interstitial nephritis (PMID 17176918). These signals should be confirmed against an official SmPC before any clinical use is considered.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The blocking data gap on regulatory warnings/contraindications (DG001) prevents even an initial safety screen (S1), and mechanism-of-action data is unconfirmed (DG002). More fundamentally, the predicted indication overlaps with the drug's own established VKA class use rather than representing a novel repurposing hypothesis, evidence level is only L3, and the drug is not currently marketed in the UK.

**To proceed, the following is needed:**
- Official SmPC/MHRA label data — warnings, contraindications, and dosing (resolves DG001)
- Confirmed mechanism of action via DrugBank (resolves DG002)
- Clarification of why Phenindione is not marketed in the UK, including any historical withdrawal or safety rationale
- A re-assessment of whether "thrombotic disease" constitutes a genuine repurposing signal, given it duplicates the drug's own pharmacological class indication
- Additional direct clinical trial evidence for phenindione specifically, rather than class-level VKA literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

