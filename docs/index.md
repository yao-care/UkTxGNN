---
layout: default
title: UkTxGNN - UK Drug Repurposing Predictions
---

# UkTxGNN

Drug repurposing predictions for the United Kingdom using TxGNN knowledge graph.

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
model, covering national drug-registration data integration, dual knowledge-graph and
deep-learning prediction, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
