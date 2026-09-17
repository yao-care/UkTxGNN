---
layout: default
title: Frovatriptan
parent: Moderate Evidence (L3-L4)
nav_order: 285
evidence_level: L3
indication_count: 3
---

# Frovatriptan
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

# Frovatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Frovatriptan is a 5-HT1B/1D receptor agonist (triptan) with an established literature record for acute migraine treatment, though this is not confirmed by a formal Taiwan/UK regulatory record in this evidence pack (drug is currently **not marketed**, 0 marketing authorisations on file). The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, a specific migraine subtype, with **no dedicated clinical trials** but **19 supporting publications** on frovatriptan's general use in migraine (with/without aura). Because this subtype is a recognised relative contraindication for the triptan class, the high model score likely reflects the drug's broad "migraine" association rather than validated efficacy/safety in this specific population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in the Taiwan/UK regulatory dataset (0 licences); literature indicates established overseas use for acute treatment of migraine, with or without aura |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal, structured mechanism-of-action record was not returned from the DrugBank query for this candidate. However, the literature consistently and independently describes frovatriptan as a serotonin **5-HT1B/1D receptor agonist**, producing intracranial and extracerebral artery vasoconstriction along with possible anti-inflammatory/neuronal effects — the standard triptan mechanism, with a notably long half-life (~26 hours) relative to other agents in the class.

The predicted new indication, migraine with brainstem aura, is not a distinct disease so much as a specific clinical subtype of migraine — the very condition frovatriptan is already used to treat. This explains the very high TxGNN score: the knowledge graph is likely picking up the drug's strong, well-established "migraine" association rather than identifying a genuinely novel therapeutic area.

The mechanistic caveat is important: 5-HT1B-mediated vasoconstriction, while beneficial in typical migraine, is the reason triptans (as a class) are conventionally considered contraindicated or used with caution in hemiplegic migraine, basilar-type migraine, and migraine with brainstem aura, due to theoretical risk of exacerbating posterior-circulation vasospasm. Consistent with this, none of the identified literature specifically enrols or studies this aura subtype — most triptan trials explicitly exclude it. The prediction is therefore mechanistically plausible only in the broadest sense, and clinically it points toward a population this drug class is typically kept away from.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18457529](https://pubmed.ncbi.nlm.nih.gov/18457529/) | 2008 | RCT | Expert Review of Neurotherapeutics | Frovatriptan indicated for acute migraine with or without aura; long half-life (26h) and low recurrence rate (17%); effective in perimenstrual prophylaxis regimen |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT subgroup analysis | Neurological Sciences | Subgroup of 18 patients with migraine with aura from a multicentre double-blind crossover study; compared frovatriptan 2.5mg vs zolmitriptan 2.5mg |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Review/Pooled analysis | J Headache Pain | Meta-analysis comparing frovatriptan vs rizatriptan/zolmitriptan/almotriptan specifically in migraine with aura; notes triptans are of uncertain efficacy when dosed during the aura phase itself |
| [24867847](https://pubmed.ncbi.nlm.nih.gov/24867847/) | 2014 | Pooled analysis | Neurological Sciences | Pooled data from 3 Italian RCTs comparing frovatriptan efficacy by BMI category (normal weight vs obese) |
| [23695053](https://pubmed.ncbi.nlm.nih.gov/23695053/) | 2013 | Pooled analysis | Neurological Sciences | Pooled data from 3 Italian RCTs comparing frovatriptan efficacy in hypertensive vs normotensive migraineurs |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/Evidence assessment | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptans as a class |
| [27757013](https://pubmed.ncbi.nlm.nih.gov/27757013/) | 2016 | Review | Drug Design, Development and Therapy | Overview of frovatriptan efficacy/safety versus other triptans across three double-blind Italian crossover studies |
| [22900951](https://pubmed.ncbi.nlm.nih.gov/22900951/) | 2012 | Review | CNS Drugs | General review of frovatriptan pharmacology, efficacy and tolerability for acute migraine |
| [15311727](https://pubmed.ncbi.nlm.nih.gov/15311727/) | 2004 | Review | International Journal of Clinical Practice | Overview of frovatriptan succinate pharmacokinetics and receptor selectivity |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of menstrual migraine treatment options, including frovatriptan's role in short-term prophylaxis |

None of the identified literature specifically studies the brainstem aura subtype; coverage is limited to migraine and migraine-with-aura more broadly.

---

## UK Market Information

No marketing authorisations are on file — this evidence pack records the drug as **not marketed** (0 licences). No MHRA product or BNF classification data is currently available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Class-based caution:** Triptans as a class (including frovatriptan) are conventionally contraindicated or used with caution in hemiplegic migraine, basilar-type migraine, and migraine with brainstem aura, owing to 5-HT1B-mediated vasoconstriction risk in the posterior cerebral circulation. This is directly relevant here, since it is the very population the predicted indication targets. This point is derived from general triptan pharmacology in the literature reviewed above, not from a drug-specific TFDA/MHRA warning (which is not yet on file for this candidate — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score most likely reflects frovatriptan's already-known association with migraine broadly, rather than a validated new indication — and the specific subtype predicted (brainstem aura) is one where triptans are typically avoided due to a recognised class-level vasoconstriction risk. No clinical trials or subtype-specific literature exist to support efficacy or safety in this population, and the drug currently has no marketing authorisation on file in this dataset.

**To proceed, the following is needed:**
- TFDA/MHRA SmPC (product labelling) confirming the formal contraindication/warning status regarding basilar-type migraine and migraine with brainstem aura (currently a Blocking data gap)
- A confirmed DrugBank mechanism-of-action record (currently a data gap; literature-derived MOA used as a substitute above)
- Dedicated safety/efficacy data or specialist neurology input specific to the brainstem aura subtype before this candidate could move beyond Hold
- Clarification of market authorisation status/plans, since the drug is not currently marketed

*Note: Two lower-ranked TxGNN outputs for this drug (atrophoderma vermiculata, ulerythema ophryogenesis) had zero supporting trials or literature and no plausible mechanistic link — these are assessed as likely model false positives and are not carried forward.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

