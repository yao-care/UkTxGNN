---
layout: default
title: Cefradine
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Cefradine
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

# Cefradine: From Bacterial Infections to Bronchitis

## One-Sentence Summary

Cefradine is a first-generation cephalosporin antibiotic with established broad-spectrum activity against Gram-positive and select Gram-negative bacteria, historically used for respiratory tract, urinary tract, and skin infections.
The TxGNN model generated ten predictions for this drug; **Bronchitis** is the highest-evidence candidate, supported by **0 registered clinical trials** and **17 publications**.
This report focuses on bronchitis as the most clinically actionable prediction (Evidence Level L3); the remaining nine predictions are rated L4–L5 and carry a Hold recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently licensed in the UK; historically used for bacterial infections (respiratory tract, urinary tract, skin and soft tissue) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 94.74% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, cefradine is a first-generation cephalosporin antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs) and disrupting peptidoglycan cross-linking, leading to osmotic lysis. This class effect is shared by all beta-lactam antibiotics and is well characterised in the literature.

Bacterial bronchitis — including acute bacterial bronchitis and acute exacerbations of chronic bronchitis (AECB) — is commonly caused by organisms within cefradine's spectrum of activity, most notably *Streptococcus pneumoniae*. First-generation cephalosporins retain good activity against *S. pneumoniae*, which is the rationale for this TxGNN prediction. However, their coverage of *Haemophilus influenzae* (a principal AECB pathogen) is limited, particularly against beta-lactamase-producing strains, and *Moraxella catarrhalis* and atypical organisms (*Chlamydophila*, *Mycoplasma*) are not covered. This incomplete pathogen spectrum is the primary mechanistic caveat.

Historical clinical data directly support cefradine's use in respiratory infections. PMID 4284 directly compared cephradine with cephalexin in respiratory and urinary tract infections, and PMID 1164460 reports a double-blind comparison with ampicillin in chest infections. Pharmacokinetic data (PMID 7399714) assessed cephradine sputum penetration in chronic bronchitis patients, confirming tissue distribution, albeit with low and variable concentrations. Multiple studies of cefroxadine — a structurally related first-generation cephalosporin — in paediatric respiratory infections provide additional indirect class-level support. Whilst the mechanistic and historical rationale is plausible, current NICE and BNF guidance favours amoxicillin, amoxicillin-clavulanate, or macrolides as first-line agents for bronchitis, reflecting broader pathogen coverage and better resistance profiles.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4284](https://pubmed.ncbi.nlm.nih.gov/4284/) | 1976 | Comparative Clinical Study | Current Therapeutic Research | Direct head-to-head comparison of cephradine (cefradine) vs cephalexin in respiratory tract and urinary tract infections; provides the most direct evidence for cefradine in this indication |
| [1164460](https://pubmed.ncbi.nlm.nih.gov/1164460/) | 1975 | Double-Blind Comparative Study | Br J Clin Practice | Double-blind comparison of cephradine vs ampicillin in chest infections; key direct evidence supporting respiratory use |
| [3323166](https://pubmed.ncbi.nlm.nih.gov/3323166/) | 1987 | Comparative Clinical Trial | J Antimicrob Chemother | Double-blind studies comparing roxithromycin with cephradine (and doxycycline) in acute bronchitis/AECB; overall clinical success rate 89% for roxithromycin, with cephradine as active comparator |
| [822982](https://pubmed.ncbi.nlm.nih.gov/822982/) | 1976 | Clinical Study | Current Therapeutic Research | Parenteral cephradine in lower respiratory tract infections; results from two prospective studies supporting efficacy in this setting |
| [7399714](https://pubmed.ncbi.nlm.nih.gov/7399714/) | 1980 | Pharmacokinetic/Clinical | Infection | Sputum and pleural concentrations of cephradine (alongside other antibiotics) in 19 chronic bronchitis patients; sputum penetration was low and highly variable, a potential clinical limitation |
| [10225580](https://pubmed.ncbi.nlm.nih.gov/10225580/) | 1999 | Retrospective Review | J Antimicrob Chemother | Retrospective analysis of 60 COPD/AECB outpatient records comparing antimicrobial efficacy and related treatment costs; cephradine included as a comparator agent |
| [7038188](https://pubmed.ncbi.nlm.nih.gov/7038188/) | 1981 | Clinical Series | Jpn J Antibiotics | Cefroxadine (structurally related first-generation cephalosporin) in 19 paediatric infections including 6 cases of acute bronchitis; overall clinical efficacy rate 100%, providing indirect class-level support |
| [7151376](https://pubmed.ncbi.nlm.nih.gov/7151376/) | 1982 | Clinical Evaluation | La Clinica Terapeutica | Oral cephalosporin in acute bacterial bronchopneumopathy; indirect class-level evidence for first-generation cephalosporins in lower respiratory tract infection |
| [7038189](https://pubmed.ncbi.nlm.nih.gov/7038189/) | 1981 | PK + Clinical Study | Jpn J Antibiotics | Cefroxadine pharmacokinetics plus clinical trial in 151 paediatric cases including acute bronchitis; detailed PK data and efficacy results, indirect class evidence |
| [383011](https://pubmed.ncbi.nlm.nih.gov/383011/) | 1979 | Randomised Controlled Study | Antimicrob Agents Chemother | Prospective, randomised, single-blind comparison of cefamandole vs ampicillin in 27 hospitalised patients with *Haemophilus* bronchopulmonary infections; both equally effective, demonstrating cephalosporin activity in Haemophilus respiratory disease |

---

## UK Market Information

Cefradine does not currently hold a Marketing Authorisation in the United Kingdom. The MHRA has no active licences on record, and the drug is not included in the current British National Formulary (BNF). Any clinical use would require either a Specials licence or a named-patient Special Clinical Need (SCN) arrangement under the Human Medicines Regulations 2012.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Of the ten TxGNN predictions evaluated for cefradine, bronchitis is the only indication reaching Evidence Level L3, underpinned by direct comparative clinical studies (PMID 4284, PMID 1164460) and pharmacokinetic data in bronchitis patients. The mechanistic link is plausible — bacterial bronchitis pathogens overlap substantially with cefradine's spectrum — but pathogen coverage is incomplete (limited *H. influenzae* activity, no atypical or anaerobic coverage), and the available evidence is predominantly from 1975–1999 and does not meet modern RCT standards. Current NICE and BNF guidance recommends alternative agents (amoxicillin, co-amoxiclav, clarithromycin) with superior coverage and resistance profiles, meaning clinical added value over existing options would need to be clearly demonstrated.

**To proceed, the following is needed:**

- Obtain MHRA Marketing Authorisation or Specials licence for UK clinical use
- Retrieve the full SmPC to assess contraindications, drug interactions, warnings, and special population guidance (renal impairment, pregnancy, paediatrics)
- Commission a systematic review or network meta-analysis comparing cefradine against current NICE-recommended agents (amoxicillin, co-amoxiclav, clarithromycin) for bronchitis
- Obtain contemporary UK antimicrobial resistance data for key bronchitis pathogens (*S. pneumoniae*, *H. influenzae*) against first-generation cephalosporins
- Define the patient subgroup most likely to benefit (e.g., penicillin-allergic patients for whom macrolides are unsuitable)
- Assess pharmacoeconomic viability against currently available licensed alternatives

> ⚠️ **Research Disclaimer:** This report is produced for research purposes only and does not constitute medical advice. Drug repurposing candidates require full clinical validation before any therapeutic application. All predictions should be interpreted alongside current clinical guidelines and local resistance data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

