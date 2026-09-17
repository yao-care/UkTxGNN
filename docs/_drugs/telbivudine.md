---
layout: default
title: Telbivudine
parent: Model Prediction Only (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
---

# Telbivudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Telbivudine: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Telbivudine is a nucleoside analogue originally developed and approved for the treatment of chronic hepatitis B (CHB), acting as a hepatitis B virus (HBV) polymerase inhibitor. The TxGNN model predicts it may also be effective against **chronic hepatitis C virus infection**, with a very high prediction score, but the **10 clinical trials** and **10 publications** currently linked to this prediction are, on inspection, exclusively about hepatitis B — not hepatitis C — so the actual evidentiary support for this specific indication is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B (CHB) — confirmed via cited literature (e.g. PMID 18201580: "LdT was approved by the US FDA... for the treatment of chronic HBV infection") |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only — no trial or publication in the evidence set actually studies telbivudine in HCV-infected patients) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data was not available for this drug (`original_moa: [Data Gap]`). Based on the cited literature within the evidence pack, telbivudine is described as "the unmodified L-enantiomer of the naturally occurring nucleoside D-thymidine... it acts as a hepatitis B virus (HBV) polymerase inhibitor and preferentially inhibits HBV second-strand (DNA-dependent) DNA synthesis" (PMID 17722961). This is a highly HBV-selective mechanism, targeting the HBV reverse transcriptase/polymerase specifically.

Chronic hepatitis B and chronic hepatitis C are frequently discussed together in the clinical literature because they share transmission routes, overlapping patient populations, and are both hepatotropic viral infections — several of the papers retrieved for this prediction are literally titled "Perspectives on the management of chronic hepatitis B **and** C" (PMID 19344237) or "Chronic Hepatitis B **and** C — current treatment and future therapeutic prospects" (PMID 16937041). This pattern of joint discussion is the most plausible explanation for the high TxGNN score: the model appears to be picking up on textual co-occurrence between HBV and HCV in review articles, rather than genuine pharmacological cross-activity.

Critically, **every one of the 10 clinical trials** returned as "evidence" for this HCV prediction is in fact a telbivudine trial in chronic hepatitis **B** (HBeAg-positive/negative CHB, paediatric CHB, or HBV mother-to-child transmission) — none enrol or treat hepatitis C patients. HCV replicates via an RNA-dependent RNA polymerase (NS5B) and requires NS3/4A protease activity, mechanistically unrelated to the HBV DNA polymerase that telbivudine inhibits. This is analogous to a false-positive pattern already flagged elsewhere in this evidence pack: the HIV prediction (rank 3) for the same drug was explicitly refuted by in vitro/clinical data (PMID 22024528, PMID 20308377) showing telbivudine has **no** antiviral activity against HIV-1, despite a similarly high TxGNN score driven by HBV/HIV co-infection literature. The hepatitis C prediction should be treated with the same scepticism until direct anti-HCV activity data emerges.

## Clinical Trial Evidence

**Caveat**: All trials below were retrieved under the "chronic hepatitis C virus infection" prediction, but on review every one is a telbivudine study in chronic hepatitis **B**, not hepatitis C. No trial in the evidence set treats HCV-infected patients with telbivudine.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00805675](https://clinicaltrials.gov/study/NCT00805675) | Phase 3 | Completed | 83 | Telbivudine 600 mg + tenofovir DF vs monotherapy on HBV DNA kinetics in HBeAg-positive compensated CHB (not HCV) |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys + entecavir vs entecavir vs Pegasys for HBeAg-negative CHB |
| [NCT00142298](https://clinicaltrials.gov/study/NCT00142298) | Phase 3 | Completed | 1,869 | Open-label extension of telbivudine treatment in chronic hepatitis B patients |
| [NCT03181607](https://clinicaltrials.gov/study/NCT03181607) | N/A | Unknown | 300 | Telbivudine/tenofovir to reduce HBV mother-to-child transmission in high viral load pregnancy |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | Completed | 44 | Early viral kinetic comparison of telbivudine vs entecavir in HBeAg-positive CHB |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | Unknown | 600 | Long-term prognosis of chronic HBV infection under antiviral treatment |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | Completed | 160 | RO7020531 SAD/MAD study including a chronic hepatitis B treatment arm |
| [NCT02058108](https://clinicaltrials.gov/study/NCT02058108) | Phase 3 | Terminated | 53 | Telbivudine oral solution/tablets in paediatric HBeAg-positive/negative CHB |
| [NCT01083251](https://clinicaltrials.gov/study/NCT01083251) | N/A | Unknown | 120 | Vitamin D as add-on to Peg-interferon or telbivudine monotherapy in chronic HBV infection |
| [NCT05466071](https://clinicaltrials.gov/study/NCT05466071) | N/A | Unknown | 200 | Tenofovir alafenamide to prevent HBV mother-to-child transmission (high viral load pregnancy) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28845882](https://pubmed.ncbi.nlm.nih.gov/28845882/) | 2018 | Cohort study | Journal of Viral Hepatitis | HBV reactivation more common *after* rather than during direct-acting antiviral (DAA) therapy for hepatitis C in a US veteran cohort — a co-infection safety signal, not evidence of anti-HCV activity |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Clinical study | J Interferon Cytokine Res | Serum IL-37 and HBeAg seroconversion during telbivudine treatment — again an HBV, not HCV, outcome |
| [18330099](https://pubmed.ncbi.nlm.nih.gov/18330099/) | 2007 | Guideline | Acta Gastro-Enterologica Belgica | Belgian 2007 guidelines for management of chronic hepatitis B |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | New data/recommendations on antiviral therapy for chronic hepatitis B and C (joint discussion, not combined efficacy) |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Overview of antiviral medications for hepatitis B and C and their renal effects; telbivudine listed only under HBV agents |
| [19344237](https://pubmed.ncbi.nlm.nih.gov/19344237/) | 2009 | Review | Expert Review of Anti-infective Therapy | "Perspectives on the management of chronic hepatitis B and C" — separate management pathways discussed |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener Medizinische Wochenschrift | Chronic hepatitis B and C current treatment/future prospects — telbivudine discussed only for HBV |
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | Journal of Perinatology | HBV and HCV in pregnancy review — telbivudine mentioned only for HBV MTCT prevention |
| [21964179](https://pubmed.ncbi.nlm.nih.gov/21964179/) | 2011 | Review | Mayo Clinic Proceedings | Antiviral drugs for viruses other than HIV — telbivudine classified as an anti-hepatitis (B) agent |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatric Drugs | Management of chronic liver disease in children — no HCV-specific telbivudine data |

**No publication in this evidence set reports direct in vitro or clinical anti-HCV activity for telbivudine.**

## UK Market Information

Telbivudine currently has **no MHRA marketing authorisation in the UK** (0 licences on record; market status: Not marketed). No product, dosage form, or approved-indication information is available to summarise.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: this evidence pack flags a **Blocking** data gap (DG001) for TFDA/SmPC warnings and contraindications, and a **High**-severity gap (DG002) for mechanism-of-action data — both of which must be resolved before any formal safety (S1) evaluation can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score for chronic hepatitis C virus infection is high, but every supporting trial and the large majority of supporting literature relate to telbivudine's genuine indication (chronic hepatitis B), not hepatitis C — the signal is most likely a literature co-occurrence artefact ("hepatitis B and C" reviewed jointly), the same failure mode explicitly confirmed for this drug's HIV prediction elsewhere in this evidence pack. Mechanistically, telbivudine inhibits the HBV DNA polymerase and has no known activity against the HCV NS5B RNA polymerase.
- The drug is not marketed in the UK (0 MHRA licences), and a Blocking data gap on SmPC warnings/contraindications prevents any safety assessment regardless.

**To proceed, the following is needed:**
- Confirmed DrugBank/SmPC mechanism-of-action data (DG002) to formally assess target specificity against HCV
- TFDA/MHRA-equivalent label warnings and contraindications (DG001) — currently blocking any S1 safety review
- Direct in vitro anti-HCV activity data for telbivudine, if this hypothesis is to be pursued further (none currently exists in the evidence set)
- Re-evaluation of rank 2 ("hepatitis B virus infection") separately, since this reflects telbivudine's already-established indication rather than a genuine repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

