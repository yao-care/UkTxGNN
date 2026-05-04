---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorphine: From Opioid Dependence and Pain Management to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial μ-opioid receptor agonist and κ-opioid receptor antagonist, widely used in clinical practice for opioid use disorder and moderate-to-severe pain management.
The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria (AIP)**,
with **no registered clinical trials** and only **1 published case report** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid dependence; moderate-to-severe pain management |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| UK Market Status | Not recorded in this dataset |
| Number of Marketing Authorisations | 0 (per dataset) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available within this dataset. Based on established pharmacological knowledge, buprenorphine is a high-affinity partial agonist at the μ-opioid receptor (MOR), an antagonist at the κ-opioid receptor (KOR), and an antagonist at the ORL1/nociceptin receptor. Its unusually slow receptor dissociation kinetics and ceiling effect on respiratory depression distinguish it from full opioid agonists, underpinning its clinical utility in both opioid use disorder treatment and analgesia.

Acute Intermittent Porphyria is a rare autosomal dominant metabolic disorder caused by a deficiency of hydroxymethylbilane synthase (HMBS), leading to the accumulation of neurotoxic porphyrin precursors — aminolaevulinic acid (ALA) and porphobilinogen (PBG) — during acute attacks. Clinical manifestations include severe abdominal pain, autonomic dysfunction, peripheral neuropathy, and neuropsychiatric disturbance, all of which involve pain pathways where opioid receptors are physiologically active. The severe pain of AIP attacks frequently requires opioid analgesia.

The biological rationale for buprenorphine in AIP rests primarily on its **low porphyrogenicity** relative to many other analgesic and anaesthetic agents. Many commonly used drugs — including barbiturates, some anticonvulsants, and certain opioids — are known to precipitate AIP attacks by inducing hepatic cytochrome P450 enzymes and upregulating haem synthesis. Buprenorphine, being considered low-risk for porphyria induction, becomes a pragmatic pain management choice in this population. This constitutes a **supportive symptomatic use** rather than a mechanistic repurposing targeting the underlying metabolic defect. There is currently no proposed mechanism by which buprenorphine would correct the enzymatic deficiency or reduce porphyrin precursor accumulation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui – The Japanese Journal of Anesthesiology | A 40-year-old woman with suspected AIP underwent modified radical hysterectomy. Buprenorphine was selected for perioperative analgesia on the basis of its comparatively low risk of precipitating a porphyric attack, providing a safety description rather than therapeutic evidence for AIP itself. |

---

## UK Market Information

This dataset records no MHRA marketing authorisations for buprenorphine. **This is likely a data gap**: buprenorphine-containing products (e.g. Subutex, Suboxone, Buvidal, Norspan) are known to hold MHRA authorisations in the United Kingdom. Clinicians should verify current authorisation status via the MHRA Product Information database and consult the British National Formulary (BNF Section 4.10.3 – Opioid dependence; and BNF Section 4.7 – Analgesics) for prescribing guidance.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Note for AIP context**: In patients with AIP, particular caution is required when selecting any drug, as numerous commonly used agents — including certain analgesics, anaesthetics, anticonvulsants, and hormonal preparations — are known to precipitate acute attacks. Buprenorphine is generally regarded as lower risk in this regard, but prescribers should verify current guidance from the European Porphyria Network (EPNET) drug database before initiating any new medicine in a confirmed AIP patient.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available evidence is a 1993 Japanese case report describing perioperative anaesthetic management in a patient with suspected AIP. This demonstrates the *safety* of buprenorphine use in the context of AIP rather than any therapeutic efficacy targeting the disease itself. No clinical trials exist, and the mechanistic link to AIP pathophysiology remains entirely uncharacterised.

**To proceed, the following is needed:**

- **Clarify the repurposing hypothesis**: distinguish between (a) optimising opioid choice for symptomatic pain control during AIP attacks — where evidence exists for opioids broadly — and (b) a novel disease-modifying hypothesis, which currently has no mechanistic basis
- **Retrieve mechanism of action data** from DrugBank (DB00921) and published literature to determine whether any aspect of buprenorphine's receptor pharmacology could plausibly interact with haem biosynthesis or AIP pathophysiology
- **Conduct a systematic literature review** of opioid use in AIP, comparing porphyrogenicity risk profiles across available agents, to contextualise buprenorphine's position
- **Verify UK marketing authorisation status** via the MHRA database to confirm currently approved indications and formulations available in the UK
- **Consult EPNET drug classification** to confirm buprenorphine's current porphyria safety classification before any clinical recommendation is made
- If a disease-modifying hypothesis is identified, **preclinical validation** (e.g. HMBS-deficient mouse models or ALA/PBG biomarker studies) would be required before any clinical evaluation is considered

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be reviewed by a qualified clinician before informing patient care decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

