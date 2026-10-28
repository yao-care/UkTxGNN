---
layout: default
title: Sulfadiazine
parent: Model Prediction Only (L5)
nav_order: 580
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
monitor_inn: "Sulfadiazine"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis"]
description: "Sulfadiazine: predicted new indication Pneumocystosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Sulfadiazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Sulfadiazine: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Sulfadiazine is a sulfonamide antibacterial and antiprotozoal agent, originally used for toxoplasmosis and related conditions.
The TxGNN model predicts it may be effective for **pneumocystosis**,
but there are currently **no registered clinical trials** and only indirect literature (**19 publications**, mostly reviews and case reports) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sulfadiazine is a sulfonamide that inhibits dihydropteroate synthase (DHPS) in the folate synthesis pathway. *Pneumocystis jirovecii* depends on the same pathway.

Sulfonamides combined with dihydrofolate reductase (DHFR) inhibitors are established therapy for Pneumocystis pneumonia; the best-known regimen is trimethoprim-sulfamethoxazole. Sulfadiazine is already used with pyrimethamine for toxoplasmosis, an infection that often occurs alongside pneumocystosis in immunocompromised patients. This shared mechanism makes the high TxGNN score plausible.

However, the evidence for pneumocystosis is indirect. The retrieved literature mainly covers opportunistic infections in AIDS and protozoan infection therapy, where sulfadiazine is discussed chiefly for toxoplasmosis. Sulfadiazine is not a standard first-line agent for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomised controlled trials were identified. The publications below are reviews, case reports and observational reports, listed in priority order.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Summarises therapy and prophylaxis for Pneumocystis carinii, Toxoplasma gondii, Leishmania and trypanosome infections |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Antiparasitic drugs of choice; trimethoprim-sulfamethoxazole is listed for pneumocystis pneumonia, with sulfadiazine combinations for other protozoa |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Treatment of infectious complications of AIDS, including Pneumocystis pneumonia and toxoplasmosis |
| [7909657](https://pubmed.ncbi.nlm.nih.gov/7909657/) | 1994 | Review | Annals of Internal Medicine | Advances in managing AIDS-related opportunistic infections |
| [29604970](https://pubmed.ncbi.nlm.nih.gov/29604970/) | 2018 | Review | Handbook of Clinical Neurology | CNS Toxoplasma infection in HIV patients |
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Clinical report | Clinical Pharmacy | Pyrimethamine-sulfadiazine for Pneumocystis carinii pneumonia and toxoplasmosis in AIDS (no abstract available) |
| [2060528](https://pubmed.ncbi.nlm.nih.gov/2060528/) | 1991 | Observational | Eur J Clin Microbiol Infect Dis | Chart review of 35 AIDS patients on toxoplasmosis maintenance therapy; relapses of both toxoplasmosis and pneumocystosis occurred |
| [15673759](https://pubmed.ncbi.nlm.nih.gov/15673759/) | 2005 | Laboratory study | Antimicrob Agents Chemother | DHPS mutations in *P. jirovecii* confer cross-resistance to sulfa drugs |
| [34941194](https://pubmed.ncbi.nlm.nih.gov/34941194/) | 2021 | Case report | Medicine | Pulmonary toxoplasmosis exacerbation during corticosteroid therapy |
| [9122147](https://pubmed.ncbi.nlm.nih.gov/9122147/) | 1997 | Review | Presse Medicale | Prevention of parasitic opportunistic infections in HIV; trimethoprim-sulfamethoxazole is the agent of choice for pneumocystis prophylaxis |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501080J0AAABAB (BNF-style code; PL number not provided) | Sulfadiazine Tablets 500 mg | Tablet | Indication text not available |

---

## Safety Considerations

- **Contraindications and conditions of concern** (from knowledge graph drug-disease contraindication links, not label text): porphyria (including inherited forms), kidney disease, urinary tract obstruction, liver disease, gallbladder disease, G6PD deficiency, slow acetylator status, asthma, and blood disorders (anaemia including macrocytic, folic acid deficiency and aplastic anaemia, leukopenia, neutropenia, agranulocytosis, thrombocytopenia). Other listed conditions are glycogen storage disease, cystinuria and galactosemia.
- **Drug interactions**: 82 interactions were identified, all of those listed being of moderate severity. The main groups are:
  - Antidiabetic agents, with a risk of enhanced hypoglycaemic effect: sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide), meglitinides (repaglinide, nateglinide) and multiple insulins.
  - Others: balsalazide, picosulfuric acid and naltrexone.
- A published case report describes acute renal failure with topical silver sulfadiazine, which is consistent with the renal and crystalluria concerns of the sulfonamide class.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, since sulfonamides inhibit DHPS and are established in Pneumocystis pneumonia. However, there are no registered trials, and the literature is indirect and mostly historical. Trimethoprim-sulfamethoxazole remains the standard, and *P. jirovecii* DHPS mutations may confer cross-resistance to sulfa drugs. The evidence level is L4, with safety data incomplete.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a direct comparison of sulfadiazine with trimethoprim-sulfamethoxazole against *P. jirovecii*
- Preclinical or clinical data specifically for sulfadiazine in pneumocystosis, for example in patients who cannot tolerate trimethoprim-sulfamethoxazole
- Full SmPC and BNF safety information (warnings and contraindications), and the approved indication text for the UK licence
- A monitoring plan for haematological, renal and hepatic parameters, and for G6PD deficiency screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

