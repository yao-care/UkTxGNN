---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

---

## One-Sentence Summary

Ritonavir is a competitive HIV-1 aspartate protease inhibitor, originally developed and used for the treatment of HIV-1 infection in humans, typically as a pharmacokinetic booster within combination antiretroviral regimens. The TxGNN model predicts it may have antiviral activity against **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **12 publications** — predominantly in vitro susceptibility assays and non-human primate (NHP) studies — currently supporting this direction. This prediction carries strong mechanistic plausibility rooted in cross-lentiviral protease homology, but remains at the preclinical evidence stage with no direct human clinical applicability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (antiretroviral therapy / pharmacokinetic boosting) |
| Predicted New Indication | Simian immunodeficiency virus (SIV) infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| UK Market Status | Not marketed (no MHRA authorisation on record in this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory record for this evidence pack. Based on well-established pharmacological knowledge, Ritonavir is a competitive inhibitor of the HIV-1 viral aspartate protease (Ki ~1 nM), blocking the proteolytic cleavage of the Gag-Pol polyprotein precursor and preventing the maturation of infectious virions. It is also a potent inhibitor of CYP3A4 and P-glycoprotein, a property that underpins its widespread use as a pharmacokinetic booster in combination antiretroviral therapy.

The mechanistic basis for activity against SIV rests on the structural conservation of the aspartate protease across primate lentiviruses. The SIV protease shares approximately 48–57% amino acid sequence identity with HIV-1 protease, with the catalytic Asp25 residue preserved at the active site — the very residue that Ritonavir engages during competitive inhibition. This degree of homology provides a direct structural rationale for cross-reactivity. Multiple in vitro studies have confirmed that Ritonavir inhibits SIVmac239 replication, with an EC₅₀ of approximately 13 nM, which is broadly comparable to its anti-HIV-1 potency (EC₅₀ ~25 nM). Non-human primate studies further demonstrate that HAART regimens containing Ritonavir can achieve rapid and sustained viral suppression in SIV-infected macaques across a wide range of viral loads.

It is important to contextualise this prediction for clinical practice: SIV infection is a disease of non-human primates, most relevant as an animal model for HIV/AIDS research rather than a human clinical indication. The translational value of this finding lies primarily in its implications for primate virology research, NHP model design, and understanding cross-lentiviral antiviral pharmacology — not in representing a conventional repurposing candidate for human patients. The predicted IC₅₀ advantage for SIV over some other lentiviruses (e.g., FIV, where the homology is far lower at ~23%) reinforces the specificity and plausibility of this particular TxGNN prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro susceptibility assay | Antimicrobial Agents and Chemotherapy | Ritonavir inhibits SIVmac239 with EC₅₀ of 13 nM in a focal infectivity assay, compared to 25 nM for HIV-1; indinavir and saquinavir also active, confirming cross-reactivity of protease inhibitors across primate lentiviruses |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Comparative in vitro study | Antiviral Therapy | Systematic evaluation of 16 approved antiretrovirals (including Ritonavir) against HIV-2, SIVmac251, SIVb670, and SHIV strains; Ritonavir demonstrated antiviral activity across multiple lentiviral isolates, with implications for treatment and post-exposure prophylaxis |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study (NHP, in vivo) | Journal of Virology | Quadruple antiretroviral therapy including Ritonavir induced rapid viral decay in SIVmac251-infected cynomolgus macaques during a 7-day subcutaneous course; viral dynamics modelling demonstrated comparable biphasic decay kinetics to HIV-1 in humans |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Chimeric virus model | Microbes and Infection | Construction of a novel SHIV (SHIV-pr) bearing an HIV-1-derived protease gene; viral replication completely blocked by a protease inhibitor in vitro; animal inoculation confirmed replication competence, validating chimeric models for in vivo efficacy testing of protease inhibitors including Ritonavir |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal study (NHP, in vivo) | mBio | Contemporary ART regimens (including Ritonavir-boosted combinations) suppressed systemic viremia in both human and macaque lentivirus models, but failed to clear brain reservoirs; lentiviral RNA and integrated DNA detected in cerebral cortex regardless of ART duration, highlighting CNS penetration as a key limitation |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal study (NHP, in vivo) | PLoS ONE | Intensive cART (including Ritonavir) achieved viral suppression in SIV-infected Chinese rhesus macaques; adjunctive HDAC inhibitor (SAHA) did not significantly reduce the viral reservoir despite latency reversal, providing evidence for Ritonavir's role in suppressive backbone therapy |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal study (NHP, in vivo) | PLoS Pathogens | Highly intensified multidrug ART (including Ritonavir) induced long-term viral suppression in SIVmac251-infected macaques across a 10,000-fold range of baseline viraemia (10³–10⁷ RNA copies/mL); significant restriction of the viral reservoir was observed, establishing a reliable simian AIDS suppression model |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study (NHP, in vivo) | Journal of Virological Methods | Oral HAART (AZT + 3TC + Lopinavir/Ritonavir) administered for 28 days in SHIV(89.6P)-infected rhesus macaques; viral load reduction and CD8 T-cell subset modulation demonstrated, confirming oral route bioavailability and antiviral efficacy in NHP |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | In vitro biochemistry | Journal of Virology | Demonstrated intravirion processing of HIV-1 Vif by viral protease both in vivo and in vitro; Ritonavir used as a tool compound to confirm protease dependence of Vif cleavage, providing mechanistic insight into protease substrate breadth |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro antiviral screen | Antiviral Chemistry & Chemotherapy | Fluoroquinolone derivative K-12 active against multiple lentiviral strains including SIV and Ritonavir-resistant HIV-1; Ritonavir-resistant strains used as reference controls, confirming Ritonavir's distinct mechanism and resistance profile relative to transcription inhibitors |

---

## UK Market Information

No MHRA marketing authorisations are currently recorded for Ritonavir in this evidence pack dataset (total licences: 0).

> **Important note for UK healthcare professionals**: This dataset entry likely reflects a data gap rather than the true UK regulatory status. Ritonavir (Norvir®, AbbVie) holds established MHRA authorisation as a pharmacokinetic booster in HIV treatment regimens and is referenced in BNF Section 5.3.1 (Antivirals: HIV infection). It is also a component of nirmatrelvir/ritonavir (Paxlovid®), authorised for COVID-19 treatment. Clinicians should verify current authorisation status via the MHRA Product Licence Register and the current BNF edition. No licence currently exists for any veterinary or SIV-related indication.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug–drug interactions) are not available in this evidence pack. All safety fields are recorded as data gaps.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Critical prescriber alert**: Ritonavir is a potent inhibitor of CYP3A4 and P-glycoprotein and is associated with an exceptionally high number of clinically significant drug–drug interactions, including life-threatening interactions with certain sedatives, antiarrhythmics, lipid-lowering agents, and immunosuppressants. The absence of DDI data in this evidence pack constitutes a **blocking data gap** for any clinical safety assessment. Full DDI screening is mandatory before any consideration of use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Whilst the mechanistic and in vitro evidence supporting Ritonavir activity against SIV is scientifically credible — grounded in conserved aspartate protease homology and confirmed by quantitative susceptibility assays and NHP treatment models — SIV infection is a non-human primate disease with no direct human clinical application. This prediction is of value to primate research, HIV/AIDS animal model design, and lentiviral pharmacology, rather than representing a conventional repurposing candidate for NHS clinical implementation. Additionally, all safety data (warnings, contraindications, DDI) are absent from this evidence pack, precluding a complete S1 safety assessment.

**To proceed, the following is needed:**

- **Clarification of clinical intent**: Confirm whether this is being evaluated as a veterinary intervention (e.g., for SIV-infected captive primates), an NHP research tool compound, or as indirect evidence supporting HIV-1 drug class activity
- **MOA data**: Retrieve full mechanism of action from DrugBank API (DB00503) to complete pharmacological documentation
- **Safety pack**: Obtain SmPC warnings, contraindications, and full DDI profile — Ritonavir's CYP3A4 and P-gp inhibition profile is clinically critical
- **MHRA licence verification**: Confirm actual UK regulatory status via the MHRA Product Licence Register; resolve the discrepancy between the dataset (0 licences) and known authorised products (Norvir, Paxlovid)
- **Quantitative potency comparison**: Document Ritonavir IC₅₀/EC₅₀ values side-by-side for HIV-1, SIVmac, SHIV, and FIV to formally quantify the cross-species potency gradient and define a clinically meaningful activity threshold

---

*This report is generated for research reference purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before application. This document should be read alongside the current SmPC, BNF, and relevant NICE guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

