---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
description: "Metronidazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Metronidazole
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

## Metronidazole: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial, originally used for anaerobic bacterial infections, giardiasis, bacterial vaginosis and rosacea.
The TxGNN model predicts it may be effective for **pneumocystosis**, but there are **no registered clinical trials** and only **10 publications** (reviews and case reports that mention metronidazole incidentally), so the prediction is **not supported by the available evidence**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Metronidazole is a nitroimidazole that is generally understood to be activated in anaerobic bacteria and protozoa, which is the basis of its established uses.

The relationship between the original and predicted indications is weak. *Pneumocystis* is a fungus and, as far as the compiled assessment indicates, lacks the nitroreductase activation pathway on which metronidazole depends. The high TxGNN score therefore does not appear to be supported by a plausible mechanism. The retrieved literature consists of general antiparasitic reviews and HIV opportunistic infection papers that mention metronidazole only incidentally. The standard treatment for *Pneumocystis* pneumonia cited in these papers is trimethoprim-sulfamethoxazole, not metronidazole.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | General review of antiparasitic agents; no evidence of metronidazole activity against *Pneumocystis* |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Lists metronidazole for amoebiasis and trichomoniasis; trimethoprim-sulfamethoxazole is the drug of choice for pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic basis of antiprotozoal therapy; no *Pneumocystis* efficacy data for metronidazole |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Treatment of infectious complications of AIDS; *Pneumocystis* pneumonia discussed as the most common complication |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV-related opportunistic infections; no evidence for metronidazole in pneumocystosis |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials; not specific to pneumocystosis |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | *Pneumocystis* and CMV pneumonia in a patient previously given metronidazole and tetracycline for diarrhoea; metronidazole was not a treatment for the pneumonia |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Two AIDS patients; metronidazole used for amoebic dysentery, not for pneumocystosis |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | Colon perforation in an AIDS patient with amoebic colitis and CMV; unrelated to pneumocystosis |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Case report | J Med Case Rep | Cerebellar abscess in sarcoidosis; unrelated to pneumocystosis |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501110C0AAAGAG | Metronidazole suppository 500 mg | Suppository (inferred from product name) | Not recorded in the data compiled for this report |

Only one single-ingredient authorisation record is available, and it is currently valid. The identifier does not follow the usual MHRA "PL" format, so it should be verified against the MHRA register before being relied on. Indication text and NICE or BNF classification details are not available here.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are drug-disease associations, not label text): liver failure and liver disease, epilepsy and brain disease, kidney disease, haematological disease (including neutropenia, agranulocytosis and leukopenia), blood coagulation disease, peripheral neuropathy and peripheral nervous system disease, optic nerve and visual pathway disease, non-infectious meningitis, diabetes mellitus and diabetic ketoacidosis, congestive heart failure, gallbladder disease, gout, dermatitis, substance abuse/dependence and pyoureter.

**Drug Interactions** (100 interactions recorded; selected examples):
- **Major:** Ethanol (avoid alcohol during and after treatment)
- **Moderate:** Paclitaxel, adalimumab, trastuzumab emtansine, ethinylestradiol, estradiol, butalbital, amobarbital, amiodarone, celecoxib, loperamide
- **Minor:** Abiraterone, tramadol, famotidine, salbutamol, alfuzosin, amisulpride, amitriptyline, anagrelide, propofol

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications Reviewed

For context, the other top-ranked predictions have similarly limited support:

| Rank | Predicted Indication | Evidence Level | Assessment |
|---|---|---|---|
| 2 | Punctate epithelial keratoconjunctivitis | L5 | Prediction only; no data |
| 3 | Ulcerative proctosigmoiditis | L5 | Biologically plausible (gut microbiota) but only general IBD reviews |
| 4 | Nocardiosis | L5 | No established activity; first-line is trimethoprim-sulfamethoxazole |
| 5 | Postmenopausal atrophic vaginitis | L5 | Oestrogen-deficiency condition; retrieved paper does not test metronidazole |
| 6 | Cryptococcal meningitis | L5 | Fungal; no antifungal mechanism |
| 7 | Papillary conjunctivitis | L5 | Prediction only; no data |
| 8 | Myiasis | L4 | Adjunct in wound care only; ivermectin is effective treatment |
| 9 | Cap polyposis | L4 | Case reports and one hypothesis paper; no controlled data |
| 10 | Ulceration of vulva | L5 | Indirect evidence (vulvar Crohn's, cutaneous amoebiasis) |

Cap polyposis and vulvar ulceration have the most substantive, though still low-grade, supporting literature and may merit a closer look as research questions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, pneumocystosis, has no clinical trials, no plausible mechanism and no literature showing efficacy, so it rests on the model score alone (L5). Established therapy for this condition is trimethoprim-sulfamethoxazole.

**To proceed, the following is needed:**
- Mechanism of action data to test whether any plausible link to *Pneumocystis* exists
- Preclinical or in vitro evidence of activity against *Pneumocystis*
- Complete UK licence details (indication text, dosage form, verified authorisation number) and SmPC warnings and contraindications
- If the programme is to be redirected, a structured review of cap polyposis and vulvar ulceration, where the existing literature is more relevant
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

