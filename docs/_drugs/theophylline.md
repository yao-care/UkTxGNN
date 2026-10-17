---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 611
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma, bronchitis…"
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Asthma to Thrombotic Disease

## One-Sentence Summary

> Theophylline is a methylxanthine bronchodilator, originally used to treat asthma, bronchitis, emphysema and other chronic airway diseases.
> The TxGNN model predicts it may be effective for **thrombotic disease** (its top-ranked prediction), but there are **no registered clinical trials** and **none of the 18 publications retrieved** evaluates theophylline for thrombosis.
> Among the other predictions, only obstructive lung disease has substantial evidence, and that is essentially the existing approved indication space.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, pulmonary emphysema and related chronic airway disease (the data compiled for this report contain no approved indication text for the UK authorisation) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

**Other predictions in the data compiled for this report**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Nasal cavity disease | 99.53% | L3 | Research question |
| 3 | Laryngotracheitis | 99.51% | L5 | Hold |
| 4 | Tracheal disease | 99.49% | L3 | Research question |
| 5 | Obstructive lung disease | 99.48% | L1 | Proceed with Guardrails |
| 6 | Pharyngitis | 99.46% | L4 | Hold |
| 7 | Acute laryngopharyngitis | 99.35% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. Theophylline is, however, a well-known non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist. PDE inhibition raises intracellular cAMP, which relaxes airway smooth muscle (the basis of its use in asthma and COPD). In platelets, raised cAMP could plausibly reduce aggregation, which is the theoretical link to thrombotic disease.

This link is theoretical only. The retrieved literature does not support it: the papers cover ticlopidine pharmacokinetics, platelet biomarker assays, microRNA sample processing and a theophylline aptasensor, and none tests theophylline as an antithrombotic. The high TxGNN score is a prediction without clinical backing, and I would not treat it as a viable repurposing lead on current data.

Two other predictions are more credible:

- **Obstructive lung disease** is essentially the original indication space, so it is not true repurposing. At low doses theophylline also activates histone deacetylase-2 (HDAC2), which may restore corticosteroid sensitivity in COPD.
- **Nasal cavity disease** (specifically allergic rhinitis) is plausible given theophylline's anti-inflammatory effects on eosinophils and T cells. A small slow-release theophylline nasal challenge study exists, as does a Phase 2 trial.

---

## Clinical Trial Evidence

