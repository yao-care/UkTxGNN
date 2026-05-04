---
layout: default
title: Selenium
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 1
---

# Selenium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Selenium: From Nutritional Supplementation to Sclerosing Cholangitis

## One-Sentence Summary

Selenium is an essential trace element recognised for its role in antioxidant enzyme systems, and is used clinically as a nutritional supplement rather than for a formally approved therapeutic indication.
The TxGNN model predicts it may have therapeutic potential in **Sclerosing Cholangitis**,
with **no registered clinical trials** and **5 observational or review publications** currently supporting this direction.
The overall evidence base remains preclinical and hypothesis-generating.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nutritional supplementation (essential trace element; no formal approved therapeutic indication on record) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L4 |
| UK Market Status | Not authorised in the UK |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Selenium is an essential trace element that is biologically incorporated as selenocysteine into key antioxidant enzymes, including glutathione peroxidase (GPx) and thioredoxin reductase. These enzymes are central to the cellular defence against oxidative damage, and selenium has been investigated in a range of inflammatory and fibrotic conditions for its potential to attenuate oxidative stress pathways.

Primary sclerosing cholangitis (PSC) is a chronic, progressive cholestatic liver disease characterised by biliary inflammation and fibrosis, driven in part by oxidative stress, TGF-β-mediated fibrogenesis, and dysregulation of the gut–biliary axis. Published observational data (PMID 9053974) have documented abnormal hepatic selenium retention in PSC patients, suggesting that selenium metabolism may be perturbed in this disease. Whether this reflects a causative factor or a secondary consequence of impaired biliary function remains unresolved.

The TxGNN model's high prediction score (99.04%) most likely reflects a knowledge graph pathway linking GPx → oxidative stress → biliary fibrosis. Whilst mechanistically plausible, this remains a computational inference. No interventional studies have examined whether selenium supplementation can meaningfully reduce biliary inflammation or slow fibrosis progression in PSC. This prediction should therefore be regarded as hypothesis-generating rather than practice-informing at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Selenium in sclerosing cholangitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Cross-sectional / Observational | Scandinavian Journal of Gastroenterology | Trace element metabolism studied in 32 PSC patients; hepatic copper and selenium retention identified, suggesting abnormal selenium metabolism in PSC |
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | Dietary Survey / Cross-sectional | Liver International | Evaluated dietary intake in PSC patients vs Nordic Nutrition Recommendations 2023; poor fat-soluble vitamin intake and suboptimal overall dietary quality documented |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Clinical Study / Nutrition | JPEN: Journal of Parenteral and Enteral Nutrition | Case report of parenteral nutrition management in overlapping PSC and ulcerative colitis; discusses oxidative stress and antioxidant deficiency as contributors to cholestatic disease pathogenesis |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | Animal Model / Proteomics | Proteomics | Hepatic proteome changes characterised in murine models of toxic-induced fibrogenesis and sclerosing cholangitis; mechanistic basis of hepatic protein expression changes discussed |
| [18941372](https://pubmed.ncbi.nlm.nih.gov/18941372/) | 2008 | Review / Chemoprevention | European Journal of Cancer Prevention | Review of chemopreventive agents in colorectal cancer, including selenium; indirect relevance to PSC-associated colorectal cancer risk only |

---

## UK Market Information

Selenium (DrugBank ID: DB11135) currently holds no MHRA marketing authorisation. There are no licensed medicinal products on the UK market for this compound as a standalone therapeutic agent.

> **Note:** Selenium-containing formulations are available as unlicensed dietary supplements and may appear as a micronutrient component within licensed parenteral nutrition solutions. However, no product holds a UK marketing authorisation for selenium as a named therapeutic indication.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Additional note for prescribers:** Selenium has a narrow therapeutic window. Chronic intake above approximately 400 µg/day may result in selenosis (hair loss, nail brittleness, gastrointestinal disturbance, peripheral neuropathy). Any interventional use outside of nutritional support should be subject to formal dose-finding evaluation and toxicity monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically plausible given selenium's antioxidant properties and documented perturbation of selenium metabolism in PSC, but the evidence base is entirely observational and preclinical (L4), with no registered interventional trials and no MHRA marketing authorisation for any therapeutic indication.

**To proceed, the following is needed:**
- Systematic review or meta-analysis of selenium status and supplementation outcomes in PSC and related cholestatic liver diseases
- Proof-of-concept interventional study (e.g., pilot RCT assessing selenium supplementation in PSC patients with confirmed selenium deficiency)
- Detailed mechanism of action data (MOA) confirming GPx-mediated antifibrotic activity specifically within biliary epithelium
- Safety and dose-ranging data at therapeutic (as opposed to nutritional supplementation) dosing levels, given selenium's narrow therapeutic index
- Early regulatory dialogue with MHRA to establish a viable development pathway for an unlicensed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

