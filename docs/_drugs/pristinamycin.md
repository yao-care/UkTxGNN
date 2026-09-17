---
layout: default
title: Pristinamycin
parent: Moderate Evidence (L3-L4)
nav_order: 482
evidence_level: L3
indication_count: 10
---

# Pristinamycin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Pristinamycin: From Bacterial Infections to Urethral Disease

## One-Sentence Summary

> Pristinamycin is a streptogramin-class antibacterial (50S ribosomal subunit inhibitor); no UK marketing authorisation or documented original indication is captured in this evidence pack.
> The TxGNN model predicts potential efficacy for **Urethral Disease** — specifically macrolide/fluoroquinolone-resistant *Mycoplasma genitalium* urethritis —
> with **no registered clinical trials** but **10+ supporting publications**, including a European clinical guideline and a published pristinamycin treatment case.

*Note: This evidence pack scored 10 candidate diseases for Pristinamycin. Nine of the ten (including the single highest TxGNN score, "disease of retroperitoneum") were explicitly flagged in the source data as mechanistically implausible, evidence-free model noise (L5, Hold). This report focuses on the one candidate with genuine mechanistic and literature support — ranked 9th by raw score but the only one reaching decision stage S2.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Pristinamycin holds no UK marketing authorisation, and no original indication data is captured in this evidence pack |
| Predicted New Indication | Urethral Disease (*Mycoplasma genitalium* / *Ureaplasma* urethritis) |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Pristinamycin was not retrievable from DrugBank at the time of this evidence pack (data gap DG002). However, the evidence pack's own mechanistic rationale confirms Pristinamycin belongs to the **streptogramin class** (a synergistic combination of type IA and type IIA streptogramin components), which inhibits bacterial protein synthesis by binding the **50S ribosomal subunit**. This class of activity is well documented against Gram-positive organisms including staphylococci, as well as against cell-wall-deficient organisms colonising the urogenital tract such as *Mycoplasma genitalium* and *Ureaplasma* species.

*M. genitalium* urethritis has become an increasingly difficult clinical problem due to rising macrolide and fluoroquinolone resistance. Because Pristinamycin's ribosomal binding site differs from macrolides, it has been used clinically — off-label in most jurisdictions — as a salvage option for multidrug-resistant *M. genitalium* urethritis. This is a direct, on-target antimicrobial application rather than an indirect knowledge-graph inference based on disease similarity, which strengthens plausibility relative to the nine other candidates in this pack.

The link between Pristinamycin's established antibacterial spectrum and urethral disease is therefore mechanistically coherent, even though no original indication field is populated and confirmatory MOA data from DrugBank is still outstanding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35182080](https://pubmed.ncbi.nlm.nih.gov/35182080/) | 2022 | Guideline | J Eur Acad Dermatol Venereol | European guideline: *M. genitalium* causes 10–35% of non-chlamydial non-gonococcal urethritis in men and is linked to cervicitis/PID in women |
| [34110731](https://pubmed.ncbi.nlm.nih.gov/34110731/) | 2021 | Case report | Sex Transm Dis | Pristinamycin initially failed in a multidrug-resistant *M. genitalium* urethritis case (A2062T 23S rRNA mutation); eventual cure required sequential therapy with minocycline |
| [40335273](https://pubmed.ncbi.nlm.nih.gov/40335273/) | 2026 | Case series | Sex Transm Infect | First five cases of multidrug-resistant *M. genitalium* urethritis successfully treated with a novel combination therapy regimen |
| [25194120](https://pubmed.ncbi.nlm.nih.gov/25194120/) | 2014 | Review | Ig Sanita Pubbl | Reviews rising antibiotic resistance in *Ureaplasma urealyticum* and the public-health impact of defensive over-prescribing |
| [5294813](https://pubmed.ncbi.nlm.nih.gov/5294813/) | 1965 | Case report | Hospital (Rio de Janeiro) | Early report of Pristinamycin use in staphylococcal urethritis and vaginitis |
| [34136](https://pubmed.ncbi.nlm.nih.gov/34136/) | 1978 | Susceptibility study | Pathol Biol | Antibiogram of urogenital *Ureaplasma* isolates ranked pristinamycin among the most active agents, after minocycline and erythromycin |
| [33532300](https://pubmed.ncbi.nlm.nih.gov/33532300/) | 2021 | Cohort | Transl Androl Urol | *Ureaplasma parvum* serovar-3/14 associated with chronic micturition urethral pain and recurrent microscopic haematuria in women |
| [30819052](https://pubmed.ncbi.nlm.nih.gov/30819052/) | 2020 | Cohort | J Int Med Res | Mollicutes antibiotic-resistance profiling in infertile couples with genital tract abnormalities |
| [26728808](https://pubmed.ncbi.nlm.nih.gov/26728808/) | 2016 | Cohort | Indian J Dermatol Venereol Leprol | Prevalence and antibiotic susceptibility of *M. hominis* and *U. urealyticum* in genital samples over 6 years |
| [14689895](https://pubmed.ncbi.nlm.nih.gov/14689895/) | 2003 | Cohort | Zhonghua Nan Ke Xue | Prevalence and drug tolerance of *Ureaplasma*/*Mycoplasma* in patients with urogenital inflammation |

---

## UK Market Information

Pristinamycin currently holds no UK marketing authorisation (0 licences; market status: Not marketed). No approved-indication or dosage-form data is available for the UK market.

---

## Other TxGNN Predictions (Not Pursued)

The remaining nine candidates generated for Pristinamycin (disease of retroperitoneum, lumbar spinal stenosis, celiac trunk compression syndrome, abdominal ectopic pregnancy, abdominal cystic lymphangioma, disease of uterine broad ligament, lymph node palisaded myofibroblastoma, sacrum chordoma, pudendal neuralgia) had similarly high raw TxGNN scores (~99.1–99.2%) but no supporting clinical trials or literature, and no plausible mechanistic link to a protein-synthesis-inhibiting antibacterial. These are assessed as knowledge-graph embedding noise (Evidence Level L5, decision stage S0, recommendation: **Hold**) and are not pursued further.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: as Pristinamycin is not licensed in the UK, no UK SmPC exists. Safety data (warnings, contraindications, drug interactions) were not retrievable in this evidence pack (data gap DG001, marked "Blocking" — this must be resolved before any safety assessment can proceed). Prescribers considering unlicensed/imported use should consult the manufacturer's SPC from a jurisdiction where the product is licensed (e.g. France) and follow the MHRA's guidance on unlicensed medicines.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The urethral disease prediction is supported by coherent antimicrobial mechanism, a European clinical guideline on the target pathogen (*M. genitalium*), and documented (if mixed) real-world use of Pristinamycin as salvage therapy for multidrug-resistant *M. genitalium* urethritis. However, evidence is limited to case reports/series and cohort studies (no RCTs), and the drug has no UK marketing authorisation.

**To proceed, the following is needed:**
- Resolution of data gap DG001 (TFDA/manufacturer SmPC warnings and contraindications) — currently blocking any safety assessment
- Resolution of data gap DG002 (confirmed MOA via DrugBank API)
- Formal drug interaction (DDI) data, currently returning no results
- An assessment of the unlicensed-medicine import/access pathway, since Pristinamycin is not marketed in the UK
- Ideally, prospective or comparative clinical data specific to *M. genitalium*/*Ureaplasma* urethritis, rather than relying solely on case reports and susceptibility surveys
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