No clinical trials are registered for thrombotic disease, the top-ranked prediction. The trials below were retrieved under the **obstructive lung disease** entry (the most evidence-rich prediction), and are shown as the nearest relevant evidence for theophylline. Up to 10 of the most relevant are listed.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01599871](https://clinicaltrials.gov/study/NCT01599871) | Phase 3 | Completed | 70 | 52-week double-blind, placebo-controlled trial of low-dose theophylline added to LABA/ICS in severe COPD; primary outcome is exacerbation rate |
| [NCT02340520](https://clinicaltrials.gov/study/NCT02340520) | Phase 3 | Completed | 13 | Pilot of theophylline and roflumilast effects on circulating HDAC levels and corticosteroid response in COPD |
| [NCT03984188](https://clinicaltrials.gov/study/NCT03984188) | Phase 3 | Completed | 100 | Low-dose theophylline in biomass-associated COPD |
| [NCT00252785](https://clinicaltrials.gov/study/NCT00252785) | Phase 3 | Completed | 340 | 8-week study of Symbicort versus Pulmicort plus theophylline (Theolong) in Japanese asthma patients |
| [NCT00000578](https://clinicaltrials.gov/study/NCT00000578) | Phase 3 | Completed | Not reported | Inhaled beclomethasone versus theophylline for moderate asthma in pregnancy |
| [NCT00299858](https://clinicaltrials.gov/study/NCT00299858) | Phase 2/3 | Completed | 24 | Theophylline's effect on exercise capacity and lung function in COPD patients on long-acting bronchodilators |
| [NCT00119496](https://clinicaltrials.gov/study/NCT00119496) | Phase 2/3 | Completed | 79 | Rosiglitazone, theophylline and inhaled corticosteroid in asthmatic smokers |
| [NCT02261727](https://clinicaltrials.gov/study/NCT02261727) | Phase 4 | Completed | 1670 | TASCS trial: low-dose theophylline, alone or with low-dose prednisone, on COPD exacerbations over 48 weeks |
| [NCT01132781](https://clinicaltrials.gov/study/NCT01132781) | Phase 2 | Completed | 28 | Theophylline in allergic rhinitis (relevant to the nasal cavity disease prediction) |
| [NCT00241631](https://clinicaltrials.gov/study/NCT00241631) | Phase 2 | Completed | 49 | Theophylline and fluticasone on induced sputum cells in COPD |

---

## Literature Evidence

No retrieved publication evaluates theophylline for thrombotic disease. The most relevant publications are shown below, drawn from the obstructive lung disease, nasal cavity disease and tracheal disease entries.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23672674](https://pubmed.ncbi.nlm.nih.gov/23672674/) | 2013 | Review | Am J Respir Crit Care Med | Theophylline as bronchodilator at high doses and anti-inflammatory agent at lower concentrations in asthma and COPD |
| [37524492](https://pubmed.ncbi.nlm.nih.gov/37524492/) | 2023 | Review | Adv Pharmacol | PDE inhibitors, beginning with theophylline, as targets in COPD, asthma and other lung diseases |
| [16267358](https://pubmed.ncbi.nlm.nih.gov/16267358/) | 2005 | Review | Proc Am Thorac Soc | Low-dose theophylline activates HDAC and has anti-inflammatory effects in COPD |
| [27844172](https://pubmed.ncbi.nlm.nih.gov/27844172/) | 2017 | Review | Handb Exp Pharmacol | Xanthines now mostly third-line because of a narrow therapeutic window and drug interactions |
| [3534060](https://pubmed.ncbi.nlm.nih.gov/3534060/) | 1986 | Clinical study | J Allergy Clin Immunol | Theophylline improves global cardiac function and reduces dyspnoea in chronic obstructive lung disease |
| [9648963](https://pubmed.ncbi.nlm.nih.gov/9648963/) | 1998 | Clinical challenge study | Eur Respir J | Slow-release theophylline and nasal eosinophilic response after allergen challenge in allergic rhinitis |
| [12535389](https://pubmed.ncbi.nlm.nih.gov/12535389/) | 2003 | Systematic review | Cochrane Database Syst Rev | Prophylactic methylxanthines for extubation in preterm infants (different population and mechanism) |
| [31565900](https://pubmed.ncbi.nlm.nih.gov/31565900/) | 2019 | Retrospective cohort (veterinary) | J Vet Sci | Theophylline-based therapy in 47 small-breed dogs with tracheal collapse |
| [2353933](https://pubmed.ncbi.nlm.nih.gov/2353933/) | 1990 | Preclinical | Biochem Pharmacol | Methylxanthine analogues relax guinea pig trachea in vitro |
| [2728504](https://pubmed.ncbi.nlm.nih.gov/2728504/) | 1989 | Case report | DICP | Theophylline toxicity after isoniazid co-administration |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0301030S0AAAMAM | Theophylline 200 mg modified-release tablets | Modified-release tablet | Not stated in the data compiled for this report |

Only one valid single-ingredient authorisation is recorded, and the dosage form, manufacturer and approved indication text are missing. The identifier shown is not in the usual MHRA PL format. Verify the authorisation details against the MHRA register, the SmPC and the BNF (respiratory system, bronchodilators, section 3.1.3) before relying on them. Check NICE guidance directly for any appraised indications.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug-disease contraindication edges, not label text; they need confirming against the SmPC):

hypertension, liver failure and liver disease, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, open-angle glaucoma, psychotic disorders, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, neutropenia and agranulocytosis. Others include dysthymic disorder, gallbladder disease, pyoureter, dermatitis herpetiformis and agranulocytosis.

**Drug interactions:** 100 interactions were recorded in total, and 20 are shown in the data compiled for this report.

- **Major:** bupropion.
- **Moderate:** H2 antagonists and PPIs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), macrolides (clarithromycin), tetracyclines (doxycycline, minocycline, tetracycline), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes) and activated charcoal.
- **Minor:** ephedrine (including nasal).

**Practical guardrails** (from the evidence retrieved):

- Theophylline has a narrow therapeutic index and needs therapeutic drug monitoring.
- CYP1A2 polymorphisms and smoking status affect clearance.
- Toxicity after isoniazid co-administration has been reported.
- Pharmacokinetic interaction studies exist, for example with azithromycin.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold** (for the lead prediction, thrombotic disease)

**Rationale:**
- Thrombotic disease has no registered trials and no supporting literature, so the prediction is model-only (L5). The platelet cAMP link is plausible in theory, but the retrieved papers are unrelated to theophylline as an antithrombotic.
- Obstructive lung disease (L1, Proceed with Guardrails) has Phase 3 RCTs, but it overlaps the established indications and is not new repurposing. Nasal cavity disease (allergic rhinitis) and tracheal disease (both L3) are research questions only.
- Laryngotracheitis, pharyngitis and acute laryngopharyngitis should be held; they have no usable evidence.

**To proceed, the following is needed:**
- Confirm the SmPC indications, dosage form and product details for the UK authorisation, and fill the missing warnings and contraindications from the SmPC and BNF.
- For thrombotic disease: preclinical or in vitro data on theophylline's effect on platelet aggregation at clinically achievable concentrations, and a literature search targeted at theophylline specifically, before any clinical work.
- For allergic rhinitis: an adequately powered randomised trial, building on NCT01132781, with a safety assessment given the narrow therapeutic index.
- For obstructive lung disease: confirm positioning against current NICE and BTS guidance, and keep theophylline within a therapeutic drug monitoring and interaction-management plan.
- Detailed mechanism-of-action data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

