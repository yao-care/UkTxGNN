---
layout: default
title: Cetirizine
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 6
---

# Cetirizine
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation, selective H1 antihistamine established as a first-line treatment for allergic rhinitis and related allergic conditions.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **3 clinical trials** and **18 publications** currently supporting this direction.
Evidence is rated at Level **L1**, including a completed Phase 3 pilot trial directly evaluating intravenous cetirizine for acute urticaria in emergency settings.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in dataset (established clinical use: allergic rhinitis) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| UK Market Status | Not recorded in dataset — likely a data gap (see note below) |
| Number of Marketing Authorisations | Not recorded in dataset |
| Recommended Decision | Proceed with Guardrails |

> **⚠️ Note on UK market data:** The MHRA regulatory records for cetirizine returned no entries in this evidence pack. This almost certainly reflects a data collection gap rather than an absence of UK authorisation. Cetirizine is a widely authorised antihistamine available in the UK both over the counter (e.g., Zirtek®, Piriteze®, Benadryl® One A Day) and on prescription. Clinicians should verify current authorisation details via the MHRA Product Licence register and the BNF (Section 3.4.1 — Antihistamines).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned in this evidence pack; however, cetirizine is a well-characterised agent in the clinical literature. It is the carboxylated metabolite of hydroxyzine, acting as a potent, selective, and long-acting competitive antagonist of peripheral histamine H1 receptors. At standard doses (10 mg daily), it markedly suppresses histamine-induced wheal and flare responses whilst exhibiting substantially lower CNS penetration than first-generation antihistamines. Additionally, cetirizine inhibits eosinophil chemotaxis during the secondary phase of the allergic response, conferring anti-inflammatory properties beyond simple H1 blockade (PMID 1981354; Drugs, 1990).

Allergic urticaria is driven by IgE-mediated allergen sensitisation leading to mast cell degranulation and histamine release — the same core mechanism that cetirizine was developed to address in allergic rhinitis. The transition from rhinitis to urticaria therefore represents an extension within a single mechanistic framework rather than a true pharmacological leap. Both conditions are characterised by excessive H1-mediated vascular permeability and sensory nerve activation, and current international guidelines (EAACI/GA²LEN/EDF/WAO) already recommend second-generation H1 antihistamines as the first-line treatment for urticaria.

The TxGNN knowledge graph model's near-perfect prediction score (99.99%) reflects the density of established mechanistic and clinical connections within its training data. The completed Phase 3 pilot trial NCT02023164 further supports an intravenous formulation route for acute urticaria in hospital emergency settings, a clinically relevant extension of the established oral route that merits formal investigation at adequate scale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicentre randomised double-blind pilot comparing IV cetirizine 10 mg versus IV diphenhydramine 50 mg for acute urticaria in Emergency Departments, Urgent Care Centres, and Allergy Clinics; designed to assess feasibility for a full Phase 3 study |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomised double-blind controlled trial evaluating addition of a short-burst corticosteroid course to conventional H1 antihistamine treatment for urticaria; cetirizine likely forms the standard-of-care comparator arm |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminated | 11 | Investigated the effect of levocetirizine (the active R-enantiomer of cetirizine) on skin-level inflammatory mediators in symptomatic dermatographism and chronic idiopathic urticaria; terminated early due to low enrolment — results incomplete |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Critically reviewed evidence for up-dosing second-generation antihistamines (including cetirizine) to 4× licensed dose in chronic spontaneous urticaria; confirms antihistamines as first-line treatment per current guidelines |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical Study | Allergy | Direct clinical studies of cetirizine in allergic rhinitis and chronic urticaria; established efficacy and tolerability profile |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Clinical Review | Drugs | Comprehensive pharmacological review of cetirizine; documents H1 antagonism plus inhibition of eosinophil chemotaxis; controlled trials confirm efficacy in chronic idiopathic urticaria |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Clinical Review | Drugs | Reappraisal confirming cetirizine as effective and well-tolerated for seasonal and perennial allergic rhinitis and chronic idiopathic urticaria in adults and children; 10 mg/day found equivalent to first-generation agents in efficacy with improved tolerability |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Comparative Review | Drugs | Evaluated second-generation antihistamines including cetirizine, fexofenadine, loratadine and others; compared efficacy and adverse-effect profiles across urticaria and rhinitis indications |
| [27110120](https://pubmed.ncbi.nlm.nih.gov/27110120/) | 2016 | Review | Ther Clin Risk Manag | Review of the antihistamine treatment landscape for allergic rhinitis and urticaria; places cetirizine within the established second-generation class and contextualises class-wide evidence |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Reviewed efficacy and safety of first- and newer-generation antihistamines for allergic rhinitis and chronic idiopathic urticaria with a pharmacy management focus; supports cetirizine as a mainstay agent |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Overview of urticaria recognition, causes, and treatment; confirms nonsedating antihistamines (including cetirizine) as the mainstay of therapy for chronic idiopathic urticaria |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Case Report | Cureus | Reports rebound pruritus and urticaria following long-term cetirizine discontinuation in an Asian patient; highlights an emerging safety consideration relevant to chronic urticaria management |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | Evidence-based review of H1 antihistamines in children; Level 1 evidence confirmed for allergic rhinoconjunctivitis, with discussion of safety and tolerability profile including cetirizine |

---

## UK Market Information

No MHRA marketing authorisation records were retrieved for cetirizine in this evidence pack. This is consistent with a data collection gap rather than a true absence of UK authorisation. For reference, cetirizine is a well-established product in the UK and is classified in the BNF under **Section 3.4.1 (Antihistamines)**. Prescribers and pharmacists should consult the current MHRA Product Licence register and relevant SmPCs for up-to-date authorisation details, approved indications, and product-specific dosing information.

---

## Safety Considerations

No safety data was returned in this evidence pack.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cetirizine's H1 receptor antagonism directly addresses the histamine-mediated pathophysiology of allergic urticaria, and the completed Phase 3 pilot trial (NCT02023164) plus multiple systematic reviews provide L1-level evidence supporting its use in this indication. The TxGNN prediction score of 99.99% is well-supported by the existing clinical literature.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current MHRA marketing authorisation status and approved indications for all cetirizine products via the Product Licence register, as the dataset shows no records (data gap)
- **Safety data retrieval**: Obtain and review the current UK SmPC for cetirizine (including warnings, contraindications, and drug interactions) — this evidence pack returned no safety data
- **Route of administration review**: The completed pilot trial (NCT02023164, n=36) evaluated IV cetirizine, which is not a standard licensed route in the UK; a larger confirmatory Phase 3 trial is needed before IV use could be formalised
- **Dosing clarification**: Confirm whether up-dosing to 4× standard dose (40 mg/day) for refractory chronic spontaneous urticaria is supported by the current UK SmPC, in line with EAACI/EDF guidelines
- **Rebound discontinuation risk**: Develop monitoring guidance in response to emerging reports (PMID 41602253, 2025) of rebound pruritus and urticaria following long-term cetirizine cessation, particularly in patients with chronic urticaria requiring prolonged therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

