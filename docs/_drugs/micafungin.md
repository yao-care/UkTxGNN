---
layout: default
title: Micafungin
parent: Moderate Evidence (L3-L4)
nav_order: 413
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Micafungin"
predicted_indications: ["urinary tract infection (disease)"]
description: "Micafungin: predicted new indication Urinary tract infection (disease) (evidence level L3). Approved use: Not recorded in the local data"
---

# Micafungin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

## Micafungin: Urinary tract infection (disease)
{: .text-alpha }

## One-Sentence Summary

Micafungin is an echinocandin antifungal, originally used to treat oesophageal candidiasis, candidaemia and disseminated candidiasis.
The TxGNN model predicts it may be effective for **urinary tract infection (Candida UTI/candiduria)**,
with **no registered clinical trials** but **13 publications** (mostly case reports, case series and observational cohorts) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Urinary tract infection (disease) |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L3 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Micafungin is an echinocandin that inhibits 1,3-beta-D-glucan synthase, an enzyme essential for building the fungal cell wall. It is active against *Candida* species. Detailed mechanism of action data were not available in the data compiled for this report, so this description reflects the known pharmacology of the echinocandin class.

The original indications (candidaemia and disseminated candidiasis) involve the same pathogens that cause Candida urinary tract infection. A pharmacokinetic report (PMID 27424599) found that urinary micafungin levels were sufficient to treat Candida UTI, despite low renal excretion of the active drug. Case series, retrospective cohorts and paediatric data describe successful eradication of candiduria, including fluconazole-resistant and non-albicans strains such as *C. glabrata* and *C. krusei*.

There are important caveats. Echinocandins generally reach low urinary concentrations, the evidence is observational, and many cases of candiduria are asymptomatic and may not need antifungal treatment at all (PMID 29109159). Micafungin would be a niche option, for example where azole resistance or toxicity limits other choices, rather than a first-line agent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Cohort | Pediatr Int | Outcomes of micafungin for hospital-acquired Candida UTI in critically ill children in PICU; treatment success analysed by species |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Cohort | Int Urol Nephrol | Rates of candiduria elimination in hospitalised patients treated with micafungin |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Pharmacokinetic study | Int J Antimicrob Agents | Six UTI cases treated successfully; urinary micafungin levels sufficient against Candida spp. |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case series | Med Mycol Case Rep | Five patients treated with micafungin for at least 6 days; candiduria resolved within 30 days of completion |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Cohort | Antimicrob Agents Chemother | Multi-institutional study showing overtreatment of asymptomatic candiduria; guidelines advise against antifungals in this setting |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case report and review | Transpl Infect Dis | Chronic symptomatic *C. krusei* UTI eradicated with increased-dose micafungin in a liver and kidney transplant recipient |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case report | Front Pediatr | Micafungin for *C. glabrata* urinary infection in a premature neonate |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | Case report | J Pharm Health Care Sci | *C. glabrata* pyelonephritis and bacteraemia in a patient on an SGLT2 inhibitor, successfully treated with micafungin |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case report | Med Mycol Case Rep | Renal fungus ball due to *C. glabrata* treated with micafungin, endoscopic extraction and ureteral stent |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case report | Cureus | *Candida auris* UTI in a nursing home patient with multiple comorbidities |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0502040B0AAABAB (BNF-style product code; no PL number in the data) | Micafungin I/V infusion 50 mg vial (dry powder) | Powder for intravenous infusion | Not stated in the data compiled for this report |

Micafungin sits in the BNF antifungal section (chapter 5, infections). The data compiled for this report contain one valid single-ingredient product and no NICE-appraised indication details.

---

## Cytotoxicity

Micafungin is not an antineoplastic drug, so this section does not apply.

---

## Safety Considerations

- **Contraindications (TxGNN model associations, not label text)**: Kidney disease and pyoureter are linked to micafungin by the TxGNN model (deep learning); these associations may reflect similarities the model learned between related diseases, not biological evidence. This is relevant because UTI patients may have renal impairment or urinary obstruction, so clinical judgement and the SmPC are needed.
- **Drug Interactions** (5 moderate-level interactions recorded):
  - Amphotericin B
  - Nitisinone
  - Everolimus
  - Ribociclib
  - Sirolimus

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and a pharmacokinetic study plus several case series, cohorts and case reports show candiduria eradication, but there are no registered trials and the evidence is observational. Low urinary concentrations and the frequent lack of need to treat asymptomatic candiduria mean use should be restricted to selected cases.

**To proceed, the following is needed:**
- A prospective or randomised comparison against standard therapy (e.g. fluconazole, amphotericin B) in symptomatic Candida UTI
- Urinary pharmacokinetic and dosing data, ideally with therapeutic drug monitoring
- Clear patient selection criteria (symptomatic infection, azole-resistant species, upper tract or invasive disease) in line with antifungal stewardship
- Confirmation of the licensed UK indications and SmPC safety information
- A renal safety review given the knowledge-graph kidney disease contraindication signal

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

