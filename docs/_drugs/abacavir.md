---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Abacavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) used as part of combination antiretroviral therapy for HIV-1 infection in adults and children.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV infection)**,
with **0 clinical trials** and **1 animal study publication** currently supporting this direction.
It is important to note at the outset that this top-ranked predicted indication is a **veterinary condition affecting domestic cats**, not a human disease, which substantially limits its direct relevance for UK healthcare professionals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Abacavir is a carbocyclic nucleoside analogue that is intracellularly phosphorylated to carbovir triphosphate, which competes with deoxyguanosine triphosphate and terminates HIV reverse transcription. Its efficacy in HIV-1 infection is well-proven, and it is commonly co-formulated with lamivudine (Kivexa) or with lamivudine and dolutegravir (Triumeq).

Feline Immunodeficiency Virus (FIV) and HIV-1 share the same viral family (Retroviridae, genus Lentivirus) and depend on reverse transcriptase for their replication cycle. This mechanistic parallel provides a scientifically coherent basis for the TxGNN model to predict cross-species NRTI activity: if Abacavir can competitively inhibit HIV-1 reverse transcriptase, analogous inhibition of FIV reverse transcriptase is structurally plausible. The single supporting in vitro study (PMID 11684314) confirms that the ZDV + 3TC + ABC triple combination suppresses FIV replication in cell culture, consistent with this rationale.

However, this remains a preclinical, veterinary observation. FIV infection in cats has historically served as a non-human primate-free surrogate model for studying lentiviral drug interactions and resistance; it does not in itself constitute a human therapeutic opportunity. Any meaningful clinical development path would need to pivot to a directly analogous human indication — most obviously HIV-2 infection or SHIV/SIV-related considerations in occupational post-exposure prophylaxis research — both of which are addressed in the second-ranked TxGNN prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Abacavir in feline acquired immunodeficiency syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Animal Study (In Vitro, Cat Model) | Antiviral Research | Triple NRTI combination of ZDV + 3TC + Abacavir (ABC) demonstrated suppression of FIV replication in vitro, supporting the domestic cat as a model organism for studying HIV drug interactions and resistance; confirms cross-lentivirus NRTI activity in principle |

---

## UK Market Information

No MHRA marketing authorisations are recorded for Abacavir in the current Evidence Pack data.

> **Note for clinicians:** This data gap warrants verification. Abacavir is a long-established antiretroviral agent in widespread clinical use for HIV infection. Prescribing information, including UK SmPCs and BNF Section 5.3.1 (*HIV infection*), should be consulted directly via the Electronic Medicines Compendium (eMC) and the NICE BNF. The apparent absence of licensing records in this dataset likely reflects an upstream data extraction issue rather than a genuine absence of authorisation.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, and drug–drug interactions) are not available in this Evidence Pack.

> Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Critical safety note for clinicians:** Although not captured in the current data extract, Abacavir carries a well-characterised risk of potentially life-threatening hypersensitivity reactions. **Screening for the HLA-B\*5701 allele is mandatory before initiation** in accordance with MHRA guidance and BHIVA guidelines. This must be factored into any future development programme or clinical use consideration, regardless of indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction for Abacavir is a veterinary disease (Feline Acquired Immunodeficiency Syndrome) that falls outside the remit of human medicine; the sole supporting evidence is a single in vitro animal study from 2002, yielding only L4 (preclinical) evidence with no registered clinical trials and no human data.

**To proceed, the following is needed:**

- **Redirect repurposing target**: Evaluate the second-ranked TxGNN prediction (Simian Immunodeficiency Virus infection, score 99.79%) as a stepping stone towards clinically relevant human lentiviral indications, particularly **HIV-2 infection** and its implications for post-exposure prophylaxis
- **MOA data retrieval**: Query the DrugBank API (DB01048) to formally document Abacavir's mechanism of action for inclusion in a complete mechanistic rationale
- **Regulatory data reconciliation**: Investigate the missing MHRA licence data — cross-reference with the eMC, MHRA Product Licence Register, and BNF to restore accurate UK market status
- **Safety data completion**: Retrieve the full SmPC including Section 4.3 (Contraindications), Section 4.4 (Special warnings), and Section 4.5 (Drug interactions), with particular attention to the HLA-B\*5701 hypersensitivity risk and abacavir–methadone interaction
- **Veterinary pathway clarification**: If any FIV-related research utility is intended, route enquiries to the Veterinary Medicines Directorate (VMD) rather than MHRA; this is outside the scope of a standard drug repurposing evaluation for human healthcare
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

