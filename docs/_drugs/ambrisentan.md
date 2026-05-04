---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to PAH Associated With Congenital Heart Disease

## One-Sentence Summary

Ambrisentan is a selective endothelin type-A (ETA) receptor antagonist licensed internationally for pulmonary arterial hypertension (PAH), though it currently holds no MHRA marketing authorisation in the United Kingdom.
The TxGNN model identifies multiple WHO Group 1 PAH subtypes as high-priority candidates; the most clinically actionable prediction is **PAH associated with congenital heart disease (CHD-PAH)**, with a prediction score of **99.37%**, supported by **9 clinical trials** and **18 publications**.
Two further PAH subtypes — connective tissue disease-associated PAH (CTD-PAH) and HIV-associated PAH — independently reach L1 evidence with a "Proceed with Guardrails" recommendation, all sharing the same ET-1/ETA mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (idiopathic/heritable; licensed in US/EU but **not currently MHRA-authorised**) |
| Predicted New Indication | PAH Associated with Congenital Heart Disease (CHD-PAH / Eisenmenger Syndrome) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L1 |
| UK Market Status | Not marketed |
| Number of MHRA Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published literature, Ambrisentan is a highly selective oral ETA receptor antagonist. Endothelin-1 (ET-1) is a potent vasoconstrictor and mitogen that drives pulmonary arterial smooth muscle cell proliferation and progressive vascular remodelling. By selectively blocking ETA receptors while largely preserving ETB-mediated ET-1 clearance and endothelial prostacyclin release, Ambrisentan reduces pulmonary vascular resistance (PVR), lowers right ventricular afterload, and improves exercise capacity. This selectivity is thought to confer advantages over non-selective ERA agents in certain PAH subpopulations.

CHD-PAH — most severely expressed as Eisenmenger syndrome — belongs to WHO Group 1 PAH and shares the same core ET-1/ETA-driven pathobiology as idiopathic PAH. Chronic left-to-right cardiac shunting subjects the pulmonary vasculature to sustained excess pressure and flow, triggering endothelial dysfunction, ET-1 upregulation, and progressive arterial remodelling that is histologically indistinguishable from idiopathic PAH. ET-1 plasma levels are markedly elevated in Eisenmenger syndrome and correlate directly with disease severity and prognosis. The ESC/ERS 2022 PAH guidelines accordingly assign ERA therapy a Class I recommendation in Eisenmenger syndrome, confirming mechanistic coherence across Group 1 subtypes.

The clinical evidence directly supports this extrapolation. A prospective cohort study at Columbia University (Zuckerman et al., 2011, PMID 21371683) demonstrated haemodynamic and functional improvements specifically with Ambrisentan in Eisenmenger syndrome patients. A 2019 systematic review and meta-analysis (Li et al., PMID 31096477) confirmed the benefit of PAH-specific targeted therapy in ES. Additionally, Phase 3 Chinese PAH trial data (NCT01808313, n=134) — in which CHD-PAH constitutes a major subgroup — and long-term paediatric extension data (NCT01342952) provide further supportive evidence. The high TxGNN score therefore reflects genuine mechanistic and clinical plausibility.

