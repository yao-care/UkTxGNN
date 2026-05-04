---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Albendazole
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

# Albendazole: From Intestinal Helminthiasis to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole antiparasitic agent, long established globally as the WHO first-line treatment for intestinal helminthiasis and other helminthic infections.
The TxGNN model predicts it may be effective for **alveolar echinococcosis** — a progressive, potentially fatal hepatic parasitosis caused by *Echinococcus multilocularis* — with **5 clinical trials** and **20 publications** currently supporting this direction.
Notably, this prediction aligns precisely with established international guidelines: Albendazole already occupies the standard-of-care role worldwide, and the principal remaining step for UK practice is obtaining formal MHRA marketing authorisation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Intestinal helminthiasis (broad-spectrum antiparasitic; no current UK licence) |
| Predicted New Indication | Alveolar echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| UK Market Status | Not currently marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Albendazole belongs to the benzimidazole class of anthelmintics. It acts by binding irreversibly to β-tubulin subunits within parasitic larvae and adult worms, blocking microtubule polymerisation and disrupting cytoskeletal integrity. This simultaneously inhibits glucose uptake across the tegument, rapidly depleting intracellular glycogen stores and causing parasitic immobilisation and, in susceptible species, death. Critically, the β-tubulin target in *Echinococcus multilocularis* metacestodes is pharmacologically homologous to that found in intestinal nematodes, providing a well-grounded mechanistic rationale for efficacy in alveolar echinococcosis (AE).

Alveolar echinococcosis is caused by the larval metacestode stage of *E. multilocularis*, which infiltrates hepatic tissue in a pseudotumoral pattern and, without treatment, carries a near-100% case-fatality rate within 10–15 years of infection. Albendazole exerts a parasitostatic rather than parasiticidal effect in this setting — it halts or slows larval growth rather than eradicating established lesions — necessitating long-term, often lifelong, treatment in inoperable or partially resected cases. Despite this limitation, the drug is firmly embedded in clinical guidelines. The 2010 WHO/ERCE International Expert Consensus (PMID 19931502) designated Albendazole as the standard pharmacological treatment for AE, a position consistently reaffirmed through 2025 in multiple international systematic reviews and clinical management guidelines.

In practical terms, this assessment is less a conventional drug repurposing exercise and more a formal UK evidence review for a globally recognised indication that currently lacks MHRA marketing authorisation. The TxGNN prediction score of 99.97% reflects the strong mechanistic and empirical overlap between Albendazole's established antiparasitic activity and AE pathobiology. The completed Phase 2 RCT (NCT07182305, n=194) provides the highest-grade direct clinical evidence currently available.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Prospective RCT of Albendazole in early-stage AE in Kyrgyzstan (completed July 2023); highest-grade direct trial evidence for this indication; confirms Albendazole as effective parasitostatic treatment for small hepatic *E. multilocularis* lesions identified by ultrasound surveillance |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA | Completed | 50 | EchinoVISTA prospective observational study (completed August 2021); characterised biological and imaging markers of parasite viability in hepatic AE patients receiving Albendazole; establishes a monitoring framework to support timely treatment-withdrawal decisions |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | NA | Unknown | 24 | RCT evaluating adjuvant Albendazole versus placebo after pulmonary hydatid cyst resection; primary endpoint is 6-month recurrence rate; applicable to the broader *Echinococcus* surgical adjuvant setting, though study status is unconfirmed |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | NA | Recruiting | 43 | Multiplex quantitative PCR diagnostic accuracy study for AE and CE; Albendazole noted as standard treatment context; no direct efficacy endpoint — provides diagnostic infrastructure relevant to future treatment trials |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Case report of misdiagnosed intramuscular hydatid cyst in the deltoid; Albendazole used post-operatively; incidental context only, no statistical contribution to efficacy evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert Consensus (WHO/ERCE) | *Acta Tropica* | International consensus on diagnosis and treatment of AE and CE; designates Albendazole as first-line medical therapy; covers dosing regimen, cyclical vs continuous use, and monitoring requirements |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | *Parasite (Paris)* | Comprehensive update on benzimidazole chemotherapy for AE; addresses parasitostatic limitations, benzimidazole-induced hepatotoxicity risk, and identification of candidate next-generation antiparasitic drugs |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Comprehensive Review | *Clin Microbiol Rev* | 21st-century advances in echinococcosis covering molecular epidemiology, improved diagnostics, and treatment outcomes with Albendazole; western China identified as highest-endemicity region |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Comparative Treatment Review | *Parasite (Paris)* | Evaluates Albendazole and mebendazole in AE and CE; reviews whole-organism drug screening for novel candidates; confirms no approved replacements currently identified |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Research Progress Review | *Chin J Schistosomiasis Control* | Chinese review specific to Albendazole use in AE; covers clinical efficacy data, pharmacokinetic limitations (low aqueous solubility, variable oral bioavailability), and novel formulation strategies under investigation |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Clinical Management Review | *World J Gastroenterol* | Current management of hepatic echinococcosis; confirms surgery plus Albendazole as the cornerstone of treatment; addresses indefinite medical management for inoperable cases |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Clinical Review | *Tidsskr Nor Laegeforen* | Norwegian clinical review of AE as a rare imported disease; management = hepatic resection combined with prolonged Albendazole; of direct relevance to UK practice where AE is similarly seen in travellers and immigrants |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Clinical Review | *Semin Liver Dis* | Hepatic AE: pseudotumoral presentation, European resurgence, and management guidance; Albendazole lifelong maintenance treatment is standard practice for inoperable or incompletely resected disease |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Novel Treatment Options Review | *Acta Tropica* | Confirms no approved non-surgical alternative to Albendazole or mebendazole exists; reviews experimental options; underscores Albendazole's uncontested position as the only recommended antiparasitic for AE |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Pharmacological Study | *Antimicrob Agents Chemother* | In vivo study of Albendazole formulations in a hepatic AE rat model; crystal dispersion system (ABZ-CSD) showed substantially improved bioavailability and therapeutic outcomes compared to standard formulation; relevant to future UK formulation selection |

