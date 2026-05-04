---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Azathioprine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Azathioprine: From Organ Transplantation to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a well-established thiopurine immunosuppressant, originally used for prevention of organ transplant rejection and management of autoimmune conditions including rheumatoid arthritis and autoimmune hepatitis.
The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)** — encompassing both Crohn's disease and ulcerative colitis — with a prediction confidence of **99.52%**.
This prediction is supported by **50 clinical trials** and **20 publications** including three Cochrane systematic reviews, confirming azathioprine as an established first-line immunomodulator for IBD maintenance therapy.

> **Editorial note:** The TxGNN model's highest-ranked prediction (rank 1) for azathioprine is a rare congenital syndrome (colobomatous microphthalmia-rhizomelic dysplasia) identified as a knowledge graph topological false positive with no supporting evidence (L5, Hold). This report focuses on the highest-ranked clinically meaningful prediction with real-world evidence: **Inflammatory Bowel Disease (rank 5, L1 evidence)**, which represents the most actionable finding for UK healthcare professionals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prevention; autoimmune conditions (UK-specific licensing data not captured in this evidence pack — please consult MHRA register) |
| Predicted New Indication | Inflammatory Bowel Disease (Crohn's disease and ulcerative colitis) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 |
| UK Market Status | UK regulatory data not available in this evidence pack |
| Number of Marketing Authorisations | Not available in this evidence pack |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, azathioprine is a thiopurine prodrug (in the same drug class as 6-mercaptopurine, or 6-MP) whose efficacy in organ transplant rejection prevention and autoimmune conditions has been extensively proven over more than 45 years of clinical use. Mechanistically, azathioprine is converted in vivo to 6-thioguanine nucleotides (6-TGN), its primary active metabolites, which inhibit T and B lymphocyte proliferation — a mechanism directly applicable to the immune dysregulation underlying inflammatory bowel disease. The active metabolites also inhibit the Rac1/TIAM1 signalling pathway in mucosal T cells, suppressing pro-inflammatory cytokines including TNF-α and IL-12 that are central to intestinal mucosal pathology.

Inflammatory bowel disease is characterised by dysregulated immune activation in the gastrointestinal mucosa. Crohn's disease is driven primarily by Th1/Th17-mediated transmural granulomatous inflammation, whilst ulcerative colitis involves Th2/Th9-mediated colonic mucosal immune overactivation. Both conditions share the hallmark of excessive lymphocyte proliferation and overproduction of pro-inflammatory cytokines. Azathioprine's ability to suppress T cell proliferation and downregulate these cytokines directly addresses the core immunopathology of both IBD subtypes.

It is important to note that azathioprine's use in IBD represents a well-established indication rather than a purely novel repurposing: it is already recognised in international guidelines (ECCO, ACG, BSG) as a first-line immunomodulator for steroid-dependent Crohn's disease and ulcerative colitis. The TxGNN model's high prediction confidence reflects this strong mechanistic and clinical alignment. For the UK context, the absence of locally confirmed regulatory data in this evidence pack means the current MHRA marketing authorisation status should be verified before prescribing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Landmark double-blind RCT in treatment-naïve Crohn's disease comparing azathioprine monotherapy, infliximab monotherapy, and combination therapy; provides direct Phase 3 evidence for AZA efficacy with large sample size |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Double-blind double-dummy RCT comparing azathioprine versus mesalazine for prevention of clinical relapse in post-operative Crohn's disease with moderate or severe endoscopic recurrence |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Multicentre RCT comparing azathioprine to mesalazine for prevention of post-operative Crohn's disease recurrence; supports AZA as preferred immunomodulator following intestinal resection |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | Investigator-initiated open RCT evaluating low-dose azathioprine plus allopurinol versus standard-dose AZA monotherapy in ulcerative colitis; explores an optimised dosing strategy to reduce treatment failures and adverse events |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Three-arm RCT comparing infliximab monotherapy, infliximab plus azathioprine, and azathioprine monotherapy in moderate-to-severe active ulcerative colitis; terminated early but provides comparative safety and efficacy data |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Phase 3 | Recruiting | 166 | Ongoing RCT directly comparing azathioprine versus methotrexate in combination with adalimumab in Crohn's disease; will define the optimal immunosuppressant partner for anti-TNF combination therapy |
| [NCT01536535](https://clinicaltrials.gov/study/NCT01536535) | Phase 4 | Completed | 431 | Multicentre open-label study evaluating standardised initial therapy (including AZA) in newly diagnosed paediatric ulcerative colitis; large real-world validation of AZA-containing treatment protocols |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Risk-stratified paediatric Crohn's disease RCT: AZA versus methotrexate in low-risk patients, AZA versus adalimumab in high-risk patients; informs personalised maintenance strategy selection |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | Terminated | 31 | Double-blind dose-ranging study of azathioprine (IMURAN) in active Crohn's disease requiring corticosteroids; sought to identify the optimal weight-based dose (terminated before target enrolment reached) |
| [NCT00554710](https://clinicaltrials.gov/study/NCT00554710) | Phase 4 | Completed | 129 | Prospective Benelux RCT comparing early aggressive therapy (immunomodulators plus biologicals) versus conventional step-up approach (AZA-containing) in newly diagnosed Crohn's disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database Syst Rev | Updated Cochrane review (2025) on azathioprine and 6-MP for maintenance of remission in ulcerative colitis; incorporates most recent trial data; represents the current gold-standard systematic evidence base |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down infliximab plus azathioprine versus azathioprine alone as maintenance therapy in acute severe UC (ASUC) responding to intravenous steroids; directly evaluates AZA-based maintenance strategy in ASUC |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Cochrane review demonstrating AZA and 6-MP reduce the likelihood of failure to maintain remission in UC; confirms role particularly in steroid-dependent disease |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Comprehensive Review | J Crohn's Colitis | State-of-the-art expert review of thiopurines in IBD; covers indications, pharmacology, metabolite-guided dosing (6-TGN/6-MMP monitoring), safety, and practical clinical management |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Cochrane Systematic Review | Cochrane Database Syst Rev | Earlier Cochrane review establishing the AZA/6-MP evidence base for UC maintenance; foundational systematic evidence informing current clinical practice guidelines |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Meta-analysis specifically addressing efficacy of azathioprine and 6-MP in ulcerative colitis; demonstrated statistically significant benefit, resolving the historic debate about thiopurine effectiveness in UC versus Crohn's |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Clinical Review | World J Gastroenterol | Practical guide to optimising 6-MP and azathioprine therapy in IBD; covers 6-TGN therapeutic drug monitoring, 6-MMP hepatotoxicity thresholds, dose adjustments, and clinical management of treatment failure |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Mechanistic Review | Expert Rev Gastroenterol Hepatol | Molecular mechanisms of azathioprine in IBD including Rac1/TIAM1 pathway inhibition and apoptotic pathways in T cells; provides biological rationale underpinning AZA's therapeutic effect in gut inflammation |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Mechanistic/Translational | Cell Reports Medicine | Identifies gut commensal Blautia wexlerae as a contributor to azathioprine therapy failure in IBD via reduced 6-MP bioavailability; clinically relevant for understanding primary non-response in thiopurine-treated patients |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | Comprehensive review of AZA and 6-MP pharmacogenetics and metabolite monitoring in IBD; covers TPMT polymorphisms, 6-TGN therapeutic ranges, and principles of individualised dosing — foundational reference for precision prescribing |

---

## Cytotoxicity

Azathioprine is a thiopurine prodrug requiring cytotoxic handling precautions. Whilst classified primarily as an immunosuppressant in current UK clinical practice, it is a cytotoxic compound and its active metabolite (6-mercaptopurine) is used as antineoplastic therapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Cytotoxic Immunosuppressant (Thiopurine class) — prodrug of 6-mercaptopurine; antimetabolite with mutagenic and teratogenic potential |
| Myelosuppression Risk | High — leucopenia, thrombocytopenia, and macrocytic anaemia are well-recognised dose-dependent toxicities; severity strongly influenced by TPMT and NUDT15 genotype; may be severe and life-threatening in poor metabolisers |
| Emetogenicity Classification | Low to minimal |
| Monitoring Items | FBC with differential: weekly for the first 8 weeks, then at least every 3 months; liver function tests; renal function; TPMT genotyping or enzyme phenotyping before initiation |
| Handling Protection | Must follow cytotoxic drug handling regulations — do not crush or split tablets; avoid skin and mucosal contact; cytotoxic waste disposal procedures apply; female staff of childbearing age should take particular care |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azathioprine has robust Level 1 evidence for inflammatory bowel disease, supported by multiple completed Phase 3 RCTs and three Cochrane systematic reviews confirming its efficacy as a first-line maintenance immunomodulator in both Crohn's disease and ulcerative colitis. This TxGNN prediction confirms a strong and well-established therapeutic signal; however, the absence of verified UK-specific regulatory data in this evidence pack means formal licensing status must be confirmed before clinical implementation.

**To proceed, the following is needed:**
- Verification of current UK marketing authorisation status via the MHRA register and review of the current azathioprine SmPC
- TPMT genotyping or enzyme activity phenotyping prior to initiation, in line with current UK standard practice, to identify patients at risk of severe myelosuppression
- Baseline assessment of contraindications: active infection, severe hepatic or renal impairment, prior hypersensitivity to azathioprine or 6-mercaptopurine, concurrent allopurinol use (significant interaction — 75% dose reduction required if co-prescription is unavoidable)
- Structured haematological and hepatic monitoring plan as per SmPC, including FBC frequency during initiation phase
- Patient counselling on increased infection risk, elevated long-term lymphoma risk (particularly hepatosplenic T-cell lymphoma in young patients on combination biological therapy), and importance of Yellow Card reporting for any suspected adverse reactions
- Review of current BSG/ECCO guidelines on optimal duration of combination therapy with anti-TNF biologicals to minimise lymphoproliferative risk whilst maintaining clinical and endoscopic remission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

