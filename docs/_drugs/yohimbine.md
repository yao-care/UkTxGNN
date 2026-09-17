---
layout: default
title: Yohimbine
parent: Model Prediction Only (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Yohimbine
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

# Yohimbine: From No Documented Original Indication to Migraine Disorder

## One-Sentence Summary

The evidence pack for yohimbine contains no original approved indication and no mechanism-of-action data, and the drug currently holds no UK marketing authorisation.
The TxGNN model predicts possible efficacy for **Migraine Disorder**, but this is currently supported by **0 clinical trials** and **20 publications**, none of which test yohimbine directly in migraine, and several of the drug's other top-ranked candidate indications show a pharmacologically contradictory rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no original indication or product data available) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for yohimbine is not available in this evidence pack (Data Gap DG002), and no original approved indication is recorded. What can be drawn from the supporting literature itself is that yohimbine is repeatedly described as "a classical α2-adrenoceptor antagonist" (e.g. PMID 23707349), i.e. it blocks presynaptic alpha-2 adrenergic receptors and increases noradrenaline release, rather than acting as an agonist.

This is important because most of the evidence linking yohimbine to migraine is indirect: it consists of older studies on reserpine (a serotonin/catecholamine-depleting agent, not yohimbine) in migraine prophylaxis, and animal studies on how noradrenergic agonists **and** antagonists influence cortical spreading depression, the mechanism thought to underlie migraine aura. None of the identified publications administer yohimbine to migraine patients or in a migraine model, so the mechanistic link is theoretical rather than demonstrated.

More broadly, across the ten TxGNN-ranked candidate indications provided for this drug, the rationale texts flag a recurring contradiction: conditions such as ADHD, open-angle glaucoma and the common cold are treated (or theoretically improved) with alpha-2 **agonists** (guanfacine, clonidine, brimonidine, oxymetazoline-type mechanisms), whereas yohimbine acts in the opposite direction as an alpha-2 **antagonist**. This raises the possibility that the model's high similarity scores reflect shared receptor-pathway nodes in the knowledge graph rather than a correct therapeutic direction, and in some cases (e.g. glaucoma) suggests a theoretical risk rather than a benefit. All ten candidates, including migraine, are scored at evidence level L5 (one at L4) and decision stage S0, with no candidate currently supported by a completed, disease-specific clinical trial of yohimbine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5634006](https://pubmed.ncbi.nlm.nih.gov/5634006/) | 1967 | Review/Mechanistic | Trans Am Neurol Assoc | Early review proposing a role for serotonin in migraine pathophysiology; does not involve yohimbine. |
| [15829916](https://pubmed.ncbi.nlm.nih.gov/15829916/) | 2005 | Preclinical (animal) | J Cereb Blood Flow Metab | Noradrenergic agonists and antagonists altered cortical spreading depression in rats, a proposed mechanism underlying migraine aura; yohimbine was not directly tested. |
| [29856967](https://pubmed.ncbi.nlm.nih.gov/29856967/) | 2018 | Preclinical (animal) | Exp Neurol | Stress-induced cortical excitability shown to be mediated via α2-adrenergic and glucocorticoid receptors in a mouse model of cortical spreading depression. |
| [39842732](https://pubmed.ncbi.nlm.nih.gov/39842732/) | 2025 | Preclinical (animal) | Free Radic Biol Med | Reserpine-induced fibromyalgia mouse model implicates Schwann cell TRPA1/NOX1 signalling in periorbital allodynia relevant to migraine–fibromyalgia comorbidity; yohimbine not tested. |
| [468534](https://pubmed.ncbi.nlm.nih.gov/468534/) | 1979 | Historical/observational | Headache | Reports on reserpine, headache and prolactin release in migraine patients (abstract not available). |
| [1270244](https://pubmed.ncbi.nlm.nih.gov/1270244/) | 1976 | Historical/observational | Headache | Explores the relationship between tyramine, blood serotonin and migraine (abstract not available). |
| [171561](https://pubmed.ncbi.nlm.nih.gov/171561/) | 1975 | Review | MMW Munch Med Wochenschr | Discusses humoral mediators (serotonin, histamine, plasmakinin, tyramine) in migraine pathogenesis and treatment. |
| [5297855](https://pubmed.ncbi.nlm.nih.gov/5297855/) | 1967 | Historical/observational | Arch Neurol | Measures plasma serotonin changes in migraine and stress states (abstract not available). |
| [15778266](https://pubmed.ncbi.nlm.nih.gov/15778266/) | 2005 | Preclinical (animal) | J Pharmacol Exp Ther | Examines dopaminergic mechanisms in a trigeminovascular nociception animal model relevant to migraine phases. |
| [934534](https://pubmed.ncbi.nlm.nih.gov/934534/) | 1976 | Historical/observational | Minerva Med | Describes open-label and subsequent double-blind use of reserpine (not yohimbine) for migraine prophylaxis in 300 patients. |

## UK Market Information

No UK marketing authorisation is recorded for yohimbine in the evidence pack (0 licenses, market status: Not Marketed).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: the evidence pack flags a **Blocking** data gap (DG001 — missing product labelling warnings/contraindications), which by itself prevents this candidate from entering an initial safety assessment (S1) regardless of the strength of the efficacy evidence.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-ranked candidate indications for yohimbine, including migraine disorder, remain at evidence level L5 (one at L4) and decision stage S0, with no clinical trial directly testing yohimbine in the proposed indication. The mechanistic rationale for several top candidates (ADHD, open-angle glaucoma, common cold) is directly contradicted by known pharmacology of alpha-2 agonists used in those conditions, and a Blocking data gap in product safety labelling prevents any safety pre-assessment.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for yohimbine from DrugBank (Data Gap DG002)
- Product labelling (SmPC-equivalent) warnings, contraindications and DDI data (Blocking Data Gap DG001) before an S1 safety assessment can begin
- Direct pharmacological or clinical evidence testing yohimbine specifically (not reserpine, clonidine, or other alpha-2 agents) in migraine or other candidate indications
- Resolution of the mechanistic contradiction identified for the ADHD, common cold and open-angle glaucoma candidates before further evaluation of those directions
- Confirmation of current global marketing/licensing status, given zero UK marketing authorisations on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

