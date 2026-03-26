# UkTxGNN - United Kingdom Drug Repurposing Predictions

Drug repurposing predictions for the United Kingdom using TxGNN knowledge graph.

## Overview

UkTxGNN uses graph neural networks to identify potential new therapeutic uses for existing drugs registered with the UK Medicines and Healthcare products Regulatory Agency (MHRA).

## Data Sources

- **Drug Data**: MHRA PARD (Pharmaceutical and Regulatory Database)
- **Knowledge Graph**: TxGNN biomedical knowledge graph
- **Clinical Trials**: ClinicalTrials.gov, EU Clinical Trials Register, ISRCTN
- **Literature**: PubMed, Google Scholar

## Installation

```bash
# Install dependencies
uv sync

# Prepare TxGNN data
uv run python scripts/prepare_external_data.py

# Run KG predictions (requires MHRA data)
uv run python scripts/run_kg_prediction.py
```

## Data Acquisition

MHRA drug data must be obtained from:
- MHRA Products Database: https://products.mhra.gov.uk/
- PARD Data: Contact MHRA for bulk access

## API Access

### FHIR R4 API

- **Base URL**: `https://uktxgnn.yao.care/fhir`
- **Capability Statement**: [/fhir/metadata](/fhir/metadata.json)

## Disclaimer

**Research Use Only**: Predictions are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation.

This is not an MHRA-approved tool.

## License

MIT License

## Contact

- Website: [yao.care](https://yao.care)
- GitHub: [yao-care/UkTxGNN](https://github.com/yao-care/UkTxGNN)
