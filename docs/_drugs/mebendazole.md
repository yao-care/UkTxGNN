---
layout: default
title: Mebendazole
parent: Moderate Evidence (L3-L4)
nav_order: 357
evidence_level: L3
indication_count: 10
---

# Mebendazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Mebendazole: From Helminthic Infections to Alveolar Echinococcosis

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic, originally used to treat intestinal worm infections (e.g. ascariasis, enterobiasis, trichuriasis).
The evidence pack indicates its established antiparasitic mechanism is also directly relevant to **Alveolar Echinococcosis** (liver infection caused by *Echinococcus multilocularis*),
supported by **1 completed clinical follow-up study** and **20 publications**, most of which are reviews confirming benzimidazoles as the standard chemotherapy for this disease.

> **Note on screening:** TxGNN's highest-scoring prediction in this pack was *acne* (score 99.2%). This has been excluded from the report — the model's own rationale confirms there is no plausible mechanistic link, and the supporting PMID (7072899) actually describes sparganosis, not acne. This is a clear literature mismatch rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (Data Gap); mebendazole is a benzimidazole anthelmintic used for intestinal nematode infections |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 94.20% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal MOA data for mebendazole is marked as a data gap in this pack, but the supporting evidence within the pack itself is consistent: mebendazole is a **benzimidazole anthelmintic** that inhibits β-tubulin polymerisation in parasites, blocking glucose uptake and ultimately killing the organism. This is the same mechanistic class as albendazole.

Alveolar echinococcosis is caused by the larval (metacestode) stage of *Echinococcus multilocularis*, a cestode parasite. Given mebendazole's established antiparasitic action against cestode larvae, its applicability to this disease is mechanistically direct rather than speculative — multiple reviews in the evidence pack describe mebendazole and albendazole as the **only benzimidazoles recommended by WHO** for alveolar echinococcosis chemotherapy, used alone or alongside surgery.

It is worth flagging that this may represent confirmation of an **already-established use** rather than a truly novel repurposing candidate — `original_indications` is empty in this pack (Data Gap DG002), so the system may be re-surfacing a known indication as if it were new. A parallel, comparably-supported signal exists for cystic echinococcosis (*Echinococcus granulosus*, rank 3, L3/S2), which follows the same rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Completed | 50 | Prospective follow-up study (EchinoVISTA) evaluating parasite viability markers and imaging/biological follow-up in hepatic alveolar echinococcosis patients treated with albendazole; supports the clinical management context in which mebendazole is used as an alternative benzimidazole. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Current management of hepatic echinococcosis; surgery remains cornerstone, benzimidazoles used adjunctively |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Review | World J Hepatol | Current status of drug therapy for alveolar echinococcosis |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Benzimidazole chemotherapy (albendazole/mebendazole) is parasitostatic; notes potential for hepatotoxicity with long-term use |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Tropica | Albendazole and mebendazole remain the only licensed anti-echinococcal drugs; no replacement yet available |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Ongoing search for novel therapeutics beyond albendazole/mebendazole for alveolar echinococcosis |
| [19296876](https://pubmed.ncbi.nlm.nih.gov/19296876/) | 2009 | Review | J Helminthol | Benzimidazoles used for CE/AE treatment alone or peri-operatively; not fully parasiticidal in AE |
| [19254162](https://pubmed.ncbi.nlm.nih.gov/19254162/) | 2009 | Review | Expert Rev Anti Infect Ther | Consensus review on benzimidazole use in cystic and alveolar echinococcosis |
| [17631693](https://pubmed.ncbi.nlm.nih.gov/17631693/) | 2007 | Review | Parasitology | Albendazole and mebendazole are current standard chemotherapy for CE/AE |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Comparative Study | J Antimicrob Chemother | Long-term mebendazole/albendazole treatment in 35 AE patients followed ~39 months; outcomes compared between regimens |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | Preclinical/Pharmacokinetic | Eur J Clin Pharmacol | Plasma mebendazole concentrations correlated with reduction in parasite weight in animal and human studies |

---

## UK Market Information

Mebendazole currently has **no recorded UK marketing authorisation** in this evidence pack (market status: not marketed; 0 licences on file). Prescribers should verify current availability via the MHRA product database or specialist/named-patient import routes, as benzimidazole anthelmintics for echinococcosis are typically supplied through specialist tropical/infectious disease services in the UK.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Additionally, one review in the evidence base (PMID 39311470) notes that long-term benzimidazole therapy (as required for alveolar echinococcosis) can cause hepatic dysfunction — this warrants routine liver function monitoring, though it is not formally captured in this pack's safety dataset (DG001, Blocking).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple review articles and one completed observational follow-up study consistently support mebendazole's role, alongside albendazole, as standard benzimidazole chemotherapy for alveolar echinococcosis. However, formal SmPC/BNF safety data is absent (Blocking data gap), and this indication may already be an established rather than genuinely novel use.

**To proceed, the following is needed:**
- SmPC warnings, contraindications and drug interaction data (DG001, Blocking)
- Confirmation of mebendazole's original licensed indication and formal MOA documentation (DG002)
- Clarification of whether alveolar echinococcosis is already covered under existing anthelmintic labelling, rather than being a new repurposing candidate
- Confirmation of UK supply/import pathway given current "not marketed" status
- Liver function monitoring protocol for long-term benzimidazole use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

