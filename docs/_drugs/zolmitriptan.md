---
layout: default
title: Zolmitriptan
parent: High Evidence (L1-L2)
nav_order: 619
evidence_level: L1
indication_count: 3
---

# Zolmitriptan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
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

# Zolmitriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan is a selective 5-HT1B/1D receptor agonist ("triptan") established for the acute treatment of migraine in general. The TxGNN model further highlights **Migraine with Brainstem Aura** as a related target, but this is less a genuinely new indication than a specific migraine subtype that carries additional diagnostic and vascular-safety considerations. Currently there are **no dedicated clinical trials** for this subtype, though **20 supporting publications** discuss zolmitriptan's use in migraine and migraine with aura more broadly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine, acute treatment (established triptan-class use; not documented in current UK licensing data) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not formally recorded in the regulatory dataset for this drug. However, based on available pharmacological literature, zolmitriptan is a selective 5-HT1B/1D receptor agonist that acts by constricting intracranial (trigeminovascular) arteries and inhibiting the release of CGRP and other vasoactive neuropeptides from the trigeminovascular system. This mechanism is the established, standard-of-care approach for acute migraine treatment and is not itself novel.

Migraine with brainstem aura (formerly known as "basilar-type migraine") sits within the same overall migraine disease spectrum that zolmitriptan is already used to treat — it is not a pharmacologically distinct disease, which is why the TxGNN model assigns it such a high similarity score. However, this subtype presents a genuine clinical challenge: its neurological symptoms (vertigo, dysarthria, diplopia, ataxia) can be difficult to distinguish from posterior circulation ischaemia, and vasoconstrictive triptans are theoretically capable of exacerbating brainstem or posterior-circulation ischaemia. For this reason, most guidelines — including the American Headache Society's evidence assessment — treat migraine with brainstem aura as a setting requiring careful differential diagnosis before triptan use, rather than a straightforward extension of the standard migraine indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Clinical report | Headache | Reports on triptan use specifically in basilar migraine and migraine with prolonged aura — directly addresses use in the brainstem aura subtype |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT subgroup analysis | Neurological Sciences | Subgroup of a double-blind, multicentre RCT comparing frovatriptan 2.5 mg vs zolmitriptan 2.5 mg in migraine with aura (n=18) |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | The Journal of Headache and Pain | Compares efficacy of frovatriptan vs rizatriptan, zolmitriptan and almotriptan specifically in migraine with aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment/Guideline | Headache | American Headache Society evidence-based assessment of acute migraine pharmacotherapies, including triptans |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opinion on Pharmacotherapy | Comprehensive review of zolmitriptan's clinical applications and RCT efficacy data in migraine |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Review | Drugs | Review of zolmitriptan efficacy/tolerability across RCTs; rapid onset of headache relief within 45 minutes |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Preclinical pharmacology | Cephalalgia | Describes zolmitriptan's dual central/peripheral 5-HT1B/1D mechanism inhibiting trigeminovascular activation |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | Clinical study | Cephalalgia | Compares triptan effect on pain reduction in migraine patients with and without aura, and cutaneous allodynia |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Frontiers in Neurology | Reviews treatment options for vestibular migraine, a subtype with brainstem-related symptoms |
| [17177580](https://pubmed.ncbi.nlm.nih.gov/17177580/) | 2007 | Observational/real-world | Clinical Drug Investigation | Postmarketing surveillance of zolmitriptan 5 mg nasal spray effectiveness and patient satisfaction |

---

## UK Market Information

Zolmitriptan currently holds no active UK marketing authorisation in the available regulatory dataset and is recorded as **not marketed**. Internationally, zolmitriptan is marketed under the brand name Zomig (tablet, orally disintegrating tablet, and nasal spray formulations) for the acute treatment of migraine; UK-specific licensing status should be confirmed directly with the MHRA product register before any clinical use.

---

## Safety Considerations

No structured SmPC warnings, contraindications, or drug interaction data are currently available for this drug (consistent with its unmarketed status in the UK dataset; a DDI query returned no results). Please refer to the SmPC and BNF for full safety information, and report suspected adverse reactions via the Yellow Card Scheme.

**Important clinical caveat:** As a vasoconstrictive triptan, zolmitriptan is theoretically capable of exacerbating brainstem or posterior-circulation ischaemia. Migraine with brainstem aura is therefore generally treated by guidelines (including the AHS) as a relative contraindication for triptans, owing to the difficulty of reliably distinguishing this presentation from posterior circulation stroke. Careful differential diagnosis is required before treatment is considered.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Zolmitriptan's efficacy in migraine, including migraine with aura, is well supported by multiple RCTs and authoritative reviews, and the biological plausibility for the brainstem aura subtype is strong given the shared disease mechanism. However, no dedicated clinical trials exist for this specific subtype, and its vasoconstrictive mechanism carries a theoretical risk in a population where ischaemic stroke can mimic the presenting symptoms — this combination of strong general evidence with subtype-specific safety uncertainty warrants guardrails rather than unrestricted proceeding.

**To proceed, the following is needed:**
- Full SmPC/BNF-sourced warnings and contraindications specific to zolmitriptan and to migraine with brainstem aura (currently a blocking data gap)
- Formal mechanism-of-action documentation from a primary source (e.g. DrugBank record)
- Confirmation of UK marketing authorisation status or an intended licensing pathway, since the drug is currently not marketed
- A clinical protocol for excluding posterior circulation ischaemia before triptan administration in suspected brainstem aura
- Drug interaction data, as the current DDI query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

