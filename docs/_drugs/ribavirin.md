---
layout: default
title: Ribavirin
parent: Moderate Evidence (L3-L4)
nav_order: 501
evidence_level: L4
indication_count: 10
---

# Ribavirin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is a guanosine-analogue antiviral historically used in combination regimens (with interferon, and later with direct-acting antivirals) for chronic hepatitis C — it has no UK marketing authorisation recorded in this evidence pack. The TxGNN model predicts a possible new indication in **chronic hepatitis B virus (HBV) infection**, but the supporting evidence (46 clinical trials, 20 publications) consists almost entirely of hepatitis C trials and HBV/HCV co‑infection reviews rather than direct evidence of ribavirin efficacy against HBV. The evidence review concludes this is most likely a knowledge‑graph artefact rather than a genuine repurposing signal, and recommends **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the UK regulatory dataset (no licences on file). Historically, ribavirin is used in combination with peginterferon for chronic hepatitis C. |
| Predicted New Indication | Chronic Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action documentation is flagged as a data gap in this evidence pack. Based on the pharmacological analysis included with the prediction, ribavirin is a guanosine nucleoside analogue that acts through inhibition of inosine monophosphate dehydrogenase (IMPDH) and induction of lethal mutagenesis in RNA virus genomes. Its established clinical antiviral effect has been demonstrated almost exclusively against **RNA viruses**, most notably hepatitis C virus (HCV), typically as an adjunct to interferon or direct-acting antivirals.

Hepatitis B virus, in contrast, is a **DNA virus that replicates via reverse transcription**. There is no established mechanism by which ribavirin's RNA-mutagenesis activity would be expected to inhibit HBV replication, and current international guidelines do not recommend ribavirin — alone or in combination — as a treatment for chronic HBV infection (standard care being nucleos(t)ide analogues or interferon).

The reviewer's mechanistic assessment (included in this evidence pack) concludes that the very high TxGNN score most likely reflects a **knowledge-graph conflation** between the large literature base on HBV/HCV *co-infection* (where ribavirin is used to treat the HCV component) and a genuine drug–disease efficacy signal for HBV itself. One directly relevant historical publication in the literature set even poses the question outright — *"Is ribavirin treatment really effective for chronic hepatitis B?"* (Kakumu, 2000) — a title that itself signals long-standing scepticism rather than support.

---

## Clinical Trial Evidence

**Caveat:** of the 46 trials retrieved for this candidate, none evaluate ribavirin as a treatment *for* HBV. The large majority are hepatitis C trials that were linked via shared co-infection terminology; several have already been graded "not relevant" (Grade C) during evidence triage. The most relevant trials are shown below for transparency.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Studies HBV reactivation risk during direct-acting antiviral treatment of HCV/HBV co-infected patients — relevant to HBV context, but does not test ribavirin efficacy against HBV. |
| [NCT01598090](https://clinicaltrials.gov/study/NCT01598090) | Phase 3 | Completed | 881 | Peginterferon lambda-1a vs alfa-2a plus ribavirin and telaprevir in genotype‑1 chronic hepatitis C. Graded not relevant to HBV (HCV-only trial). |
| [NCT00215865](https://clinicaltrials.gov/study/NCT00215865) | Phase 3 | Completed | 600 | PEG-Intron plus ribavirin dosing comparison in prior hepatitis C non-responders. Graded not relevant to HBV. |
| [NCT01830127](https://clinicaltrials.gov/study/NCT01830127) | Phase 2 | Completed | 35 | BI 207127 + faldaprevir + ribavirin in genotype‑1b hepatitis C with hepatic impairment. Graded not relevant to HBV. |

---

## Literature Evidence

**Caveat:** the literature base is dominated by reviews of HBV/HCV *co-infection management* rather than primary studies of ribavirin efficacy in HBV monoinfection. One historical paper directly questions ribavirin's efficacy in HBV.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10832679](https://pubmed.ncbi.nlm.nih.gov/10832679/) | 2000 | Commentary | J Gastroenterol | Title directly questions whether ribavirin is effective for chronic hepatitis B — the single most on-topic reference, and a sceptical one. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Reviews treatment and outcomes of dual chronic HCV/HBV infection; ribavirin discussed only as part of anti-HCV combination therapy. |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatology International | Discusses viral interaction dynamics in dual HBV/HCV infection, not ribavirin monotherapy for HBV. |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | Treatment challenges in HBV/HCV co-infection; ribavirin featured only as HCV-directed therapy. |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | Reviews chemo- and immunotherapy for HBV and HCV separately; notes ribavirin's role is HCV-specific. |
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection review; peginterferon plus ribavirin discussed as HCV-directed regimen only. |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | Treatment strategies for chronic HBV and chronic HCV presented separately; ribavirin appears only in the HCV section. |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Review | Semin Liver Dis | Host genetics of chronic HBV and HCV outcomes; no ribavirin efficacy data for HBV. |
| [8314494](https://pubmed.ncbi.nlm.nih.gov/8314494/) | 1993 | Historical review | Gut | Historical overview of chronic HBV and HCV treatment prior to interferon era; no ribavirin/HBV efficacy claim. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism and HBV outcomes; ribavirin relevance is via HCV treatment response, not HBV. |

---

## UK Market Information

No UK marketing authorisation is recorded for ribavirin in this evidence pack (market status: not marketed; 0 licences on file). Prescribers should check the current MHRA product database and BNF directly, as ribavirin-containing products (e.g. in combination with peginterferon or as part of historical hepatitis C regimens) may exist outside the scope of this dataset.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Additional safety signals identified during literature review** (not part of the formal safety dataset, but relevant to any future consideration of this candidate):
- Interferon/ribavirin combination therapy has been associated with case reports of porphyria cutanea tarda emerging or worsening during treatment (e.g. PMID 12395349, 18855993, 15763350).
- A case report describes occult pulmonary granulomatosis developing during interferon-alfa/ribavirin therapy in a patient with hepatopulmonary syndrome (PMID 25161156) — a safety signal, not an efficacy signal, for that candidate indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score for chronic hepatitis B is not supported by mechanism (ribavirin acts on RNA virus replication; HBV is a DNA virus) or by direct clinical evidence — the retrieved trials and literature address HCV treatment or HBV/HCV co-infection management, not ribavirin efficacy against HBV itself, and one directly relevant historical paper explicitly questions this efficacy. This pattern is consistent with a knowledge-graph artefact arising from HBV/HCV co-infection literature overlap rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Product labelling (SmPC) warnings and contraindications, currently a blocking data gap (DG001) — required before any Stage 1 safety review can proceed.
- Confirmed original mechanism-of-action documentation from DrugBank (DG002).
- A targeted literature search restricted to "ribavirin AND hepatitis B" primary efficacy studies (excluding co-infection/HCV-focused papers) to confirm whether any dedicated evidence base exists.
- Confirmation of current UK marketing/licensing status directly with MHRA, given the "not marketed" flag in this dataset.

*Note: Nine additional lower-ranked candidates (ranks 2–10, e.g. hepatopulmonary syndrome, hepatoportal sclerosis, IgG4-related conditions) were also generated for this drug. All carry Evidence Level L4–L5 and a "Hold" recommendation, with either no supporting literature or literature describing adverse effects rather than efficacy.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

