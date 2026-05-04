---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adefovir Dipivoxil: From HIV Antiretroviral Development to Hepatitis B Virus Infection

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.

---

## One-Sentence Summary

Adefovir dipivoxil (Hepsera®) is an acyclic nucleotide analogue originally investigated at high doses for HIV infection in the 1990s; following dose-limiting nephrotoxicity at higher doses, it was repositioned and approved internationally at 10 mg daily for chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **Hepatitis B Virus Infection** (TxGNN rank 6 of 10; rank 1 prediction of chronic HCV lacks mechanistic support and carries zero trial evidence), with **over 50 registered clinical trials** and **20 publications** directly supporting this indication — representing the strongest evidence in this Evidence Pack.
This report focuses on the HBV indication (evidence level L1, decision: Proceed with Guardrails) as the clinically actionable finding, while noting that the highest-ranked TxGNN predictions (chronic HCV, neurodevelopmental disorder) are assessed as likely false positives due to fundamental mechanistic mismatch or absence of any supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no UK marketing authorisation; drug developed for HIV at high doses, discontinued due to nephrotoxicity) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.87% (rank 6 of 10; highest-ranked prediction with substantive clinical evidence) |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| UK Market Status | Not marketed |
| Number of UK Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Adefovir dipivoxil is an oral prodrug of adefovir, an acyclic nucleoside phosphonate (ANP). Following oral administration, it is converted intracellularly to adefovir diphosphate, the pharmacologically active moiety. Adefovir diphosphate acts as a competitive inhibitor of HBV DNA polymerase — which possesses reverse transcriptase activity — by competing with the natural substrate deoxyadenosine triphosphate (dATP), and by incorporating into the growing viral DNA strand to cause obligate chain termination. Critically, this mechanism retains potency against lamivudine-resistant YMDD mutant strains of HBV, giving adefovir a distinct clinical niche in patients with lamivudine-resistant chronic hepatitis B.

The drug was initially developed at substantially higher doses (60–120 mg/day) as an antiretroviral agent for HIV, where adefovir diphosphate similarly inhibits HIV reverse transcriptase. That programme was halted because of dose-dependent nephrotoxicity (Fanconi syndrome risk). At the approved HBV dose of 10 mg/day, renal safety is substantially improved — though routine monitoring of renal function remains essential. The same nucleotide analogue class (acyclic nucleoside phosphonates) later yielded tenofovir disoproxil fumarate (TDF) and tenofovir alafenamide (TAF), which now supersede adefovir in many settings due to superior potency and safety profiles; head-to-head Phase 3 RCTs (NCT00116805, NCT01300234) demonstrated TDF's superiority over adefovir for HBV.

