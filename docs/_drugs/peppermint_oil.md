---
layout: default
title: Peppermint Oil
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil: From No UK-Licensed Indication to Cardiovascular Disease

## One-Sentence Summary

Peppermint oil (DrugBank DB11198) has no UK marketing authorisation on record, and no original indication or mechanism-of-action data is available in this evidence pack. TxGNN generated 10 candidate indications, but of these only **Cardiovascular Disease** is backed by real clinical trial and literature evidence — **2 completed exploratory trials** and **6 relevant publications**, supporting a plausible menthol/TRPM8-mediated mechanism, though none of the trials is a confirmatory Phase 2/3 RCT.

> **Important caveat:** the highest-scoring TxGNN prediction (leprosy, 99.80%, rank 1) and 7 of the other 9 candidates have **zero supporting trials or literature** and are explicitly flagged in this evidence pack as likely knowledge-graph noise rather than genuine signal. This report therefore focuses on the one candidate — Cardiovascular Disease — where actual evidence exists.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — peppermint oil has no UK marketing authorisation on record (0 licences); `original_moa` is also a recorded data gap |
| Predicted New Indication | Cardiovascular Disease |
| TxGNN Prediction Score | 99.13% (rank 9,343 of 9,996 candidates) |
| Evidence Level | L3 (small completed exploratory trials + supporting literature; no confirmatory Phase 2/3 RCT) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for peppermint oil is not available in this evidence pack (recorded as a High-severity data gap, DG002). Based on the supporting literature identified for the cardiovascular disease candidate, peppermint oil's principal active constituent, **menthol**, is a known TRPM8 (transient receptor potential melastatin 8) receptor agonist. One physiology study (PMID 30070742) found that gastric cooling combined with menthol increased cardiac parasympathetic efferent activity in healthy adult volunteers, offering a plausible physiological route by which oral peppermint intake could influence blood pressure and cardiac autonomic tone.

Two small, completed (but non-phase-designated) human trials have since tested this directly: one assessed oral peppermint supplementation on cardiometabolic parameters (n=36), and a second assessed effects on cardiometabolic outcomes in participants with mild-to-moderate hypertension (n=40). A subsequent RCT protocol (PMID 40333716, published 2025) was designed specifically to test peppermint oil against placebo in pre-hypertension and stage 1 hypertension, indicating active research interest but no completed confirmatory RCT result yet.

By contrast, the remaining 9 TxGNN candidates in this pack — including the top-ranked prediction, leprosy (99.80%) — have no clinical trials, no literature, and no plausible mechanistic rationale beyond a general note that menthol/peppermint pharmacology (TRPM8 activation, antispasmodic effects) does not connect meaningfully to conditions such as leprosy, pneumocystosis, or vocal cord/uterine/middle ear/frontal sinus polyps. These are explicitly annotated in the evidence pack as likely artefacts of the knowledge-graph model rather than genuine repurposing signals, and are scored Evidence Level L5 with a "Hold" recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05071833](https://clinicaltrials.gov/study/NCT05071833) | N/A (exploratory) | Completed | 36 | Assessed effects of oral peppermint supplementation on cardiometabolic parameters; explored dietary intervention as a lower-risk alternative to pharmacological therapy |
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | N/A (exploratory) | Completed | 40 | Assessed peppermint oil effects on cardiometabolic outcomes in participants with mild-to-moderate hypertension; builds on earlier randomised findings of improved systolic blood pressure |

*Note: one additional registered trial (NCT04966546) was identified in the search but assessed as not relevant — it concerned cortical spreading depolarisation after chronic subdural haematoma surgery, unrelated to cardiovascular disease, and was withdrawn (n=0). It has been excluded from this table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | RCT (protocol) | PLoS One | Protocol for a placebo-controlled RCT of peppermint oil in pre- and stage 1 hypertension; notes menthol/flavonoid content as basis for hypothesised hypotensive benefit |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Physiological intervention study | Experimental Physiology | Gastric cooling combined with menthol increased cardiac parasympathetic efferent activity in healthy adults, reducing heart rate |
| [25037671](https://pubmed.ncbi.nlm.nih.gov/25037671/) | 2014 | Review | Explore (New York, N.Y.) | Brief evidence review covering peppermint oil for irritable bowel syndrome among other complementary therapies |
| [19198983](https://pubmed.ncbi.nlm.nih.gov/19198983/) | 2009 | Review | Internal and Emergency Medicine | General practice/cardiovascular medicine evidence update |
| [27277875](https://pubmed.ncbi.nlm.nih.gov/27277875/) | 2016 | Analytical methodology study | Bioanalysis | Real-time breath analysis of exhaled menthone following oral peppermint oil capsule ingestion; confirms systemic absorption/metabolism kinetics |
| [17577363](https://pubmed.ncbi.nlm.nih.gov/17577363/) | 2007 | Case report | Contact Dermatitis | Allergic contact dermatitis reported following use of a peppermint foot spray (safety signal) |

*Note: two additional records returned by the literature search (PMID 39139335, PMID 28889028) concerned formulation studies of unrelated drugs (lercanidipine, candesartan) and were excluded as not relevant to peppermint oil.*

---

## UK Market Information

Peppermint oil has no UK marketing authorisation recorded in this evidence pack (0 licences). It may be available as a food supplement or traditional herbal remedy outside MHRA prescription-medicine licensing, but no such record is captured here — this should be verified separately against the MHRA Traditional Herbal Registration (THR) scheme if relevant.

---

## Safety Considerations

Key warnings, contraindications and drug-interaction data are recorded as data gaps (DG001, Blocking severity — MHRA/SmPC label data has not yet been retrieved). One relevant safety signal was identified in the literature search: a case report of allergic contact dermatitis following topical peppermint oil use (PMID 17577363), which should be noted for topical/dermal exposure but does not inform oral-route safety.

Please refer to the SmPC and BNF for full safety information once a UK-licensed or THR-registered product is identified. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only candidate with genuine supporting evidence — cardiovascular disease — is based solely on small, non-phase-designated exploratory trials (n=36–40) and a not-yet-completed placebo RCT protocol; this does not meet the bar for progression. Separately, the Blocking data gap on UK/MHRA warnings and contraindications (DG001) means this candidate cannot yet enter formal safety screening (S1) regardless of the clinical evidence.

**To proceed, the following is needed:**
- Retrieval of MHRA/SmPC warnings, contraindications and interaction data for peppermint oil (resolves DG001, currently Blocking)
- Mechanism-of-action data from DrugBank (resolves DG002)
- Completion and publication of the ongoing placebo-controlled RCT (PMID 40333716 protocol) to establish a confirmatory efficacy signal
- Clarification of current UK availability status (e.g. THR registration, food supplement classification) given 0 formal marketing authorisations are on record
- No further action recommended on the remaining 9 TxGNN candidates (including the top-ranked leprosy prediction) unless independent supporting evidence emerges, as they currently show no clinical trial or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

