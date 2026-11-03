---
layout: default
title: Data Sources
nav_order: 93
permalink: /sources/
description: "Data sources behind UkTxGNN: the NHSBSA BNF code list, TxGNN, ClinicalTrials.gov, PubMed and DrugBank."
---

# Data Sources

<div class="key-takeaway">
Every conclusion traces back to a public data source — nothing is a black box.
</div>

---

## Source overview

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Source</th><th>Used for</th></tr>
</thead>
<tbody>
<tr><td>Local medicine list</td><td><a href="https://opendata.nhsbsa.net/">NHSBSA</a></td><td>BNF presentation codes: medicines in current NHS prescribing use and their ingredients</td></tr>
<tr><td>Prediction model</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Drug&ndash;disease association prediction</td></tr>
<tr><td>Clinical trials</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidence grading (NCT)</td></tr>
<tr><td>Literature</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidence grading (PMID)</td></tr>
<tr><td>Drug information</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Ingredient mapping and target data</td></tr>
<tr><td>Interactions</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Drug&ndash;drug interaction data</td></tr>
</tbody>
</table>

---

## United Kingdom medicine data

| Item | Detail |
|------|--------|
| Dataset | BNF code information, current year (latest monthly `BNF_CODE_CURRENT_<YYYYMM>` CSV) |
| Publisher | NHS Business Services Authority (NHSBSA) open data portal |
| Download | `https://opendata.nhsbsa.net/api/3/action/package_show?id=bnf-code-information-current-year` (dataset record; the latest CSV resource is used) |
| Nature of the data | Prescribing presentation codes, not a licence register: MHRA licence status is not included |
| Update | Downloaded again every Monday by an automated workflow; listing status in drug reports is updated from the new file |

---

## Licensing

Each source has its own licence — please check before citing:

- **TxGNN**: academic use; cite Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: US NIH public data
- **DrugBank**: non-commercial use subject to its licence terms
- **NHSBSA BNF code information**: published by the NHS Business Services Authority; check its terms of use before reuse

---

## Update frequency

| Data | Frequency |
|------|-----------|
| NHSBSA BNF code list | Weekly (every Monday, automated) |
| Trial / literature evidence | Re-collected periodically |
| Interaction data | Reviewed quarterly |

---

## Academic citation

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
