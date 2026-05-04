---
layout: default
title: Camphor
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Camphor
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

# Camphor: From Unlicensed Use to Migraine Disorder

## One-Sentence Summary

Camphor is a naturally occurring bicyclic monoterpenoid with a long history of topical application as a counterirritant; it currently holds no marketing authorisation in the United Kingdom and has no formally approved therapeutic indication.
The TxGNN model predicts a potential role in **Migraine Disorder**, achieving a prediction score of **99.85%** (rank 2,125 amongst all evaluated drug–disease pairs).
Supporting clinical evidence is sparse: **no dedicated clinical trials** have been registered, and the **5 available publications** relate primarily to case reports of headache *exacerbation* rather than therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally approved indication (not licensed in the UK) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Camphor is a known agonist of TRPV1 (transient receptor potential vanilloid 1) and TRPA1 ion channels, both of which are expressed on trigeminal sensory neurons and have well-established roles in nociceptive signalling. TRPV1 activation influences the release of calcitonin gene-related peptide (CGRP) — the central mediator in migraine pathophysiology and the molecular target of recently approved anti-CGRP monoclonal antibodies (such as erenumab and fremanezumab). In this context, the TxGNN prediction carries a degree of biological plausibility: a drug capable of modulating the TRPV1–CGRP axis could, in theory, influence migraine pain processing.

Camphor also has a counterirritant mechanism of action, whereby stimulation of peripheral nociceptors may paradoxically dampen the perception of deeper or more diffuse pain signals — a principle exploited in various topical analgesic preparations. Traditional medicine systems across multiple cultures have used camphor-containing preparations topically for headache relief, lending further historical plausibility to this prediction direction.

However, a critical concern must be highlighted: the two most directly relevant publications in the available evidence base document camphor-containing essential oil products **triggering** cluster headache in susceptible patients, rather than alleviating it. This adverse signal inverts the expected therapeutic direction and substantially complicates the risk–benefit assessment. No formal preclinical or clinical studies have evaluated camphor's effect on migraine outcomes in a controlled setting, and the mechanistic evidence, whilst biologically interesting, remains highly speculative.

---

## Clinical Trial Evidence

Currently no clinical trials evaluating camphor in migraine disorder have been registered on ClinicalTrials.gov or the ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | Phase 3 RCT | The Journal of Headache and Pain | ⚠️ False positive: Phase 3 study of **erenumab** (anti-CGRP monoclonal antibody) for chronic migraine prevention in Asian patients — not a camphor study; retrieved due to keyword overlap |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case Series | Headache | Five patients developed cluster headache following use of toothpastes containing pro-convulsant essential oils including camphor — documents an **adverse effect** rather than therapeutic benefit |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case Report | BMJ Case Reports | Two cases of cluster headache temporally related to use of camphor- and eucalyptus-containing toothpastes — further **adverse effect signal** directly implicating camphor |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Historical Review | Zeitschrift für Kinder- und Jugendpsychiatrie und Psychotherapie | Broad historical review of neuropsychopharmacological treatments used in children and adolescents in the 1940s–50s; only tangential relevance to camphor or migraine |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Historical Report | Minerva Medica | Historical Italian-language report on the therapy of essential hemicrania; no abstract available; clinical context and methodology cannot be assessed |

---

## UK Market Information

Camphor holds no MHRA marketing authorisation and is not currently available as a licensed medicinal product in its own right in the United Kingdom. It may appear as an excipient or active ingredient in some unlicensed traditional or herbal preparations, but no Product Licences (PLs) are on record. There are no authorisations to tabulate.

Clinicians considering any clinical use should note that camphor would need to be assessed under UK medicines legislation (Human Medicines Regulations 2012) prior to any formal therapeutic evaluation.

---

## Safety Considerations

Detailed safety data for camphor are not available in the current Evidence Pack.

> **Important adverse effect signal from the literature**: Two peer-reviewed publications (PMIDs [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) and [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/)) document cluster headache triggered by topical camphor-containing essential oil products. Healthcare professionals should be aware that camphor may **provoke rather than relieve** headache disorders in susceptible individuals — this directly conflicts with the proposed therapeutic direction and represents a key safety concern.
>
> Additionally, camphor is a known CNS stimulant at higher doses and has a well-established seizure risk (it is classified as pro-convulsant), which is particularly relevant given its overlap with a predominantly neurological patient population.

Please refer to the relevant Summary of Product Characteristics (SmPC) and the BNF for any formulation-specific safety information. Suspected adverse reactions should be reported via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score and theoretical mechanistic plausibility through the TRPV1–CGRP pathway, camphor currently has no UK marketing authorisation, no registered clinical trials in migraine, and the available clinical literature predominantly documents a **headache-triggering** rather than analgesic effect. The evidence base is insufficient — and potentially cautionary — to support clinical development without substantial prior research.

**To proceed, the following is needed:**

- **Preclinical programme**: Controlled studies evaluating camphor's dose-dependent effects on trigeminal nociception, CGRP release, and cortical spreading depression in validated migraine models
- **Safety signal resolution**: Formal investigation into whether camphor at sub-counterirritant doses relieves or exacerbates headache, distinguishing acute provocation effects from potential preventive mechanisms
- **Mechanistic characterisation**: Full elucidation of the pharmacological mechanism of action (MOA), dose–response relationship, and any therapeutic window between analgesic and pro-convulsant doses
- **Route of administration assessment**: Determination of whether a topical, intranasal, or other route could deliver therapeutic concentrations without systemic CNS effects
- **Regulatory pathway scoping**: Engagement with the MHRA regarding camphor's regulatory status in the UK before any human studies are initiated
- **Systematic review**: A formal critical appraisal of traditional medicine claims for camphor in headache, to establish whether historical use reflects genuine efficacy or confounding factors

> *This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require formal clinical validation before therapeutic application. Results generated by the TxGNN model should be interpreted with appropriate caution.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

