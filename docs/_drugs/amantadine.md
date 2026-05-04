---
layout: default
title: Amantadine
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 4
---

# Amantadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Amantadine: From Influenza / Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is a well-established antiviral and antiparkinsonian agent with a long history of clinical use, traditionally indicated for influenza A prophylaxis and treatment, as well as Parkinson's disease management.
The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis** — a rare, progressive autoimmune focal encephalitis —
however, **no clinical trials or published literature** currently support this specific repurposing direction, placing the evidence at level **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Influenza A (antiviral); Parkinson's disease (antiparkinsonian) — no current UK marketing authorisation on record |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| UK Market Status | Not currently marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological literature, Amantadine is understood to act via two principal pathways: (1) **antiviral activity**, through blockade of the influenza A M2 proton ion channel, preventing viral uncoating and replication; and (2) **central nervous system activity**, including dopamine release facilitation, dopamine reuptake inhibition, and antagonism at the N-methyl-D-aspartate (NMDA) glutamate receptor — the latter mechanism underpinning its use in Parkinson's disease and levodopa-induced dyskinesia.

Rasmussen Subacute Encephalitis (Rasmussen Encephalitis, RE) is a rare, severe, immune-mediated focal encephalitis characterised by progressive hemispheric destruction, intractable focal seizures, and hemiplegia. It is principally driven by autoimmune mechanisms involving anti-GluR3/GluA3 antibodies directed against ionotropic glutamate receptors. The theoretical rationale for Amantadine in RE centres on **NMDA receptor antagonism**: by attenuating glutamate-driven excitotoxicity, Amantadine could, in principle, slow the progressive neuronal injury that characterises the disease. A secondary mechanistic thread exists via Amantadine's antiviral properties, given that a viral trigger is hypothesised in a subset of RE cases.

That said, this mechanistic reasoning remains entirely inferential. No published clinical trials, case series, or observational studies have specifically evaluated Amantadine in Rasmussen Encephalitis. The TxGNN prediction is driven solely by the knowledge graph's topological associations between Amantadine's known biological targets and RE's molecular pathology, without any direct clinical corroboration at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Amantadine does not currently hold a Marketing Authorisation granted by the MHRA in the United Kingdom. No product licences are registered in this dataset.

> **Note for prescribers:** Amantadine has historically been available in the UK (e.g., as *Symmetrel*) for Parkinson's disease and influenza A. Clinicians requiring current availability information should consult the MHRA Product Licence Register and the BNF. Access via the unlicensed medicines (specials) route may be applicable where appropriate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

> **Important data gap:** Full MHRA SmPC safety data — including warnings, contraindications, and drug–drug interactions — were not available at the time of this report (Data Gap DG001: Blocking severity). This prevents formal S1 safety screening. Retrieval of the SmPC is a prerequisite before any clinical progression recommendation can be made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN graph-based prediction score (99.48%), the complete absence of clinical trial registrations and published literature for Amantadine in Rasmussen Subacute Encephalitis means this candidate cannot progress beyond the hypothesis stage. The mechanistic link, while biologically coherent, is inferential and has not been tested in any preclinical or clinical setting.

**To proceed, the following is needed:**

- **Resolve blocking data gap (DG001):** Obtain and parse the MHRA SmPC for Amantadine to complete safety screening — this is a prerequisite for any further evaluation
- **Confirm mechanism of action (DG002):** Retrieve full MOA data from DrugBank (DB00915) to formally characterise NMDA antagonism and antiviral activity relevant to RE pathophysiology
- **Targeted literature search:** Conduct an expanded search of MEDLINE, Embase, and grey literature specifically for NMDA antagonists (including memantine and ketamine) in Rasmussen Encephalitis or related autoimmune encephalitides, to assess class-level evidence
- **Preclinical feasibility:** If the mechanistic review is supportive, consider a rodent model of focal autoimmune encephalitis to evaluate NMDA antagonism before committing to clinical study design
- **Consider alternative predicted indications:** Within this evidence pack, **myelitis (rank 3, evidence level L3)** presents a substantially stronger evidentiary basis for Amantadine repurposing, including a double-blind placebo-controlled RCT (PMID [7611638](https://pubmed.ncbi.nlm.nih.gov/7611638/)) and two Cochrane systematic reviews in post-polio syndrome. A separate evaluation report for myelitis is recommended as a higher-priority repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