**Note on the top-ranked TxGNN prediction (Rank 1: Pulmonary Arteriovenous Malformation, score 99.41%):** PAVM is primarily a structural anatomical abnormality treated by vascular embolisation rather than pharmacotherapy. The single case report identified (PMID 33969094) describes PAH arising as a complication of hereditary haemorrhagic telangiectasia (HHT), wherein ETA antagonism may address the PAH component but exerts no effect on the PAVM itself. This prediction is rated **Hold (L4)** and does not constitute a meaningful repurposing candidate; the CHD-PAH and CTD-PAH predictions are substantially more actionable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01808313](https://clinicaltrials.gov/study/NCT01808313) | Phase 3 | Completed | 134 | Open-label, single-arm, multicentre study in Chinese PAH patients; 12-week primary evaluation of Ambrisentan 5 mg on 6MWT; CHD-PAH is highly prevalent in Chinese PAH cohorts, making this a key direct efficacy data source |
| [NCT01342952](https://clinicaltrials.gov/study/NCT01342952) | Phase 2 | Completed | 38 | Long-term open-label extension in paediatric PAH (ages 8–18); CHD is the leading cause of paediatric PAH; follow-up until age 18 or product approval, providing long-term safety and tolerability data in a CHD-predominant population |
| [NCT01332331](https://clinicaltrials.gov/study/NCT01332331) | Phase 2 | Terminated | 41 | Randomised open-label dose-comparison (weight-adjusted high vs low dose) in paediatric PAH; terminated early, limiting statistical power, but supplies dose-exploration and safety data relevant to paediatric CHD-PAH prescribing |
| [NCT01884675](https://clinicaltrials.gov/study/NCT01884675) | Phase 3 | Terminated | 33 | Randomised double-blind placebo-controlled study of Ambrisentan in inoperable CTEPH; terminated early — an important safety signal indicating that Ambrisentan is **not** appropriate for fibrotic lung disease or Group 3 PH |
| [NCT01894022](https://clinicaltrials.gov/study/NCT01894022) | Phase 3 | Terminated | 19 | Open-label long-term extension of the CTEPH trial; terminated after parent study was discontinued; contributes limited long-term safety data |
| [NCT04095286](https://clinicaltrials.gov/study/NCT04095286) | Phase 1 | Completed | 29 | Relative bioavailability crossover study comparing a lower-dose dispersible paediatric Ambrisentan formulation with the marketed tablet in healthy adults; supports development of age-appropriate dosing for paediatric CHD-PAH |
| [NCT02688387](https://clinicaltrials.gov/study/NCT02688387) | Phase 1 | Completed | 112 | PK and relative bioavailability study of fixed-dose Ambrisentan + Tadalafil combination tablets; pharmacological foundation for the dual combination therapy used widely in CHD-PAH and Eisenmenger syndrome |
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Iloprost (not Ambrisentan) in adult Eisenmenger syndrome patients; provides comparative safety and efficacy context for the CHD-PAH treatment landscape |
| [NCT00593905](https://clinicaltrials.gov/study/NCT00593905) | N/A | Withdrawn | 0 | Pharmacogenomics study of ERA efficacy/toxicity in PAH; withdrawn before enrolment — no direct contribution to efficacy data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Comprehensive review of PAH diagnosis and treatment; confirms ERAs (including Ambrisentan) as first-line therapy for WHO Group 1 PAH; PAH prevalence approximately 10.6 cases per million adults in the US |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic Review / Meta-analysis | Medicine | Systematic review and meta-analysis of PAH-specific drug therapy in Eisenmenger syndrome; ERA and other PAH-targeted agents improve WHO functional class and exercise capacity in ES |
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | Prospective Clinical Study | Am J Cardiology | Ambrisentan in consecutive Eisenmenger syndrome patients at Columbia University (2007–2008); demonstrated improvements in resting and exercise haemodynamics and functional status — direct evidence specifically for CHD-PAH |
| [34921523](https://pubmed.ncbi.nlm.nih.gov/34921523/) | 2022 | Clinical Study | Pediatric Pulmonology | Real-world safety and tolerability of Ambrisentan + Tadalafil combination in paediatric pulmonary hypertension; generally well tolerated, supporting combination use in paediatric CHD-PAH |
| [41727855](https://pubmed.ncbi.nlm.nih.gov/41727855/) | 2025 | Review | Frontiers in Pediatrics | ET-1 pathobiology in failing Fontan circulation; directly demonstrates how ET-1 axis drives pulmonary vascular injury in complex single-ventricle CHD, reinforcing the mechanistic rationale for ETA antagonism |
| [22104452](https://pubmed.ncbi.nlm.nih.gov/22104452/) | 2011 | Cohort / Registry | Postgraduate Medicine | Texas Adult Congenital Heart Program: characterises disease burden and treatment patterns in adults with CHD-PAH; underscores clinical need for targeted PAH therapy in this population |
| [18333354](https://pubmed.ncbi.nlm.nih.gov/18333354/) | 2007 | Review | Romanian J Intern Med | Management of CHD-PAH including Eisenmenger syndrome; ERA therapy established as part of standard care, with approximately 30% of unrepaired shunt patients progressing to pulmonary vascular disease |
| [28348949](https://pubmed.ncbi.nlm.nih.gov/28348949/) | 2017 | Case Report | Respir Med Case Reports | Adult Eisenmenger syndrome patient achieving meaningful clinical improvement with advanced PAH therapies including ERA; illustrates real-world benefit in a severe and historically undertreated condition |
| [38447536](https://pubmed.ncbi.nlm.nih.gov/38447536/) | 2024 | Case Report | Kidney Blood Pressure Res | Cyanotic nephropathy as a systemic complication of Eisenmenger syndrome; highlights the importance of targeted PAH management to mitigate multi-organ consequences |
| [41868707](https://pubmed.ncbi.nlm.nih.gov/41868707/) | 2026 | Case Series | Respir Med Case Reports | Sotatercept (activin signalling inhibitor) in severe refractory corrected complex CHD-PAH; illustrates the emerging role of combination and salvage strategies in CHD-PAH, and the unmet need in refractory disease |

---

## UK Market Information

Ambrisentan currently holds **no MHRA marketing authorisation** and is not listed as commercially available in the United Kingdom based on the data in this evidence pack (0 licences on record).

> **Note for UK clinicians:** Ambrisentan is authorised by the European Medicines Agency as **Volibris** (5 mg and 10 mg film-coated tablets; originally GSK, later AstraZeneca) for WHO functional class II–III PAH. Post-Brexit, this EMA authorisation no longer automatically applies in Great Britain. Prescribers seeking access in the UK should consider:
>
> - **MHRA Unlicensed Medicines (Specials) framework** — named patient supply via a licensed Specials manufacturer or importer
> - **'Apply for a licence' pathway** — a formal MHRA marketing authorisation application, potentially via a reliance route based on the existing EMA approval
> - **Existing NICE technology appraisals** for the ERA drug class in PAH (refer to current BNF section 2.5.1.2, Pulmonary arterial hypertension, and relevant NICE guideline NG191 for PAH) — these may inform formulary decisions pending a formal licence
>
> Any prescribing outside a marketing authorisation carries prescriber responsibility under General Medical Council guidance, and patients should be informed accordingly.

---

## Safety Considerations

No UK-specific SmPC warnings, contraindications, or drug interaction data were available in this evidence pack.

Please refer to the **European SmPC for Volibris (ambrisentan)** and the **BNF** for complete prescribing information. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

Key safety signals identified from clinical trial evidence within this pack:

- **Teratogenicity**: ERA agents carry a serious teratogenicity risk (contraindicated in pregnancy, Pregnancy Prevention Programme required per EMA). This must be communicated to all women of childbearing potential prior to prescribing.
- **Hepatotoxicity**: The ERA drug class is associated with aminotransferase elevations. The VOLT post-marketing registry (PMID 27282418, n=702) was specifically designed to characterise the incidence of LFT elevations >3× ULN. Baseline and regular hepatic function monitoring is required.
- **Contraindication in pulmonary fibrosis / Group 3 PH**: The Phase 3 CTEPH trial (NCT01884675) was terminated early after safety signals emerged in patients with fibrotic lung disease. Ambrisentan must **not** be used in Group 3 PH (PH due to lung disease/hypoxia) or interstitial lung disease-associated PAH.
- **Fluid retention and oedema**: ERA class effect; monitor carefully in CHD patients with compromised cardiac reserve or renal impairment.
- **Drug interaction — ciclosporin**: Ciclosporin significantly elevates Ambrisentan plasma concentrations via P-glycoprotein inhibition; dose adjustment required. Relevant for post-transplant CHD patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CHD-PAH and idiopathic PAH share the same ET-1/ETA-driven vascular pathobiology, and ERA therapy receives Class I recommendation (ESC/ERS 2022) for Eisenmenger syndrome. Direct prospective clinical data with Ambrisentan in Eisenmenger syndrome, Phase 3 trial data in Asian PAH cohorts with high CHD-PAH prevalence, and a supporting systematic review/meta-analysis collectively constitute L1 evidence. Ambrisentan is already EMA-authorised as Volibris, providing a clear regulatory precedent and reducing the evidentiary burden for UK access routes. Two further high-evidence indications — CTD-PAH (L1, 3 clinical trials, 19 publications, ARIES-1/2 and AMBITION subgroup data) and HIV-PAH (L1, Phase 3 RCT NCT00709956) — further strengthen the case for UK access across the PAH spectrum.

**To proceed, the following is needed:**

- **Confirm UK availability status**: Verify whether Volibris retains a valid MHRA (or Great Britain) licence post-Brexit, or whether a fresh application or Specials route is required
- **Retrieve full SmPC safety data**: Obtain MHRA/EMA SmPC including teratogenicity warnings, contraindication list (ILD, pregnancy), hepatotoxicity monitoring requirements, and complete drug interaction profile
- **Complete mechanistic dossier**: Retrieve full DrugBank (DB06403) mechanism of action data to strengthen the regulatory-facing evidence pack
- **Define eligible patient population**: CHD-PAH must be WHO Group 1 confirmed by right heart catheterisation; exclude patients with ILD, fibrotic lung disease, or Group 3 PH
- **Establish safety monitoring protocol**: LFTs at baseline and monthly for the first 3 months, then quarterly; pregnancy test and contraception counselling before initiation
- **Explore NICE submission pathway**: Current PAH appraisals (NG191) may require updating to include Ambrisentan specifically for CHD-PAH/Eisenmenger syndrome, particularly given there are currently no MHRA-licensed ERAs filling this UK gap
- **Consider registry enrolment**: UK CHD-PAH patients initiated on Ambrisentan via Specials or compassionate use should be enrolled in a prospective registry (e.g., NHS Digital or BPH registry) to generate UK-specific real-world evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

