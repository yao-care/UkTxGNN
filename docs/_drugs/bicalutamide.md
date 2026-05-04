---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

---

## One-Sentence Summary

Bicalutamide is a non-steroidal anti-androgen and competitive antagonist of the androgen receptor (AR), established in oncology practice as an androgen deprivation therapy for prostate cancer.
The TxGNN model predicts it may have therapeutic utility in **Hypertrichosis**, with **no registered clinical trials** and **1 expert commentary** currently available to support this direction.

> **Note to reader:** Hypertrichosis represents the highest TxGNN-ranked prediction in this evidence pack. However, the strongest clinical evidence across all ten predictions belongs to **Female Breast Carcinoma** (Rank 9; 1 Phase 2 trial, 20 publications; Evidence Level L2 — summarised in the Conclusion section). Clinicians may wish to prioritise a separate repurposing evaluation for that indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (established pharmacological use; no MHRA authorisation identified in current dataset — direct verification recommended) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| UK Market Status | Not captured in current dataset (probable data gap — see UK Market Information) |
| Number of Marketing Authorisations | 0 identified (MHRA database verification required) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bicalutamide competitively blocks androgen binding to the androgen receptor (AR), preventing downstream transcriptional activation in AR-expressing tissues. Although formal mechanism of action data were not captured by the DrugBank pipeline in this evidence pack, bicalutamide's pharmacology is well characterised from its use in prostate cancer: it attenuates androgen-driven cellular proliferation without reducing circulating androgen levels.

Hypertrichosis — pathological excess hair growth beyond what is normal for a patient's age, sex, or ethnic background — can in certain forms be driven or amplified by androgenic stimulation of hair follicles. In principle, AR blockade may reduce androgen-dependent follicular over-activation. The specific clinical context captured in the available literature concerns **minoxidil-induced hypertrichosis**: an unwanted side effect arising in women treated with minoxidil for female pattern hair loss (androgenetic alopecia). Here, bicalutamide's AR antagonism may partially counteract minoxidil's non-selective stimulation of hair follicles across body sites, offering a mechanistically coherent but off-label management strategy.

It is important to note that this represents an **off-target application**. The rationale applies only to androgen-sensitive forms of hypertrichosis and does not extend to congenital or genetic subtypes (such as Ambras syndrome or isolated hair shaft disorders), where the pathology is unrelated to androgen excess or AR activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter / Expert Comment | Journal of the American Academy of Dermatology | Expert commentary responding to a retrospective review of 35 patients; discusses the potential of bicalutamide to improve minoxidil-induced hypertrichosis in women treated for female pattern hair loss |

---

## UK Market Information

No MHRA marketing authorisations for bicalutamide have been identified in the current dataset. This is almost certainly a **data pipeline gap** rather than a genuine absence of UK authorisation — bicalutamide (brand name **Casodex**, AstraZeneca) is a well-established androgen deprivation agent with longstanding international approval for prostate cancer, including historic MHRA authorisation.

Clinicians should verify current authorisation status directly via:
- [MHRA Products database](https://products.mhra.gov.uk/)
- [BNF — Bicalutamide (NICE/BNF)](https://bnf.nice.org.uk/drugs/bicalutamide/)

---

## Cytotoxicity

Bicalutamide is an antineoplastic agent (androgen deprivation therapy for prostate cancer) and meets the threshold for inclusion of this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted hormonal therapy — Non-steroidal anti-androgen (Androgen Receptor Antagonist); **not** a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Low — bicalutamide is not associated with clinically significant myelosuppression |
| Emetogenicity Classification | Minimal |
| Monitoring Items | Liver function tests (LFTs) at baseline and at regular intervals; full blood count (FBC) to detect anaemia; blood glucose in patients with diabetes |
| Handling Protection | Standard oral tablet precautions apply; cytotoxic handling regulations (e.g., dedicated preparation facilities, PPE) are not routinely required for this agent |

---

## Safety Considerations

Formal safety data (MHRA SmPC warnings, contraindications, and drug interaction records) were not captured in this evidence pack. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Notable Additional Prediction — Female Breast Carcinoma (Rank 9)

Although outside the primary scope of this report, the following prediction carries substantially stronger clinical evidence and merits attention:

| Indication | TxGNN Score | Evidence Level | Clinical Trials | Publications | Decision |
|-----------|-------------|---------------|----------------|-------------|---------|
| Female Breast Carcinoma | 99.11% | L2 | 1 (Phase 2) | 20 | Proceed with Guardrails |

**Mechanistic basis:** AR is widely expressed in breast cancer — approximately 70–90% of ER-positive tumours and 40–70% of the **Luminal Androgen Receptor (LAR) subtype of triple-negative breast cancer (TNBC)**. Bicalutamide inhibits AR-driven tumour cell proliferation, suppresses AR-mediated β-catenin transcriptional activity, may trigger ferroptosis in AR-positive TNBC cells (in combination with ERK inhibitors), and has been shown preclinically to enhance standard chemotherapy sensitivity.

**Clinical evidence highlights:**

| Trial / Publication | Details |
|--------------------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) — Phase 2 | Nivolumab + Bicalutamide + Ipilimumab in metastatic HER2-negative breast cancer; n=30; Active, not recruiting (data pending) |
| [PMID 24888812](https://pubmed.ncbi.nlm.nih.gov/24888812/) | Case report: complete response in metastatic AR-positive breast cancer treated with bicalutamide |
| [PMID 40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 systematic review: anti-androgen therapy (bicalutamide, enzalutamide, enobosarm) as precision therapy for AR-positive TNBC |
| [PMID 32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | Preclinical: bicalutamide inhibits proliferation and invasion of MDA-MB-231 TNBC cells |

A dedicated repurposing evaluation report for **Female Breast Carcinoma** is strongly recommended.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Hypertrichosis)*

**Rationale:**
The evidence base for bicalutamide in hypertrichosis comprises a single expert commentary (tier 3, no primary patient-level data), with no registered clinical trials. Although the AR-antagonist mechanism is biologically coherent for androgen-sensitive hypertrichosis (particularly minoxidil-induced hypertrichosis), the data are insufficient to support clinical repurposing at this stage.

**To proceed, the following is needed:**

- **MHRA authorisation verification:** Confirm UK licensing status via the MHRA Products database; populate the regulatory data fields in a future version of this evidence pack
- **Formal MOA data retrieval:** Query the DrugBank API to resolve the mechanism of action data gap (DG002)
- **Safety data retrieval:** Obtain and parse the MHRA SmPC to resolve the warnings/contraindications data gap (DG001), particularly relevant for use in non-oncology populations
- **Primary literature search:** Conduct a targeted PubMed search (`bicalutamide AND hypertrichosis`) and review any clinical case series or prospective observational data
- **Safety assessment for non-oncology use:** Evaluate risk–benefit profile in women of childbearing potential, given the teratogenic potential of anti-androgens
- **Separate repurposing report for Female Breast Carcinoma:** This is the highest-evidence prediction in the evidence pack (L2; 1 Phase 2 trial; 20 publications) and warrants a full standalone evaluation with a "Proceed with Guardrails" recommendation

---

*This report is generated for research purposes only. Findings are based on computational prediction and do not constitute a clinical recommendation. All repurposing candidates require prospective clinical validation before application. Suspected adverse reactions should be reported via the Yellow Card Scheme.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

