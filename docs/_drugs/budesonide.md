---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Asthma and Inflammatory Conditions to Atopic Eczema

## One-Sentence Summary

Budesonide is a synthetic glucocorticoid corticosteroid with established clinical use in inflammatory respiratory and gastrointestinal conditions, including asthma, COPD, and inflammatory bowel disease.
The TxGNN model predicts it may be effective for **Atopic Eczema**, with **2 clinical trials** and **20 publications** retrieved in the current evidence search.
However, evidence is currently rated at **Level 4** (mechanistic and preclinical data only), and a critical drug-specific safety concern — contact hypersensitivity to budesonide in atopic dermatitis patients — must be resolved before clinical translation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current MHRA dataset |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| UK Market Status | Not recorded in current dataset (data gap) |
| Number of Marketing Authorisations | 0 (MHRA data pending integration) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available within this dataset. Based on well-established pharmacological knowledge, budesonide is a synthetic glucocorticoid that acts via glucocorticoid receptor (GR) activation to inhibit NF-κB signalling. This results in downregulation of pro-inflammatory Th2 cytokines — including IL-4, IL-5, and IL-13 — along with reduced eosinophil infiltration and mast cell degranulation. These effects underpin its established efficacy across a broad range of inflammatory conditions affecting mucosal surfaces, including the airways and gastrointestinal tract.

Atopic eczema (ICD-10: L20) is a chronic, Th2-dominated inflammatory skin condition characterised by barrier dysfunction and immune dysregulation driven by many of the same cytokine pathways that budesonide suppresses. Notably, topical corticosteroids are already first-line therapy for atopic eczema in current clinical guidelines, lending strong class-level biological plausibility. A 2024 preclinical study (PMID 38275852) specifically explored budesonide-loaded polymeric nanoparticles formulated into hydrogels for local delivery in atopic dermatitis, leveraging the characteristic pH shift at inflamed atopic skin lesions to achieve site-targeted drug release — providing direct proof of concept for a novel budesonide formulation in this indication.

However, a clinically significant and drug-specific safety concern requires priority evaluation. Multiple published studies (PMID 35133669, PMID 24603519, PMID 30053491, PMID 33931866) consistently document that patients with atopic dermatitis carry a heightened risk of developing contact hypersensitivity to budesonide itself. This risk is sufficiently well established that budesonide is included in the European Baseline Patch Test Series as a standard marker for corticosteroid group allergy. The target population for this repurposing direction — patients with atopic eczema — is precisely the group most likely to have been exposed to topical corticosteroids and to have developed sensitisation, making this a potentially disqualifying safety barrier rather than a manageable side effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|------|--------|---------|------------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy to prevent asthma in atopic wheezing children aged 18 months–3 years. Atopic eczema is a comorbidity inclusion criterion, not the primary endpoint. Budesonide is not the study intervention. Not directly relevant to this indication. |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A (Observational) | Unknown | 150 | Characterisation of severe paediatric asthma endotypes via immune, metabolomics, and microbiota analyses in children aged 0–12 years. Atopic dermatitis assessed as a comorbidity phenotype. Not a treatment trial; status unconfirmed. |

