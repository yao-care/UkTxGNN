---
layout: default
title: Tacrolimus
parent: High Evidence (L1-L2)
nav_order: 590
evidence_level: L1
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
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

# Tacrolimus: From Atopic Eczema to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor, originally used as a topical treatment for atopic eczema (atopic dermatitis).
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
with **2 clinical trials** (one completed Phase 3) and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema / atopic dermatitis (from the knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* L1 in the scoring data rests on one completed Phase 3 trial plus one completed Phase 4 trial for seborrheic dermatitis. Strictly, the L1 rule asks for two or more completed Phase 3 RCTs, so this level should be regarded as provisional until trial results are reviewed.

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From the literature, tacrolimus is a calcineurin inhibitor. It blocks NFAT-dependent T-cell activation and the release of pro-inflammatory cytokines such as IL-2 and IL-4. This is the basis of its efficacy in atopic eczema.

Seborrheic dermatitis is a chronic, relapsing inflammatory condition of sebaceous-rich skin, mainly the face and scalp. It involves an inflammatory response to *Malassezia* yeast colonisation. The anti-inflammatory mechanism that works in atopic eczema is therefore plausibly applicable.

A further practical advantage is its steroid-sparing profile. Long-term topical corticosteroid use on the face can cause skin atrophy, so a non-steroid option for maintenance treatment is attractive.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Tacrolimus ointment (Protopic) as maintenance treatment of severe adult facial seborrheic dermatitis, aiming to reduce relapses, prolong remission and reduce topical steroid use. Results not provided in the data compiled. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once- or twice-weekly 0.1% tacrolimus ointment to keep adult facial seborrheic dermatitis in remission and reduce exacerbations. Results not provided in the data compiled. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | RCT / clinical study | Annals of Dermatology | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment; low-dose intermittent use is modelled on the AD maintenance approach. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | American Journal of Clinical Dermatology | Topical treatment of facial seborrheic dermatitis, covering antifungals, keratolytics and corticosteroids. |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | American Journal of Clinical Dermatology | Topical calcineurin inhibitors are a safe alternative to corticosteroids for seborrheic dermatitis, which have limited long-term use because of adverse effects. |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic review / network meta-analysis | Clinical and Experimental Allergy | Cochrane review of topical anti-inflammatory treatments for eczema (indirect evidence). |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | Journal of Drugs in Dermatology | Current status and therapeutic horizons for facial seborrheic dermatitis. |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical trial | Annals of Parasitology | Sertaconazole 2% cream compared with tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis. |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | Journal of Cutaneous Medicine and Surgery | Off-label use of topical calcineurin inhibitors across dermatological disorders. |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Review | Expert Opinion on Investigational Drugs | New roles for topical tacrolimus beyond atopic dermatitis. |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Seminars in Cutaneous Medicine and Surgery | Topical immunomodulators explored for psoriasis, seborrheic dermatitis, lichen planus and other diseases. |
| [20347654](https://pubmed.ncbi.nlm.nih.gov/20347654/) | 2010 | Review | Clinics in Dermatology | Tinea incognito can be masked by topical tacrolimus and mimic seborrheic or atopic dermatitis, so misdiagnosis is a safety point. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1305030C0AAAAAA | Tacrolimus ointment 0.1% | Ointment (not stated in the licence data) | Not stated in the licence data |

Only one authorisation record is present in the data compiled for this report, and its indication text, dosage form and manufacturer are blank. The identifier is also not in the usual MHRA "PL" format, so it should be verified against the MHRA register. Reference to the BNF and relevant NICE guidance on topical calcineurin inhibitors for atopic eczema is advised.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not product label text, and mostly reflecting systemic tacrolimus): cancer and lymphoma (including primary CNS lymphoma), infections (herpes simplex, herpes zoster, infectious mononucleosis, chronic Epstein-Barr virus infection, progressive multifocal leukoencephalopathy), hypertension, long QT syndrome and torsades de pointes, liver failure, kidney disease, diabetes and hyperglycaemia, epilepsy, and posterior leukoencephalopathy syndrome. Their relevance to low-exposure topical use needs to be checked against the SmPC.
- **Drug interactions:** 100 interactions were recorded. Those listed as major are amphotericin B (including the lipid complex), loperamide, mesalazine, omeprazole and balsalazide. Moderate examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, pioglitazone, famotidine, rabeprazole and metronidazole. These records probably reflect systemic tacrolimus, and topical systemic exposure is minimal.
- **Cancer risk:** a 2023 systematic review and meta-analysis (PMID 36370744) examined cancer risk with topical calcineurin inhibitors in atopic dermatitis. It is the key reference for long-term safety counselling.
- **Diagnostic caution:** topical calcineurin inhibitors can mask tinea infection (tinea incognito).

Please refer to the SmPC and BNF for authoritative warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial and a completed Phase 4 trial directly address tacrolimus ointment in facial seborrheic dermatitis, backed by a published maintenance-therapy study and several reviews. The product is already marketed in the UK for atopic eczema. However, trial results are not summarised in the data, and seborrheic dermatitis would be an off-label use.

**To proceed, the following is needed:**
- Review of the actual results and endpoints of NCT02004860 and NCT01591070
- Confirmation of the UK licence details (indication, dosage form, authorisation number format) against the MHRA register
- Mechanism of action data from DrugBank
- Review of the SmPC warnings and contraindications, since label-based safety data were not available
- A guardrail plan covering facial use only, exclusion of fungal infection, and long-term cancer and infection monitoring

---

*Other predicted indications (not recommended for progression):*
- **Parapsoriasis** (score 99.24%, evidence level L4, Hold): only two case reports on pityriasis lichenoides and no clinical trials.
- **Dermatitis (broad)** (score 99.17%): the trials mostly concern atopic dermatitis, which is the existing indication, so they reflect established use rather than new repurposing. Value is limited to non-atopic subtypes, which would need subtype-specific evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

