---
layout: default
title: Naratriptan
parent: Moderate Evidence (L3-L4)
nav_order: 404
evidence_level: L3
indication_count: 3
---

# Naratriptan
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **3** 
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

# Naratriptan: From Acute Migraine Treatment to Migraine with Brainstem Aura

## One-Sentence Summary

> Naratriptan is a triptan-class agent internationally used for the acute treatment of migraine attacks, though the local marketing authorisation and formal original-indication text are not available in this evidence pack (Naratriptan is not currently marketed under `taiwan_regulatory`). The TxGNN model's top prediction is **Migraine with Brainstem Aura**, but the supporting literature and pharmacological rationale indicate this is more likely a **known safety signal** (triptans are relatively/absolutely contraindicated in this migraine subtype) than a genuine new therapeutic opportunity, with only **0 clinical trials** and **20 publications**, none of which specifically study naratriptan in brainstem-aura migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no local marketing authorisation on record); internationally, naratriptan is indicated for acute treatment of migraine attacks with or without aura |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap for this drug. Based on known pharmacology, naratriptan is a selective **5-HT1B/1D receptor agonist**, exerting its acute anti-migraine effect through cranial vasoconstriction and inhibition of trigeminovascular nociceptive transmission — a well-established mechanism shared across the triptan class.

However, the relationship between the original indication (migraine) and the predicted indication (migraine **with brainstem aura**, formerly termed basilar-type migraine) is not a straightforward disease-expansion story. Because triptans act via vasoconstriction, and migraine with brainstem aura is theoretically associated with vertebrobasilar circulation involvement, current clinical guidance (including AHS/AAN evidence assessments) lists this subtype as a **relative or absolute contraindication** for triptan use rather than an approved or plausible extension of use. In other words, the high TxGNN score here most likely reflects a strong knowledge-graph association driven by shared "migraine" terminology and receptor biology, rather than evidence of therapeutic benefit.

Consequently, this prediction should be interpreted primarily as a **pharmacovigilance/safety signal worth verifying against the SmPC contraindications**, not as a novel repurposing opportunity to pursue for efficacy development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the identified publications specifically studied naratriptan in migraine with brainstem aura; the list below reflects the closest available evidence on naratriptan and migraine-with-aura populations, provided for context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomised double-blind crossover comparing naratriptan vs sumatriptan for headache recurrence in recurrence-prone migraine patients |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/Evidence Assessment | Headache | AHS updated evidence assessment of pharmacological therapies for acute migraine, including triptans |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT | Headache | Randomised, double-blind, placebo-controlled study of naratriptan 1mg/2.5mg BID as short-term prophylaxis of menstrually associated migraine |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT (small) | Cephalalgia | Naratriptan administered during migraine prodrome for prevention of headache onset |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort/Comparative | Neurology | Compared acute treatment outcomes (sumatriptan) in migraine with aura vs without aura — relevant context for aura-subtype triptan response |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Pilot study | Neurological Sciences | Open, non-comparative pilot study of naratriptan for short-term prophylaxis of pure menstrual migraine |
| [17578540](https://pubmed.ncbi.nlm.nih.gov/17578540/) | 2007 | Open-label study | Headache | Long-term tolerability of naratriptan for short-term prevention of menstrually related migraine |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of treatment options for menstrual migraine, including naratriptan |
| [16268666](https://pubmed.ncbi.nlm.nih.gov/16268666/) | 2005 | Review | CNS Drugs | Review of triptan use, including naratriptan, in management of menstrual migraine |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Case series/Review | Headache | Managing intractable migraine with naratriptan |

---

## UK Market Information

No marketing authorisations are recorded for naratriptan in this evidence pack; the drug is currently **not marketed** in this jurisdiction (0 licenses on file). Local SmPC/BNF entries should be checked directly for current UK marketed status (e.g. Naramig®) if this is being evaluated for clinical use.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Important note beyond the formal safety fields:** the repurposing rationale for this prediction itself flags that triptans, including naratriptan, are conventionally listed as contraindicated or requiring caution in migraine with brainstem (basilar-type) aura due to theoretical vasospasm risk in the vertebrobasilar territory. This should be explicitly checked against the current SmPC contraindications section before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction most plausibly reflects a pharmacological/safety association rather than a genuine efficacy-based repurposing opportunity — migraine with brainstem aura is conventionally treated as a caution/contraindication for triptans, not a target indication, and no clinical trials or disease-specific literature support use in this population. The two lower-ranked candidates (atrophoderma vermiculata, ulerythema ophryogenesis, both L5) have no mechanistic plausibility or evidence and are not viable leads.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent SmPC and labelled warnings/contraindications (currently a **Blocking** data gap, DG001)
- Formal mechanism of action documentation from DrugBank (High-priority data gap, DG002)
- Confirmation from the current SmPC on whether migraine with brainstem aura is a listed contraindication
- If pursued despite the above, a targeted literature/pharmacovigilance review specific to triptan use in brainstem-aura migraine populations before any further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

