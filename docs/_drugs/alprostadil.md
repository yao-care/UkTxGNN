---
layout: default
title: Alprostadil
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Alprostadil
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

# Alprostadil: From Ductus-Dependent Congenital Heart Disease to Aortic Malformation

## One-Sentence Summary

Alprostadil (prostaglandin E1, PGE1) is a potent vasodilating prostaglandin analogue with a long-established role in maintaining patency of the ductus arteriosus in neonates with duct-dependent congenital heart disease, serving as a critical bridge to definitive surgical repair.
The TxGNN model predicts it may be effective specifically for **Aortic Malformation** — encompassing interrupted aortic arch, critical aortic coarctation, and hypoplastic left heart syndrome —
with **2 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ductus-dependent congenital heart disease (maintenance of ductal patency pending surgical correction) |
| Predicted New Indication | Aortic Malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (Observational studies, case series, and clinical management reviews) |
| UK Market Status | Not found in evidence pack (data gap — see UK Market Information below) |
| Number of Marketing Authorisations | 0 (as recorded in evidence pack; reflects incomplete data collection) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alprostadil is the synthetic form of prostaglandin E1, a naturally occurring lipid mediator. It acts by binding to EP4 prostaglandin receptors on the smooth muscle cells of the ductus arteriosus, activating intracellular cyclic AMP (cAMP) signalling. This relaxes ductal smooth muscle, preventing the postnatal constriction that would otherwise close the vessel within hours of birth. This mechanism — maintaining a pharmacologically patent ductus arteriosus (PDA) — is the cornerstone of its established neonatal use and has been documented in clinical practice since the late 1970s.

Aortic malformations, including interrupted aortic arch (IAA), critical aortic coarctation, and hypoplastic left heart syndrome (HLHS), share a common and immediately life-threatening haemodynamic feature: complete or near-complete dependency on the patent ductus arteriosus for systemic perfusion distal to the aortic obstruction or discontinuity. Without ductal patency, systemic circulatory collapse — manifesting as metabolic acidosis, end-organ ischaemia, and death — can ensue within hours. Alprostadil infusion to maintain the ductus therefore directly addresses the critical pathophysiology of aortic malformations, serving as the definitive pre-operative stabilising measure while the neonate is resuscitated and transferred to a cardiac surgical centre.

