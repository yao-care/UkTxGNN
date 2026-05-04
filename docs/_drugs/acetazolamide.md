---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Altitude Sickness & Glaucoma to Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor with long-established uses including glaucoma, altitude sickness prophylaxis, and epilepsy — conditions where reducing fluid accumulation or modulating acid-base balance is the therapeutic goal. The TxGNN model predicts it may be effective for **Cardiomyopathy** (specifically in acute decompensated heart failure), with **3 clinical trials** and **10 publications** currently supporting this direction. Notably, the landmark ADVOR trial (*New England Journal of Medicine*, 2022) has already demonstrated significant clinical benefit when acetazolamide is added to standard loop diuretics, lending strong mechanistic and clinical credibility to this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved from MHRA database (data gap); known BNF-listed uses include glaucoma, altitude sickness, and epilepsy |
| Predicted New Indication | Cardiomyopathy (Acute Decompensated Heart Failure) |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L2 |
| UK Market Status | Not found in MHRA dataset (possible data gap — verify via MHRA register and BNF) |
| Number of Marketing Authorisations | 0 (data not retrieved) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acetazolamide inhibits carbonic anhydrase (CA) isoforms II and IV in the proximal renal tubule, blocking bicarbonate reabsorption and driving natriuresis — the excretion of sodium alongside water. This mechanism complements loop diuretics (which act on the ascending limb of the loop of Henle), making it particularly valuable in patients with diuretic resistance, a common and difficult problem in chronic heart failure. By promoting bicarbonate loss, acetazolamide simultaneously reverses the metabolic alkalosis that accumulates with prolonged loop diuretic use — alkalosis itself further suppresses diuretic responsiveness, creating a vicious cycle that acetazolamide can break.

Cardiomyopathy — particularly dilated cardiomyopathy — is the leading underlying cause of acute decompensated heart failure (ADHF). Patients with ADHF typically present with severe volume overload, and incomplete decongestion before discharge is strongly associated with rehospitalisation and mortality. The physiological rationale for adding a proximal tubule agent such as acetazolamide to standard loop diuretics is therefore compelling: the two agents act at different nephron segments, avoiding competition for the same transporter, and together restore effective tubuloglomerular feedback.

Detailed mechanism of action data (MOA) was not available in this Evidence Pack. However, the mechanistic argument is well-supported by clinical evidence: the ADVOR trial (NCT03505788, *NEJM* 2022, n=519) demonstrated that intravenous acetazolamide added to furosemide achieved successful decongestion in 42.2% of patients versus 30.5% with placebo (p=0.003), without excess adverse events. Three ongoing Phase 4 trials are now extending this evidence base to oral formulations, head-to-head diuretic comparisons, and personalised urine sodium–guided algorithms, all directly centred on the cardiomyopathy/heart failure patient population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | Oral acetazolamide for acute decompensation of chronic heart failure (CHF), including cardiomyopathy aetiology; oral extension of the ADVOR IV trial concept, exploring real-world applicability |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | Large double-blinded RCT comparing loop diuretics + acetazolamide vs loop diuretics + metolazone vs loop diuretics alone in acute heart failure with volume overload; co-primary aim to identify optimal loop diuretic type |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | Recruiting | 466 | TAILOR-AHF: personalised, urine sodium–guided diuretic algorithm in acutely decompensated heart failure; acetazolamide included as an algorithm option when standard response is inadequate |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Narrative Review | ESC Heart Failure | 2024 update on heart failure management; covers evolving evidence for novel diuretic combinations (including acetazolamide), SGLT2 inhibitors, and finerenone in heart failure with preserved and reduced ejection fraction |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Narrative Review | Eur Heart J Cardiovasc Pharmacother | Review of new cardiovascular pharmacological agents in 2022; discusses mavacamten for obstructive HCM and emerging diuretic strategies including acetazolamide combinations |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | J Cardiology Cases | Acetazolamide used to treat hypochloraemia in an 87-year-old with advanced heart failure and hypertrophic cardiomyopathy; demonstrates acetazolamide's chloride-modulating role and highlights need for urinary electrolyte monitoring |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Animal Study | Saudi Medical Journal | Acetazolamide effects on ischaemia–reperfusion injury in isolated rabbit hearts (2-week and 8-week-old); explores potential cardioprotective properties at the myocardial level |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Series | Acta Neurol Scand | Cardiac involvement including cardiomyopathy in hypokalaemic periodic paralysis — a condition in which acetazolamide is a standard prophylactic treatment; documents cardiac co-morbidity in this population |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurol Scand | Heart muscle disease in familial hypokalaemic periodic paralysis; patient treated with acetazolamide 750–1000 mg/day; exercise-induced angina observed, raising cardiac monitoring considerations |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Adverse Event Case Report | Acute Medicine & Surgery | ⚠️ Safety signal: non-cardiogenic pulmonary oedema occurring one hour after IV acetazolamide in a patient with dilated cardiomyopathy and flail chest; resolved with additional diuretics and vasodilator |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian J Ophthalmology | Oral acetazolamide used for cystoid macular oedema in Danon disease (X-linked vacuolar cardiomyopathy + retinopathy); illustrates use in a cardiomyopathy-associated systemic condition |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Observational | J Nuclear Medicine | SPECT cerebral blood flow assessment in mitochondrial encephalomyopathy; acetazolamide used as vasodilatory challenge — indirect evidence of carbonic anhydrase activity on perfusion in mitochondrial disease affecting both brain and heart |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | J Medical Case Reports | Congenital hydrocephalus in trisomy 9p with coexisting congenital heart disease; acetazolamide used for CSF production reduction alongside cardiac management — illustrates acetazolamide use in complex multi-organ disease including cardiac involvement |

