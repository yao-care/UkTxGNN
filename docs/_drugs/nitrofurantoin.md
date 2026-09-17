---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

> Nitrofurantoin is an established antibacterial used for urinary tract infection, and is not currently marketed under this evidence pack's regulatory dataset. The TxGNN model's top-ranked prediction is **Rheumatoid Arthritis** (score 99.89%), but on review the supporting literature runs in the **opposite direction** — describing antibiotic-associated RA flares and nitrofurantoin-related pulmonary toxicity in RA patients, not therapeutic benefit — with **0 clinical trials** and **12 publications**, none of which are efficacy evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (established clinical use; not captured as structured data in this evidence pack) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack (DG002). Based on the functional description recovered from the literature review, nitrofurantoin is a nitrofuran-class antibacterial: bacterial nitroreductases reduce the drug to reactive intermediates that damage bacterial DNA and ribosomal proteins. It is renally excreted and concentrates almost exclusively in urine, which is why its clinical use is essentially restricted to uncomplicated lower urinary tract infection.

There is no established immunomodulatory or anti-inflammatory pathway linking this nitrofuran redox chemistry to rheumatoid synovitis pathogenesis. A high TxGNN embedding score (99.89%) reflects graph-based statistical association, not causal or therapeutic evidence, and can arise from indirect co-occurrence patterns rather than genuine pharmacology.

Critically, the 12 retrieved publications do not support a treatment hypothesis — they run the other way. One cohort study found antibiotic exposure associated with **RA flares**, and a case report describes nitrofurantoin combined with methotrexate causing **irreversible pulmonary fibrosis** in an RA patient being treated for a concurrent UTI. The remainder are general reviews of drug-induced interstitial lung disease that list nitrofurantoin among culprit drugs, or unrelated case reports retrieved by keyword overlap. This prediction should be treated as a knowledge-graph artefact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Med J | Reviews drug-induced pulmonary fibrosis; lists nitrofurantoin among causative drugs and notes RA itself predisposes to pulmonary fibrosis — not a treatment link |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | RA patients hospitalised for interstitial lung fibrosis; supports RA-lung disease association, unrelated to nitrofurantoin efficacy |
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Antibiotic exposure associated with **flares** of RA in a UK CPRD cohort — a harm signal, opposite to a treatment hypothesis |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Cureus | Nitrofurantoin + methotrexate combination caused irreversible pulmonary fibrosis in an RA patient treated for UTI — adverse interaction, not efficacy evidence |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case Report | Cureus | Differential diagnosis of autoimmune hepatitis; nitrofurantoin listed as a drug to rule out, RA mentioned only as an unrelated autoimmune comparator |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | Rev Prat | Review of drug-induced interstitial lung disease listing nitrofurantoin as a causative antibiotic |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case Report | Ann Dermatol Venereol | Phenylbutazone-induced sialadenitis; nitrofurantoin mentioned only as another drug capable of causing sialadenitis |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case Report | Rev Pneumol Clin | Gold-salt-induced pneumonitis with methotrexate comparison; no direct nitrofurantoin-RA link |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Med Scand | Short-term nitrofurantoin therapy for bacteriuria in a middle-aged female population; unrelated to RA |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | General synopsis of alveolitis and pulmonary fibrosis; no specific RA-nitrofurantoin content |

---

## UK Market Information

Nitrofurantoin holds no marketing authorisation on record in this evidence pack (total licences: 0; market status: **Not marketed**). No product-level licence data is currently available for extraction.

---

## Safety Considerations

The structured safety fields in this evidence pack (`key_warnings`, `contraindications`, `ddi`) are all data gaps, and DG001 flags this as **Blocking** — retrieval of the official SmPC/label warnings is required before this candidate can enter an initial safety assessment (S1).

That said, the literature surfaced during the indication search independently corroborates several well-established nitrofurantoin risks, which should not be overlooked even though the top-line safety fields are empty:
- **Pulmonary toxicity**, including a reported fatal interaction with methotrexate causing irreversible fibrosis
- **Methemoglobinaemia and haemolytic anaemia**, particularly in neonates and G6PD-deficient patients, confirmed by dedicated toxicology and case-report literature (ranks 8 and 10 below)
- **Hepatotoxicity**, including autoimmune-hepatitis-like presentations, listed among drugs requiring exclusion in differential diagnosis

Please refer to the SmPC and BNF for complete prescribing information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications (Screened, Not Progressed)

The evidence pack scored 10 candidate indications for nitrofurantoin. None progressed beyond L4/L5, and several illustrate the same failure modes seen above — zero-evidence rare genetic diseases (statistical artefacts of the knowledge graph) or literature that documents an *adverse* association rather than a therapeutic one.

| Rank | Disease | TxGNN Score | Evidence Level | Note |
|------|---------|------|------|------|
| 2 | Familial hematuria–retinal arteriolar tortuosity–contractures syndrome | 99.81% | L5 | Zero literature/trials; rare monogenic collagen disorder unrelated to antibacterial mechanism |
| 3 | Brain small vessel disease 1 with/without ocular anomalies | 99.81% | L5 | 19 retrieved papers are all unrelated congenital ophthalmic conditions — keyword mismatch |
| 4 | Diabetic nephropathy | 99.76% | L4 | Literature only shows diabetic nephropathy patients are prone to UTI (a nitrofurantoin *indication*, not treatment of the nephropathy); nitrofurantoin is contraindicated at reduced renal function |
| 5 | Brachydactyly-syndactyly syndrome | 99.75% | L5 | Zero evidence; skeletal dysplasia, no biological link |
| 6 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.71% | L5 | Zero evidence; congenital syndrome, no biological link |
| 7 | Sclerosing cholangitis | 99.59% | L4 | Literature only shows indirect UTI–autoimmune-liver-disease association; nitrofurantoin itself carries a known hepatotoxicity signal |
| 8 | Methemoglobinaemia, alpha type | 99.42% | L5 | Direction reversed — nitrofurantoin is a known **cause**, not treatment, of methemoglobinaemia |
| 9 | Gout | 99.42% | L5 | Single unrelated 1975 pyelonephritis citation |
| 10 | Methemoglobinaemia | 99.38% | L4 | Confirmed adverse-reaction literature (nitrofurantoin/its photoproduct induces methemoglobinaemia), not an indication |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Across all 10 TxGNN-predicted indications, none reach beyond L4 evidence, no clinical trials exist for any candidate, and the top-ranked candidate (rheumatoid arthritis) is directly contradicted by the retrieved literature, which documents antibiotic-associated RA flares and nitrofurantoin-related pulmonary toxicity rather than benefit. Two other candidates are known adverse-effect associations (methemoglobinaemia) mistakenly surfaced by the model as indications.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/SmPC-equivalent label warnings and contraindications before any safety screen (S1) can begin
- Resolve DG002: obtain a confirmed mechanism-of-action record via the DrugBank API
- Independent mechanistic or preclinical evidence in the correct causal direction, should the RA hypothesis be revisited
- No further development action is recommended for any of the 10 candidates at this time given the current L4/L5 evidence ceiling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

