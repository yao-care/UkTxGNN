---
layout: default
title: Amantadine Hcl
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 0
---

# Amantadine Hcl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amantadine HCL: Drug Repurposing Evaluation — Evidence Pack Incomplete, Assessment on Hold

---

## One-Sentence Summary

Amantadine hydrochloride is a well-established agent with dual antiviral and anti-Parkinsonian properties, used clinically for influenza A prophylaxis and Parkinson's disease management. The current Evidence Pack contains critical data gaps — the TxGNN prediction pipeline returned no output, UK regulatory data appears to be missing or erroneous, and all safety fields are absent — meaning a full repurposing evaluation cannot be completed at this stage. **A Hold decision is recommended pending data remediation.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in Evidence Pack — see note below |
| Predicted New Indication | Not available — TxGNN predictions absent |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| UK Market Status | Reported as "Not Marketed" — likely a data pipeline error |
| Number of Marketing Authorisations | 0 (reported) — likely a data collection error |
| Recommended Decision | **Hold** |

> **Note on Original Indication:** The Evidence Pack's `original_indications` array is empty and `drugbank_id` is null, preventing automated retrieval. From established pharmaceutical knowledge, amantadine is licensed in the UK (Symmetrel, Alliance Pharmaceuticals) for Parkinson's disease, drug-induced extrapyramidal reactions, and influenza A prophylaxis/treatment, and is listed in BNF section 4.9.1. The reported "Not Marketed" status is inconsistent with this and should be investigated.

---

## Why This Prediction Cannot Currently Be Assessed

The Evidence Pack for amantadine HCL is missing several components required for a repurposing evaluation:

**Missing TxGNN predictions.** The `predicted_indications` array is empty. Without model output, no candidate new indication can be evaluated, and this report cannot proceed beyond a preliminary assessment. This is the primary blocker.

**Absent mechanism of action data.** The DrugBank ID is null, preventing automated MOA retrieval. From general pharmaceutical knowledge, amantadine acts as an uncompetitive NMDA receptor antagonist and also promotes presynaptic dopamine release — a dual mechanism that underpins both its antiparkinsonian and antiviral activity, and which has historically generated interest in neurological repurposing (e.g. MS-related fatigue, traumatic brain injury recovery, levodopa-induced dyskinesia). This context cannot be formally cited from the current Evidence Pack but provides useful background for the remediation team.

**UK regulatory data not retrieved.** The system reports zero MHRA marketing authorisations. Amantadine is known to hold UK licences and is listed in the BNF; this is almost certainly a data collection failure rather than a genuine absence from the UK market. The MHRA Product Licence database and the BNF should be consulted to correct this.

---

## Clinical Trial Evidence

Currently no related clinical trial evidence is available in this Evidence Pack.

> *This section will be populated once TxGNN predictions are generated and the evidence collection pipeline is re-run against ClinicalTrials.gov, ISRCTN, and the EU Clinical Trials Register.*

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack.

> *This section will be populated following successful evidence collection via PubMed and other sources once a predicted indication is available.*

---

## UK Market Information

The Evidence Pack reports no UK marketing authorisations for amantadine HCL. This is inconsistent with known pharmaceutical data.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| *Not retrieved* | *Symmetrel (known — not confirmed by pipeline)* | *Capsule / Syrup* | *Parkinson's disease; drug-induced extrapyramidal reactions; influenza A (known — not confirmed by pipeline)* |

> The MHRA Product Licence database and BNF section 4.9.1 should be consulted to formally populate this table. Any NICE technology appraisals relevant to amantadine should also be checked.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> All safety fields in the Evidence Pack — including key warnings, contraindications, and drug–drug interactions — are absent. Known safety considerations for amantadine (e.g. CNS toxicity, renal dose adjustment, live attenuated influenza vaccine interaction, teratogenicity risk) cannot be formally reported from the current data. The SmPC available from the MHRA website should be reviewed before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for amantadine HCL is critically incomplete. No TxGNN predictions have been generated, UK regulatory data is absent or erroneous, and all safety and MOA fields are missing. A meaningful repurposing evaluation cannot be conducted until these gaps are resolved.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for amantadine HCL — this is the primary blocker; without a predicted indication the report cannot advance beyond this stage
- **Retrieve DrugBank ID** (amantadine is DB00915 in DrugBank) to populate MOA, drug category, and safety fields
- **Correct UK regulatory data collection** — cross-reference the MHRA Product Licence register and BNF section 4.9.1 to capture all current UK marketing authorisations for amantadine
- **Obtain SmPC from MHRA** to populate warnings, contraindications, and drug interaction fields; confirm whether NICE has issued relevant guidance
- **Determine antineoplastic status** — once DrugBank categories are retrieved, confirm whether the Cytotoxicity section is required (currently assessed as unlikely, given the known drug class)
- **Re-generate the Evidence Pack** once the above remediation steps are complete, then proceed to full evaluation

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Suspected adverse reactions should be reported via the MHRA Yellow Card Scheme at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

