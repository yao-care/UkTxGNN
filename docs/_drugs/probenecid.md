---
layout: default
title: Probenecid
parent: Moderate Evidence (L3-L4)
nav_order: 521
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Probenecid: predicted new indication Renal hypouricaemia (evidence level L4). Approved use: Gout"
---

# Probenecid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Probenecid: From Gout to Renal Hypouricaemia

## One-Sentence Summary

Probenecid is a uricosuric drug originally used to treat gout and hyperuricaemia.
The TxGNN model predicts it may be relevant to **renal hypouricaemia**, but the data compiled for this report show **0 clinical trials** and **20 publications**, none of which evaluates probenecid as a treatment. The prediction appears to reflect shared urate-transport biology rather than a therapeutic relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; hyperuricaemia (the licence record held no approved indication text, so these come from the knowledge-graph indication edges) |
| Predicted New Indication | Renal hypouricaemia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Probenecid is, however, a known uricosuric. It inhibits the renal urate transporter URAT1 (SLC22A12) and the organic anion transporters OAT1 and OAT3. This reduces urate reabsorption in the kidney and lowers serum urate, which is why it is used in gout.

The predicted indication is mechanistically problematic. Hereditary renal hypouricaemia is caused by loss-of-function variants in URAT1 (SLC22A12) or GLUT9 (SLC2A9). These variants already cause excessive urinary urate loss. Probenecid would be expected to **worsen** this defect rather than correct it. It could increase urate wasting and the risk of exercise-induced acute kidney injury and urolithiasis.

The high TxGNN score probably reflects network proximity through urate-transport biology, not a therapeutic relationship. A more plausible role for probenecid is as a pharmacological probe. Several of the retrieved case reports used the uricosuric response to probenecid, alongside pyrazinamide, to characterise the tubular defect.

Two lower-ranked predictions were also generated. **Lesch-Nyhan syndrome** (score 99.39%, L5) and **partial HGPRT deficiency** (score 99.37%, L5) both involve purine overproduction. In both, increasing urinary urate load may raise the risk of urate stones and nephropathy, and xanthine oxidase inhibition (for example allopurinol) is the standard of care. Neither has clinical trials. Lesch-Nyhan syndrome has two retrieved publications, a computational modelling study and a 1976 biochemical overview of Tourette syndrome. Partial HGPRT deficiency has none.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Twenty publications were retrieved for renal hypouricaemia. They are reviews, case reports, and cohort or mechanistic studies of the disease. **None evaluates probenecid as a treatment.** Ten of the most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort (genetic analysis) | J Am Soc Nephrol | SLC22A12 (URAT1) sequenced in 32 patients with idiopathic renal hypouricaemia; links genotype to urinary urate excretion |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | Hereditary renal hypouricaemia is mostly due to loss-of-function mutations in URAT1 |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Narrative update on the causes and clinical approach to hypouricaemia |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Review/Case report | Am J Kidney Dis | Prevention of exercise-induced acute renal failure in renal hypouricaemia |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Attenuated uric acid clearance response to probenecid and pyrazinamide, suggesting a proximal tubular reabsorption defect |
| [8533596](https://pubmed.ncbi.nlm.nih.gov/8533596/) | 1995 | Case report | Acta Paediatr Jpn | Acute renal failure after exercise in a child; probenecid and pyrazinamide tests showed a total defect of uric acid transport |
| [2709741](https://pubmed.ncbi.nlm.nih.gov/2709741/) | 1989 | Case report | Klin Wochenschr | Uric acid nephropathy with acute renal failure; probenecid enhanced fractional urate excretion |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Hypouricaemia with urolithiasis; probenecid increased urate clearance; urolithiasis treated by urine alkalinisation |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Mechanistic (mouse) | J Am Soc Nephrol | Function and localisation of the mouse URAT1 homologue in kidney |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Observational | Nephron | Renal hypouricaemia with high urate clearance in 14 patients with type 1 diabetes |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001040K0AAAAAA | Probenecid Tablets 500 mg | Tablet (not stated in the licence record) | Not stated in the licence record |

This is the only authorisation in the compiled data, and the identifier does not follow the usual PL number format. Please verify the authorisation details against the MHRA register.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph.** These come from drug-disease contraindication links in the TxGNN knowledge graph, not from label text:
- Liver failure, kidney disease and impaired renal function
- Haematological disorders, including thrombocytopenia, leukopenia, agranulocytosis and neutropenia (including congenital forms)
- Peptic ulcer disease
- Muscle disorders, including myopathy and rhabdomyolysis
- Gastrointestinal conditions, including diarrhoeal disease and *Clostridium difficile* colitis

These links are directly relevant to this report. Renal impairment and rhabdomyolysis overlap with the main risk in renal hypouricaemia, which is exercise-induced acute kidney injury.

**Drug interactions (71 recorded; selected examples):**
- **Major:** phenylbutyric acid; glycerol phenylbutyrate
- **Moderate:** aspirin (acetylsalicylic acid); sulfonylureas and related antidiabetic drugs (chlorpropamide, glimepiride, glipizide, glyburide, tolbutamide, tolazamide, acetohexamide); meglitinides (repaglinide, nateglinide)
- **Minor:** famotidine, amoxicillin, levofloxacin, eluxadoline

For full warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism points in the wrong direction. A drug that increases renal urate excretion is unlikely to help conditions in which urate is already wasted through the kidney, and it may cause harm. No clinical trials exist, and none of the retrieved publications tests probenecid as a treatment. The same applies to Lesch-Nyhan syndrome and partial HGPRT deficiency, where uricosuric therapy is generally disfavoured.

**To proceed, the following is needed:**
- Mechanism of action data for probenecid, and licence label text covering indications, warnings and contraindications, so that the safety screen can be completed
- A clear case for a therapeutic (rather than diagnostic) rationale in renal hypouricaemia. Without one, repurposing is not recommended
- Mechanistic or preclinical studies showing benefit in any of the three predicted conditions, with particular attention to the risks of urolithiasis and acute kidney injury
- A review of whether the diagnostic use of probenecid in characterising tubular urate defects is of interest in its own right
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

