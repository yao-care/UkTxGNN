---
layout: default
title: Flurbiprofen
parent: High Evidence (L1-L2)
nav_order: 281
evidence_level: L1
indication_count: 10
---

# Flurbiprofen
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

Flurbiprofen 的十個 TxGNN 候選中，rank 1（acromesomelic dysplasia）分數最高但 evidence pack 自身的 rationale 已標註為知識圖譜嵌入偏差、無臨床意義；只有 rank 8（ankylosing spondylitis）有實質文獻證據（L1、20篇文獻、S3、Proceed with Guardrails）。依報告角色設定的專業判斷，以 rank 8 作為本報告主軸，並在文中說明排除 rank 1 的理由。

# Flurbiprofen: From NSAID Analgesic Use to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen is a propionic-acid derivative NSAID; it is not currently marketed in the UK. Among ten TxGNN-predicted indications reviewed, only **Ankylosing Spondylitis** is supported by genuine clinical evidence — **20 publications**, including seven randomised controlled trials from the 1970s–1980s. The remaining nine top-ranked predictions (mostly rare congenital skeletal dysplasias) are flagged in the evidence pack itself as knowledge-graph embedding artefacts with no plausible inflammatory mechanism and no supporting literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No UK marketing authorisation data available (drug not currently marketed in the UK) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% (model rank 750) |
| Evidence Level | L1 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on known pharmacology, flurbiprofen is a propionic-acid derivative, non-steroidal anti-inflammatory drug (NSAID) that inhibits cyclo-oxygenase (COX-1/COX-2), reducing prostaglandin synthesis and producing analgesic, anti-inflammatory and antipyretic effects — the standard NSAID class mechanism.

Ankylosing spondylitis (AS) is a chronic inflammatory spondyloarthropathy in which NSAIDs are first-line, guideline-standard symptomatic therapy. The mechanistic link here is not a novel repurposing hypothesis: it is a well-established NSAID class effect, and the cited literature (dating from 1974–1986) shows flurbiprofen was directly and repeatedly studied head-to-head against indomethacin, phenylbutazone and naproxen specifically in AS populations.

Note on the model's top-ranked candidate: TxGNN's single highest-scoring prediction (acromesomelic dysplasia, Hunter-Thompson type, score 99.99%) and several other top-10 candidates are structural/genetic skeletal or connective-tissue disorders with no inflammatory pathology relevant to NSAID action. The evidence pack's own rationale identifies these as likely artefacts of node proximity within a "skeletal system" cluster in the knowledge graph, without clinical meaning — no trials or literature exist for any of them. Ankylosing spondylitis, ranked 8th by score but the only candidate reaching evidence stage S3, is therefore the clinically meaningful signal in this set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT (double-blind, parallel) | Current Medical Research and Opinion | Flurbiprofen 150–200mg/day vs indomethacin 75–100mg/day, 26 AS patients, 6 weeks; both equally effective for pain and joint tenderness |
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT (double-blind crossover) | British Medical Journal | Flurbiprofen 150mg/day vs phenylbutazone 300mg/day, 35 AS patients, 4 weeks; flurbiprofen well tolerated, efficacy approaching phenylbutazone |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT (double-blind crossover) | The New Zealand Medical Journal | Flurbiprofen 200mg/day vs naproxen 750mg/day, 30 AS patients, 4 weeks; both effective, no significant difference; more side effects with flurbiprofen |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT (double-blind, randomised) | The American Journal of Medicine | Flurbiprofen 200mg/day vs indomethacin, 57 AS patients, 26 weeks; effective pain control, some patients controlled on 100mg BID |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT (double-blind, parallel) | Southern Medical Journal | Flurbiprofen vs indomethacin, 26 AS patients, 6 weeks; equally effective for pain and tenderness relief |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT (double-blind, randomised) | The American Journal of Medicine | Flurbiprofen 200mg/day vs phenylbutazone 300mg/day, 90 AS patients, 26 weeks; equally effective |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT (double-blind, parallel) | European Journal of Clinical Pharmacology | Flurbiprofen vs phenylbutazone, 27 AS patients, 6 weeks; equally effective, phenylbutazone non-significantly favoured |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Cohort/Safety | The American Journal of Medicine | Pooled renal/hepatic safety data from 9 Phase III trials, 1,677 patients (AS, OA, RA); no clinically significant abnormalities |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Review of flurbiprofen pharmacology and use in rheumatic disease incl. AS; efficacy comparable to aspirin/indomethacin with fewer side effects |
| [3514311](https://pubmed.ncbi.nlm.nih.gov/3514311/) | 1986 | Open-label, multicentre | The Journal of International Medical Research | 336 AS/psoriatic arthropathy patients (of 1,396 total), 12-month UK study; significant pain improvement from week 2 onward |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Seven double-blind RCTs plus pooled safety data consistently support flurbiprofen's efficacy in ankylosing spondylitis, comparable to indomethacin, phenylbutazone and naproxen — this is an established NSAID class-effect indication rather than a novel mechanistic hypothesis. However, flurbiprofen currently holds no UK marketing authorisation, and the supporting evidence predates 1990 with no modern comparator (e.g. COX-2 selective agents, biologics) or placebo-controlled data.

**To proceed, the following is needed:**
- SmPC/BNF-equivalent warnings, contraindications and DDI data (currently a Blocking data gap — DG001)
- Confirmed mechanism of action documentation (High-priority data gap — DG002)
- A UK licensing or import pathway assessment, since the product is not currently marketed
- Contemporary comparative evidence against current standard-of-care AS therapy (modern NSAIDs, biologics)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

