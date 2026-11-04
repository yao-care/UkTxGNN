---
layout: default
title: UkTxGNN - UK Drug Repurposing Predictions
description: "TxGNN drug repurposing reports for 583 medicines in the NHSBSA BNF code information (UK), with evidence levels L1–L5 from clinical trials and literature."
last_modified_at: 2026-11-04
---

# UkTxGNN

Drug repurposing predictions for the United Kingdom using the TxGNN graph neural network.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## United Kingdom: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines in the [NHSBSA BNF code information](https://opendata.nhsbsa.net/) (United Kingdom).

### United Kingdom medicine data

| Item | Detail |
|------|--------|
| Dataset | BNF code information, current year (latest monthly `BNF_CODE_CURRENT_<YYYYMM>` CSV) |
| Publisher | NHS Business Services Authority (NHSBSA) open data portal |
| Download | `https://opendata.nhsbsa.net/api/3/action/package_show?id=bnf-code-information-current-year` (dataset record; the latest CSV resource is used) |
| Nature of the data | Prescribing presentation codes, not a licence register: MHRA licence status is not included |
| Update | Downloaded again every Monday by an automated workflow; listing status in drug reports is updated from the new file |

Details: [Data Sources]({{ '/sources/' | relative_url }}).

Reports by evidence level:

| Evidence level | Reports | Share |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

54 predicted drug–disease pairs on this site appear on no other of the 30 TxGNN sites.

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Dapsone](/drugs/dapsone/) | L1 |
| [Ketamine](/drugs/ketamine/) | L1 |
| [Bupropion](/drugs/bupropion/) | L2 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Pirenzepine](/drugs/pirenzepine/) | L3 |
| [Diethylstilbestrol](/drugs/diethylstilbestrol/) | L4 |
| [Sulfapyridine](/drugs/sulfapyridine/) | L5 |
| [Sulfinpyrazone](/drugs/sulfinpyrazone/) | L5 |
| [Indoramin](/drugs/indoramin/) | L5 |
| [Dihydrotachysterol](/drugs/dihydrotachysterol/) | L5 |
| [Methysergide](/drugs/methysergide/) | L5 |
| [Oxandrolone](/drugs/oxandrolone/) | L5 |
| [Gamolenic Acid](/drugs/gamolenic-acid/) | L5 |
| [Meptazinol](/drugs/meptazinol/) | L5 |
| [Cholesterol](/drugs/cholesterol/) | N/A |
| [Ethanolamine Oleate](/drugs/ethanolamine-oleate/) | N/A |
| [Etilefrine](/drugs/etilefrine/) | N/A |
| [Fenbufen](/drugs/fenbufen/) | N/A |
| [Metipranolol](/drugs/metipranolol/) | N/A |

<!-- local-home:end -->

## Overview

UkTxGNN uses graph neural networks to identify potential new therapeutic uses for existing drugs authorised by the UK Medicines and Healthcare products Regulatory Agency (MHRA).

## Data Sources

- **Drug Data**: [NHSBSA BNF code information](https://opendata.nhsbsa.net/) (BNF presentation codes)
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
| MedicationKnowledge | Drug information from the NHSBSA BNF code information |
| ClinicalUseDefinition | Predicted drug-disease indications |

## Disclaimer

**Research Use Only**: The predictions provided by UkTxGNN are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.

This is not an MHRA-approved tool. Always consult healthcare professionals and refer to NICE guidelines for medical decisions.

## Contact

- Website: [yao.care](https://yao.care)
- GitHub: [yao-care/UkTxGNN](https://github.com/yao-care/UkTxGNN)

---

*Last updated: {{ page.last_modified_at | date: "%Y-%m-%d" }}*

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.
