---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Septicemic Plague

## One-Sentence Summary

> Ofloxacin is a broad-spectrum fluoroquinolone antibacterial. Among ten indications proposed by the TxGNN model for this drug, most (7 of 10) are flagged within the evidence pack itself as low-confidence, mechanistically unsupported predictions. The strongest candidate is **Septicemic Plague** (Yersinia pestis infection), supported by **17 preclinical/animal-model publications** and a clear class-effect with two already FDA-approved fluoroquinolones (ciprofloxacin, levofloxacin); no human clinical trials exist because they are ethically infeasible for this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections generally (broad-spectrum fluoroquinolone antibacterial — no specific indication text is recorded in this evidence pack) |
| Predicted New Indication | Septicemic Plague (Yersinia pestis) |
| TxGNN Prediction Score | 99.79% (rank 2717 of full candidate set) |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: predicted_indications[0] in the raw data (hyperamylasemia) was not selected as the report focus — the evidence pack itself labels it, and six other top-ranked predictions, as likely TxGNN embedding-space noise with no mechanistic or evidentiary basis (see Conclusion).*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ofloxacin is not available from DrugBank in this evidence pack (data gap, high severity). Based on information contained within the evidence pack's own repurposing rationale, ofloxacin is a broad-spectrum fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV — the same mechanism by which it, and its class relatives, act against *Yersinia pestis*.

This is a clear class-effect case rather than a novel mechanistic hypothesis. Ciprofloxacin and levofloxacin — both fluoroquinolones in the same class as ofloxacin — have already been approved by the FDA for plague treatment and prophylaxis under the Animal Efficacy Rule, precisely because human efficacy trials cannot ethically be conducted for a rare, highly lethal, biothreat-relevant pathogen. Multiple studies in this evidence pack directly test ofloxacin (not just its class relatives) against experimental *Y. pestis* infection in mice and other models, with consistent efficacy findings across decades of publications.

The main limitation is the total absence of human clinical trial data (the `clinical_trials` field is empty) and the absence of any UK marketing authorisation for ofloxacin — meaning any use for this indication would currently sit outside the licensed product landscape and would need to be considered via unlicensed/specials or stockpiling pathways rather than routine prescribing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Preclinical | Antibiotiki i khimioterapiia | Ofloxacin efficacy in prophylaxis and treatment of experimental plague, tested against antigen-complete and antigen-defective *Y. pestis* strains |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Preclinical | Antimicrob Agents Chemother | Ofloxacin among agents assessed in vitro and in a standardised murine *Y. pestis* infection model, active alongside reference drug streptomycin |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Preclinical | Antibiotiki i khimioterapiia | Combined emergency fluoroquinolone (including ofloxacin) prophylaxis plus specific vaccination outperformed either strategy alone in mice |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Preclinical | Antibiotiki i khimioterapiia | Comparative fluoroquinolone efficacy (levofloxacin, lomefloxacin, moxifloxacin vs others) in experimental plague in albino mice |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Review/Preclinical | Clin Infect Dis | African Green Monkey pneumonic plague model underpinning FDA approval of fluoroquinolone antimicrobials under the Animal Rule |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Preclinical | Clin Infect Dis | Effect of treatment delay on ciprofloxacin and levofloxacin efficacy in African Green Monkey pneumonic plague model |
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Preclinical | PLoS Negl Trop Dis | Levofloxacin cures experimental pneumonic plague in African Green Monkeys |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Preclinical | Antimicrob Agents Chemother | Mouse model of pneumonic plague comparing streptomycin to fluoroquinolone-class antibiotics with limited clinical experience |
| [17517837](https://pubmed.ncbi.nlm.nih.gov/17517837/) | 2007 | Preclinical | Antimicrob Agents Chemother | Pharmacodynamic model comparing streptomycin vs levofloxacin for plague therapy, including resistance emergence |
| [21127743](https://pubmed.ncbi.nlm.nih.gov/21127743/) | 2010 | Review | Open Microbiol J | Fluoroquinolone protection in animal models of respiratory infection with *Bacillus anthracis*, *Y. pestis*, and *Francisella tularensis* |

---

## UK Market Information

Ofloxacin currently has **no marketing authorisations on record in the United Kingdom** (0 licences; market status: not marketed) per this evidence pack. Any clinical use for either its original antibacterial applications or this predicted indication would need to proceed via an unlicensed medicine route (e.g. Specials, named-patient importation, or national stockpiling arrangements), pending confirmation of current MHRA licensing status directly with the MHRA.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

One point noted within the evidence pack itself is relevant to this indication: fluoroquinolones as a class (including ofloxacin) carry a known association with peripheral neuropathy, which should be borne in mind when weighing this drug against alternative agents for plague management, even though the specific TFDA/MHRA warning and contraindication data for ofloxacin itself is currently a data gap (see Conclusion).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple independent animal-model studies across species (mouse, rat, African Green Monkey), spanning decades, consistently support fluoroquinolone efficacy against *Y. pestis*, and two class relatives (ciprofloxacin, levofloxacin) already hold FDA approval for plague under the Animal Rule. However, no human trial data exist for ofloxacin in this indication, and critical safety data (TFDA/MHRA warnings and contraindications) remain an unresolved **Blocking** data gap that currently prevents a full S1 safety pre-screen.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications for ofloxacin
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to strengthen the mechanistic case
- Clarify UK licensing/import pathway, since ofloxacin is not currently marketed in the UK
- Assess this indication within a biodefence/stockpiling framework rather than routine commercial development, given the rarity of plague and the precedent set by ciprofloxacin/levofloxacin approvals

**Note on other TxGNN predictions for this drug:** Seven of the ten predicted indications (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, monoclonal gammopathy, hematological disease with acquired peripheral neuropathy, congenital hematological disorder) are explicitly flagged within the evidence pack as lacking any mechanistic plausibility or supporting evidence and are recommended **Hold**. A tenth candidate, punctate epithelial keratoconjunctivitis (L4, Research Question), may merit a brief separate scoping review given ofloxacin's established use as a topical ophthalmic antibacterial, though the cited literature does not directly test this specific indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

