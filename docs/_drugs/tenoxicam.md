---
layout: default
title: Tenoxicam
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Tenoxicam
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

# Tenoxicam: From Arthritic Joint Disease to Rheumatoid Arthritis

## One-Sentence Summary

Tenoxicam is an oxicam-class non-steroidal anti-inflammatory drug (NSAID), originally used for arthritic joint disease and arthropathy.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, with **no registered clinical trials** but **20 publications** (including randomised comparative trials) supporting this direction. Because rheumatoid arthritis is closely related to the original indications, this is closer to an on-label or near-label use than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arthritic joint disease; arthropathy (the licence record contains no approved indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 (based on the data compiled for this report; see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* No registered trials are listed for this indication. The L1 rating comes from the published randomised, double-blind comparative studies in rheumatoid arthritis. Most of these are older studies and the abstracts supplied are truncated, so this rating should be verified against the full publications.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the known drug class, tenoxicam is an oxicam NSAID that inhibits cyclooxygenase (COX-1 and COX-2). This reduces prostaglandin-mediated inflammation, pain and swelling in joints.

Rheumatoid arthritis is an inflammatory joint disease, closely related to the original indications of arthritic joint disease and arthropathy. The same anti-inflammatory and analgesic effect is expected to give symptomatic relief. Reviews report that tenoxicam 20 mg once daily was at least as effective as piroxicam 20 mg in rheumatoid arthritis, osteoarthritis and ankylosing spondylitis.

NSAIDs provide symptom relief only. There is no evidence in the data compiled that tenoxicam modifies the course of the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

For reference, one trial was found for a lower-ranked prediction, headache disorder (acute migraine):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06786650](https://clinicaltrials.gov/study/NCT06786650) | Phase 4 | Active, not recruiting | 100 | Compares intravenous tenoxicam with intravenous ibuprofen for headache relief in acute migraine; no results reported yet |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clin Rheumatol | Double-blind, 3-month trial in 292 rheumatoid arthritis patients comparing aceclofenac and tenoxicam; both groups improved clinically |
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | Comparative trial | J Rheumatol | Tenoxicam 20 mg vs piroxicam 20 mg in 102 rheumatoid arthritis patients; no difference in efficacy, similar adverse event rates |
| [2695152](https://pubmed.ncbi.nlm.nih.gov/2695152/) | 1989 | Double-blind RCT | Br J Clin Pract | 1,328 patients with osteoarthritis or rheumatoid arthritis; tenoxicam vs piroxicam, both improved pain and stiffness |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | Clinical study | Eur J Rheumatol Inflamm | Double-blind trials; tenoxicam 20 mg at least as effective as piroxicam in osteoarthrosis, rheumatoid arthritis and ankylosing spondylitis |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | Multicentre study | J Int Med Res | 2,963 general practice patients with osteoarthritis or rheumatoid arthritis treated with 20 mg/day for 12 weeks or longer |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | Tenoxicam is an effective analgesic and anti-inflammatory agent in rheumatoid arthritis and other rheumatic conditions, and was at least as well tolerated as piroxicam |
| [3315620](https://pubmed.ncbi.nlm.nih.gov/3315620/) | 1987 | Review | Drugs | Pharmacology and efficacy review; 20 mg daily comparable to piroxicam 20 mg daily |
| [3329109](https://pubmed.ncbi.nlm.nih.gov/3329109/) | 1987 | Review | Eur J Rheumatol Inflamm | Overview of 133 clinical studies; efficacy shown in double-blind comparisons, optimal dose 20 mg |
| [8137596](https://pubmed.ncbi.nlm.nih.gov/8137596/) | 1994 | Pharmacokinetic review | Clin Pharmacokinet | Completely absorbed orally, about 99% protein bound |
| [1778090](https://pubmed.ncbi.nlm.nih.gov/1778090/) | 1991 | Open study | Curr Med Res Opin | 736 African outpatients with rheumatic disorders given 20 mg daily; efficacy and tolerability assessed |

Most of this evidence dates from the 1980s and 1990s.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 100101040AAAAAA | Tenoxicam Tab 20 mg | Not stated | Not stated in the data compiled |

One authorisation (single-ingredient, valid) is recorded. The format of this number does not match a standard MHRA "PL" number, so please verify it against the MHRA register.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

One signal appeared in the literature: a published case report (PMID 9303679, 1997) describes alopecia as a possible adverse effect of tenoxicam. As with other NSAIDs, standard class precautions apply (gastrointestinal, cardiovascular and renal risks). Check these against the SmPC.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Rheumatoid arthritis is closely related to the drug's original indications. Several randomised and comparative studies support symptomatic efficacy equivalent to piroxicam. However, the evidence is old, there are no registered trials, and the safety and licensing data are incomplete.

**To proceed, the following is needed:**
- Confirm the current UK licensed indications, dosage form and SmPC for the authorisation
- Retrieve full safety data (warnings, contraindications, interactions) from the SmPC and BNF
- Confirm mechanism of action data from DrugBank
- Review how tenoxicam compares with current NICE-recommended management of rheumatoid arthritis, since NSAIDs give symptom relief only

**Other predicted indications (for context):**
- **Headache disorder:** worth further research. One Phase 4 trial (NCT06786650) is ongoing; the mechanism is plausible, but there is no tenoxicam-specific literature. Evidence level L4.
- **Alopecia:** Hold. The only evidence is an adverse-effect case report, which argues against benefit.
- **Osteoarthritis susceptibility, trigeminal autonomic cephalalgia, diffuse alopecia areata, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, hypotrichosis simplex of the scalp and congenital hypotrichosis milia:** Hold. These are model predictions only (L5), with no trials, literature or mechanistic support. Symptomatic osteoarthritis would be a separate, better-supported indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