The prediction by TxGNN is therefore not a novel repurposing hypothesis in the conventional sense: adefovir dipivoxil has been approved by the US FDA (as Hepsera®, 2002) and by multiple other regulatory agencies for chronic HBV infection. Its absence from the UK market, despite established global evidence, is the key gap this report addresses. The mechanistic rationale is unambiguous, the clinical evidence base is mature (L1), and the drug's role is well-characterised — particularly for patients with lamivudine-resistant HBV where first-line agents have failed, or in resource-limited settings where newer agents are unavailable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00095121](https://clinicaltrials.gov/study/NCT00095121) | Phase 3 | Completed | 173 | Double-blind, placebo-controlled RCT evaluating adefovir dipivoxil safety and efficacy in children and adolescents (aged 2–17) with chronic HBV over 48 weeks (blinded) + 192 weeks open-label. Highest-grade direct evidence in a paediatric population. |
| [NCT00116805](https://clinicaltrials.gov/study/NCT00116805) | Phase 3 | Completed | 266 | Double-blind RCT comparing tenofovir DF vs adefovir dipivoxil in HBeAg-positive chronic HBV over 48 weeks, followed by open-label TDF for up to 480 weeks. Demonstrated superiority of TDF over adefovir. |
| [NCT01300234](https://clinicaltrials.gov/study/NCT01300234) | Phase 3 | Completed | 512 | Double-blind, double-dummy RCT: TDF 300 mg vs adefovir 10 mg in Chinese subjects with CHB (HBeAg+ and HBeAg−). Long-term data up to 240 weeks. Confirmed TDF superiority; provided pivotal data for Chinese regulatory approval. |
| [NCT00531167](https://clinicaltrials.gov/study/NCT00531167) | Phase 4 | Completed | 219 | Prospective randomised study comparing adefovir add-on therapy versus switching to entecavir in patients with lamivudine-resistant chronic HBV. Key resistance management strategy data. |
| [NCT01480284](https://clinicaltrials.gov/study/NCT01480284) | Phase 3 | Completed | 166 | Multi-centre double-blind active-controlled RCT: GSK548470 (besifovir) vs entecavir in Japanese treatment-naïve compensated CHB patients. Adefovir used as contextual reference; Phase 3 design for Japanese population. |
| [NCT01329419](https://clinicaltrials.gov/study/NCT01329419) | Phase 4 (PMS) | Completed | 4,393 | Large-scale post-marketing surveillance in Korean CHB patients receiving adefovir dipivoxil per licensed prescribing information. Provides the largest real-world safety dataset for adefovir at 10 mg. |
| [NCT01205165](https://clinicaltrials.gov/study/NCT01205165) | Phase 4 | Completed | 104 | Open-label multicentre Phase 4 study in Korean HBV patients with compensated liver disease. Primary endpoint: mean log₁₀ reduction in HBV DNA at Week 12; secondary endpoints at 52 weeks including histological and biochemical improvement. |
| [NCT02075294](https://clinicaltrials.gov/study/NCT02075294) | N/A | Completed | 242 | Efficacy and safety comparison of adefovir versus entecavir specifically in elderly patients with chronic HBV. Relevant special-population data; addresses an increasingly important demographic. |
| [NCT00023309](https://clinicaltrials.gov/study/NCT00023309) | Phase 2 | Completed | 41 | NIH-sponsored study evaluating lamivudine plus adefovir combination versus adefovir monotherapy in chronic HBV. Provided early combination therapy rationale and resistance prevention data. |
| [NCT00033163](https://clinicaltrials.gov/study/NCT00033163) | Phase 2 | Completed | 90 | Randomised controlled trial comparing adefovir dipivoxil vs tenofovir DF for lamivudine-resistant HBV in HIV co-infected patients on HAART. Key data for HBV/HIV co-infection management. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22242973](https://pubmed.ncbi.nlm.nih.gov/22242973/) | 2012 | Review | Expert Opinion on Pharmacotherapy | Comprehensive review of adefovir dipivoxil history and current uses for HBV. ADV 10 mg/day associated with improved liver histology, decreased HBV DNA, ALT normalisation, and HBeAg seroconversion. Details resistance profile (rtN236T, rtA181T/V mutations). |
| [14498759](https://pubmed.ncbi.nlm.nih.gov/14498759/) | 2003 | Systematic Review | Drugs | Systematic review of adefovir dipivoxil in chronic HBV. Demonstrated histological improvement in ~53–68% of patients vs ~25% placebo; efficacy maintained in both HBeAg-positive and HBeAg-negative disease. First comprehensive synthesis of Phase 3 trial data. |
| [15482214](https://pubmed.ncbi.nlm.nih.gov/15482214/) | 2004 | Review | Expert Review of Anti-infective Therapy | Evidence review of adefovir dipivoxil for chronic HBV including decompensated liver disease and post-transplant patients. Confirmed sustained efficacy over 3 years in HBeAg-negative CHB. |
| [15500383](https://pubmed.ncbi.nlm.nih.gov/15500383/) | 2004 | Review | Expert Opinion on Pharmacotherapy | Evaluation of adefovir in HBeAg-positive and HBeAg-negative patients including lamivudine-resistant strains; reviewed pre- and post-liver transplant data. Highlighted renal monitoring requirement. |
| [14749147](https://pubmed.ncbi.nlm.nih.gov/14749147/) | 2003 | Review | Clinical Therapeutics | Overview of adefovir dipivoxil pharmacology, clinical efficacy, and safety in the context of then-available HBV treatments (interferon alfa-2b, lamivudine). Summarises Phase 3 regulatory approval data. |
| [12698207](https://pubmed.ncbi.nlm.nih.gov/12698207/) | 2003 | Drug Review | Drugs of Today | Early review following FDA approval; documents adefovir's activity against wild-type and lamivudine-resistant HBV in vitro and in vivo. Recommended dose 10 mg daily; highlights renal and tolerability profile. |
| [27977591](https://pubmed.ncbi.nlm.nih.gov/27977591/) | 2016 | Meta-analysis (Cohort) | Medicine | Meta-analysis investigating relationship between long-term adefovir therapy and nephrotoxicity in CHB patients. Identifies risk factors for renal dysfunction (duration of therapy, baseline eGFR). Important safety reference for monitoring protocols. |
| [14697813](https://pubmed.ncbi.nlm.nih.gov/14697813/) | 2003 | Review | Lancet | Major Lancet review of chronic HBV infection epidemiology, pathogenesis, and treatment advances including adefovir. Contextualises the global burden (>400 million chronically infected) and treatment landscape. |
| [14990784](https://pubmed.ncbi.nlm.nih.gov/14990784/) | 2004 | Review | Annals of Pharmacotherapy | Review of adefovir dipivoxil pharmacology for CHB, covering mechanism, clinical trial outcomes in three patient populations (HBeAg+, HBeAg−, lamivudine-resistant YMDD mutants). |
| [15192800](https://pubmed.ncbi.nlm.nih.gov/15192800/) | 2004 | Clinical Review | Seminars in Liver Disease | Treatment outcomes with adefovir across three CHB populations. Documents HBV DNA suppression mechanism via DNA polymerase inhibition and chain termination; discusses clinical endpoints and durability of response. |

---

## UK Market Information

Adefovir dipivoxil currently holds **no UK marketing authorisations** and has not been submitted to the MHRA for approval. It is not listed in the British National Formulary (BNF). The drug is approved and marketed in other jurisdictions (notably the United States as Hepsera® [Gilead Sciences, 2002], Japan, South Korea, and China), but no Product Licence (PL) has been granted in Great Britain or Northern Ireland.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|-------------------|
| — | — | — | No UK authorisations exist. See MHRA Public Assessment Reports for related nucleotide analogues (e.g., tenofovir disoproxil fumarate [PL 21727/0005], tenofovir alafenamide). |

For UK clinical use, prescribers would need to consider the Medicines and Healthcare products Regulatory Agency (MHRA) Unlicensed Medicines guidance, or a formal Marketing Authorisation Application (MAA). Given that tenofovir DF and tenofovir alafenamide (both NICE-recommended) are available with superior efficacy and safety profiles, any UK market entry strategy for adefovir would require a clearly differentiated clinical niche (e.g., specific resistance patterns, cost considerations in resource-limited settings, or paediatric formulations).

---

## Safety Considerations

Detailed MHRA SmPC and formal contraindication data are not available in this Evidence Pack. The following is based on published clinical evidence and internationally approved product information:

**Key Warnings (from clinical trial evidence and international SmPCs):**
- **Nephrotoxicity:** Dose-dependent renal tubular toxicity is the principal safety concern. At 10 mg/day, clinically significant nephrotoxicity occurs in a minority of patients, but the risk increases with prolonged use, pre-existing renal impairment, and concomitant nephrotoxic drugs. Long-term meta-analyses (PMID 27977591) confirm this risk. Regular monitoring of serum creatinine, eGFR, and serum phosphate is mandatory.
- **Fanconi syndrome:** Proximal renal tubular dysfunction (Fanconi syndrome), including hypophosphataemia, hypouricaemia, glycosuria, and amino aciduria, has been reported — particularly with long-term therapy or in HIV co-infected patients.
- **HBV exacerbation on discontinuation:** Acute exacerbation of hepatitis (ALT flares) can occur upon abrupt cessation of therapy. Liver function must be monitored closely for several months after stopping treatment.
- **Lactic acidosis / severe hepatomegaly with steatosis:** A class effect of nucleoside/nucleotide analogues; rare but potentially fatal.
- **HIV resistance:** If used in patients with unrecognised or untreated HIV co-infection, the 10 mg dose may select for HIV resistance mutations. HIV status must be confirmed before initiating therapy.
- **Pregnancy:** Embryotoxicity and teratogenicity have been observed in animal studies. Adefovir is not recommended during pregnancy.

Please refer to the internationally approved Summary of Product Characteristics (SmPC) for Hepsera® and the BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Adefovir dipivoxil has an established, internationally approved indication for chronic hepatitis B virus infection, supported by multiple Phase 3 RCTs (evidence level L1), extensive real-world post-marketing data (n > 4,000 in surveillance studies alone), and a well-characterised mechanistic basis. However, it does not hold UK marketing authorisation, and superior agents (tenofovir DF, tenofovir alafenamide, entecavir) are already available on the UK market with NICE guidance — positioning adefovir as a second-line or niche option rather than a first-line repurposing priority.

**To proceed, the following is needed:**

- **MHRA regulatory pathway assessment:** Determine whether a full MAA, bibliographic application (Article 10a), or hybrid application route is most appropriate, given the established global clinical data package.
- **NICE health technology appraisal:** A formal cost-effectiveness analysis comparing adefovir with currently recommended first-line agents (tenofovir alafenamide, entecavir) would be required for NHS formulary access.
- **Defined clinical niche:** Articulate the specific patient population for whom adefovir offers advantages (e.g., lamivudine-resistant HBV where newer agents are unavailable, specific resistance mutation profiles, paediatric liquid formulation needs, or health economic considerations in certain commissioning contexts).
- **Renal safety monitoring protocol:** A clear renal monitoring plan (baseline eGFR, serum phosphate, urinalysis; repeat at 3-month intervals) should be pre-specified for any UK clinical use, given the nephrotoxicity risk with long-term therapy.
- **SmPC and MHRA warnings/contraindications:** Formal MHRA assessment of the product-specific contraindications and warnings is required before UK prescribing (data gap DG001 in this Evidence Pack).
- **MOA documentation:** Detailed formal mechanism of action data (DrugBank DB00718 record review) should be completed to support the regulatory submission (data gap DG002).
- **HIV co-infection screening protocol:** A protocol for mandatory HIV status screening prior to initiation to prevent inadvertent subtherapeutic antiretroviral monotherapy.

---

*Report generated: 4 April 2026 | Evidence Pack version: v4 | Data cutoff: 4 April 2026 | DrugBank ID: DB00718*

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

