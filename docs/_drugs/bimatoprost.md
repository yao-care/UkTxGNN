---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Bimatoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bimatoprost: From Glaucoma to Alopecia

## One-Sentence Summary

Bimatoprost is a prostaglandin F2α analogue (prostamide) originally developed as a glaucoma eye drop to reduce intraocular pressure, and later approved by the FDA as Latisse for promoting eyelash growth in hypotrichosis.
The TxGNN model predicts it may be effective for **Alopecia** (androgenetic alopecia and female pattern hair loss), with **11 clinical trials** — including multiple completed Phase 2 RCTs totalling over 850 participants — supporting this indication.
Although TxGNN's highest-ranked prediction (periodontal malformation syndrome, rank 1) is likely a knowledge graph false positive, the alopecia prediction (TxGNN rank 8, score 99.99%) represents the strongest and most clinically actionable finding in this evidence pack and is the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma and ocular hypertension (IOP reduction); eyelash hypotrichosis (Latisse, FDA-approved) |
| Predicted New Indication | Alopecia (androgenetic alopecia; female pattern hair loss) |
| TxGNN Prediction Score | 99.99% (TxGNN internal rank 293) |
| Evidence Level | L2 |
| UK Market Status | Not marketed (no MHRA licences on record in current dataset — verification required) |
| Number of Marketing Authorisations | 0 (data gap; MHRA database verification recommended) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data was not available in this evidence pack. Based on established pharmacology, bimatoprost is a selective agonist at the prostaglandin FP receptor, structurally related to PGF2α but classified as a prostamide (prostaglandin-ethanolamide analogue). In the eye, FP receptor activation increases uveoscleral aqueous outflow, thereby reducing intraocular pressure in glaucoma. The drug's hair-related biology was discovered serendipitously: patients using bimatoprost eye drops consistently developed longer, darker, and thicker eyelashes. This observation led directly to FDA approval of Latisse (bimatoprost 0.03% ophthalmic solution) for eyelash hypotrichosis in 2008 — directly validating FP receptor stimulation as a mechanism for promoting hair follicle growth, extending the anagen (active growth) phase, and enlarging the dermal papilla.

The mechanistic bridge from eyelash follicles to scalp hair follicles is the core repurposing rationale. Scalp follicles express FP receptors and share the same anagen-promoting biology demonstrated in ciliary follicles. PMID 23104985 explicitly draws a parallel with minoxidil — originally an antihypertensive that was serendipitously found to cause unwanted hair growth and subsequently repurposed for androgenetic alopecia — reinforcing that this class of serendipitous hair-growth discovery has a proven regulatory pathway. The FP receptor stimulation mechanism (anagen extension, dermal papilla enlargement) is mechanistically coherent regardless of follicle anatomical location.

