---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Nitrofurantoin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not recorded in the licence data (nitrofurantoin is a urinary antibac…"
monitor_inn: "Nitrofurantoin"
predicted_indications: ["rheumatoid arthritis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "sclerosing cholangitis", "methemoglobinemia, alpha type", "gout", "methemoglobinemia"]
---

# Nitrofurantoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Nitrofurantoin is an antibacterial agent used for urinary tract infections, although no approved indication text is recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **no registered clinical trials** and the **9 publications** retrieved mostly describe toxicity or co-occurrence rather than benefit.
This prediction should be treated as a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data (nitrofurantoin is a urinary antibacterial) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrofurantoin is a nitrofuran antibacterial whose efficacy in urinary tract infection is well established. No anti-inflammatory or immunomodulatory mechanism relevant to rheumatoid arthritis has been established.

The high TxGNN score (0.9989) appears to reflect network associations rather than a therapeutic rationale. The retrieved papers describe nitrofurantoin-associated pulmonary toxicity, including a case where a methotrexate-nitrofurantoin interaction caused irreversible pulmonary fibrosis in a patient with rheumatoid arthritis. They also include a UK self-controlled case series examining antibiotic exposure and rheumatoid arthritis flares. These point to co-occurrence and possible harm, not treatment benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | UK CPRD GOLD analysis of antibiotic use and rheumatoid arthritis flares in 31,992 newly diagnosed patients; examines association, not treatment effect |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis; lists nitrofurantoin as a cause and rheumatoid arthritis as a predisposing disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung diseases; nitrofurantoin among implicated antibiotics |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | Methotrexate plus nitrofurantoin caused irreversible pulmonary fibrosis in a 94-year-old woman with rheumatoid arthritis |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Poor prognosis in rheumatoid arthritis patients hospitalised with interstitial lung fibrosis; not specific to nitrofurantoin |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury; nitrofurantoin listed among drugs to exclude |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de Pneumologie Clinique | Gold salt-induced pneumonitis in rheumatoid disease context; not about nitrofurantoin therapy |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis; nitrofurantoin mentioned as a rare cause |

None of these publications shows a therapeutic benefit of nitrofurantoin in rheumatoid arthritis.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501130R0AAAAAA (BNF code) | Nitrofurantoin capsules 50 mg | Capsule | Not recorded in the data compiled for this report |

## Safety Considerations

- **Conditions flagged as contraindications or cautions in the knowledge graph** (these come from a knowledge graph, not from label text, and should be checked against the SmPC): impaired renal function, anuria, G6PD deficiency, interstitial lung disease, pulmonary fibrosis, peripheral neuropathy, optic neuritis, drug-induced liver injury, hepatitis, biliary tract disease, obstructive jaundice, vitamin B12 deficiency, vitamin B deficiency, diabetes mellitus, diabetic ketoacidosis, *Clostridium difficile* colitis, cystinuria, galactosemia and glycogen storage disease.
- **Safety signals in the retrieved literature**: pulmonary fibrosis and interstitial lung disease (including with methotrexate co-use in rheumatoid arthritis), hepatotoxicity including autoimmune-like hepatitis, and haemolytic anaemia and methemoglobinaemia, particularly in G6PD deficiency.
- **Drug interactions**: 100 interactions were identified. Those listed in the data include moderate interactions with balsalazide, metronidazole, picosulfuric acid, naltrexone, rosuvastatin and simvastatin. Minor interactions include antimuscarinics (atropine, hyoscyamine, glycopyrronium, dicyclomine, scopolamine and others) and magnesium-containing antacids.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, the literature shows toxicity and co-occurrence rather than benefit, and the safety profile (pulmonary, hepatic and haematological) is unfavourable in a population often treated with methotrexate.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale for rheumatoid arthritis
- Preclinical evidence of anti-inflammatory or immunomodulatory activity
- Complete licence details (approved indication and dosage form) and SmPC warnings and contraindications
- A formal safety assessment, including interaction with methotrexate and long-term pulmonary and hepatic risk

**Other predicted indications:** None of the other nine predictions (including diabetic nephropathy, sclerosing cholangitis, methemoglobinemia and gout) has trial evidence or a supportive mechanism. For methemoglobinemia, sclerosing cholangitis and the ocular anomaly signal, the literature indicates adverse drug effects rather than therapeutic opportunity. All are also recommended as Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

