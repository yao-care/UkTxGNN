---
layout: default
title: Etodolac
parent: High Evidence (L1-L2)
nav_order: 249
evidence_level: L2
indication_count: 10
---

# Etodolac
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Etodolac: From Rheumatic Pain and Arthritis to Ankylosing Spondylitis

> **Note on indication selection:** TxGNN's single highest-scoring prediction (acromesomelic dysplasia, Hunter-Thompson type, rank 1) has zero supporting evidence and is explicitly flagged in the underlying rationale as likely graph-embedding noise, with a "Hold" recommendation. This report instead focuses on **Ankylosing Spondylitis** — the only predicted indication in this evidence pack backed by actual clinical-trial and literature evidence (Evidence Level L2, "Proceed with Guardrails").

## One-Sentence Summary

Etodolac is a non-steroidal anti-inflammatory drug (NSAID) with a long history of use in rheumatic pain and inflammatory joint conditions. The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**, and published literature going back to the late 1980s/1990s already documents etodolac's use in this condition, though there is currently **no dedicated etodolac-specific randomised controlled trial** and **no active UK marketing authorisation** on record.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from UK regulatory data (drug not currently marketed in the UK). Published literature indicates historical use in rheumatoid arthritis, osteoarthritis and general pain states. |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this evidence pack. Based on the literature evidence gathered, etodolac is an NSAID whose "primary anti-inflammatory mechanism of action is through a selective effect on cyclo-oxygenase-2 (COX-2)" (Bellamy, 1997, PMID 17694363), distinguishing it somewhat from purely non-selective older NSAIDs.

NSAIDs are a first-line, guideline-recommended (ASAS/EULAR) symptomatic treatment for axial inflammation and pain in Ankylosing Spondylitis. Etodolac's efficacy in rheumatic disease more broadly — rheumatoid arthritis, osteoarthritis and, notably, ankylosing spondylitis itself — was already documented in comparative and open-label studies from the late 1980s and 1990s (e.g. Balfour & Buckley, 1991, PMID 1717225; Bacon, 1990, PMID 2146130), where it performed comparably to naproxen and piroxicam.

In other words, this is less a *novel* mechanistic hypothesis and more a *class-effect* prediction: etodolac's anti-inflammatory/analgesic action is mechanistically aligned with AS's treatment paradigm, and this has historical clinical support — it is simply absent from current UK licensing data because the product is not presently marketed in the UK.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Evaluates standard-dose vs reduced-dose TNF inhibitor in AS patients with stable disease. **Does not test etodolac directly** — relevance is population-level only (AS patients), graded C (weak) in the underlying evidence assessment. |

No etodolac-specific interventional trial in Ankylosing Spondylitis was identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2146130](https://pubmed.ncbi.nlm.nih.gov/2146130/) | 1990 | Review | European Journal of Rheumatology and Inflammation | Randomised, double-blind trials show etodolac (200–300 mg b.i.d.) comparable to naproxen and piroxicam in RA, OA and AS. |
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | Review | Drugs | Etodolac effective in RA, OA and AS, and in postoperative/gout/traumatic pain; adverse-effect profile similar to other NSAIDs. |
| [17694363](https://pubmed.ncbi.nlm.nih.gov/17694363/) | 1997 | Review | Inflammopharmacology | Clinical review confirming COX-2-selective mechanism; widely used in RA, AS, gout and OA. |
| [2525800](https://pubmed.ncbi.nlm.nih.gov/2525800/) | 1989 | Cohort | La Revue de Médecine Interne | Open trial in 4,947 patients (RA/AS/OA of lower limbs) assessing efficacy, safety and therapeutic benefit. |
| [2150569](https://pubmed.ncbi.nlm.nih.gov/2150569/) | 1990 | Cohort | Rheumatology International | Large-scale French open-label safety study, 4,947 patients (RA/AS/OA), plus 51,355-patient postmarketing safety cohort. |
| [2150568](https://pubmed.ncbi.nlm.nih.gov/2150568/) | 1990 | Cohort | Rheumatology International | Postmarketing surveillance across Italy, Switzerland, UK and France (8,334 patients, OA/RA, one cohort including AS). |
| [21140116](https://pubmed.ncbi.nlm.nih.gov/21140116/) | 2010 | Cohort | Singapore Medical Journal | Pamidronate trial in NSAID-refractory/intolerant AS — contextual evidence on NSAID's role as first-line therapy, not etodolac-specific. |
| [20829199](https://pubmed.ncbi.nlm.nih.gov/20829199/) | 2011 | Review | Annals of the Rheumatic Diseases | ASAS recommendations for standardising NSAID-intake reporting in axial spondyloarthritis trials. |
| [22071858](https://pubmed.ncbi.nlm.nih.gov/22071858/) | 2011 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Reviews NSAID safety (incl. etodolac class) alongside methotrexate in inflammatory arthritis, including AS. |
| [24449987](https://pubmed.ncbi.nlm.nih.gov/24449987/) | 2013 | Review | The Israel Medical Association Journal | Discusses diagnostic boundaries of axial spondyloarthritis; contextual, not etodolac-specific. |

---

## UK Market Information

Etodolac currently has **no active UK marketing authorisation** on record (0 licenses; market status: not marketed). Any repurposing pathway would need to address this before clinical use — this is a first-order gap that must be resolved ahead of, or alongside, the indication-repurposing question.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(No structured warnings, contraindications, or drug interaction data were retrievable in this evidence pack — this is flagged as a Blocking data gap, see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and historical-literature case for etodolac in Ankylosing Spondylitis is reasonably solid — decades-old comparative and cohort data (thousands of patients) support NSAID-class efficacy — but no etodolac-specific RCT exists, the supporting literature predates modern AS trial standards (pre-ASAS era), and the drug has no current UK marketing authorisation.

**To proceed, the following is needed:**
- UK SmPC/PIL retrieval for warnings and contraindications — flagged as a **Blocking** data gap (DG001) that must be resolved before any S1 safety screen
- Confirmed mechanism-of-action detail from DrugBank (DG002, High severity)
- Clarification of the regulatory pathway, since the product is not currently marketed in the UK (this is a marketing-authorisation question, not solely a repurposing/off-label question)
- Contemporary comparative or guideline-referenced data on etodolac in AS, given existing evidence is >30 years old
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

