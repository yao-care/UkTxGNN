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
