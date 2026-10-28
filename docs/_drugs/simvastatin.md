---
layout: default
title: Simvastatin
parent: Model Prediction Only (L5)
nav_order: 569
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "Simvastatin"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Simvastatin: predicted new indication Brain stem infarction (evidence level L5). Approved use: Not recorded in the local data"
---

# Simvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Simvastatin: Brain stem infarction
{: .text-alpha }

## One-Sentence Summary

Simvastatin is an HMG-CoA reductase inhibitor (statin) originally used for lipid disorders and the prevention of atherosclerotic vascular disease, including stroke.
The TxGNN model predicts it may be effective for **familial hypercholesterolaemia**, with **8 clinical trials** and **20 publications** compiled for this direction.
Familial hypercholesterolaemia overlaps with simvastatin's existing indications, so this is largely a confirmation of current use rather than true repurposing, and most trials test simvastatin in combination with other agents.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Simvastatin inhibits HMG-CoA reductase, the rate-limiting enzyme of hepatic cholesterol synthesis. Lower intracellular cholesterol upregulates LDL receptors, which increases clearance of LDL cholesterol (LDL-C) from the blood. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects the well-established pharmacology of the statin class.

In familial hypercholesterolaemia, LDL-C is persistently raised, mostly through LDL receptor pathway defects, and patients develop premature coronary artery disease. Because statins act on this same pathway, and residual LDL receptor function in heterozygous patients allows the response, the prediction is mechanistically coherent. Homozygous familial hypercholesterolaemia is already among simvastatin's listed original indications.

An important caveat: several Phase 3 trials test ezetimibe or alirocumab added to simvastatin, so the evidence for simvastatin alone is partly confounded by combination therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) (ENHANCE) | Phase 3 | Completed | 720 | Ezetimibe plus high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH (simvastatin-alone comparator arm) |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe with simvastatin vs simvastatin alone in adolescents (10–17 years) with heterozygous FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label safety and tolerability extension of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab vs placebo in heterozygous FH on lipid-modifying therapy (simvastatin likely background only) |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Open-label comparison of renal effects of rosuvastatin and simvastatin in Fredrickson type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab vs placebo in children and adolescents with heterozygous FH on statin therapy (simvastatin role not confirmed) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab in children and adolescents with homozygous FH (simvastatin at most background) |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Completed | 527 | Dose-ranging study of LY3015014 in primary hypercholesterolaemia with background statins (simvastatin not the test drug) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Trial report (ENHANCE) | N Engl J Med | Simvastatin with or without ezetimibe in FH, assessing effects on atherosclerosis progression |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolaemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Updated review of statins in children with FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Benefits and risks of simvastatin in FH; long-term safety and tolerability |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Benefit–risk assessment of simvastatin in FH |
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | Randomised double-blind trial | Circulation | Ezetimibe with atorvastatin or simvastatin in 50 patients with homozygous FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative study | Nutr Metab Cardiovasc Dis | Atorvastatin vs simvastatin for LDL-C goal attainment in heterozygous FH |
| [2679083](https://pubmed.ncbi.nlm.nih.gov/2679083/) | 1989 | Clinical study | Am J Med | Simvastatin 20 mg lowered LDL-C by 38% at 8 weeks, and 42% at 40 mg, in FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional study | J Clin Med | Cellular immunity in children with FH treated with simvastatin 10 mg |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guideline | J Am Coll Cardiol | 2026 ACC/AHA multisociety dyslipidaemia guideline, replacing the 2018 cholesterol guideline |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0212000Y0AAAAAA | Simvastatin Tab 10 mg | Not stated | Not stated |

Only one single-ingredient authorisation is recorded in the data compiled for this report. The dosage form and indication text are missing, and the identifier is not in the usual MHRA PL format, so it should be checked against the MHRA register. Please also consult the BNF (lipid-regulating drugs) and relevant NICE guidance for current UK use in familial hypercholesterolaemia.

---

## Safety Considerations

**Contraindications (from disease associations in the knowledge graph, not label text):** liver disease, pancreatitis, gallbladder disease, myopathy and other muscle diseases, rhabdomyolysis, thrombocytopenia, blood coagulation disorders, diabetes mellitus and diabetic ketoacidosis, hyperglycaemia, gout, peptic ulcer disease, hypotensive disorder, substance abuse/dependence, and several cardiac conditions (acute coronary syndrome, coronary artery disease, myocardial infarction). Several of these, such as coronary artery disease, are likely to be graph artefacts rather than true contraindications, so they should be verified against the SmPC.

**Drug Interactions:** The data list 100 interactions. Those classed as Major include:
- Amiodarone
- Amlodipine
- Fenofibrate

Moderate interactions include nifedipine, paclitaxel, omeprazole, zidovudine, ethanol, apalutamide and aprepitant. Simvastatin is a CYP3A4 substrate, so exposure rises markedly with CYP3A4 inhibitors such as HIV protease inhibitors and cobicistat, increasing the risk of myopathy and rhabdomyolysis.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials in familial hypercholesterolaemia include simvastatin, and its mechanism is well established, supporting evidence level L1. However, most trials test combinations, and the indication overlaps with existing use, so this confirms current practice rather than demonstrating new efficacy.

**To proceed, the following is needed:**
- Complete MHRA authorisation details (dosage form, indication text and a verified PL number)
- SmPC warnings and contraindications to replace the graph-derived list
- Evidence isolating simvastatin monotherapy from combination effects
- A drug-interaction management plan, particularly for CYP3A4 inhibitors and fibrates
- Detailed mechanism-of-action data from DrugBank

---

### Other Predicted Indications (for reference)

| Predicted Indication | Score | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|
| HIV infectious disease | 0.9922 | L3 | Research Question | Evidence concerns drug interactions and HIV-associated dyslipidaemia, not antiviral effect; one pilot study found no anti-HIV activity |
| Brain stem infarction | 0.9941 | L5 | Hold | Only a tangential preclinical paper; no trials |
| CETP deficiency | 0.9939 | L5 | Hold | Model prediction only |
| ABri amyloidosis | 0.9913 | L5 | Hold | Model prediction only |
| Neurodevelopmental disorder with ataxic gait and absent speech | 0.9910 | L5 | Hold | Model prediction only |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

