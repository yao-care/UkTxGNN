---
layout: default
title: Nalidixic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 432
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Nalidixic Acid: predicted new indication Conjunctivitis (evidence level L4). Approved use: Not recorded in the compiled data (the authorisation entry has no ind…"
monitor_inn: "Nalidixic acid"
predicted_indications: ["conjunctivitis", "sclerosing cholangitis", "rheumatoid arthritis", "infectious otitis media"]
---

# Nalidixic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

## Nalidixic Acid: From Bacterial Infection (Original Indication Not Recorded) to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Nalidixic acid is a first-generation quinolone antibacterial. It is marketed in the UK as an oral suspension, but the data compiled for this report do not record its approved indication.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **no registered clinical trials** and only **5 publications**, none of which studies nalidixic acid in eye infection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the compiled data (the authorisation entry has no indication text) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data are not available in the compiled data. Based on general pharmacology, nalidixic acid is a quinolone antibacterial that inhibits bacterial DNA gyrase (topoisomerase II) and topoisomerase IV. Bacterial conjunctivitis is, in principle, susceptible to antibacterial activity, which is the likely basis for the model's prediction.

However, the prediction is weakly supported. The retrieved literature concerns *Shigella* and *Yersinia* serotyping, plasmids and antibiotic resistance in diarrhoeal disease, not ocular infection. Nalidixic acid is also a first-generation quinolone with a narrow spectrum (mainly Gram-negative Enterobacteriaceae) and limited potency. Later fluoroquinolones and other topical agents are the established ocular options. The high TxGNN score is therefore not backed by disease-specific clinical evidence.

Other predictions in the data are weaker still:
- **Sclerosing cholangitis** (score 99.63%): no trials or literature, purely computational (L5). Hepatic and CNS toxicity are concerns in a hepatobiliary disease.
- **Rheumatoid arthritis** (score 99.41%): one observational study of oral *Staphylococcus* colonisation, not drug-specific (L5).
- **Infectious otitis media** (score 99.04%): the only paper evaluates ofloxacin, a different quinolone. Nalidixic acid is poorly suited to the usual otitis pathogens (L4).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17446289](https://pubmed.ncbi.nlm.nih.gov/17446289/) | 2007 | Microbiological characterisation | J Med Microbiol | Novel *Shigella dysenteriae* serovar identified in patients with diarrhoea in Bangladesh; no ocular relevance |
| [16914657](https://pubmed.ncbi.nlm.nih.gov/16914657/) | 2006 | Microbiological surveillance | J Med Microbiol | Over 60% of *Shigella sonnei* isolates in Bangladesh were resistant to nalidixic acid; no ocular relevance |
| [15824427](https://pubmed.ncbi.nlm.nih.gov/15824427/) | 2005 | Microbiological characterisation | J Med Microbiol | Provisional *Shigella boydii* serovar E16553 isolated from diarrhoeal patients |
| [9442487](https://pubmed.ncbi.nlm.nih.gov/9442487/) | 1997 | Molecular/microbiological study | Microb Drug Resist | A 70-kb plasmid in epidemic *S. dysenteriae* type 1 linked to drug resistance and virulence |
| [3206956](https://pubmed.ncbi.nlm.nih.gov/3206956/) | 1988 | In vitro/experimental | Zh Mikrobiol Epidemiol Immunobiol | Invasiveness and cytotoxicity as criteria for *Yersinia* attenuation; nalidixic acid-resistant mutants used as a tool |

None of these papers evaluates nalidixic acid as a treatment for conjunctivitis.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501120N0AAAAAA (BNF-style code; not a PL number) | Nalidixic Acid Oral Suspension 300 mg/5 ml | Oral suspension | Not recorded in the compiled data |

The compiled data show one valid single-ingredient product. Dosage form and indication text were not supplied beyond the product name, so this entry should be verified against the MHRA record and the current BNF.

---

## Safety Considerations

**Contraindication-related conditions (from a drug-disease knowledge graph, not label text):**
The knowledge graph links nalidixic acid with contraindication to the following conditions, which should be checked against the SmPC:
- Neurological: epilepsy, central nervous system disease, peripheral neuropathy and other peripheral nervous system disease, nervous system disorder
- Metabolic: porphyria (including inherited porphyria), G6PD deficiency, glycogen storage disease, cystinuria, galactosaemia
- Hepatobiliary: liver disease, gallbladder disease
- Musculoskeletal: tendinitis, periarthritis, exostosis
- Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotising enterocolitis
- Other: narcolepsy-cataplexy syndrome, Balo concentric sclerosis, X-linked adrenoleukodystrophy

**Drug Interactions:** The interaction screen returned 100 records. The sample reviewed includes:
- **Major:** hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids), bupropion, chlorpropamide
- **Moderate:** antidiabetic agents (acarbose, albiglutide, alogliptin, canagliflozin, dapagliflozin, saxagliptin), aspirin, balsalazide, alosetron, and calcium, citrate and electrolyte-containing products

The corticosteroid interactions are consistent with the known quinolone-associated tendon risk. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a plausible antibacterial mechanism only. No clinical trials exist, the literature is unrelated to ocular infection, and better-established agents are available for conjunctivitis. Label-level safety data and the approved indication are also missing from the compiled data.

**To proceed, the following is needed:**
- Confirmation of the current UK approved indication, dosage form and SmPC warnings and contraindications (the missing label data block safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Disease-specific evidence for nalidixic acid in conjunctivitis, such as in vitro susceptibility of ocular pathogens or comparative clinical studies
- A rationale for using nalidixic acid over established ocular antibacterials, including an assessment of an ophthalmic formulation, as only an oral suspension is currently authorised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

