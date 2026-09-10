---
layout: default
title: Mexiletine
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Mexiletine
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

# Mexiletine: From Cardiac Arrhythmia to Headache Disorder (Trigeminal Autonomic Cephalalgia)

## One-Sentence Summary

Mexiletine is a Class Ib antiarrhythmic (sodium channel blocker), historically used for ventricular arrhythmias and more commonly repurposed off-label today for myotonia and neuropathic pain. The TxGNN model — together with a cluster of case-series and open-label literature — points to **Headache Disorder, particularly trigeminal autonomic cephalalgias (TACs) and refractory chronic daily headache**, as the most credible repurposing signal among ten candidates generated, supported by **7 relevant publications** and **no registered clinical trials**.

> **Note on methodology**: TxGNN generated 10 candidate indications for this drug. The single highest-scoring candidate (hypertrichosis, 99.78%) and five others (NSIAD, Ambras syndrome, Dandy-Walker syndrome, hair shaft abnormality, migraine with brainstem aura) were explicitly flagged in the evidence pack itself as biologically implausible "graph noise" with zero supporting literature or mechanistic rationale. This report therefore focuses on the two candidates — **Headache Disorder** (rank 10) and **Migraine Disorder** (rank 6) — for which genuine, drug-specific literature exists.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack's regulatory data (no licences on file); literature within the pack identifies mexiletine as a Class Ib antiarrhythmic, also used off-label for myotonia and neuropathic pain |
| Predicted New Indication | Headache Disorder (incl. trigeminal autonomic cephalalgias / SUNCT-SUNA) |
| TxGNN Prediction Score | 99.48% (rank 5162 of candidate pool) |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). However, the literature captured alongside the prediction confirms mexiletine's known pharmacology: it is a Class Ib antiarrhythmic that blocks voltage-gated sodium channels (including neuronal Nav1.7/Nav1.8), an action already established as the basis for its use in myotonia and neuropathic pain.

Headache disorders — particularly trigeminal autonomic cephalalgias such as SUNCT/SUNA — are thought to involve abnormal, hyperexcitable firing within the trigeminovascular system. Sodium channel blockade is a mechanistically plausible way to dampen this abnormal neuronal firing, which is consistent with mexiletine's established use in other channelopathy-driven pain conditions. This provides a coherent, if not yet definitively proven, rationale for the prediction.

Supporting this, the evidence pack contains a near-40-year span of clinical reports (1981–2021) describing mexiletine's use specifically for vascular/chronic daily headache and, in combination with IV lidocaine, for TACs — giving this candidate a track record of real-world clinical interest rather than being a purely model-generated association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40197813](https://pubmed.ncbi.nlm.nih.gov/40197813/) | 2025 | Cochrane Review (myotonia, tangential) | Cochrane Database Syst Rev | Reviews drug treatment for myotonic disorders; sodium-channel blockers (incl. mexiletine class) are standard therapy, supporting the underlying channel-blockade mechanism |
| [24820732](https://pubmed.ncbi.nlm.nih.gov/24820732/) | 2014 | Review (general, tangential) | Curr Pain Headache Rep | Update on new daily persistent headache; no specific treatment established, highlighting an unmet need this candidate could address |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective open-label study (single-arm meta-analysis) | J Neurol Neurosurg Psychiatry | Evaluates medical treatment options for SUNCT/SUNA, a condition with very limited evidence-based options |
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Case series / open-label | Curr Pain Headache Rep | IV lidocaine and mexiletine (both Class Ib sodium channel blockers) used in management of trigeminal autonomic cephalalgias, with reported efficacy in neuropathic-type pain syndromes |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case series (n=9) | Headache | Mexiletine used for refractory chronic daily headache in a treatment-resistant population |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Case series | N Z Med J | Early report describing mexiletine's use in vascular headaches |

*One additional paper (PMID 91699, 1979) was excluded as irrelevant — it concerns mexiletine's antiarrhythmic use in ventricular extrasystoles and does not relate to headache.*

---

## UK Market Information

No UK marketing authorisations are currently recorded for mexiletine in this evidence pack (0 licences on file, market status: not marketed). Before any further development, current UK/MHRA licensing status should be independently confirmed, as historical mexiletine products (e.g. Mexitil) may no longer hold active marketing authorisation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Key warnings, contraindications and drug-drug interaction data were flagged as a Blocking data gap in this evidence pack (TFDA/MHRA label data not yet retrieved) and are not available for review. This gap must be resolved before any Phase S1 safety assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the headache disorder / TAC indication is limited to case series and one prospective open-label study spanning four decades (L3, no RCTs), and the compound currently has no UK marketing authorisation. Critically, mandatory safety data (SmPC warnings, contraindications, DDI) is entirely missing, which blocks any formal S1 safety evaluation regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- Retrieve MHRA/SmPC label data (warnings, contraindications, interactions) — currently a Blocking gap
- Confirm formal mechanism-of-action data via DrugBank to support the mechanistic rationale
- Assess whether a controlled trial (vs. case series) exists or could be designed for mexiletine in TACs/refractory headache
- Clarify current UK licensing/import pathway status, given the drug is not currently marketed
- Deprioritise the six candidates explicitly flagged as graph noise (hypertrichosis, NSIAD, Ambras syndrome, Dandy-Walker–associated syndrome, isolated hair shaft abnormality, migraine with brainstem aura) and treat pulmonary hypertension (rank 8) as a low-confidence, drug-class-analogy signal only, since supporting evidence relates to lidocaine, not mexiletine directly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

