---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 60
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Amoxicillin: predicted new indication Hyperamylasaemia (evidence level L5). Approved use: Urinary tract infection, infectious otitis media…"
monitor_inn: "Amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Amoxicillin: From Bacterial Infections to Hyperamylasaemia

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic originally used for common bacterial infections such as urinary tract infection, otitis media, pharyngitis and bacterial pneumonia.
The TxGNN model predicts it may be effective for **hyperamylasaemia**, but there are **no clinical trials** and **no publications** supporting this prediction, and no plausible mechanism has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia, staphylococcal infection, pharyngitis and others (the licence record in the data compiled for this report has no indication text) |
| Predicted New Indication | Hyperamylasaemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Amoxicillin is known to be a beta-lactam antibiotic that inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections is well established.

Hyperamylasaemia, however, is a laboratory finding (raised serum amylase) rather than a bacterial disease, and it has no established antibacterial target. The review of the data found no mechanistic link between amoxicillin and this condition. The high TxGNN score (99.63%) is a graph-based prediction only and is not backed by any trial or publication, so it should be treated with caution.

Other high-scoring predictions (polyclonal hyperviscosity syndrome, congenital analbuminaemia, premalignant haematological disease and others) show the same pattern: no mechanistic rationale and no supporting data. The only prediction with a biologically plausible antibacterial rationale is **septicaemic plague** (a *Yersinia pestis* infection). It is scored lower (99.13%) and is classed as a research question. Standard plague therapy relies on aminoglycosides, fluoroquinolones or tetracyclines, and beta-lactams are generally not preferred.

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasaemia.

## Literature Evidence

Currently no related literature available for hyperamylasaemia.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501013B0AAAAAA | Amoxicillin capsules 250 mg | Capsule | Not stated in the compiled data |

The identifier above is a product code from the compiled data rather than a standard MHRA PL number. Please verify the authorisation details against the MHRA record, the BNF (section 5.1.1.3, penicillins with broader spectrum) and the relevant SmPC.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are drug-disease associations from the TxGNN knowledge graph, not label text, and must be checked against the SmPC):
- Hepatic: liver failure, liver disease, cholestasis (including benign recurrent and familial intrahepatic cholestasis), gallbladder disease
- Renal: kidney disease, pyoureter
- Cardiac rhythm: long QT syndrome, torsades de pointes, ventricular tachycardia (including catecholaminergic polymorphic and incessant infant forms)
- Metabolic: porphyria (inherited porphyria, porphyrin metabolism disease)
- Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotising enterocolitis
- Neuromuscular: myasthenia gravis (including adult-onset), neuromuscular junction disease
- Bone: osteoporosis, postmenopausal osteoporosis, bone fracture
- Infectious: infectious mononucleosis, chronic Epstein-Barr virus infection syndrome

**Drug Interactions** (100 interactions recorded; examples of those listed):
- **Major**: methotrexate; live cholera vaccine (*Vibrio cholerae* CVD 103-HgR)
- **Moderate**: tetracyclines (doxycycline, minocycline, demeclocycline), oestrogens (ethinylestradiol, estradiol), coumarin-type anticoagulants (anisindione, dicoumarol), mycophenolate mofetil, entecavir, balsalazide, and live probiotic preparations
- **Minor**: allopurinol, amiloride, macrolides (azithromycin, clarithromycin, erythromycin)

Package-insert warnings and contraindications were not available in the compiled data. Please refer to the SmPC and BNF, and report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or published evidence, no plausible mechanism, and only a graph-based score for amoxicillin in hyperamylasaemia (Evidence Level L5). The prediction is not actionable at present.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking amoxicillin to hyperamylasaemia, and the missing mechanism of action data
- Any clinical or preclinical evidence supporting the prediction
- Package-insert safety data (warnings and contraindications) and the approved indication text for the UK authorisation
- If the team wishes to pursue a more plausible direction, a separate evaluation of septicaemic plague as a research question, noting that current standard therapy does not favour beta-lactams
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