---

## UK Market Information

No marketing authorisation records for Acetazolamide were returned by the MHRA dataset used in this analysis. This is likely a **data retrieval gap** rather than a true absence from the UK market, as acetazolamide (e.g., **Diamox®** 250 mg tablets and 500 mg powder for solution for injection) is documented in the British National Formulary (BNF) under the following classifications:

- **BNF 11.6** — Treatment of glaucoma (reduces aqueous humour production)
- **BNF 4.8.1** — Adjunctive treatment of absence (petit mal) and other seizures
- **BNF 1.1** — Altitude sickness prophylaxis
- **BNF 2.2.8** — Diuresis in states of oedema

Clinicians should verify the current authorisation status, available dosage forms, and licensed indications directly via the **MHRA Product Licence register** and the current edition of the **BNF** before clinical use.

> No marketing authorisation records were retrieved for Acetazolamide in this dataset. The table below cannot be populated.

---

## Safety Considerations

No formal safety data (SmPC warnings, contraindications, or drug–drug interaction records) was retrieved from the regulatory database for this candidate. The following considerations are drawn from published literature and established pharmacological knowledge, and are particularly relevant in the heart failure context:

- **Adverse event signal (pulmonary oedema)**: One case report (PMID 29123889) documented acute non-cardiogenic pulmonary oedema within one hour of IV acetazolamide administration in a patient with dilated cardiomyopathy. Close respiratory monitoring following initiation is warranted, especially with the IV route.
- **Electrolyte disturbances**: Acetazolamide promotes renal loss of sodium, potassium, and bicarbonate, which can cause hypokalaemia, hyponatraemia, and metabolic acidosis. Heart failure patients typically receive multiple diuretics, ACE inhibitors/ARBs, and aldosterone antagonists — compounding electrolyte risk. Regular monitoring of serum K⁺, Na⁺, Cl⁻, and HCO₃⁻ is essential.
- **Renal function**: Acetazolamide is renally cleared; dose adjustment or avoidance is necessary in renal impairment (eGFR < 30 mL/min/1.73 m²), which is common in advanced heart failure.
- **Sulfonamide sensitivity**: Acetazolamide is a sulfonamide derivative. A careful allergy history should be obtained prior to use.
- **Hepatic encephalopathy risk**: In patients with hepatic congestion secondary to right heart failure or cirrhosis, carbonic anhydrase inhibition may increase ammonia toxicity by alkalinising urine and reducing renal NH₃ excretion — use with caution in this subgroup.

Please refer to the current **SmPC** and the **BNF** for complete safety information. Report suspected adverse reactions via the **Yellow Card Scheme**: [https://yellowcard.mhra.gov.uk/](https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ADVOR trial (NEJM 2022, Phase 3, n=519) provides robust evidence that acetazolamide added to loop diuretics significantly improves decongestion in acute heart failure — the primary clinical manifestation of cardiomyopathy — and three Phase 4 trials are actively extending this evidence base. The mechanistic rationale (proximal tubular carbonic anhydrase inhibition synergising with loop diuretics to overcome diuretic resistance) is pharmacologically sound and well-characterised. However, key regulatory and safety data gaps must be resolved before formal repurposing pathways are pursued in the UK.

**To proceed, the following is needed:**

- **Regulatory clarification**: Confirm current MHRA marketing authorisation status, licensed indications, and available UK dosage forms for acetazolamide (verify via MHRA register and current BNF edition)
- **Full SmPC review**: Obtain the SmPC to complete a structured S1 safety assessment, including contraindications, special warnings, and interactions with standard heart failure pharmacotherapy (furosemide, spironolactone, ACE inhibitors, beta-blockers, SGLT2 inhibitors)
- **Mechanism of action documentation**: Retrieve full DrugBank MOA profile (DrugBank ID: DB00819) to formally document carbonic anhydrase isoform selectivity and secondary pharmacological effects relevant to cardiac physiology
- **Patient subgroup definition**: Specify target cardiomyopathy subtype (dilated, ischaemic, hypertrophic) and heart failure phenotype (HFrEF vs HFpEF) to enable precise patient selection criteria aligned with ongoing trial cohorts
- **ADVOR trial data review**: Conduct a full review of the completed ADVOR trial (NCT03505788) dataset to assess applicability to UK practice, including subgroup analyses by cardiomyopathy aetiology and baseline renal function
- **Electrolyte monitoring protocol**: Establish a standardised monitoring protocol for serum K⁺, Na⁺, Cl⁻, bicarbonate, creatinine, and eGFR, consistent with NICE heart failure guidelines and UK clinical pharmacy practice
- **Evidence watch**: Monitor completion of NCT06166654 (n=939, estimated completion September 2027) as the most likely pivotal evidence for standard-of-care integration in the UK

---

> ⚠️ **Disclaimer**: This report is produced for research purposes only and does not constitute medical advice. Drug repurposing candidates require full clinical validation before therapeutic application. All prescribing decisions must comply with current MHRA authorisations, NICE guidance, and individual patient clinical assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