The critical clinical question — whether bimatoprost can overcome androgen-mediated follicular miniaturisation in androgenetic alopecia — was directly tested in at least three large Phase 2 RCTs (NCT01325337, NCT01325350, NCT01904721) totalling over 850 participants across male and female subtypes. Notably, the original developer (Allergan) did not advance to Phase 3 despite completing these studies. This is the principal uncertainty that governs the "Proceed with Guardrails" recommendation: the mechanistic basis is sound and the clinical programme was substantial, but the reason for halting at Phase 2 must be understood before further resources are committed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Randomised, double-blind; three bimatoprost doses vs vehicle and minoxidil 5% in men with androgenetic alopecia — primary efficacy and safety dataset for male AGA |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Randomised, double-blind; three doses vs vehicle and minoxidil 2% in women with female pattern hair loss — primary FPHL dataset |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy of bimatoprost in male AGA — independent corroborating Phase 2 dataset alongside NCT01325337 |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Mechanistic RCT: evaluated bimatoprost effect specifically on androgen-dependent hair follicles; provides FP receptor pathway validation data |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | CO₂ fractional laser combined with bimatoprost 0.03% for alopecia areata — novel enhanced-delivery approach; completed 2021 |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability, and pharmacokinetics of new topical bimatoprost formulations in alopecia patients — dose-selection basis for Phase 2 programme |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Local skin pharmacokinetics of bimatoprost applied to the scalp in male AGA over 14 days; provides scalp absorption parameters relevant to formulation design |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Safety and efficacy of bimatoprost 0.03% for eyelash loss/hypotrichosis in children (ages not stated) — validates safety profile across age groups via the adjacent approved indication |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | Exploratory | Completed | 14 | Bimatoprost vs latanoprost for eyelash regrowth in alopecia areata — small, exploratory; provides an early signal that PG analogues may be active in immune-mediated alopecia |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | **Terminated** | 53 | Dose escalation safety and PK in male AGA — **early termination; reason not documented. Must clarify whether a safety signal (e.g., systemic prostaglandin effects, dermal irritation) contributed before proceeding** |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | Mechanistic Review | FASEB Journal | Reviews FP receptor biology in hair follicles; proposes bimatoprost as a novel scalp alopecia therapy; draws explicit mechanistic parallel with minoxidil's serendipitous repurposing from an antihypertensive — provides the conceptual framework for this repurposing candidate |
| [27377163](https://pubmed.ncbi.nlm.nih.gov/27377163/) | 2016 | Case Report | Pediatric Dermatology | Successful treatment of steroid-resistant multifocal alopecia areata of the scalp in a paediatric patient using topical bimatoprost — proof-of-concept that the mechanism is active in immune-mediated, as well as androgenetic, alopecia |

---

## UK Market Information

No MHRA marketing authorisation records were retrieved for bimatoprost in the current dataset (market status: not marketed; 0 licences on record). This is likely a data collection gap rather than a true absence of UK licensing.

Healthcare professionals should verify current UK authorisation status directly via:

- **MHRA Product Licence database**: https://products.mhra.gov.uk/
- **British National Formulary (BNF)**: Ophthalmologicals / prostaglandin analogues section
- **NICE guidance**: Review any relevant technology appraisals for glaucoma management

> International regulatory context: Bimatoprost is authorised in multiple jurisdictions as *Lumigan* (ophthalmic solution for glaucoma/ocular hypertension) and *Latisse* (0.03% for eyelash hypotrichosis). The current MHRA-approved SmPC should be consulted for UK-specific prescribing information, approved indications, and contraindications relevant to any new use.

---

## Safety Considerations

Safety data specific to bimatoprost was not available in this evidence pack. Please refer to the current SmPC and BNF for full prescribing information. Report suspected adverse reactions via the **Yellow Card Scheme**: https://yellowcard.mhra.gov.uk/

**Early termination of NCT02676310:** The Phase 1 dose escalation study in male AGA was terminated after enrolling 53 participants. The reason is not documented in the available data and must be clarified — specifically whether a safety signal (e.g., systemic prostaglandin effects, ocular exposure from scalp absorption, cutaneous irritation) contributed to the decision.

**Formulation-specific concern:** Topical scalp application involves substantially higher drug dose per application area than ophthalmic drops. Systemic absorption and class-effect risks (prostaglandin-mediated: vasodilation, bronchospasm in susceptible individuals, periorbital fat changes) at scalp doses require careful review of PK data from NCT01189279 and NCT02848300.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for bimatoprost in alopecia is directly validated by the FDA-approved Latisse eyelash indication — not merely theoretical — and multiple completed Phase 2 RCTs across male AGA and female pattern hair loss provide a substantial clinical evidence base. However, Allergan's decision not to advance to Phase 3 despite completing three major Phase 2 studies with hundreds of participants is a material concern that must be understood before committing further development resources.

**To proceed, the following is needed:**

- Obtain and critically appraise full results from NCT01325337 and NCT01325350 (the two pivotal Phase 2 RCTs, 307 and 306 participants respectively) — determine whether primary endpoints (e.g., target area hair count, hair density) were met and assess the effect size relative to minoxidil comparator
- Clarify the reason for early termination of NCT02676310 — specifically rule out or characterise any safety signal at the dose levels studied
- Retrieve the current MHRA SmPC for Lumigan (bimatoprost ophthalmic solution) — confirm licensed indications, contraindications, and warnings applicable to any new use
- Obtain detailed MOA data from DrugBank (DB00905) and primary pharmacology literature to complete the mechanistic dossier
- Confirm current UK authorisation status via the MHRA product licence database
- Assess whether a topical scalp formulation requires a separate new marketing authorisation or can be pursued under a line extension to an existing licence
- Evaluate a regulatory bridging strategy using the Latisse (eyelash hypotrichosis) approval as precedent for an expanded hair indication
- If Phase 3 is contemplated, consider early scientific advice from MHRA and a NICE Health Technology Assessment scoping exercise

---

*This report is generated for research purposes only and does not constitute medical advice. Repurposing candidates require full clinical validation before any therapeutic application. All predictions should be interpreted in the context of complete clinical, safety, and regulatory review.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

