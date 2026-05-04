---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid (ICS) prodrug, marketed internationally as Alvesco® for the maintenance treatment of asthma. The TxGNN model predicts it may be effective for **Atopic Eczema**, however there are currently **no clinical trials** and **no publications** directly supporting this specific repurposing direction. Notably, ciclesonide is only available in inhaled and intranasal formulations, presenting a significant route-of-administration mismatch for a dermatological indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (maintenance treatment via inhalation) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, ciclesonide is a glucocorticoid prodrug that is converted by esterases into its active metabolite, des-ciclesonide, which activates the glucocorticoid receptor (GR). GR activation suppresses inflammatory gene transcription, reduces eosinophilic infiltration, inhibits cytokine release, and decreases mucus secretion — effects that underpin its established use in asthma via the inhaled route.

The mechanistic link between ciclesonide and atopic eczema is plausible at the drug class level. Topical corticosteroids are a cornerstone of atopic eczema management, working through GR-mediated suppression of the Th2-driven inflammatory cascade (including IL-4, IL-13, and IL-31). In principle, ciclesonide's anti-inflammatory mechanism could be applicable to atopic eczema if it were delivered topically.

However, the practical barriers are substantial. Ciclesonide is currently available only as an inhaled (metered-dose inhaler) and intranasal formulation. There is no topical preparation, and as a prodrug requiring esterase activation, its bioavailability in the skin's stratum corneum — where esterase activity differs markedly from pulmonary tissue — is unknown. Furthermore, the therapeutic landscape for atopic eczema is already well-served by over 30 existing topical corticosteroids, along with calcineurin inhibitors (tacrolimus, pimecrolimus), dupilumab, and JAK inhibitors. The clinical necessity for developing a new topical ciclesonide formulation is therefore extremely low.

## Clinical Trial Evidence

Currently no related clinical trials registered for ciclesonide in atopic eczema.

## Literature Evidence

Currently no related literature available for ciclesonide in atopic eczema.

## UK Market Information

Ciclesonide currently holds no MHRA marketing authorisations in the United Kingdom. Internationally, it is marketed as Alvesco® (inhaled) and Omnaris®/Zetonna® (intranasal) in other jurisdictions for asthma and allergic rhinitis, respectively. Healthcare professionals seeking further information should consult the BNF and relevant international regulatory databases.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

As ciclesonide has no UK marketing authorisation, prescribers considering off-label or unlicensed use should be aware of the following general class-level considerations for inhaled corticosteroids:
- Oropharyngeal candidiasis and dysphonia (though ciclesonide's prodrug profile may reduce these risks relative to other ICS)
- Potential cross-sensitisation with other corticosteroids — one case report (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)) documented patch test cross-reactivity between budesonide and ciclesonide in a patient with systemic allergic dermatitis
- Standard ICS class effects including adrenal suppression at high doses

## Additional Predicted Indications

The TxGNN model generated five further predictions for ciclesonide. These are summarised below for completeness:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Key Consideration |
|------|---------------------|-------------|----------------|----------------|-------------------|
| 2 | 2-Hydroxyethyl methacrylate sensitisation | 99.76% | L5 | Hold | Extremely rare occupational condition; avoidance is primary strategy |
| 3 | Dermatitis, atopic | 99.73% | L5 | Hold | Duplicate of atopic eczema (ICD-10: L20); same analysis applies |
| 4 | Bronchitis | 99.70% | L4 | Research Question | 1 guideline publication; ICS class has evidence in COPD/chronic bronchitis but not acute bronchitis |
| 5 | Contact dermatitis | 99.25% | L5 | Hold | 1 case report is actually a **safety signal** (cross-sensitisation), not efficacy evidence |
| 6 | Asthma-related traits | 99.13% | L1 (known) | Proceed with Guardrails | This is the **existing approved indication** — model validation rather than true repurposing |

### Notable Observations

**Bronchitis (Rank 4)** is the most clinically interesting secondary prediction. One publication (PMID [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/)) — a Finnish COPD guideline — discusses ICS use in chronic obstructive pulmonary disease, within which chronic bronchitis is a component. Ciclesonide's favourable oropharyngeal side-effect profile (owing to its prodrug design and low oral deposition) could theoretically differentiate it from other ICS agents in this setting, though dedicated clinical trial evidence is lacking.

**Contact Dermatitis (Rank 5)** warrants caution. The sole literature finding (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)) describes ciclesonide as a potential **cause** of allergic contact dermatitis via cross-reactivity, not as a treatment. This represents a safety signal rather than therapeutic evidence.

**Asthma-related Traits (Rank 6)** confirms model validity — ciclesonide is already licensed for asthma internationally, and the TxGNN model correctly identifies this established drug-disease relationship.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.96%), ciclesonide lacks any clinical trial or literature evidence supporting its use in atopic eczema. The fundamental barrier is a formulation mismatch: ciclesonide exists only as inhaled and intranasal preparations, whereas atopic eczema requires topical dermatological delivery. The existing therapeutic armamentarium for atopic eczema is extensive and well-established, offering no unmet clinical need that ciclesonide could uniquely address.

**To proceed, the following would be needed:**
- Development and characterisation of a topical ciclesonide formulation with demonstrated cutaneous esterase activation and local bioavailability data
- Preclinical studies confirming anti-inflammatory efficacy in skin models (e.g., murine atopic dermatitis models)
- A clear differentiation argument over the 30+ existing topical corticosteroids
- Detailed mechanism of action data specific to dermal tissue
- UK MHRA marketing authorisation or established access pathway (e.g., specials manufacturing)
- Safety monitoring plan including assessment of cross-sensitisation risk with other corticosteroids

---

*This report was generated on 5 April 2026 based on data collected up to 5 April 2026. This analysis is for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application. Report suspected adverse reactions via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

