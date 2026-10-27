---
layout: default
title: Mycophenolate Mofetil
parent: Model Prediction Only (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mycophenolate Mofetil: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Mycophenolate mofetil"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "bone Paget disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "multiple sclerosis", "hemosiderosis", "Heiner syndrome", "African iron overload", "neonatal hemochromatosis"]
---

# Mycophenolate Mofetil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Mycophenolate Mofetil: From Transplant Immunosuppression to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Mycophenolate mofetil is an immunosuppressant that inhibits inosine monophosphate dehydrogenase (IMPDH). The TxGNN model predicts it may be effective for **HIV infectious disease**, with **4 clinical trials** (none yielding efficacy data) and **20 publications** currently linked to this direction. Evidence is limited and mostly indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 (as assigned in the compiled data; see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

*Note on evidence level: the L2 grading is not well supported by the trials listed. The only Phase 2 trials are a pilot of a different drug (DAPD) with MMF as an add-on arm, and a withdrawn study with no participants. The only randomised publication, in treatment-naive patients, is a small RCT from 2004. A more cautious reading is closer to L3.*

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the compiled data. However, the repurposing rationale describes MMF as an inhibitor of IMPDH, which depletes guanosine nucleotide pools. This limits lymphocyte proliferation, potentially reducing the pool of activated target cells for HIV. It may also potentiate nucleoside analogues such as abacavir and didanosine, by depleting intracellular deoxyguanosine triphosphate (dGTP).

The original indication is not recorded in the compiled data, so a direct comparison with HIV cannot be made. The mechanism is plausible, and small studies have explored it. Clinical antiviral benefit has not been established, and immunosuppression in people with HIV raises safety concerns.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn | 0 | Safety and antiviral activity of MMF added to abacavir in treatment-experienced HIV; directly relevant but no participants enrolled, so no data |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Placebo-controlled pilot of DAPD versus DAPD plus MMF added to anti-HIV regimens; MMF link is indirect |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine and MMF versus cyclophosphamide and prednisolone in anti-erythropoietin pure red cell aplasia; HIV link is tangential and the trial was too small to inform |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Stem cell transplant for HIV-positive patients using cyclosporine and MMF after conditioning; not an evaluation of MMF for HIV |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | RCT | AIDS | HAART with or without MMF in treatment-naive HIV-1 patients; effect on plasma HIV-1 RNA decay and latent reservoir |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD study | Clin Pharmacokinet | Pharmacokinetics of low-dose MMF with abacavir, efavirenz and nelfinavir; therapeutic drug monitoring recommended |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Clinical study | AIDS Res Hum Retroviruses | No detrimental immunological effects of MMF with HAART in treatment-naive patients |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Pilot (5 patients) | J Acquir Immune Defic Syndr | Adding MMF to abacavir-containing regimens was associated with dGTP depletion and a fall in plasma HIV-1 RNA |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Immunosuppressive drugs in HIV disease, targeting immune activation alongside HAART |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | Virostatics as a means of targeting HIV infection |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Preclinical / ex vivo | J Clin Invest | Antiproliferative drugs selectively target HIV-infected CD4+ T-cell clones |
| [20840478](https://pubmed.ncbi.nlm.nih.gov/20840478/) | 2010 | Retrospective study | Am J Transplant | Kidney transplantation in HIV-infected patients using MMF-based immunosuppression (27 patients) |
| [39396546](https://pubmed.ncbi.nlm.nih.gov/39396546/) | 2025 | Case report | Trop Doct | IgA vasculitis in an HIV patient treated with steroid and MMF |
| [19112763](https://pubmed.ncbi.nlm.nih.gov/19112763/) | 2008 | Case report | J Drugs Dermatol | Psoriasis and psoriatic arthritis in an HIV patient treated safely with MMF |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0802010M0AAABAB | Mycophenolate Mofetil Tab 500mg | Tablet (not stated in the data) | Not stated in the data |

Only one authorisation is recorded, and its indication text and dosage form are not available in the compiled data. Please check the SmPC and BNF for the licensed indications.

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** the TxGNN knowledge graph links MMF to a range of conditions, including liver disease, active peptic ulcer disease, neutropenia, agranulocytosis, aplastic anaemia, cytomegalovirus infection, herpes simplex and herpes zoster infection, progressive multifocal leukoencephalopathy, lymphoma, and skin cancer. These should be confirmed against the SmPC.

**Drug Interactions:** 92 interactions were identified in total. Examples include:
- **Major:** activated charcoal
- **Moderate:** proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, rabeprazole, dexlansoprazole), antacids (aluminium hydroxide, magnesium oxide, calcium carbonate), and antibiotics (amoxicillin, clarithromycin, doxycycline, tetracycline, minocycline, vancomycin)
- **Minor:** zinc salts and iron

Interactions with antiretrovirals such as abacavir would need specific review for any HIV use.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and early studies explored MMF alongside antiretrovirals. However, the only directly relevant interventional trial was withdrawn, the one randomised publication dates from 2004, and no study has established clinical antiviral benefit. Immunosuppression in HIV adds safety concerns, and warnings and contraindications for the UK product are not available.

**To proceed, the following is needed:**
- Retrieval of the SmPC and BNF safety information (a blocking gap for safety screening)
- The original licensed indication and dosage form for the UK authorisation
- Detailed mechanism-of-action data
- A review of whether modern, well-powered controlled data exist for MMF in HIV
- A specific interaction and safety plan for use with current antiretroviral regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