The TxGNN model's high-confidence prediction (99.98%) is thus strongly congruent with established clinical practice rather than representing a speculative repurposing hypothesis. The knowledge graph connectivity between alprostadil's EP4/cAMP mechanism and the ductus-dependent haemodynamics of aortic malformations is mechanistically robust. Multiple clinical publications dating from 1982 onwards document PGE1 infusion as the standard of care in neonates with IAA, aortic atresia, and critical aortic coarctation — precisely the conditions encompassed by this predicted indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | Terminated | 10 | Investigated the acute effects of alprostadil on cerebral and pulmonary blood flow following bidirectional cavopulmonary connection (Glenn procedure) in single-ventricle palliation; alprostadil was administered to improve pulmonary and cerebral perfusion. Terminated early with only 10 participants enrolled; efficacy conclusions cannot be drawn, but the trial confirms feasibility of alprostadil use in complex congenital cardiac surgery. |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | Completed | 39 | Cross-sectional imaging comparison of Colour Doppler Ultrasonography and MR Angiography in systemic large vessel vasculitis; not a direct alprostadil treatment trial. Provides peripheral context on non-invasive assessment of aortic and large vessel pathology. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | RCT | Zhonghua Yi Xue Za Zhi | Alprostadil (Lipo-PGE1) combined with ulinastatin significantly attenuated systemic inflammatory response and lung injury following cardiopulmonary bypass in paediatric congenital heart disease patients; supports alprostadil's cardioprotective role in surgical CHD management |
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Clinical Review | Semin Thorac Cardiovasc Surg | Landmark management review of interrupted aortic arch; credits introduction of PGE1 in the late 1970s as having "revolutionised" pre-operative stabilisation; advocates complete multi-day resuscitation under PGE1 before undertaking primary neonatal repair |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Prospective Case Series | Pharmacotherapy | Seminal early evaluation of alprostadil in congenital heart disease, including aortic lesions; demonstrated that PGE1 infusion dilates the ductus, increases pulmonary blood flow, and improves systemic oxygenation, establishing the pharmacological basis for its neonatal use |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Clinical Review | Cardiology in the Young | Preoperative management of neonatal critical aortic valvar stenosis; details PGE1 infusion as essential to maintain ductal patency and systemic coronary and peripheral perfusion pending catheter-based or surgical intervention; outlines PGE1 dosing strategy and monitoring |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case Series | Pediatric Cardiology | PGE1 infusion in 7 neonates with hypoplastic left ventricle and aortic atresia; demonstrated transient haemodynamic and metabolic improvement in 6/7 infants; highlights the severity of the condition and the limits of ductal bridging in the most extreme aortic malformations |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Prospective Case Series | J Am Coll Cardiol | Long-term PGE1 infusion (mean 39 days, range 8–104) in 17 neonates including patients with aortic coarctation; established feasibility and tolerability of extended ductal maintenance as a bridge to staged surgery |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Retrospective Cohort | Asian J Surg | Outcomes of staged surgical repair for interrupted aortic arch; contextualises PGE1-supported preoperative stabilisation within contemporary staged repair strategies; supports the ongoing relevance of ductal maintenance in IAA management |
| [16368373](https://pubmed.ncbi.nlm.nih.gov/16368373/) | 2006 | Retrospective Cohort | Ann Thorac Surg | Late outcomes of closed transventricular aortic valvotomy for critical neonatal aortic stenosis; highlights persistent high morbidity and mortality despite optimised PGE1 pre-operative stabilisation, underscoring the need for timely surgical correction |
| [28508920](https://pubmed.ncbi.nlm.nih.gov/28508920/) | 2017 | Case Report | Pediatric Cardiology | **Important safety signal:** second- and third-degree atrioventricular block occurring during prolonged low-dose PGE1 infusion in a neonate with critical aortic coarctation; blocks resolved promptly upon PGE1 discontinuation — highlights need for cardiac conduction monitoring |
| [1926911](https://pubmed.ncbi.nlm.nih.gov/1926911/) | 1991 | Review | DICP Ann Pharmacother | Early guidance recommending PGE1 stabilisation prior to neonatal transport for all suspected ductus-dependent defects, including aortic arch lesions; instrumental in establishing pre-transport PGE1 as standard of care in district and community hospital settings |

---

## UK Market Information

No MHRA marketing authorisation data was returned in this evidence pack, and the market status is recorded as not marketed with zero licences. This almost certainly reflects a **data collection gap** rather than a genuine absence from the UK market.

Based on established clinical information, Alprostadil is available in the United Kingdom under several marketing authorisations, including:

- **Prostin VR** (alprostadil 500 micrograms/mL concentrate for solution for infusion) — indicated for temporary maintenance of patency of the ductus arteriosus in neonates with duct-dependent congenital heart disease, pending corrective surgery. This is the formulation directly relevant to the predicted aortic malformation indication.
- **Caverject** and **MUSE** — indicated for erectile dysfunction.

In the BNF, alprostadil appears under both cardiovascular preparations (peripheral vasodilators) and urological preparations. UK prescribers should consult the current edition of the BNF and the relevant product SmPC for authorised indications, dosing regimens, and up-to-date safety information.

> **Action required:** The absence of MHRA licence data in this evidence pack is flagged as a Blocking data gap (DG001) in the evidence pack metadata. The MHRA product licence database should be queried directly to retrieve full authorisation details before any regulatory or clinical decision is finalised.

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

Based on literature identified in this evidence pack, the following safety signals are of particular relevance in the neonatal aortic malformation setting:

- **Cardiac conduction disturbances:** Second- and third-degree atrioventricular block reported with prolonged low-dose PGE1 infusion in critical aortic coarctation (PMID 28508920); continuous ECG monitoring is warranted.
- **Apnoea:** A well-recognised adverse effect of intravenous alprostadil in neonates, particularly at higher doses; resuscitation facilities must be immediately available.
- **Prolonged infusion effects:** Cortical bone proliferation, hypertrophic pyloric stenosis (PMID 25263728), and soft tissue swelling of the extremities have been reported with extended PGE1 use; duration of infusion should be minimised in accordance with surgical planning.
- **Systemic hypotension and fever:** Common dose-dependent effects requiring haemodynamic monitoring.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The use of alprostadil to maintain ductus arteriosus patency in neonates with duct-dependent aortic malformations represents an established, mechanistically robust clinical practice documented in the literature since the late 1970s. The TxGNN prediction reflects genuine clinical utility, and an L3 evidence base of observational studies, prospective case series, and authoritative management reviews provides adequate grounding for progression, provided outstanding data gaps are resolved.

**To proceed, the following is needed:**

- **MHRA licence verification:** Query the MHRA product licence database to confirm the scope of the existing Prostin VR authorisation, and determine whether aortic malformations are already encompassed within the current ductus-dependent CHD indication, or whether a licence variation would be required.
- **SmPC review:** Retrieve and review the current Prostin VR SmPC for authorised indications, dosing in neonates (weight-based PGE1 infusion rates), contraindications, and monitoring requirements.
- **MOA documentation:** Retrieve the formal mechanism of action record from DrugBank (DB00770) to complete the drug profile and support any regulatory submission (data gap DG002).
- **Safety monitoring plan:** Develop a neonatal monitoring protocol covering apnoea, cardiac conduction, haemodynamics, pyloric function (with prolonged use), and bone changes.
- **Clinical audit or registry linkage:** Given the rarity of specific aortic arch malformation subtypes (e.g., IAA), consider linkage with the National Congenital Heart Disease Audit (NCHDA) or the Congenital Heart Disease Intelligence Network to generate UK-specific outcomes data for this indication.

---

> *This report is generated for research and evaluation purposes only and does not constitute clinical or regulatory advice. Drug repurposing candidates require prospective clinical validation before application to patient care.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

