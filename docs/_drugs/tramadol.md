---
layout: default
title: Tramadol
parent: Moderate Evidence (L3-L4)
nav_order: 589
evidence_level: L4
indication_count: 10
---

# Tramadol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tramadol: From Moderate-to-Severe Pain to Juvenile Idiopathic Arthritis

> **Note on candidate selection**: TxGNN's top-ranked predictions (ranks 1–6, 8–10 — mostly rare skeletal dysplasias such as acromesomelic dysplasia and brachyolmia) carry extremely high scores (>99.9%) but are explicitly flagged in the evidence pack as likely knowledge-graph artefacts with no plausible mechanistic link to an opioid analgesic. This report therefore focuses on **Juvenile Idiopathic Arthritis (JIA)**, the only prediction (rank 7) that reached decision stage S1 with any supporting literature.

## One-Sentence Summary

Tramadol is a centrally-acting weak opioid analgesic (weak μ-opioid agonism combined with monoamine reuptake inhibition), generally used for moderate-to-severe pain. The TxGNN model's highest-scoring predictions are almost certainly knowledge-graph false positives, but the model also flagged **Juvenile Idiopathic Arthritis**, for which there is indirect, symptom-relief-only literature support (no tramadol-specific trials). Overall evidence remains weak (**L4**), and no UK marketing or safety data are currently on file.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack; Tramadol is generally indicated for moderate-to-severe pain |
| Predicted New Indication | Juvenile Idiopathic Arthritis (most evidence-supported candidate; the model's top-ranked skeletal-dysplasia predictions were assessed as implausible false positives) |
| TxGNN Prediction Score | 99.92% (global rank 1341 of all TxGNN predictions) |
| Evidence Level | L4 |
| UK Market Status | Not Marketed (per this evidence pack; no licences on file) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Tramadol is not available in the structured drug record. Based on the pharmacological description embedded in the evidence pack's rationale text, Tramadol acts as a centrally-acting weak opioid analgesic — a weak μ-opioid receptor agonist combined with inhibition of serotonin and noradrenaline reuptake. Its established clinical role is symptomatic relief of moderate-to-severe pain.

Juvenile Idiopathic Arthritis is a chronic inflammatory joint disease in children that frequently causes significant pain, particularly during disease flares. Tramadol has been used off-label in paediatric populations for moderate-to-severe pain, including pain arising from inflammatory joint disease. This represents a plausible pathway for symptomatic use, but it is important to be clear that this would be **analgesic support, not disease modification** — Tramadol has no known anti-inflammatory or immunomodulatory mechanism and would not alter the underlying course of JIA (unlike a DMARD or biologic).

By contrast, the model's higher-scoring predictions (acromesomelic dysplasia, brachyolmia, myosclerosis, pseudoachondroplasia, etc.) are structural or developmental skeletal disorders with no established relationship to opioid or monoamine pharmacology. The evidence pack's own rationale assesses these as likely artefacts of "analgesic–skeletal disease symptom co-occurrence" in the underlying knowledge graph, rather than genuine disease-modifying signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20799760](https://pubmed.ncbi.nlm.nih.gov/20799760/) | 2010 | PK/Efficacy study (**ketoprofen**, not Tramadol) | Paediatric Drugs | Reviews ketoprofen pharmacokinetics and central analgesic potential in children; used here only as indirect support that centrally-acting analgesics are relevant in paediatric inflammatory/musculoskeletal pain, not as direct Tramadol evidence |
| [12180751](https://pubmed.ncbi.nlm.nih.gov/12180751/) | 2002 | Case report (comorbidity, unrelated to Tramadol) | The Journal of Rheumatology | Describes two cases of coexistent sickle cell disease and juvenile rheumatoid arthritis with delayed diagnosis; not related to Tramadol treatment |

**Caution**: Neither publication studies Tramadol directly in JIA. Both are included in the evidence pack as indirect, low-relevance literature and should not be interpreted as clinical evidence of efficacy.

---

## UK Market Information

No UK marketing authorisation records are present in this evidence pack for Tramadol (`total_licenses: 0`, market status recorded as "Not Marketed"). This is worth verifying independently, as it does not necessarily reflect current UK availability — it may indicate a gap in the source dataset rather than genuine absence of a UK licence.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Important**: This evidence pack flags the absence of TFDA/MHRA-equivalent labelling data (warnings, contraindications) as a **Blocking** data gap (DG001) — meaning a formal safety pre-assessment (S1) cannot currently be completed for this drug-indication pair.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The majority of TxGNN's highest-scoring predictions for Tramadol lack any plausible mechanistic basis and appear to be knowledge-graph artefacts.
- The one candidate with partial evidentiary support, Juvenile Idiopathic Arthritis, is backed only by indirect, non-Tramadol-specific literature (L4) — no Tramadol clinical trials or Tramadol-specific studies in JIA exist in the current record.
- A Blocking data gap (missing UK-equivalent labelling: warnings and contraindications) prevents even a basic safety pre-assessment.

**To proceed, the following is needed:**
- Official UK SmPC/BNF entry for Tramadol (warnings, contraindications) — resolves Blocking gap DG001
- Confirmed original indication and formal mechanism-of-action documentation — resolves High-severity gap DG002
- Tramadol-specific (not ketoprofen-substitute) pharmacokinetic and efficacy data in paediatric JIA populations
- Verification of actual UK marketing status, given the discrepancy between the recorded "Not Marketed" status and Tramadol's broader real-world availability
- A mechanistic re-review of the top-ranked skeletal dysplasia predictions before any further action, given the strong internal assessment that these are false positives
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

