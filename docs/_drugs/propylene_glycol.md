---
layout: default
title: Propylene Glycol
parent: Model Prediction Only (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
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

# Propylene Glycol: From Pharmaceutical Excipient to Bronchitis (Signal Not Supported by Current Evidence)

## One-Sentence Summary

Propylene glycol has no approved therapeutic indication of its own — it is used almost exclusively as a pharmaceutical excipient and solvent (e.g. in inhalation and ophthalmic formulations). The TxGNN model predicts a possible link to **Bronchitis**, but on close inspection the underlying **4 clinical trials** relate to Cyclosporine Inhalation Solution (with propylene glycol only as a solvent), and the **3 supporting publications** actually discuss propylene glycol as a *risk* factor in e-cigarette-associated lung injury rather than as a treatment. This is very likely a knowledge-graph co-occurrence artefact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None — propylene glycol has no approved therapeutic indication; it is used solely as a pharmaceutical excipient/solvent |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (mechanistic/preclinical only; cited trials do not test PG as the active substance) |
| UK Market Status | Not marketed as a standalone medicinal product |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for propylene glycol as a therapeutic agent is not available, and none is expected: propylene glycol is a small-molecule diol used industry-wide as a solvent/vehicle in inhaled, oral, topical and ophthalmic pharmaceutical products, not as a pharmacologically active drug in its own right.

The TxGNN score for bronchitis appears high, but the four supporting clinical trials all investigate **Cyclosporine Inhalation Solution (CIS)** for bronchiolitis obliterans syndrome after lung/stem-cell transplantation. In each of these studies, propylene glycol (or a related excipient) is present only as part of the inhalation vehicle — the active substance being tested is cyclosporine, not propylene glycol. Efficacy signals from these trials cannot be attributed to propylene glycol itself.

The literature evidence points in the opposite direction to a therapeutic benefit: the three cited publications are reviews/animal studies discussing e-cigarette liquid constituents (propylene glycol and vegetable glycerin) as **potential contributors to airway injury, chronic bronchitis and COPD-like pathology**, not as treatments for bronchitis. Taken together, the most plausible explanation is that TxGNN has picked up a co-occurrence pattern (propylene glycol frequently appears in inhaled-drug knowledge-graph nodes) rather than a true drug–disease pharmacological relationship.

---

## Clinical Trial Evidence

*(Extracted from the top-ranked predicted indication: Bronchitis)*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | Cyclosporine Inhalation Solution (CIS) in bronchiolitis obliterans syndrome after transplant. **PG relevance: Low (Grade C)** — PG is a formulation excipient, not the active substance; efficacy cannot be attributed to PG |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | Terminated | 17 | Long-term follow-up extension of inhaled cyclosporine for chronic rejection prevention. **PG relevance: Low (Grade C)** — trial terminated; cyclosporine is the active agent |
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Randomised controlled trial of CIS to prevent bronchiolitis obliterans syndrome post lung transplant. **PG relevance: Low (Grade C)** — cyclosporine is the active substance |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended-access CIS for bronchiolitis obliterans in transplant recipients. **PG relevance: Low (Grade C)** — extension study, not evidence of PG efficacy |

**Note:** None of these trials test propylene glycol as the active investigational product; all relevance gradings are "C" (low), indicating the evidence should not be interpreted as support for propylene glycol's efficacy in bronchitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | American Journal of Physiology – Lung Cellular and Molecular Physiology | Discusses whether chronic e-cigarette use (propylene glycol/glycerin-based liquids) may cause lung disease, including chronic bronchitis — a **risk**, not a treatment, signal |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Current Allergy and Asthma Reports | Reviews e-cigarette constituents (including propylene glycol) as airway irritants potentially worsening pre-existing respiratory disease |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Animal model | Respiratory Research | Elastase/LPS mouse model of COPD/chronic bronchitis; does not investigate propylene glycol |

**Note:** This literature set does not provide evidence of therapeutic benefit for propylene glycol in bronchitis; two of the three papers instead flag propylene glycol-containing aerosols as a possible cause of airway injury.

---

## UK Market Information

Propylene glycol is not currently marketed in the UK as a standalone medicinal product, and no marketing authorisations are recorded in this evidence pack. It is widely present as a licensed **excipient** within numerous MHRA-authorised products (oral, topical, inhaled and ophthalmic formulations), but this evidence pack does not contain product-level excipient licensing data.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug-specific warnings, contraindications or interaction data were available in this evidence pack to review. Given the literature signal that propylene glycol/glycerin aerosols may be associated with airway irritation, any inhalation-route development should specifically consider respiratory tolerability.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The apparent TxGNN signal for bronchitis is not supported on closer review: the cited trials test cyclosporine (not propylene glycol) as the active substance, and the cited literature associates propylene glycol aerosol exposure with respiratory *harm* rather than benefit. Combined with the complete absence of an original indication, marketing authorisation, or defined mechanism of action for propylene glycol as a therapeutic agent, this candidate does not meet the threshold to proceed. The nine lower-ranked predictions (diabetic retinopathy, and seven cataract subtypes) are similarly unsupported — most are rated L5 with no clinical trial or literature evidence at all, and several share identical TxGNN scores, suggesting ontology-clustering artefacts rather than independent pharmacological signals.

**To proceed, the following is needed:**
- Confirmation of whether propylene glycol has any genuine, non-excipient pharmacological activity relevant to airway or ocular disease (currently no MOA data available)
- Independent evidence (trials or studies) in which propylene glycol itself, not a co-formulated active drug, is the investigational agent
- Reassessment of the TxGNN candidate list to exclude likely knowledge-graph co-occurrence/ontology-clustering artefacts (notably the near-identical scores across cataract subtypes)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