---

## UK Market Information

Albendazole currently holds **no MHRA marketing authorisation** in the United Kingdom. There are no licensed products available through the standard NHS dispensing pathway (MHRA total licences: 0).

In current UK clinical practice, patients requiring Albendazole for AE are managed through one of the following routes:

- **Specials** — manufactured or imported unlicensed medicine under MHRA exemption (Section 10, Human Medicines Regulations 2012)
- **Named Patient Basis** — via a licensed manufacturer or importer
- **NHS England Highly Specialised Services** — for rare imported parasitic diseases, typically managed through specialist tropical medicine or hepatology centres (e.g., Hospital for Tropical Diseases, London; Liverpool School of Tropical Medicine)

Clinicians should consult the **BNF section on anthelmintics** and refer to UKTIS/TOXBASE for toxicity information when prescribing on an unlicensed basis. Informed consent documentation and adherence to MHRA guidance on unlicensed medicines are required.

---

## Safety Considerations

Formal UK SmPC safety data is not available for Albendazole (no current MHRA marketing authorisation). Please refer to the WHO/ERCE 2010 consensus guidelines, the BNF, and published pharmacological literature for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole is internationally recognised as the sole pharmacological standard of care for alveolar echinococcosis, endorsed by the 2010 WHO/ERCE Expert Consensus and supported by a completed Phase 2 RCT (NCT07182305, n=194, completed July 2023). The primary barrier to formal UK use is the absence of MHRA marketing authorisation, not a lack of clinical evidence.

**To proceed, the following is needed:**
- Determine the most appropriate UK licensing pathway: MHRA marketing authorisation application (e.g., well-established use bibliographic application under Directive 2001/83/EC Article 10a) or continuation under a Specials route for individual patients in the interim
- Retrieve full safety data (SmPC, drug interaction profile, contraindication list) from DrugBank and WHO sources to complete the pharmacovigilance review — this remains a formal data gap in the current pack
- Establish a UK-specific clinical monitoring protocol: full blood count (FBC with differential), liver function tests (LFTs), and renal function at baseline and at regular intervals throughout treatment, particularly for long-term AE management
- Define the target UK patient population: predominantly travellers, immigrants, or residents from endemic regions (Central Asia, Central Europe, western China, Switzerland); design referral pathway through specialist hepatology or tropical medicine centres
- Develop contraception and pregnancy guidance for women of childbearing potential, given the known teratogenicity of benzimidazole compounds
- Consult NICE regarding whether a highly specialised technologies appraisal or NHS England commissioning guidance document is required, given AE's rare disease classification in the UK
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

