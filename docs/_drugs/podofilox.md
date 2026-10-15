---
layout: default
title: Podofilox
parent: Model Prediction Only (L5)
nav_order: 505
evidence_level: L5
indication_count: 10
---

# Podofilox
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Podofilox: From Anogenital Warts to Vulvovaginal Candidiasis

## One-Sentence Summary

Podofilox (podophyllotoxin) is a topical antimitotic originally used for anogenital human papillomavirus infection (genital warts) and common warts.
The TxGNN model's top-ranked prediction is **vulvovaginal candidiasis**, but this is supported by **no clinical trials** and only **1 general review**, and a credible mechanistic link is lacking.
The only well-supported prediction in the list is human papillomavirus infection, which is the drug's existing indication rather than a new one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anogenital human papillomavirus infection; common wart |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, podofilox is a purified form of podophyllotoxin. It binds tubulin, inhibits microtubule assembly and arrests mitosis, which causes necrosis of wart tissue. This is a lesion-directed effect rather than a true antiviral effect, so it does not eradicate the virus and recurrence is common.

The prediction for vulvovaginal candidiasis is **not mechanistically convincing**. Candidiasis is a fungal infection, and antimitotic activity has no known antifungal action. The single retrieved paper is a 1999 general review of sexually transmitted disease treatment that covers both vaginal infections and genital warts. It most likely mentions podofilox only in the context of warts. The high score probably reflects co-occurrence of these conditions in the STD literature rather than a real therapeutic link.

Other predicted indications (photosensitivity disease, herpes zoster, benign neoplasms of the tongue and hypopharynx, cystic neoplasm, mesenchymoma, nasal inverting papilloma, testicular tumour) also have no clinical trials or literature. Several involve sites unsuitable for topical podofilox. Etoposide, a podophyllotoxin derivative, is used in testicular cancer, but it is a different compound with a different mechanism (topoisomerase II inhibition) and does not support podofilox.

The prediction that matches the evidence is **human papillomavirus infection** (score 99.20%). This is already the labelled use, so it confirms the original indication rather than representing repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvovaginal candidiasis or for any of the other predicted indications in the data compiled for this report.

## Literature Evidence

**Vulvovaginal candidiasis (top prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10537386](https://pubmed.ncbi.nlm.nih.gov/10537386/) | 1999 | Review | American Family Physician | General review of CDC 1998 STD treatment guidance covering vaginal infections and genital warts. Does not appear to support podofilox use in candidiasis. |

**Human papillomavirus infection (existing indication, for context)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2186623](https://pubmed.ncbi.nlm.nih.gov/2186623/) | 1990 | RCT | American Journal of Medicine | Double-blind trial of self-applied 0.5% podofilox solution versus vehicle for penile warts. |
| [2014088](https://pubmed.ncbi.nlm.nih.gov/2014088/) | 1991 | RCT | Obstetrics and Gynecology | Double-blind, placebo-controlled trial of 0.5% podofilox in 72 women with external genital warts. |
| [2564912](https://pubmed.ncbi.nlm.nih.gov/2564912/) | 1989 | Double-blind trial | Lancet | 25 of 56 podofilox-treated patients became wart-free versus none of 53 on placebo. Warts cleared by 73.6% versus 8.3%. |
| [9449907](https://pubmed.ncbi.nlm.nih.gov/9449907/) | 1998 | Clinical study | Archives of Dermatology | Safety and efficacy of 0.5% podofilox gel in anogenital warts. |
| [8192173](https://pubmed.ncbi.nlm.nih.gov/8192173/) | 1994 | Clinical study | American Journal of Medicine | 0.5% podofilox solution for treatment and suppression of anogenital warts. |
| [39964927](https://pubmed.ncbi.nlm.nih.gov/39964927/) | 2025 | Review | American Family Physician | Rapid evidence review of genital warts. |
| [25251091](https://pubmed.ncbi.nlm.nih.gov/25251091/) | 2014 | Review | American Family Physician | Management of external genital warts, including patient-applied treatments. |
| [11737696](https://pubmed.ncbi.nlm.nih.gov/11737696/) | 2001 | Retrospective analysis | Pediatric Dermatology | 15 of 17 children treated with podofilox gel improved or cleared. |
| [8245513](https://pubmed.ncbi.nlm.nih.gov/8245513/) | 1993 | Animal study | Journal of Investigative Dermatology | Podofilox-induced papilloma regression in rabbits may be independent of host immunity. |
| [2216198](https://pubmed.ncbi.nlm.nih.gov/2216198/) | 1990 | Clinical study | Obstetrics and Gynecology | Topical 0.5% podofilox for condylomata acuminata in 37 women. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1307000K0AAABAB | Podophyllotoxin cream 0.15% | Not specified | Not specified in the data compiled |

Dosage form and approved indication text are not available in the data compiled for this report. Please confirm the licence details against the MHRA record and the BNF.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Practical guardrails from the existing wart indication: use only on external anogenital or common warts, limit the treated area and dose, avoid use in pregnancy, and monitor for local irritation. Topical use on mucosal sites raises concern about systemic absorption and toxicity.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted new indication, vulvovaginal candidiasis, has no clinical trials, no plausible antifungal mechanism, and appears to be an artefact of co-occurrence in STD literature. The other new predictions are also computational only (evidence level L5). The one well-evidenced prediction, HPV infection and genital warts, is the existing licensed use and would be Proceed with Guardrails as a confirmation of the original indication, not as repurposing.

**To proceed, the following is needed:**
- Any in vitro or clinical evidence of antifungal activity, which is currently absent
- Mechanism of action data to be confirmed from DrugBank
- Full licence details (dosage form, approved indication) for the UK authorisation
- Safety data from the SmPC, including warnings and contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

