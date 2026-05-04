---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a broad-spectrum aminopenicillin antibiotic, widely used in clinical practice for a range of bacterial infections across the respiratory, urinary, and gastrointestinal tracts.
The TxGNN model predicts it may be effective for **laryngitis**, with **1 post-marketing surveillance study** retrieved in this evidence pack — though no direct literature specifically linking ampicillin to laryngitis was identified.
The prediction is mechanistically plausible given ampicillin's established activity against the bacterial pathogens most commonly implicated in upper respiratory tract infections.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Broad-spectrum bacterial infections (aminopenicillin antibiotic class) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (no MHRA licences retrieved in this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ampicillin exerts its bactericidal effect by binding irreversibly to penicillin-binding proteins (PBPs), inhibiting the final transpeptidation step of peptidoglycan synthesis in the bacterial cell wall. This leads to cell lysis and death. Its spectrum of activity covers a broad range of organisms including *Streptococcus pyogenes*, *Streptococcus pneumoniae*, non-beta-lactamase-producing strains of *Haemophilus influenzae*, enterococci, and *Listeria monocytogenes* — many of which are causative agents in upper respiratory tract infections.

Bacterial laryngitis, though less common than viral laryngitis, can be caused by *Streptococcus pyogenes*, *Staphylococcus aureus*, and *Haemophilus influenzae* — organisms within ampicillin's documented spectrum of activity. Ampicillin is already established as a first-line or alternative agent for closely related upper respiratory conditions, including pharyngitis, tonsillitis, otitis media, and acute bronchitis. The TxGNN prediction therefore reflects the known pharmacological profile of the aminopenicillin class rather than a genuinely novel hypothesis.

It is important to recognise that the majority of laryngitis cases in clinical practice are of viral aetiology, for which antibiotics are inappropriate. The mechanistic relevance of this prediction is therefore confined to confirmed or strongly suspected bacterial laryngitis. In that clinical context, an aminopenicillin such as ampicillin or its oral analogue amoxicillin would be a reasonable empirical treatment choice, and the high prediction score is consistent with this established clinical pattern.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completed | 363 | Post-marketing surveillance of CLAVAMOX® (amoxicillin/clavulanate) in Japanese paediatric patients covering multiple upper respiratory and skin indications, including laryngitis; designed to collect real-world safety and efficacy data under routine clinical conditions |

> **Important caveat:** This trial evaluates amoxicillin/clavulanate (a related but distinct aminopenicillin combination), not ampicillin directly. Laryngitis is one of several included indications, and the study is a surveillance study rather than a controlled trial. It provides indirect, supportive — not confirmatory — evidence.

---

## Literature Evidence

Currently no literature directly evaluating ampicillin for laryngitis is available in this evidence pack.

---

## UK Market Information

No MHRA marketing authorisations for ampicillin were retrieved in this evidence pack.

> **Note for clinicians:** This may reflect a data collection gap rather than a true absence of UK licences. Ampicillin and its derivatives are included in the British National Formulary (BNF) under Section 5.1.1 (Penicillins). Clinicians should consult the MHRA product database directly for current authorised ampicillin products in the United Kingdom.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.97%) for ampicillin in laryngitis — a finding that is mechanistically coherent given the drug's well-established activity against common upper respiratory bacterial pathogens — the current evidence pack does not contain direct clinical trials or literature specifically evaluating ampicillin for laryngitis, and no MHRA marketing authorisations were retrieved for this drug.

**To proceed, the following is needed:**

- Verification of current MHRA product licences for ampicillin in the UK (the absence in this dataset is likely a data collection artefact)
- A systematic review or targeted literature search specifically examining aminopenicillins (ampicillin, amoxicillin) in confirmed bacterial laryngitis
- Full SmPC data including contraindications, key warnings, and drug interactions
- Mechanism of action data sourced from DrugBank (DrugBank ID: DB00415)
- Assessment of contemporary UK antimicrobial resistance data for the relevant respiratory pathogens (*S. pyogenes*, *H. influenzae*) to confirm the continued clinical utility of ampicillin in this setting
- Clarification of the clinical indication scope: whether the repurposing target is acute bacterial laryngitis specifically, or a broader category of upper respiratory tract infections in which ampicillin already has recognised use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

