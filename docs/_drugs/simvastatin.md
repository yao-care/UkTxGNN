---
layout: default
title: Simvastatin
parent: High Evidence (L1-L2)
nav_order: 531
evidence_level: L1
indication_count: 8
---

# Simvastatin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **8** 
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

Using the report as specified—flagging upfront that the evidence pack itself notes this "new indication" (familial hypercholesterolaemia) is not a genuine repurposing candidate but an already-established statin indication, and that several data gaps (UK licensing, MOA, SmPC safety data) are blocking.

---

# Simvastatin: From Hypercholesterolaemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is an HMG-CoA reductase inhibitor originally used to treat hypercholesterolaemia and mixed dyslipidaemia.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia**,
with **18 clinical trials** and **17 publications** currently supporting this direction — although, as detailed below, this is not a true repurposing signal but confirmation of an already-established statin indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolaemia / mixed dyslipidaemia (established statin-class indication; not captured in the current UK licensing data supplied — see gap below) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| UK Market Status | Not Marketed (per evidence pack — see note under UK Market Information) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is a recorded data gap, DG002). However, the repurposing rationale supplied alongside the top prediction is itself informative: **Simvastatin is an HMG-CoA reductase inhibitor that directly blocks the hepatic cholesterol biosynthesis pathway.** In patients with familial hypercholesterolaemia (FH), a defect in the LDL receptor causes LDL-C accumulation; statins upregulate hepatic LDL receptor expression, which is a well-established pharmacological mechanism rather than a speculative TxGNN association.

Importantly, the evidence pack's own annotation for this candidate states this explicitly: *"此為 statin class 之標準適應症，非典型老藥新用案例"* — this is a standard indication for the statin class, not a typical repurposing case. In other words, the high TxGNN score here reflects that statins (including simvastatin) are already guideline-recommended first-line therapy for FH, rather than uncovering a genuinely novel therapeutic use. This should temper how the "Proceed with Guardrails" decision is interpreted — the guardrails relate to confirming licensing/safety documentation, not to establishing efficacy, which is already well demonstrated.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Placebo-controlled RCT of alirocumab added to existing lipid-modifying therapy (incl. statins) in heterozygous FH not adequately controlled |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab efficacy/safety on LDL-C in children/adolescents with homozygous FH, on top of background treatment (incl. statins) |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam added to stable-dose statin (incl. simvastatin) in paediatric heterozygous FH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin vs simvastatin alone in adolescents with heterozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs simvastatin in Fredrickson Type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term safety/tolerability of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Placebo-controlled RCT of alirocumab in heterozygous FH inadequately controlled on lipid-modifying therapy |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab as add-on to stable statin therapy vs placebo in heterozygous FH / high CV risk hypercholesterolaemia |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Phase 3 | Completed | 986 | Long-term open-label extension assessing safety/efficacy of alirocumab in heterozygous FH |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | N Engl J Med | ENHANCE: simvastatin with or without ezetimibe in FH — landmark trial on atherosclerosis progression |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of statins (incl. simvastatin) for children with FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Benefits and risks assessment of simvastatin specifically in FH |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | 2026 ACC/AHA dyslipidaemia management guideline (retires 2018 cholesterol guideline) |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Observational | J Am Coll Cardiol | Statins in FH: association with reduced CAD events and all-cause mortality |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Benefits and risks of simvastatin specifically in FH patients |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative study | Nutr Metab Cardiovasc Dis | Atorvastatin vs simvastatin for LDL-C goal attainment in heterozygous FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Observational | J Clin Med | Cellular immunity parameters in children with FH treated with simvastatin |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Observational | Pharmacogenomics J | Combined FH/statin pharmacogenomic genetic testing implementation study |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | Observational | Atherosclerosis | Real-world FH treatment patterns and LDL-C goal attainment (Slovakia) |

## UK Market Information

No marketing authorisation records were returned in this evidence pack (0 licenses, market status recorded as "Not Marketed"). This is notable, since simvastatin is a widely used generic statin in UK clinical practice under multiple manufacturers — this likely reflects a gap in the underlying regulatory dataset rather than genuine absence from the UK market. **This should be verified directly against the MHRA products database / current BNF listing before any decision is finalised.**

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: the safety dataset in this evidence pack returned no warnings, contraindications, or drug interactions (all fields recorded as data gaps, DG001 — Blocking). This is a critical omission for a statin, given the well-known class risks of myopathy/rhabdomyolysis and CYP3A4-mediated interactions (e.g. with protease inhibitors, as surfaced incidentally in this pack's HIV-related literature search). This gap must be closed before clinical use.*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3 RCTs (notably ENHANCE, NCT00552097/PMID 18376000) directly evaluating simvastatin in FH populations. However, this is not a novel repurposing signal — it confirms an already-established statin-class indication — and two data gaps are currently blocking or high-severity: missing SmPC warnings/contraindications (DG001, Blocking) and missing MOA documentation (DG002, High).

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent SmPC warnings and contraindications (DG001 — blocking; required before any S1 safety assessment)
- Confirmed drug-drug interaction data, particularly CYP3A4-mediated interactions (myopathy/rhabdomyolysis risk)
- Verification of actual current UK marketing authorisation status via MHRA (the "0 licenses / not marketed" result is inconsistent with simvastatin's known widespread UK generic availability and should be re-checked)
- Formal mechanism of action documentation (DG002)
- Clarification of whether "familial hypercholesterolemia" should be scored/tracked as a genuine repurposing candidate, given it is already a guideline-recommended statin indication rather than a new therapeutic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