> **Note:** Neither trial directly evaluates budesonide as a treatment for atopic eczema. No registered clinical trial evidence for this specific drug–disease combination is currently available.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | RCT Subgroup Analysis | Allergologia et immunopathologia | Budesonide response compared in atopic versus non-atopic infants/preschoolers with recurrent wheezing; atopic subgroup (including children with eczema) analysed separately |
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical / Formulation Study | Gels (Basel) | Budesonide-loaded Eudragit L100 nanoparticles in pH-sensitive hydrogels for topical atopic dermatitis therapy; exploits atopic lesion pH change for targeted drug release — direct proof of concept for this repurposing direction |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Prospective Clinical Study | Dermatology (Basel) | Topical glucocorticosteroids in children with atopic dermatitis; systemic effects on IGF axis, bone and collagen turnover quantified, highlighting risks from percutaneous absorption |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional Study | Contact Dermatitis | Contact sensitisation patterns in an Asian dermatology centre; similar or higher positive patch-test rates in atopic dermatitis versus non-AD patients; budesonide identified as a relevant allergen |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Cross-sectional Study | Dermatitis | Contact hypersensitivity to European standard series and corticosteroid series in adolescents and adults with atopic dermatitis; budesonide sensitisation rates documented in the AD population |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Cross-sectional Study | J Am Acad Dermatol | Allergic contact dermatitis to personal care products and topical medications in adults with atopic dermatitis; budesonide among sensitising topical agents identified in AD patients |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Epidemiological Study | Contact Dermatitis | Italian SIDAPA patch-test data (2018–2019); budesonide included in European Baseline Series as the most suitable marker for corticosteroid hypersensitivity; declining trend in allergy rates observed over two decades |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid allergy in asthmatic patients; delayed contact allergy and occasional immediate hypersensitivity reactions to inhaled budesonide described; relevant class-level safety context |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Case Report | Cureus | Steroid-induced angioedema and urticaria in an 81-year-old patient with a background of atopic dermatitis; Type I hypersensitivity reaction to corticosteroid documented |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids and HPA axis suppression in patients with co-existing allergic rhinitis and atopic dermatitis; cumulative systemic corticosteroid exposure quantification relevant to multi-route use |

---

## UK Market Information

MHRA marketing authorisation data for budesonide is not available in the current dataset (0 records returned). This is a known data gap reflecting incomplete UK regulatory data integration into this system.

> **Note for reviewers:** Budesonide is a well-established medicine in UK clinical practice with multiple MHRA-authorised products across several formulation types, including inhaled preparations for asthma and COPD (e.g., Pulmicort®, Symbicort®), intranasal spray for allergic rhinitis (e.g., Rhinocort®), and oral/rectal preparations for inflammatory bowel disease (e.g., Entocort®, Budenofalk®). Healthcare professionals should consult the BNF and relevant Summary of Product Characteristics (SmPC) documents directly via the MHRA website or the electronic Medicines Compendium (emc.medicines.org.uk) for current authorised indications and prescribing information.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme (yellowcard.mhra.gov.uk).

> **Priority safety alert for this repurposing direction:** A consistent body of peer-reviewed evidence documents contact hypersensitivity to budesonide itself in atopic dermatitis patients — the very target population for this prediction. Budesonide is included in the European Baseline Patch Test Series specifically as a standard marker for corticosteroid group allergy. Any clinical investigation of topical budesonide in atopic eczema must incorporate systematic patch-test screening to exclude pre-sensitised patients and should prospectively monitor for new sensitisation. This safety concern is specific to this drug–disease combination and may constitute a contraindication in a clinically significant subset of the target population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for budesonide in atopic eczema is currently limited to preclinical mechanistic data (Level 4), with no registered clinical trials directly evaluating this indication. More critically, a consistent safety signal — drug-specific contact hypersensitivity in the exact target population — represents a potential disqualifying barrier that must be formally characterised before any clinical development pathway can be justified.

**To proceed, the following is needed:**
- Systematic safety review of budesonide contact hypersensitivity incidence in atopic dermatitis patients, including cross-reactivity data with other topical corticosteroids, sensitisation rates by route of exposure, and risk stratification by disease severity
- Full MOA data retrieval from DrugBank (DB01222) to enable rigorous mechanistic pathway analysis
- MHRA licensing data integration to establish the current UK authorisation status and inform assessment of off-label use implications
- Proof-of-concept clinical study of a novel budesonide delivery system (e.g., nanoparticle hydrogel per PMID 38275852), incorporating mandatory pre-screening patch-test protocol to exclude sensitised patients and prospective sensitisation monitoring
- Assessment of clinical differentiation from currently approved topical corticosteroids (e.g., hydrocortisone, mometasone furoate) to establish whether investment in budesonide-specific development is warranted

> **Broader context:** Across all 10 TxGNN-predicted indications for budesonide, **bronchitis** (rank 2; TxGNN score 99.81%) carries the strongest evidence base with a Level 2 rating, supported by multiple completed Phase 2–4 trials and a meta-analysis (PMID 37954384). The bronchitis indication carries a recommendation to **Proceed with Guardrails** and may represent a more immediately actionable repurposing direction for this drug within the UK healthcare setting.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. This report was generated using the TxGNN UK Drug Repurposing System (data cut-off: 5 April 2026).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

