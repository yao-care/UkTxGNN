---
layout: default
title: Cyproheptadine
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Cyproheptadine: From Allergic Rhinitis to Cold Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation antihistamine, originally used for allergic conditions such as allergic rhinitis, urticaria and allergic conjunctivitis.
The TxGNN model predicts it may be effective for **allergic urticaria** (top-ranked) and **cold urticaria** (the best-supported prediction), with **no registered clinical trials** but **9 and 16 publications** respectively. Most of these are small, dated studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, atopic/vernal/papillary conjunctivitis, familial dermatographia, urticaria, angioedema (the UK licence entry carries no indication text) |
| Predicted New Indication | Allergic urticaria (rank 1); cold urticaria (rank 2) is the best-supported prediction |
| TxGNN Prediction Score | 99.96% (allergic urticaria); 99.76% (cold urticaria) |
| Evidence Level | L3 (cold urticaria); L5 (nasal cavity disease, acute laryngopharyngitis) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails (cold urticaria); Hold for allergic urticaria as a repurposing candidate, nasal cavity disease and acute laryngopharyngitis |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Cyproheptadine is known to be a first-generation H1 antihistamine with additional serotonin (5-HT2) antagonism and anticholinergic activity.

Urticaria is mediated mainly by histamine released from mast cells, with serotonin playing a lesser role. Blocking H1 receptors is the established approach to controlling wheals, flare and itch. Cold urticaria is a physically induced form of urticaria with the same mast-cell/histamine pathway, so the mechanistic rationale is direct.

Note that urticaria and angioedema already appear among cyproheptadine's original indications. The predicted "allergic urticaria" therefore largely overlaps with existing use rather than being true repurposing, which is consistent with its very high score. Cold urticaria is more specific, and it is where the published evidence is concentrated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table below covers cold urticaria, the best-supported prediction, ordered by study design.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | Double-blind comparative trial | Arch Dermatol | Cyproheptadine, chlorpheniramine and placebo compared in 8 patients with primary acquired cold urticaria (4 mg three times daily, 7-day periods); cold-stimulation time and symptoms measured |
| [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/) | 1984 | Randomised double-blind trial | J Am Acad Dermatol | Cyproheptadine, doxepin, hydroxyzine and cinnarizine compared in idiopathic cold urticaria using ice cube tests; the authors highlighted doxepin as useful |
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | Double-blind crossover trial | Dermatologica | In 18 patients, cyproheptadine and acrivastine both significantly reduced wheal area versus placebo; acrivastine was significantly more effective |
| [6102102](https://pubmed.ncbi.nlm.nih.gov/6102102/) | 1980 | Clinical study | J Allergy Clin Immunol | Patients were asymptomatic on cyproheptadine and ice cube tests reverted to normal; histamine release was studied before and after therapy |
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Double-blind crossover study | Asian Pac J Allergy Immunol | Cyproheptadine compared with ketotifen in 6 Thai children with primary acquired cold urticaria |
| [1364168](https://pubmed.ncbi.nlm.nih.gov/1364168/) | 1992 | Randomised single-blind crossover | J Investig Allergol Clin Immunol | Loratadine and cetirizine compared with cyproheptadine and ketotifen in 7 patients with acquired cold urticaria |
| [1305812](https://pubmed.ncbi.nlm.nih.gov/1305812/) | 1992 | Diagnostic study | Asian Pac J Allergy Immunol | In children, the ice cube test became only 17% positive at 3 minutes after four weeks of cyproheptadine |
| [475987](https://pubmed.ncbi.nlm.nih.gov/475987/) | 1979 | Single-patient study | Br J Dermatol | Several regimens, including cyproheptadine, each gave favourable results in one patient with severe cold urticaria |
| [2802271](https://pubmed.ncbi.nlm.nih.gov/2802271/) | 1989 | Case report | Ann Allergy | One of two patients did not respond to cyproheptadine but responded well to ketotifen |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review (indirect) | Drugs | Review of acrivastine in allergic rhinitis and urticaria; only indirectly relevant to cyproheptadine |

Most studies are small and decades old. The study type classifications are drawn from titles and abstracts, so the design of some studies could not be fully confirmed.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0304010K0AAABAB | Cyproheptadine HCl Tab 4 mg | Tablet (not specified in the data) | Not specified in the data compiled |

The authorisation number shown is as recorded in the data compiled for this report and is not in the usual UK "PL" format, so it should be verified against the MHRA register.

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** hypertension, peptic ulcer disease, benign prostatic hyperplasia, ocular hypertension, angle-closure glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis), and bladder neck obstruction.

**Drug Interactions:** 100 interactions were identified in total; the first 20 are summarised here.
- **Major:** potassium citrate and potassium chloride.
- **Moderate (mostly additive anticholinergic or CNS-depressant effects):** hyoscyamine, atropine, glycopyrronium, dicyclomine, trospium, mepenzolate, methscopolamine, propantheline, scopolamine, loperamide, morphine, opium, dronabinol, nabilone, eluxadoline, metoclopramide and fenfluramine.

Practical cautions from the literature and the mechanism: sedation, anticholinergic effects and appetite/weight gain, with particular care in children and the elderly. Please refer to the SmPC and BNF for full warnings. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (cold urticaria only)**

**Rationale:**
- Cold urticaria has direct mechanistic plausibility and several small controlled studies, including double-blind comparisons, although none are recent. Evidence is L3 and no trials are registered. Modern second-generation H1 antihistamines are preferred first-line for better tolerability, so cyproheptadine would be a second-line or adjunct option.
- Allergic urticaria largely overlaps with the existing urticaria indication, so it is not a true repurposing opportunity. Nasal cavity disease (too non-specific) and acute laryngopharyngitis (no clinical evidence) remain at **Hold** (L5, prediction only).

**To proceed, the following is needed:**
- Confirmation of the UK licensed indications and dosage form from the SmPC and MHRA register, as the data compiled here lack them
- Mechanism of action data and full label warnings and contraindications (not available in the data compiled)
- Appraisal of the older studies' designs, and any renewed evaluation using modern trial methods with cold-challenge threshold testing as the endpoint
- A monitoring plan for sedation and anticholinergic effects, especially in children and older adults
- Review against current UK urticaria guidance (including NICE and BNF recommendations) to define cyproheptadine's place after second-generation antihistamines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

