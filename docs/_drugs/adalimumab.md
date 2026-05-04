---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab is a fully human anti-tumour necrosis factor-alpha (anti-TNF-α) monoclonal antibody (IgG1), most widely used in the treatment of rheumatoid arthritis and related inflammatory conditions.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** — a severe systemic extra-articular complication of rheumatoid arthritis characterised by immune-mediated blood vessel inflammation —
with **5 clinical trials** and **20 publications** currently identified in support of this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis (and other TNF-α-mediated inflammatory diseases) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| UK Market Status | Data not recorded in current Evidence Pack |
| Number of Marketing Authorisations | 0 recorded (data gap — see UK Market Information section) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the repurposing rationale and published literature, adalimumab is a fully human IgG1 monoclonal antibody that selectively neutralises both soluble and transmembrane forms of TNF-α, preventing binding to its p55 and p75 cell surface receptors. This leads to suppression of downstream NF-κB activation, reduced secretion of pro-inflammatory cytokines (IL-1β, IL-6), and downregulation of endothelial adhesion molecules including ICAM-1 and E-selectin — all of which are mechanistically relevant to the pathogenesis of vasculitis.

In rheumatoid vasculitis (RV) — affecting an estimated 1–5% of patients with longstanding, seropositive RA — TNF-α plays a central pathogenic role in immune complex deposition, neutrophil infiltration of vessel walls, and complement-mediated endothelial injury. Blockade of TNF-α directly targets these mechanisms, providing a clear biological rationale for the TxGNN prediction. RV and RA share the same immunological underpinnings, and controlling the systemic TNF-α-driven inflammatory milieu may simultaneously suppress vasculitic progression. A 2021 PRISMA-compliant systematic review (PMID 33058033) confirmed that biological agents — including TNF-α inhibitors — are increasingly incorporated into the management of rheumatoid vasculitis, lending clinical plausibility to the model's output.

An important safety caveat must be acknowledged before proceeding: several published case reports document adalimumab itself inducing drug-related vasculitis, including leukocytoclastic vasculitis (PMID 28719435) and ANCA-associated nephritis (PMID 19482531). When considering adalimumab in the setting of established rheumatoid vasculitis, clinicians must carefully distinguish between potential therapeutic benefit and the rare but recognised risk of drug-induced vasculitic reactions. Baseline serological screening (ANA, ANCA, complement, anti-dsDNA) and close renal monitoring are therefore essential.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional observational study of biologic DMARD treatment patterns and demographics in RA patients in China; no vasculitis-specific endpoint designed |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional multinational study of tocilizumab in RA patients with inadequate response to prior DMARDs or biologics; real-world safety and efficacy data, no vasculitis endpoint |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large registry evaluating incident IMID risk in patients treated with biologics and immunosuppressants; provides indirect immunomodulation safety context for adalimumab but is not a vasculitis efficacy study |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Assessment of immunosuppressant management around elective total shoulder arthroplasty in rheumatology patients; no direct relevance to vasculitis treatment |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | Retrospective real-world safety study of brolucizumab in neovascular AMD; no relevance to rheumatoid vasculitis — identified as database retrieval noise |

