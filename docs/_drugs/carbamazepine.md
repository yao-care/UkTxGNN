---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy and Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is a well-established antiepileptic drug and the first-line pharmacological treatment for trigeminal neuralgia, acting by blocking voltage-gated sodium channels (Nav) to suppress pathological neuronal discharges.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm**, with **0 clinical trials** and **20 publications** currently identified in support of this direction.
However, this prediction very likely reflects knowledge graph drift between trigeminal neuralgia (an established CBZ indication) and trigeminal nerve neoplasm through shared anatomical nodes, rather than a genuine anti-tumour effect — CBZ has no known anti-tumour mechanism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy (partial and generalised tonic-clonic seizures); Trigeminal Neuralgia; Neuropathic Pain |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.9976% |
| Evidence Level | L4 |
| UK Market Status | Not retrieved (0 licences found in dataset; MHRA data collection incomplete) |
| Number of Marketing Authorisations | 0 (dataset gap — see UK Market Information below) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carbamazepine is a dibenzazepine anticonvulsant whose principal mechanism is blockade of voltage-gated sodium channels (Nav1.1, Nav1.2, Nav1.6). By stabilising the inactivated state of these channels, CBZ reduces the sustained high-frequency neuronal firing that underlies both partial epileptic seizures and the paroxysmal lancinating pain of trigeminal neuralgia. This well-characterised Nav-blocking mechanism also suppresses ectopic discharges arising from injured or compressed peripheral nerve tissue — an effect demonstrated in experimental neuroma models (PMID 3181365) — which provides a plausible pharmacological basis for symptomatic benefit whenever the trigeminal nerve is subject to mechanical distortion, whether by a blood vessel or by a neoplastic mass.

