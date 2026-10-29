---
layout: default
title: UkTxGNN - UK Drug Repurposing Predictions
---

# UkTxGNN

Drug repurposing predictions for the United Kingdom using the TxGNN graph neural network.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## United Kingdom: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed in the registration data of [MHRA](https://www.gov.uk/mhra) (United Kingdom).

Reports by evidence level: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Salmeterol](/drugs/salmeterol/) | L1 |
| [Tiotropium](/drugs/tiotropium/) | L1 |
| [Tizanidine](/drugs/tizanidine/) | L1 |
| [Letrozole](/drugs/letrozole/) | L1 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Fenbufen](/drugs/fenbufen/) | L1 |
| [Indoramin](/drugs/indoramin/) | L3 |
| [Methysergide](/drugs/methysergide/) | L3 |
| [Pirenzepine](/drugs/pirenzepine/) | L3 |
| [Diethylstilbestrol](/drugs/diethylstilbestrol/) | L4 |
| [Sulfapyridine](/drugs/sulfapyridine/) | L5 |
| [Sulfinpyrazone](/drugs/sulfinpyrazone/) | L5 |
| [Dihydrotachysterol](/drugs/dihydrotachysterol/) | L5 |
| [Oxandrolone](/drugs/oxandrolone/) | L5 |
| [Gamolenic Acid](/drugs/gamolenic-acid/) | L5 |
| [Meptazinol](/drugs/meptazinol/) | L5 |
| [Cholesterol](/drugs/cholesterol/) | N/A |
| [Ethanolamine Oleate](/drugs/ethanolamine-oleate/) | N/A |
| [Etilefrine](/drugs/etilefrine/) | N/A |
| [Metipranolol](/drugs/metipranolol/) | N/A |

<!-- local-home:end -->

## Overview

UkTxGNN uses graph neural networks to identify potential new therapeutic uses for existing drugs authorised by the UK Medicines and Healthcare products Regulatory Agency (MHRA).

## Data Sources

- **Drug Data**: MHRA PARD (Pharmaceutical and Regulatory Database)
- **Knowledge Graph**: TxGNN biomedical knowledge graph
- **Clinical Trials**: ClinicalTrials.gov, EU Clinical Trials Register, ISRCTN
- **Literature**: PubMed, Google Scholar
- **Guidelines**: NICE (National Institute for Health and Care Excellence)

## API Access

### FHIR R4 API

Access prediction data via FHIR R4 resources:

- **Base URL**: `https://uktxgnn.yao.care/fhir`
- **Capability Statement**: [/fhir/metadata](/fhir/metadata.json)

#### Available Resources

| Resource Type | Description |
|--------------|-------------|
| MedicationKnowledge | Drug information from MHRA |
| ClinicalUseDefinition | Predicted drug-disease indications |

## Disclaimer

**Research Use Only**: The predictions provided by UkTxGNN are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.

This is not an MHRA-approved tool. Always consult healthcare professionals and refer to NICE guidelines for medical decisions.

## Contact

- Website: [yao.care](https://yao.care)
- GitHub: [yao-care/UkTxGNN](https://github.com/yao-care/UkTxGNN)

---

*Last updated: {{ site.time | date: "%Y-%m-%d" }}*

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

UkTxGNN is the the United Kingdom site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, deep-learning prediction that excludes uses already recorded in the knowledge graph, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
