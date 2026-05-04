---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Brinzolamide
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

# Brinzolamide: From Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a topical carbonic anhydrase inhibitor (CAI) with a well-established role in reducing intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension, although no MHRA marketing authorisation is currently recorded for the United Kingdom in this evidence pack.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** — a genetically determined subtype caused by mutations in genes such as *CYP1B1* and *MYOC* — with a prediction score of **99.48%**.
However, **no clinical trials or published literature** currently support this specific indication, yielding an evidence level of **L5** and a recommendation to **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No MHRA marketing authorisation currently recorded for the UK |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available from this evidence pack (recorded as a data gap). Based on the peer-reviewed literature retrieved, Brinzolamide is a highly selective inhibitor of carbonic anhydrase II (CA-II) expressed in the ciliary body epithelium. By blocking CA-II, it reduces the bicarbonate-dependent secretion of aqueous humour, thereby lowering IOP by approximately 15–18% from baseline when administered as a 1% ophthalmic suspension. This mechanism is corroborated by an extensive body of Phase 3 and Phase 4 evidence in primary open-angle glaucoma and ocular hypertension spanning over two decades (1998–2025).

Primary hereditary glaucoma encompasses congenital glaucoma (*CYP1B1* mutations causing trabecular meshwork maldevelopment) and juvenile-onset open-angle glaucoma (*MYOC*/myocilin mutations). In both subtypes, impaired aqueous outflow leads to chronically elevated IOP and progressive optic nerve damage. Because elevated IOP is the final common pathological pathway, the pharmacological rationale for CA-II inhibition is mechanistically coherent: IOP reduction confers clinical benefit regardless of the upstream genetic aetiology. This is analogous to the well-accepted role of brinzolamide as adjunctive therapy in adult open-angle glaucoma.

However, two critical limitations temper enthusiasm for this prediction. First, surgical intervention — goniotomy or trabeculotomy — is the established first-line treatment for primary congenital glaucoma; pharmacotherapy serves only as a temporising bridge before surgery or as post-operative adjunctive management. Second, the safety, tolerability, and pharmacokinetics of topical carbonic anhydrase inhibitors have not been formally characterised in neonates, infants, or young children through dedicated clinical trials. Brinzolamide is a sulfonamide derivative, and paediatric sulfonamide safety data (including concerns about systemic absorption, metabolic acidosis risk, and corneal endothelial effects in immature eyes) are currently insufficient. The very high TxGNN score (0.9948) most likely reflects the dense graph-level connectivity between glaucoma disease nodes in the underlying knowledge graph rather than a signal of specific, translatable clinical evidence for this genetic subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma.

> **Contextual note for clinicians:** Whilst no trials exist specifically for primary hereditary glaucoma, an extensive body of Phase 3 and Phase 4 evidence supports Brinzolamide's IOP-lowering efficacy in adult open-angle glaucoma (TxGNN ranks 2–4; evidence level L1; over 48 registered trials identified). Key high-grade trials include [NCT01357616](https://clinicaltrials.gov/study/NCT01357616) (Phase 3 RCT, n=328, Brinzolamide/Timolol fixed combination vs monotherapy in Chinese POAG patients) and two pivotal Phase 3 studies comparing Brinzolamide/Brimonidine fixed combination ([NCT01297920](https://clinicaltrials.gov/study/NCT01297920), n=1,062; [NCT01309204](https://clinicaltrials.gov/study/NCT01309204), n=1,184). These trials collectively demonstrate clinically meaningful and sustained IOP reduction, but were conducted exclusively in adult populations with open-angle disease.

---

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

> **Contextual note:** The evidence pack identified 20 publications for the related indication "glaucoma 1, open angle" (TxGNN rank 2), including systematic reviews, Phase 3 RCT data, and drug reviews spanning 1998–2025. A 2025 clinical practice review (*The Medical Letter*, PMID 40261315) continues to list Brinzolamide as a standard treatment option for open-angle glaucoma, confirming over 20 years of sustained clinical use. None of these publications address hereditary or paediatric glaucoma populations specifically.

---

## UK Market Information

No MHRA marketing authorisations are recorded for Brinzolamide in this evidence pack. Clinicians should verify the current authorisation status directly via the MHRA Public Assessment Reports database or the Electronic Medicines Compendium (eMC). Note that Azopt® (brinzolamide 1% ophthalmic suspension, Alcon Laboratories) has historically held a European marketing authorisation; post-Brexit UK authorisation status should be confirmed with the MHRA.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|------------|-------------------|
| *No records found* | — | — | — |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Important safety signal — Angle Closure Risk:** A 2025 case report (PMID 39870471, *BMJ Case Reports*) documents a rare but clinically significant adverse event: topical Brinzolamide-induced **ciliary body effusion with secondary angle closure and myopic shift**. The proposed mechanism involves sulfonamide-related ciliary body oedema causing anterior displacement of the lens–iris diaphragm, narrowing the drainage angle and acutely raising IOP. This finding is particularly pertinent when considering use in primary hereditary glaucoma patients, who may have underlying anatomical susceptibilities (shallow anterior chamber, narrow angle). Two further publications (PMID 34307961, 2021 case series; PMID 38585162, 2024 prescription audit) reference this mechanism in the context of drug-induced angle closure. Additionally, a canine primary closed-angle glaucoma study (PMID 26334202) suggests prophylactic topical CAIs including brinzolamide may delay IOP elevation in fellow eyes, but extrapolation to humans requires caution.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently no clinical trial or published literature evidence supporting the use of Brinzolamide in primary hereditary glaucoma; the TxGNN prediction score of 99.48% is likely driven by graph-level proximity to densely connected adult open-angle glaucoma nodes, rather than indicating an evidence-backed repurposing opportunity for this specific genetic indication. An important safety signal — sulfonamide-induced ciliary body effusion and secondary angle closure — further complicates the risk–benefit profile in this population.

**To proceed, the following is needed:**

- **Paediatric safety and pharmacokinetic data:** Dedicated studies on the systemic absorption, metabolic effects (particularly metabolic acidosis risk), and ocular tolerance of topical brinzolamide in neonates, infants, and children with primary congenital glaucoma
- **Clinical case series or registries:** Prospective observational data on Brinzolamide use as adjunctive pre-/post-operative therapy in children undergoing goniotomy or trabeculotomy for *CYP1B1*- or *MYOC*-associated glaucoma
- **Paediatric regulatory pathway:** Clarification of whether a new paediatric indication would require a Paediatric Investigation Plan (PIP) under UK MHRA/ICH E11 guidelines, and whether extrapolation from adult data is considered acceptable
- **MOA data gap remediation:** Formal mechanism of action data from DrugBank (identified as a high-severity data gap in this evidence pack)
- **UK authorisation status verification:** Confirmation of current MHRA marketing authorisation for Brinzolamide (Azopt®) via eMC or MHRA direct query, given the data gap in this evidence pack
- **Safety signal characterisation:** Further evaluation of the ciliary body effusion / secondary angle closure risk in patients with hereditary glaucoma phenotypes, particularly those with anatomically narrow angles

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Suspected adverse reactions should be reported via the Yellow Card Scheme (yellowcard.mhra.gov.uk).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

