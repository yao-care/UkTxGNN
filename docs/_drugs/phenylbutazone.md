---
layout: default
title: Phenylbutazone
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Phenylbutazone
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

# Phenylbutazone: Revisiting a Historical NSAID Use in Rheumatoid Arthritis

## One-Sentence Summary

Phenylbutazone is a pyrazolone-class NSAID with no confirmed marketing authorisation currently on record in the UK dataset. TxGNN's top-ranked prediction is **Rheumatoid Arthritis**, but the underlying evidence indicates this is largely a re-identification of the drug's long-established historical use rather than a novel repurposing signal, supported by **20 publications** (no registered clinical trials) spanning 1952–2009.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the regulatory dataset; historically used as a pyrazolone NSAID for rheumatic/inflammatory joint disease |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` is unrecorded in this dataset). Based on the supporting literature and repurposing rationale, phenylbutazone is a **pyrazolone-class NSAID** that inhibits COX-1/COX-2, producing anti-inflammatory and analgesic effects — a mechanism directly relevant to the joint inflammation seen in rheumatoid arthritis.

Importantly, the evidence pack itself flags that rheumatoid arthritis is **not a novel predicted use** for this drug, but rather a condition in which phenylbutazone already has a long clinical history (dating back to the 1950s–1980s double-blind trials). The same pattern holds for two other high-ranking predictions in this pack — **gout** (rank 4) and **osteoarthritis** (rank 7) — both supported by head-to-head trials against comparator NSAIDs (naproxen, indomethacin, flufenamic acid, aspirin). This suggests TxGNN is largely recovering the drug's established pharmacological class effect rather than surfacing a genuinely new therapeutic hypothesis.

By contrast, several lower-tier predictions in this pack (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, acromesomelic dysplasia, brachyolmia, myosclerosis) are rare congenital skeletal/connective-tissue disorders with **no supporting literature or trials (L5)** and no plausible mechanistic link to NSAID pharmacology. One prediction — sclerosing cholangitis — is arguably contraindicated in direction, since the RA literature includes a documented case of phenylbutazone-induced hepatitis, i.e. a hepatic *risk* signal rather than a therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4903691](https://pubmed.ncbi.nlm.nih.gov/4903691/) | 1969 | RCT | Canadian Medical Association journal | Double-blind comparison of monobutazone vs phenylbutazone in RA; fewer side effects with monobutazone |
| [788739](https://pubmed.ncbi.nlm.nih.gov/788739/) | 1976 | Cohort | British Journal of Clinical Pharmacology | Double-blind dose-response study (50–300 mg/day) showing plasma concentration correlates with clinical response |
| [913873](https://pubmed.ncbi.nlm.nih.gov/913873/) | 1977 | Cohort | Journal of International Medical Research | Double-blind dose-response study (50–400 mg/day); plasma levels linked to effectiveness |
| [6884415](https://pubmed.ncbi.nlm.nih.gov/6884415/) | 1983 | Dose-finding (double-blind) | European Journal of Clinical Pharmacology | Determined 300 mg/day as minimum effective dose across 8 dose levels; 7/32 patients had adverse reactions |
| [334476](https://pubmed.ncbi.nlm.nih.gov/334476/) | 1977 | Controlled trial | Current Medical Research and Opinion | Comparison of flurbiprofen vs phenylbutazone; rash observed in phenylbutazone arm |
| [6345427](https://pubmed.ncbi.nlm.nih.gov/6345427/) | 1983 | Double-blind trial | International Journal of Tissue Reactions | Suxibuzone (prodrug) vs phenylbutazone; comparable efficacy, significantly fewer GI side effects with prodrug |
| [786193](https://pubmed.ncbi.nlm.nih.gov/786193/) | 1976 | Review | Archives of Internal Medicine | Overview of RA treatment including anti-inflammatory agents |
| [13009482](https://pubmed.ncbi.nlm.nih.gov/13009482/) | 1952 | Clinical evaluation | California Medicine | Landmark 409-patient evaluation of phenylbutazone across rheumatic diseases including RA and gout |
| [1145012](https://pubmed.ncbi.nlm.nih.gov/1145012/) | 1975 | Case Report | Rheumatology and Rehabilitation | Phenylbutazone-associated hepatitis; review of 41 case histories (hepatic safety signal) |
| [13126544](https://pubmed.ncbi.nlm.nih.gov/13126544/) | 1954 | Clinical report | British Medical Journal | Early clinical experience with phenylbutazone use in RA |

---

## UK Market Information

Phenylbutazone currently holds **no marketing authorisations** on record in this dataset (market status: Not Marketed; total licences: 0). No product, dosage form, or approved indication text is available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: The evidence pack flags UK safety data (warnings/contraindications) as a **Blocking** data gap — this must be resolved before any safety review can proceed. Separately, literature evidence for this indication includes a documented case report of phenylbutazone-associated hepatitis (PMID 1145012), which should be considered when assessing hepatic risk.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The safety data gap (DG001, Blocking) means an initial safety assessment (S1) cannot be completed, regardless of efficacy evidence strength.
- The top prediction (rheumatoid arthritis) largely reflects the drug's own pre-existing historical use rather than a novel repurposing opportunity, and the drug has no current UK marketing authorisation to build on.
- The remaining higher-ranked predictions in this pack (rare skeletal dysplasias, sclerosing cholangitis) either lack any supporting evidence (L5) or point in a direction inconsistent with a known hepatotoxicity signal.

**To proceed, the following is needed:**
- UK SmPC/MHRA-equivalent safety data (warnings, contraindications, DDI) to resolve DG001
- Confirmed mechanism of action and formally documented original indication(s) to resolve DG002
- Clarification of UK regulatory/marketing pathway, given zero current licences
- If pursuing genuinely novel indications, independent mechanistic or preclinical validation for the L5-rated candidates, as none currently have literature or trial support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

