---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 1
---

# Dapsone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the drug-repurposing evaluation report template to structure this Dapsone → Pneumocystosis evidence pack.

# Dapsone: From Leprosy to Pneumocystosis

## One-Sentence Summary

Dapsone is a sulfone antimicrobial classically used for leprosy (Hansen's disease) and dermatitis herpetiformis, with decades of established off-label use in Pneumocystis pneumonia prophylaxis. The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PCP), with **14 clinical trials** and **19 publications** currently supporting this direction — including three completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy (Hansen's disease); dermatitis herpetiformis *(per literature evidence — no formal UK/Taiwan licence text available in this evidence pack)* |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record for dapsone is not yet available in this evidence pack (data gap DG002). However, the mechanistic basis for its activity against Pneumocystis jirovecii is well characterised in the literature and is not merely a network-inference artefact. Dapsone is a sulfone, structurally related to the sulfonamides. It inhibits dihydropteroate synthetase (DHPS) in *Pneumocystis jirovecii*, blocking folate biosynthesis — the same pathway targeted by trimethoprim-sulfamethoxazole (TMP-SMX), the current first-line agent for PCP prophylaxis and treatment. This is a direct antimicrobial mechanism against the pathogen itself, rather than a host-immune-modulating effect, which gives the prediction stronger mechanistic grounding than a typical model-only signal.

The link between dapsone's original indication (leprosy, caused by *Mycobacterium leprae*) and the predicted new indication (pneumocystosis, caused by the fungal pathogen *Pneumocystis jirovecii*) is not through a shared original disease category, but through dapsone's core antifolate/antimicrobial pharmacology, which has broad activity across structurally unrelated pathogens sensitive to DHPS inhibition. In practice, this repurposing is not novel or purely theoretical — dapsone (with or without pyrimethamine or trimethoprim) has been used clinically as a second-line PCP prophylaxis and treatment option for HIV-infected and other immunocompromised patients intolerant of TMP-SMX for over three decades, and is referenced in international guidelines (e.g., ECIL-5, PMID 27550992).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Compared three anti-Pneumocystis regimens (including dapsone) plus zidovudine for primary PCP prevention in advanced HIV infection. |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim vs clindamycin/primaquine vs standard SMX/TMP for mild-to-moderate PCP treatment in AIDS. |
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Daily dapsone vs daily atovaquone for PCP prophylaxis in HIV patients intolerant of TMP/sulfonamides. |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3130 | Prospective HLA-B*1301 genetic screening to reduce incidence of dapsone hypersensitivity syndrome across multiple dapsone indications including PCP. |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | N/A | Dapsone vs TMP-SMX for first-episode PCP in AIDS patients. |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | N/A | Completed | N/A | Dapsone 100mg vs 50mg as primary PCP prophylaxis in AIDS-related complex. |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Monthly aerosolised pentamidine vs thrice-weekly dapsone for PCP prophylaxis in patients intolerant of TMP/sulfonamides. |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly oral dapsone dosing regimens for PCP prophylaxis in paediatric HIV infection; pharmacokinetics assessed. |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | N/A | Completed | 168 | Case-control study of PCP risk factors post-allogeneic HSCT; notes elevated PCP incidence (7.2%) on low-dose dapsone prophylaxis. |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate/leucovorin plus dapsone vs TMP/SMX for moderately severe PCP; safety and pharmacokinetics. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8018144](https://pubmed.ncbi.nlm.nih.gov/8018144/) | 1993 | RCT | The American Journal of Medicine | Randomised trial of dapsone vs aerosolised pentamidine for prophylaxis of PCP and toxoplasmic encephalitis in HIV infection. |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | RCT | AIDS | Compared aerosolised pentamidine, cotrimoxazole, and dapsone-pyrimethamine for primary PCP/toxoplasmic encephalitis prophylaxis. |
| [7979291](https://pubmed.ncbi.nlm.nih.gov/7979291/) | 1994 | PK/safety study | Antimicrobial Agents and Chemotherapy | Established maximum tolerated weekly dapsone dose (200mg) for PCP prevention. |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Network meta-analysis | Clinical Microbiology and Infection | Compared efficacy/safety of PCP treatment regimens (including dapsone-based) in people living with HIV. |
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Network meta-analysis | Clinical Microbiology and Infection | Compared TMP-SMX, dapsone-based regimens, aerosolised pentamidine and atovaquone for PCP prophylaxis in PWH. |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guideline | Journal of Antimicrobial Chemotherapy | ECIL-5 evidence-based guideline for PCP prophylaxis in haematological malignancy/HSCT recipients; dapsone listed as an alternative regimen. |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | Clinical Infectious Diseases | Comprehensive review of dapsone's anti-Pneumocystis activity, pharmacokinetics and clinical use for prevention/treatment of PCP. |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opinion on Pharmacotherapy | Review of Pneumocystis jirovecii prevention and treatment options, including dapsone-based regimens. |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | Journal of the Formosan Medical Association | Overview of Pneumocystis pneumonia pathophysiology and treatment, including dapsone-containing regimens. |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case report (safety) | The Annals of Pharmacotherapy | Reports methemoglobinemia in a patient receiving dapsone for PCP prophylaxis. |

---

## UK Market Information

No UK marketing authorisation is currently on record for dapsone in this evidence pack (0 licences; market status: Not Marketed). Historically, dapsone has been supplied in the UK primarily as an unlicensed ("specials") medicine for dermatological indications (e.g., dermatitis herpetiformis) rather than under a standard MHRA product licence — this would need to be confirmed against the current MHRA/BNF record before any procurement decision, as it falls under data gap DG001 (SmPC/labelling not yet retrieved).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: no key warnings, contraindications, or drug interaction data were returned for dapsone in this evidence pack — this is flagged as data gap DG001, classified Blocking, since it prevents a formal S1 safety pre-assessment. Case reports in the literature evidence above independently document methemoglobinemia, hypoxia, and photosensitivity associated with dapsone therapy and should inform any monitoring plan.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clinical evidence is strong — three completed Phase 3 RCTs (NCT00000991, NCT00000640, NCT00000802) and an international guideline (ECIL-5) support dapsone's efficacy for PCP prophylaxis/treatment, and the DHPS-inhibition mechanism is well established rather than purely predictive. However, two data gaps block full sign-off: no formal UK/TFDA safety labelling (DG001, Blocking) and no confirmed DrugBank MOA record (DG002, High), and the drug currently holds no UK marketing authorisation.

**To proceed, the following is needed:**
- Retrieve the SmPC/PIL or equivalent labelling data to close the Blocking safety gap (DG001) before any S1 safety assessment
- Confirm formal DrugBank/mechanism-of-action record (DG002)
- Determine UK market access pathway given zero current marketing authorisations (e.g., unlicensed import/specials manufacturing)
- Define a monitoring protocol addressing known sulfone-class risks (methemoglobinemia, haemolysis in G6PD deficiency, hypersensitivity syndrome — cf. NCT02550080 HLA-B*1301 screening) relative to the existing TMP-SMX standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

