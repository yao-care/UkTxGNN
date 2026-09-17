---
layout: default
title: Eletriptan
parent: Moderate Evidence (L3-L4)
nav_order: 230
evidence_level: L4
indication_count: 4
---

# Eletriptan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Eletriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Eletriptan is a selective 5-HT1B/1D receptor agonist (triptan) originally developed for the acute treatment of migraine.
The TxGNN model predicts potential efficacy in **Migraine with Brainstem Aura**, a distinct and clinically sensitive migraine subtype,
but this signal is currently supported only by **general migraine literature (18 publications)** — there are **no clinical trials or subtype-specific studies**, and the underlying mechanism raises a genuine safety concern rather than confirming benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine, acute treatment (with or without aura) — based on published pharmacology literature; no UK licensing record is available in this evidence pack |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Eletriptan is not currently recorded in DrugBank (a flagged data gap). Based on the available pharmacology literature, however, eletriptan is a selective 5-HT1B/1D receptor agonist within the triptan class, acting through cranial vasoconstriction and inhibition of trigeminovascular neurotransmission to abort acute migraine attacks (PMID 12498013).

Migraine with brainstem aura (formerly "basilar-type migraine") is a specific ICHD-3 subtype involving brainstem-localised aura symptoms. Because triptans act by constricting cranial vasculature, this subtype — along with hemiplegic migraine — has traditionally been treated as a relative or absolute contraindication for the triptan class, out of concern for vasoconstriction in the vertebrobasilar circulation supplying the brainstem itself.

This is why the very high TxGNN score should be treated with caution rather than as validation: it most likely reflects textual/semantic similarity between "migraine" and "migraine with brainstem aura" in the model's disease embeddings, rather than a genuine, tested therapeutic signal. A dedicated RCT dosing eletriptan during the aura phase found no benefit (PMID 15469451), and a published case report describes a myocardial infarction temporally associated with eletriptan use (PMID 25155004) — both point toward vascular caution rather than support for this specific indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15469451](https://pubmed.ncbi.nlm.nih.gov/15469451/) | 2004 | RCT (aura-phase dosing) | European Journal of Neurology | Eletriptan 80 mg given during the aura phase showed no benefit over expected placebo response — directly relevant to, and cautionary for, aura-subtype use |
| [25155004](https://pubmed.ncbi.nlm.nih.gov/25155004/) | 2014 | Case report | Revista Portuguesa de Cardiologia | Non-ST-elevation MI shortly after eletriptan use in a patient with migraine with aura and coronary disease — vascular safety signal |
| [17636718](https://pubmed.ncbi.nlm.nih.gov/17636718/) | 2007 | Cochrane review (withdrawn) | Cochrane Database of Systematic Reviews | Systematic review of eletriptan efficacy/harms in acute migraine (general population, not aura-subtype specific) |
| [11687056](https://pubmed.ncbi.nlm.nih.gov/11687056/) | 2001 | Cochrane review | Cochrane Database of Systematic Reviews | Earlier systematic review establishing eletriptan's efficacy and tolerability profile in acute migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptans |
| [12807526](https://pubmed.ncbi.nlm.nih.gov/12807526/) | 2003 | RCT (subgroup) | Cephalalgia | Eletriptan effective and well tolerated in patients with prior poor response to sumatriptan |
| [11844898](https://pubmed.ncbi.nlm.nih.gov/11844898/) | 2002 | RCT | European Neurology | Eletriptan 40/80 mg more effective than Cafergot and placebo in acute migraine |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | Drug profile | Current Opinion in Investigational Drugs | Describes eletriptan's 5-HT1B/1D receptor pharmacology and comparative receptor affinity |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review (paediatric) | Paediatric Drugs | Reviews triptan use, including eletriptan, in paediatric migraine populations |
| [23465038](https://pubmed.ncbi.nlm.nih.gov/23465038/) | 2013 | Review | Headache | Safety recommendations for migraine treatments, including triptans, during breastfeeding |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: MHRA label warnings and contraindications for Eletriptan could not be retrieved for this evaluation (blocking data gap) — this must be resolved before any safety assessment can proceed (see Next Steps).*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or subtype-specific literature exist for migraine with brainstem aura, and the drug class carries a longstanding theoretical vascular contraindication for this exact subtype; the high TxGNN score most likely reflects label-text similarity rather than a genuine signal, and a cardiovascular safety signal (PMID 25155004) argues for caution, not progression.

**To proceed, the following is needed:**
- MHRA SmPC warnings and contraindications for Eletriptan, specifically regarding basilar-type/brainstem-aura and hemiplegic migraine (currently a blocking data gap)
- Verified DrugBank mechanism-of-action record
- Cardiovascular risk assessment given the reported MI association
- Any dedicated studies of triptans in migraine with brainstem aura, should they emerge, to replace the current absence of subtype-specific evidence

*Note: three further TxGNN-predicted indications for this drug (atrophoderma vermiculata, ulerythema ophryogenesis, sciatic neuropathy) returned zero supporting trials or literature and are assessed as low-confidence model noise (Evidence Level L5) — not clinically actionable.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

