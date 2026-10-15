---
layout: default
title: Lopinavir
parent: Moderate Evidence (L3-L4)
nav_order: 379
evidence_level: L4
indication_count: 3
---

# Lopinavir
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

# Lopinavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV protease inhibitor, originally used to treat HIV infection and AIDS (in the UK it is given in a fixed combination with ritonavir).
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but this is essentially an animal-model extension of the existing HIV indication rather than a new human indication.
Currently there are **0 clinical trials** and **3 publications** (all preclinical non-human primate studies) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the marketing authorisation records compiled for this report contain no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lopinavir is an HIV protease inhibitor, its efficacy in HIV infection and AIDS is established, and mechanistically it may be applicable to SIV infection.

SIV is a lentivirus closely related to HIV, and its protease is a homologous target, so a protease inhibitor effect is biologically plausible. However, SIV infection occurs in non-human primates, so this prediction is best read as an animal-model extension of the HIV indication, not a new human therapeutic use. Its main value is as a preclinical research model.

Two other predictions were also generated, but both are weaker. Feline acquired immunodeficiency syndrome (score 99.90%) is a veterinary indication with no supporting studies, so it is outside the scope of human drug repurposing. A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter (score 99.90%) has no identifiable mechanistic link to protease inhibition and may reflect a network artefact in the model.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical animal study (non-human primate) | Journal of Virology | Rapid viral decay in SIV-infected cynomolgus macaques given a 7-day course of quadruple antiretroviral therapy; used to compare viral dynamics with HIV-1 |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical animal study (SHIV construct, rhesus macaque) | Microbes and Infection | Construction of a SHIV carrying the HIV-1 protease gene, whose growth was blocked by a protease inhibitor in cell culture; proposed as a tool for in vivo testing of protease inhibitors |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical animal study (non-human primate) | Journal of Virological Methods | Oral HAART (AZT, 3TC and lopinavir/ritonavir) for 28 days in chronically SHIV-infected rhesus macaques; assessed the effect on the peripheral blood CD8 subset |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010G0BBACAC | Kaletra Tab 200mg/50mg | Not specified | Not specified |
| 0503010G0AAADAD | Lopinavir/Ritonavir Tab 100mg/25mg | Not specified | Not specified |

Both authorisations are valid single-ingredient records. The authorisation numbers shown are as listed in the data compiled for this report and are not in the standard MHRA PL format, so they should be verified against the MHRA register. Please check the BNF (section 5.3.1, HIV infection) and the relevant NICE guidance for the current approved indications.

---

## Safety Considerations

**Contraindications (from knowledge-graph drug-disease edges, not label text):** the TxGNN knowledge graph links lopinavir with caution or contraindication in the following groups:
- **Cardiac and rhythm disorders**: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, myocardial ischaemia, coronary artery disease, cardiomyopathy (including hypertrophic), endomyocardial fibrosis
- **Liver and biliary disease**: liver disease, cirrhosis, gallbladder disease, chronic hepatitis B and C infection, hyperbilirubinaemia, Gilbert syndrome
- **Metabolic disorders**: diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, hypertriglyceridaemia, familial combined hyperlipidaemia, potassium deficiency
- **Other**: pancreatitis, haemophilia

**Drug Interactions:** 65 interactions were recorded. Examples include:
- **Major**: dolasetron, papaverine
- **Moderate**: acarbose, dapagliflozin, metformin, levofloxacin, ondansetron, palonosetron, famotidine, and several laxatives (bisacodyl, castor oil, lactulose, lactitol, glycerin, magnesium citrate, magnesium hydroxide, mineral oil, phenolphthalein)
- **Minor**: cimetidine, clotrimazole

Several of these (dolasetron, ondansetron, levofloxacin, papaverine) relate to QT-prolongation risk, consistent with the cardiac contraindications above.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is three preclinical non-human primate studies, there are no registered clinical trials, and SIV infection is not a human disease. The prediction extends the existing HIV indication rather than offering a new human use. The other two predicted indications have no supporting evidence at all.

**To proceed, the following is needed:**
- Detailed mechanism of action data (for example from DrugBank)
- Full SmPC warnings and contraindications from the BNF or MHRA, as the data compiled for this report contains none
- Approved indication text, dosage forms and verified MHRA authorisation numbers for the two listed products
- A clear rationale for any use beyond preclinical research, such as a defined research role as a protease inhibitor model in SIV/SHIV systems
- A cardiac (QT), hepatic and metabolic safety review, given the contraindication and interaction signals above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

