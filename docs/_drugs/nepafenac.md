---
layout: default
title: Nepafenac
parent: High Evidence (L1-L2)
nav_order: 439
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Nepafenac: predicted new indication Eye disease (evidence level L1). Approved use: Not available in the UK licence data compiled for this report"
monitor_inn: "Nepafenac"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
---

# Nepafenac
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Nepafenac: From Ocular Inflammation Use to Eye Disease
{: .text-alpha }

## One-Sentence Summary

Nepafenac is a topical non-steroidal anti-inflammatory drug (NSAID) eye drop, marketed in the UK as a 1 mg/ml eye drop.
The TxGNN model predicts it may be effective for **eye disease** (a broad category), with **40 clinical trials** and **19 publications** compiled for this direction.
Note that this is largely confirmation of an existing ocular use (post-cataract-surgery inflammation, pain and macular oedema) rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the UK licence data compiled for this report |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L1 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nepafenac is a prodrug. Ocular tissue hydrolases convert it to amfenac, which inhibits both COX-1 and COX-2. This reduces prostaglandin synthesis, and so lowers ocular inflammation, pain and breakdown of the blood-retinal barrier. Detailed mechanism-of-action data were not available in the source database, but this mechanism is well described in the literature compiled for this report.

The predicted indication "eye disease" is very broad. The trial and literature evidence centres on post-cataract-surgery inflammation and pain, and on prevention of macular oedema (including in diabetic patients). The mechanism fits these conditions directly. Smaller studies extend to retinal surgery, photorefractive keratectomy (PRK) pain and laser iridotomy.

The other nine predictions in the data are much weaker. Optic papillitis has only indirect evidence (a rabbit retinal oedema study and one cataract-surgery trial), and vitreous detachment has one biomarker trial in a related condition (retinal detachment). The remaining seven (for example seborrheic keratosis and lagophthalmos) have no trials or literature and no plausible mechanism; they are computational predictions only and are not recommended for further pursuit.

---

## Clinical Trial Evidence

Forty trials were compiled. The most relevant are listed below (selected by relevance and size).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Nepafenac 0.3% for prevention and treatment of inflammation and pain after cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% vs vehicle for clinical outcomes in diabetic patients after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Replicate of the above diabetic cataract-surgery study; once-daily nepafenac 0.3% vs vehicle |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for inflammation and pain after cataract surgery |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Once-daily nepafenac 0.3% vs placebo for prevention of pseudophakic cystoid macular oedema |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | NEVANAC 0.1% vs vehicle for macular oedema after cataract surgery in diabetic retinopathy |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | Completed | 227 | European study: nepafenac 0.1% vs ketorolac 0.5% vs placebo after cataract surgery |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% vs vehicle in Chinese adults after cataract surgery |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | Terminated | 175 | NEVANAC for macular oedema in diabetic retinopathy within 90 days of cataract surgery |
| [NCT07736690](https://clinicaltrials.gov/study/NCT07736690) | Phase 4 | Completed | 60 | Perioperative topical nepafenac and early recovery after epiretinal membrane surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Systematic review / network meta-analysis | Eye (London) | Compared topical NSAIDs for macular oedema and visual outcome after phacoemulsification |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Cochrane review | Cochrane Database Syst Rev | Topical NSAIDs for diabetic cystoid macular oedema |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Nepafenac in cataract surgery: high ocular penetration, reduces inflammation, pain and macular oedema risk |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | 0.1% nepafenac vs 1% prednisolone after micro-incisional cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | 0.1% nepafenac vs 1% prednisolone acetate after laser peripheral iridotomy |
| [41039316](https://pubmed.ncbi.nlm.nih.gov/41039316/) | 2025 | Comparative study | BMC Ophthalmol | Analgesic efficacy of seven topical NSAIDs in panretinal photocoagulation pain |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAIDs in retinal diseases |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Preclinical PK study | Exp Eye Res | Topical nepafenac and amfenac reach the posterior segment of the eye |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | Case report | J Cataract Refract Surg | Corneal melt associated with nepafenac after cataract surgery (safety signal) |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclinical (rat) | Diabetes | Topical nepafenac inhibited early diabetic retinal microvascular disease |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1108020AFAAAAAA (BNF/dm+d product code) | Nepafenac eye drops 1 mg/ml | Eye drops | Not stated in the data compiled |

One valid single-ingredient authorisation is recorded. Dosage form and indication text were not available in the compiled data, so please check the SmPC and the relevant NICE guidance.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** rheumatoid arthritis, diabetes mellitus, diabetic ketoacidosis, blood coagulation disease, keratitis, keratoconjunctivitis, dry eye syndrome, xerophthalmia and corneal ulcer. These are model-derived associations and should be checked against the SmPC.
- **Corneal safety:** a published case report describes corneal melt with nepafenac in a patient with graft-versus-host disease after cataract surgery, consistent with the known class concern of topical NSAIDs and corneal healing problems.
- **Drug interactions:** no interaction data were found in the compiled data.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For the core ocular inflammation, pain and macular oedema setting, multiple completed Phase 3 trials (including large studies of 800 to 2,000 participants) support efficacy, and the drug is already marketed in the UK. However, "eye disease" is a very broad prediction, and the other predicted indications (optic papillitis, vitreous detachment and the dermatological or rare-disease predictions) lack meaningful evidence and should be held.

**To proceed, the following is needed:**
- Confirmation of the licensed UK indications, dosage form and warnings from the SmPC and BNF
- A defined, specific target indication (for example diabetic macular oedema prevention or vitreoretinal surgery) rather than "eye disease"
- Review of corneal safety risk in patients with keratitis, dry eye, corneal ulceration, diabetes or rheumatoid arthritis
- Mechanism-of-action data from DrugBank to complete the record
- Further controlled evidence before considering any of the lower-ranked predictions (optic papillitis, vitreous detachment)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