> **Note:** No clinical trials specifically designed to evaluate adalimumab in rheumatoid vasculitis were identified. All five retrieved trials carry low direct relevance (all graded C). This is a critical evidence gap for formal repurposing.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-compliant systematic review of biological therapy in rheumatoid vasculitis; confirms TNF-α inhibitors are used therapeutically in the management of RV |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | 15-year RA patient with RA-associated digital vasculitis (necrotising fingertip ulcers) showed marked response to adalimumab after failure of conventional therapy |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis in a patient with rheumatoid vasculitis arose 8 months after adalimumab dose reduction; highlights the importance of maintaining TNF-α blockade for vasculitis control |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Narrative Review | Journal of Clinical Medicine | Review of RA-associated episcleritis and scleritis (ocular vasculitic manifestations); discusses the role of biologics including TNF-α inhibitors in management |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Pharmacoepidemiology Cohort | RMD Open | BSRBR-RA registry analysis comparing the risk of vasculitis-like events (VLEs) in TNFi-treated versus non-biological DMARD-treated RA patients; characterises drug-specific risk profiles |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report (Adverse Event) | American Journal of Dermatopathology | First reported case of leukocytoclastic vasculitis with dermal perivascular haemophagocytosis attributable to adalimumab in RA; critical drug-induced vasculitis safety signal |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | ANCA-associated nephritis during concurrent abatacept and adalimumab therapy for RA; tocilizumab achieved resolution — highlights renal vasculitic risk with biologic combination |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Case Report | Nephrologie & Therapeutique | ANCA-associated extracapillary necrotising glomerulonephritis arising during adalimumab therapy for RA; important early drug-induced vasculitis safety signal |
| [23559388](https://pubmed.ncbi.nlm.nih.gov/23559388/) | 2013 | Case Report + Literature Review | Clinical Rheumatology | First reported case of adalimumab-associated antiphospholipid syndrome; includes a review of adalimumab-induced vasculitis and APS in the published English literature |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | Case Report | Clinical and Experimental Rheumatology | Systemic rheumatoid vasculitis refractory to multiple drugs including anti-TNF agents successfully treated with humanised anti-IL-6 receptor antibody; contextualises management of treatment-resistant RV |

---

## UK Market Information

No MHRA marketing authorisation data is recorded in the current Evidence Pack (recorded licences: 0; market status: not recorded). This represents a data gap and does not reflect the actual regulatory position of adalimumab in the United Kingdom.

> **For clinical reference:** Adalimumab is approved and widely available in the UK as the originator product Humira® (AbbVie) and numerous MHRA-authorised biosimilars, including Amgevita, Hyrimoz, Imraldi, Idacio, Hadlima, Yuflyma, and Hukyndra. UK-authorised indications include rheumatoid arthritis, psoriatic arthritis, axial spondyloarthritis (ankylosing spondylitis and non-radiographic), Crohn's disease, ulcerative colitis, plaque psoriasis, hidradenitis suppurativa, non-infectious uveitis, and juvenile idiopathic arthritis. Prescribers should consult the relevant SmPC and the current BNF (Chapter 10.1.3 — Drugs affecting the immune response) for full and up-to-date prescribing information. Suspected adverse reactions should be reported via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Specific safety alert from this Evidence Pack:** Multiple case reports within the retrieved literature document adalimumab-associated vasculitic adverse events, including leukocytoclastic vasculitis (PMID 28719435), ANCA-associated nephritis (PMID 19482531, PMID 36418100), and antiphospholipid syndrome (PMID 23559388). When evaluating adalimumab specifically for rheumatoid vasculitis, clinicians should ensure baseline and ongoing monitoring includes: ANA and ANCA titres, renal function and urinalysis (for haematuria/proteinuria), full blood count with differential, complement levels (C3/C4), and clinical surveillance for new or evolving cutaneous vasculitic lesions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Rheumatoid vasculitis shares its immunological foundations with rheumatoid arthritis, and TNF-α blockade via adalimumab provides a mechanistically coherent approach; a published systematic review confirms biologics including TNF-α inhibitors are used in RV management. However, no dedicated randomised controlled trial exists, evidence is confined to observational studies and case series (Evidence Level L3), and adalimumab paradoxically carries a recognised risk of inducing drug-related vasculitis — necessitating careful patient selection, baseline serological profiling, and structured monitoring.

**To proceed, the following is needed:**

- **Correct the UK regulatory data gap** — the current Evidence Pack records zero MHRA marketing authorisations, which must be resolved before any clinical application or commissioning discussion
- **Dedicated prospective registry or observational study** in established rheumatoid vasculitis with prespecified vasculitic endpoints (e.g., Birmingham Vasculitis Activity Score, biopsy-confirmed remission, skin ulcer healing rate)
- **Formal pharmacovigilance analysis** to characterise the benefit–risk balance: therapeutic suppression of RV versus the risk of adalimumab-induced vasculitis — patient-level predictors of each outcome should be identified
- **Mechanism of action data from DrugBank** (flagged as a data gap in this Evidence Pack; severity: High)
- **MHRA/NICE review** to determine whether rheumatoid vasculitis falls within or outside the current commissioning framework for adalimumab (refer to NICE TA130 and successor technology appraisals, and the NHS England Commissioning Policy for biological DMARDs in inflammatory arthritis)
- **Standardised baseline screening protocol** prior to any trial initiation: ANA, ANCA (MPO/PR3), complement C3/C4, anti-dsDNA, renal function, urinalysis, and chest X-ray (for latent tuberculosis per current SmPC requirements)
- **Specialist MDT input** from rheumatology, nephrology, and dermatology given the multi-system nature of rheumatoid vasculitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

