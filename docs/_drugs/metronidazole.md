---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic Bacterial and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

> Metronidazole is a nitroimidazole antimicrobial established for anaerobic bacterial and protozoal infections (e.g. trichomoniasis, amoebiasis, giardiasis, bacterial vaginosis, anaerobic sepsis).
> The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis jirovecii pneumonia)**,
> but the underlying evidence — **24 clinical trials** and **9 publications** — does not actually support this: none evaluate metronidazole against Pneumocystis, and the drug's mechanism does not cover this pathogen. This is best read as a low-confidence, likely spurious signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no MHRA licence data returned). Metronidazole is internationally established for anaerobic bacterial and protozoal infections (trichomoniasis, amoebiasis, giardiasis, bacterial vaginosis). |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack (MOA recorded as a data gap). Based on general pharmacology, metronidazole is a nitroimidazole that is selectively activated by the nitroreductase enzymes of anaerobic bacteria and certain protozoa, generating cytotoxic free radicals; this restricts its activity to anaerobes and protozoa such as *Entamoeba histolytica*, *Giardia*, and *Trichomonas vaginalis*.

*Pneumocystis jirovecii*, the organism causing pneumocystosis, is a fungus-like pathogen with a fundamentally different biology — it is neither an anaerobic bacterium nor a protozoan in the sense relevant to metronidazole's activation pathway. Standard treatment for pneumocystosis is co-trimoxazole (trimethoprim-sulfamethoxazole), not metronidazole. The literature returned by this search largely reflects **comorbidity, not treatment efficacy**: several case reports describe HIV/AIDS patients who received metronidazole for a separate anaerobic or amoebic infection and were separately found to have Pneumocystis pneumonia. This pattern is consistent with the model having learned a co-occurrence association (both conditions cluster in immunocompromised/AIDS patients) rather than a genuine pharmacological relationship. The evidence pack's own mechanistic assessment reaches the same conclusion: this is most likely a false-positive prediction driven by data noise rather than a biologically plausible repurposing candidate.

## Clinical Trial Evidence

The search returned 24 registered trials linked to this drug–disease pair. On review, none investigate metronidazole for pneumocystosis — they are unrelated primary care, health-services, or care-delivery studies picked up through data-linkage noise. A representative sample:

| Trial Number | Phase | Status | Enrolment | Relevance Assessment |
|---------|------|------|------|---------|
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | N/A | Completed | 65 | Grade C — head and neck cancer survivorship care tool; unrelated to drug or disease |
| [NCT01909076](https://clinicaltrials.gov/study/NCT01909076) | N/A | Completed | 53 | Grade C — opioid risk reduction in primary care; unrelated |
| [NCT03466866](https://clinicaltrials.gov/study/NCT03466866) | Phase 3 | Completed | 156 | Grade C — diabetes emergency-visit education programme; unrelated |
| [NCT05892666](https://clinicaltrials.gov/study/NCT05892666) | N/A | Recruiting | 4000 | Grade C — comparison of ambulatory care settings; unrelated |

No further trials are listed, as the remainder carry the same "not relevant" pattern. **No clinical trial evaluating metronidazole for pneumocystosis exists in this evidence pack.**

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Lists metronidazole for amoebic colitis and trichomoniasis; Pneumocystis pneumonia is separately attributed to trimethoprim-sulfamethoxazole, not metronidazole |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Reviews antiprotozoal pharmacokinetics and dosing rationale; no data on Pneumocystis |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | Overview of HIV-related opportunistic infections including PCP; does not discuss metronidazole as therapy |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Reviews treatment of AIDS-related infections, listing PCP and amoebic disease as separate entities with separate drug regimens |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | General review of antiparasitic agents; does not address Pneumocystis specifically |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | Am Rev Respir Dis | Patient later diagnosed with PCP had previously received metronidazole for an unrelated diarrhoeal illness — coincidental comorbidity, not evidence of PCP treatment |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Report | Kansenshogaku Zasshi | AIDS patient treated with metronidazole for amoebic dysentery/liver abscess later separately developed PCP — again comorbidity, not a treatment link |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | J Formos Med Assoc | AIDS patient with amoebic colitis (metronidazole-treated) and separate CMV colitis; PCP not part of the clinical picture |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | General critique of antimicrobial prophylaxis trials; not specific to metronidazole or Pneumocystis |

**No publication demonstrates or even directly investigates metronidazole efficacy against Pneumocystis jirovecii.**

## UK Market Information

No marketing authorisation records were returned in this evidence pack (0 licences; market status recorded as "not marketed"). This is inconsistent with metronidazole's status as a long-established, widely prescribed generic antimicrobial in UK clinical practice — the gap most likely reflects incomplete data capture in this evidence pack rather than genuine absence from the market. Please verify current licence status directly via the MHRA product register or BNF before making any regulatory assumptions.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN score (99.99%), no clinical trial or publication provides direct or even indirect evidence that metronidazole treats pneumocystosis, and the drug's known mechanism (anaerobic/protozoal nitroreductase activation) does not extend to *Pneumocystis jirovecii*. The supporting literature reflects comorbidity in immunocompromised patients rather than a pharmacological effect — this is a high-confidence-score but low-plausibility prediction.

**To proceed, the following is needed:**
- Independent in vitro/in vivo evidence of metronidazole activity against *Pneumocystis jirovecii*, if such a hypothesis is to be pursued at all
- Formal MOA documentation from DrugBank/SmPC
- Confirmed UK marketing authorisation and safety/DDI data
- Reassessment of whether the TxGNN signal reflects a genuine biological relationship or a knowledge-graph artefact from shared comorbidity edges (HIV/AIDS-associated infections)

**Note on other candidates in this evidence pack:** among the 10 predictions reviewed, rank 9 (**cap polyposis**, L4, decision stage S2, "Research Question") has the most direct supporting evidence — a mechanistic case series specifically asking whether metronidazole works via anti-inflammatory rather than antibacterial action — and may warrant closer follow-up ahead of pneumocystosis. Rank 3 (ulcerative proctosigmoiditis) and rank 10 (vulvar ulceration, via cutaneous amoebiasis) also carry plausible mechanistic links, albeit with thinner evidence, and are flagged as "Research Question" rather than "Hold."
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