Trigeminal nerve neoplasms (schwannomas, neurolymphomatosis, meningiomas compressing the fifth nerve, and rarer primary malignancies in Meckel's cave) frequently present with facial pain clinically indistinguishable from idiopathic trigeminal neuralgia. It is therefore well-documented in case reports that patients with undiagnosed trigeminal nerve tumours receive CBZ as an empirical first-line analgesic. In some instances CBZ affords partial or transient relief (PMID 25142539); in others it fails entirely, prompting imaging that reveals the underlying tumour (PMID 15235745, PMID 30741017). This clinical overlap — rather than any novel anti-tumour effect — is almost certainly the mechanistic link exploited by the TxGNN knowledge graph.

**Knowledge graph drift alert:** The evidence pack's own repurposing rationale explicitly flags this as a likely false-positive prediction, arising from the knowledge graph over-linking the node "trigeminal neuralgia (CBZ approved indication)" with the node "trigeminal nerve neoplasm" through shared anatomical and symptomatic edges. CBZ possesses no anti-proliferative, pro-apoptotic, or anti-angiogenic properties. Any potential use in trigeminal nerve neoplasm would be strictly symptomatic pain management — a supportive role — and would not modify tumour biology or prognosis. This distinction must be made explicit before any clinical translation is considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carbamazepine in trigeminal nerve neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Trigeminal neuralgia aetiology includes both vascular compression and tumour-related nerve compression; reviews pharmacological and surgical treatment options |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurotherapeutics | Comprehensive TN treatment review; vascular compression → focal demyelination → aberrant discharge; CBZ established as first-line medical therapy |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Cohort/Survey | Br J Oral Maxillofac Surg | UK BAOMS survey (254 consultants) on TN investigation and management; highlights need to screen for secondary TN and monitor CBZ plasma levels |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | Br J Neurosurgery | Primary neurolymphomatosis of the trigeminal nerve presenting as unilateral facial pain; CBZ prescribed empirically but provided no relief; MRI subsequently revealed nerve swelling and a Meckel's cave mass |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case Report | Rinsho Shinkeigaku (Clinical Neurology) | Malignant lymphoma with perineural spread along the trigeminal nerve mimicking classical TN; CBZ initially improved neuralgic pain; later became ineffective as additional cranial nerve symptoms emerged with tumour progression |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia affecting bilateral facial and trigeminal nerve distributions (delayed radiotherapy sequela); episodic involuntary contractions with neuromyotonic EEG discharges responded to CBZ |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case Report | Arq de Neuro-Psiquiatria | Primary melanoma of Meckel's cave presenting as TN with a normal initial MRI; CBZ failed to control pain; diagnosis of neoplasm only made after surgical exploration prompted by treatment failure |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Preclinical | Experimental Neurology | IV CBZ dose-dependently inhibited spontaneous ectopic discharges from experimental saphenous neuromas in rats (A-α/β and A-δ fibres); supports Nav blockade as the mechanism underlying nerve-injury pain suppression |
| [32454201](https://pubmed.ncbi.nlm.nih.gov/32454201/) | 2020 | Case Report | World Neurosurgery | Trigeminal schwannoma of the pterygopalatine fossa resected via endoscopic endonasal approach; contextualises the broad anatomical distribution and surgical management of trigeminal nerve tumours |
| [22647513](https://pubmed.ncbi.nlm.nih.gov/22647513/) | 2012 | Case Report | No Shinkei Geka | Combined trigeminal and glossopharyngeal neuralgia caused by vascular compression; CBZ recommended as initial medical treatment; microvascular decompression indicated if medical therapy inadequate |

---

## UK Market Information

MHRA marketing authorisation data was not retrieved for Carbamazepine in this dataset (0 licences recorded). This is likely a data collection gap: Carbamazepine has been available in the UK for decades under multiple brand names, most notably **Tegretol®** (Novartis), and is listed in the BNF (Section 4.8.1: Drugs used in epilepsy; and for trigeminal neuralgia). Prescribers should consult the current BNF and the MHRA product licence register directly for authorised indications, dosage forms, and prescribing information.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|-------------------|
| Not retrieved | MHRA data not available in this dataset | — | Please refer to MHRA product register and current BNF |

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

*Note: Key warnings, contraindications, and drug interaction data were not captured in this evidence pack. For a drug with CBZ's extensive interaction profile (particularly CYP3A4 induction and effects on oral contraceptives, warfarin, and other antiepileptics), a full DDI review from the SmPC is essential before any clinical use.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials have been registered for Carbamazepine in trigeminal nerve neoplasm, and the 20 identified publications are almost entirely case reports and reviews in which CBZ was used empirically for symptom control in patients later confirmed to have trigeminal nerve tumours — not evidence of a repurposing opportunity with disease-modifying intent. The TxGNN prediction is most plausibly explained by knowledge graph drift between the established trigeminal neuralgia indication and the neoplasm entity, and CBZ has no anti-tumour mechanism; further investment in this specific prediction is not currently justified without first resolving the clinical question below.

**To proceed, the following is needed:**

- **Clarify the clinical hypothesis**: Is the research question about symptomatic neuropathic pain management in patients with confirmed trigeminal nerve neoplasms, or does the proposal assert any anti-tumour activity? These require entirely different evidence frameworks.
- **If symptomatic only**: Conduct a systematic review of case reports and series documenting CBZ use in histologically confirmed trigeminal nerve neoplasms, with structured outcomes for pain response, duration of benefit, and failure patterns.
- **Mechanism review**: Commission a formal KG artefact review to determine whether the TxGNN score reflects a genuine disease–drug relationship or a drift pathway via shared trigeminal anatomy nodes.
- **MHRA regulatory data retrieval**: Obtain current UK marketing authorisation data from the MHRA product licence register to confirm licensing status, authorised indications, and any NICE appraisals.
- **Safety dossier**: Retrieve the full SmPC to document CBZ's boxed warnings (including serious dermatological reactions, SJS/TEN risk, and HLA-B\*15:02 screening requirements in relevant populations), contraindications, and drug interaction profile before any clinical protocol is drafted.
- **Oncology pathway consideration**: If CBZ is to be used for pain in the context of a trigeminal nerve tumour, this should be coordinated with the treating oncology team; pain management plans for neoplasm-associated neuropathy typically involve multidisciplinary input beyond a single antiepileptic agent.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

