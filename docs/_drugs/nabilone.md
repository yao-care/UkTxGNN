---
layout: default
title: Nabilone
parent: Model Prediction Only (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Nabilone
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

# Nabilone: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder

## One-Sentence Summary

Nabilone is a synthetic cannabinoid (CB1/CB2 receptor agonist), marketed in the UK as a 1 mg capsule.
The TxGNN model predicts it may be useful for **migraine disorder**, with **no registered clinical trials** and only **one directly relevant systematic review** currently supporting this direction. The strongest signal in the data compiled for this report is a small preliminary randomised trial of nabilone in the closely related condition of **medication overuse headache**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK authorisation data compiled for this report (nabilone is generally used for chemotherapy-induced nausea and vomiting refractory to conventional antiemetics) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (migraine); L3 for the related headache disorder prediction |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Nabilone is, however, a synthetic analogue of delta-9-tetrahydrocannabinol (THC) and an agonist of CB1 and CB2 cannabinoid receptors. It is approved for chemotherapy-induced vomiting that has not responded to other antiemetics.

The endocannabinoid system is thought to modulate trigeminovascular pain signalling, CGRP release and central pain processing, all of which are relevant to migraine. This offers a plausible, though unproven, biological link between nabilone's pharmacology and migraine.

The only direct source is a 2026 systematic review of cannabinoid-based interventions for low back pain and migraine. The available data do not show whether it contains nabilone-specific migraine data. The high TxGNN score reflects a graph-based association, not clinical confirmation.

**Related predictions in the same output:**
- **Headache disorder** (score 99.78%, L3): a small, preliminary, double-blind, active-controlled randomised trial of nabilone in medication overuse headache (30 patients, 2012) is the most direct clinical evidence.
- **Migraine with brainstem aura**, **migraine susceptibility** and **trigeminal autonomic cephalalgia**: no independent evidence. The susceptibility term is essentially a duplicate of migraine.
- **Tourette syndrome** and **manic bipolar disorder**: only indirect evidence. In bipolar disorder there is also a concern that cannabinoids could worsen mania or psychosis.
- **Atrophoderma vermiculata, nephrogenic syndrome of inappropriate antidiuresis, ulerythema ophryogenesis**: no plausible mechanism, likely graph artefacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42773786](https://pubmed.ncbi.nlm.nih.gov/42773786/) | 2026 | Systematic review of RCTs | Cannabis and Cannabinoid Research | Evaluated isolated, synthetic and plant-derived cannabinoids for low back pain, migraine and medication-overuse headache. Nabilone-specific migraine findings are not shown in the available data. |
| [23070400](https://pubmed.ncbi.nlm.nih.gov/23070400/) | 2012 | Preliminary double-blind, active-controlled RCT | J Headache Pain | Tested nabilone in 30 patients with intractable medication overuse headache, assessing pain, headache frequency, analgesic intake and quality of life. Small, early-phase evidence. |
| [28281107](https://pubmed.ncbi.nlm.nih.gov/28281107/) | 2017 | Review | Curr Pain Headache Rep | Primer on cannabis for pain and headache; supportive context on the endocannabinoid system only. |
| [11152013](https://pubmed.ncbi.nlm.nih.gov/11152013/) | 2000 | Review | Drugs | General review of cannabinoids in clinical practice; no independent migraine evidence. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000R0AAAAAA (BNF-style product code; no PL number supplied) | Nabilone capsules 1 mg | Capsule | Not stated in the data compiled for this report |

Dosage form and indication text are not recorded for this authorisation, so please check the current SmPC and BNF.

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (derived from drug-disease graph links, not from label text): hypertension and hypotension, liver failure, coronary artery disease, sudden cardiac arrest, heart conduction disease, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophrenia and related disorders (schizophreniform, schizoaffective), mental disorder, and substance-related disorder or substance abuse/dependence. These should be checked against the SmPC.
- **Drug Interactions**: 100 interactions were identified, with the 20 listed all rated Moderate. Main examples:
  - **Opioids:** fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - **Sedating antihistamines:** chlorpheniramine, cetirizine, phenyltoloxamine
  - **Other CNS depressants:** alprazolam, amobarbital, dichloralphenazone, amitriptyline, ethanol
  - **Antihypertensives and diuretics:** acebutolol, nifedipine, amlodipine, alfuzosin, amiloride, hydrochlorothiazide
  - **Other:** aldesleukin

  Additive sedation and blood pressure effects are the main practical concerns.
- **Population concern:** cannabinoids may worsen mania or psychosis, which matters for any use in patients with psychiatric comorbidity.

Please also refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no registered trials for migraine and no confirmed nabilone-specific migraine data. The closest evidence is one small preliminary trial in medication overuse headache. The knowledge-graph flags (cardiovascular, psychiatric, substance-related) call for caution.

**To proceed, the following is needed:**
- Review of the 2026 systematic review to establish whether it includes nabilone-specific migraine data
- Full results and critical appraisal of the 2012 medication overuse headache trial
- Mechanism of action data to support the mechanistic link
- Confirmation of UK authorisation details (PL number, dosage form, approved indication) and SmPC warnings and contraindications
- A properly designed, adequately powered randomised trial in migraine or headache disorders
- A safety monitoring plan covering psychiatric, cardiovascular and sedation risks, and CNS-depressant interactions
- Consolidation of duplicate migraine entries (migraine with brainstem aura, migraine susceptibility) under the main migraine indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

