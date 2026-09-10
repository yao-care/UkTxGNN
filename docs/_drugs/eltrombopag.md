---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 1
---

# Eltrombopag
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Eltrombopag: From Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is a thrombopoietin receptor agonist (TPO-RA) used to raise platelet counts in patients with thrombocytopenia, including thrombocytopenia occurring alongside chronic HCV infection and HIV-associated immune thrombocytopenia. The TxGNN model predicts it may be effective for **HIV infectious disease** itself, with a prediction score of **99.26%**, but the underlying evidence base (5 clinical trials, 10 publications) is dominated by studies of platelet management rather than direct anti-HIV activity. Current evidence level is **L4**, reflecting mechanism/preclinical-only support for a true HIV-treatment indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocytopenia (including HCV-related and immune thrombocytopenia) — inferred from trial context; formal indication data not available |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally documented for this drug (Data Gap). Based on the evidence collected, eltrombopag is known to act as a **thrombopoietin receptor agonist (TPO-RA)**, stimulating the c-Mpl receptor on megakaryocytes to promote platelet production. It has no established antiviral mechanism.

The clinical and literature evidence overwhelmingly relates to using eltrombopag to **manage thrombocytopenia in patients who happen to have HCV or HIV infection** — for example, enabling patients to tolerate interferon/ribavirin therapy, or treating HIV-associated immune thrombocytopenic purpura (ITP) after optimised antiretroviral therapy. This is fundamentally different from treating the HIV infection itself, and none of the five registered trials target HIV viral suppression as an endpoint.

The one mechanistic thread suggesting direct relevance to HIV is a single in vitro high-throughput screening study (PMID 32977702), which identified eltrombopag as a possible modulator of HIV-1 proviral transcription. This is a preliminary screening signal only, with no confirmatory cell, animal, or clinical data. The very high TxGNN score (99.26%) likely reflects the knowledge graph's dense "drug–thrombocytopenia–HIV comorbidity" connectivity rather than genuine antiviral evidence, and should be interpreted with caution.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Rollover safety/tolerability study of eltrombopag in HCV-related thrombocytopenia enabling antiviral therapy initiation; not HIV-specific (relevance grade C) |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | Efficacy/safety of eltrombopag in thrombocytopenic patients with chronic hepatitis C and compensated cirrhosis; not HIV-specific (relevance grade C) |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | Large RCT assessing eltrombopag to maintain platelet counts for HCV antiviral therapy (Peg-IFN alfa-2a + ribavirin); measured sustained virological response for HCV, not HIV (relevance grade C) |
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | Companion RCT with Peg-IFN alfa-2b + ribavirin, same HCV thrombocytopenia population; not HIV-directed (relevance grade C) |
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Eltrombopag to reduce platelet transfusion need in chronic liver disease patients undergoing invasive procedures; terminated, not HIV-directed (relevance grade C) |

*Note: none of the above trials were designed to evaluate eltrombopag as a treatment for HIV infection; all relate to thrombocytopenia management in patients with HCV or chronic liver disease.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematology/Oncology Clinics of North America | Chronic HCV, HIV and H. pylori infections can cause secondary immune thrombocytopenia; treating the underlying infection often improves platelet counts |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Seminars in Hematology | Overview of therapeutic strategies for infection-related immune thrombocytopenia, including HCV and HIV |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Review | Internal Medicine Journal | TPO receptor agonists in immune thrombocytopenia of less than 6 months' duration |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | Review/In vitro screening | Viruses | High-throughput screen of FDA-approved drugs identifying eltrombopag as a possible modulator of HIV-1 proviral transcription; preliminary, unconfirmed in vivo |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Cohort | Platelets | Danish cohort on TPO-receptor agonist use in refractory ITP, including some HIV-related and secondary cases |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case report | AIDS (London) | Successful use of eltrombopag without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case series | Journal of the International Association of Providers of AIDS Care | Initial experience with TPO-receptor agonists (eltrombopag, romiplostim) in refractory HIV-associated ITP |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case report | AIDS (London) | Successful treatment of HIV-associated aplastic anaemia with eltrombopag, suggesting an immunomodulatory role |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case report | Farmacia Hospitalaria | Two case reports of eltrombopag for thrombocytopenia in chronic hepatitis C (not HIV) |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case report | JCPSP | Hepatitis B-related megaloblastic anaemia and severe thrombocytopenia; low relevance (not HIV or eltrombopag treatment) |

## UK Market Information

Eltrombopag is currently **not marketed** under this evidence pack's regulatory data source, with no marketing authorisations recorded.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base predominantly supports eltrombopag's established role in managing thrombocytopenia (including as a complication of HIV infection or its treatment), not in treating HIV infection itself. The only direct mechanistic link to antiviral activity comes from a single unconfirmed in vitro screening study, and no clinical trial has evaluated HIV virological or immunological endpoints. The TxGNN score is likely inflated by shared graph connections between thrombocytopenia, HCV, and HIV rather than genuine repurposing evidence.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for eltrombopag (currently a blocking/high-severity data gap)
- SmPC/product label warnings and contraindications (currently unavailable — blocking gap for safety assessment)
- Preclinical or in vivo validation of the HIV-1 proviral transcription modulation signal (PMID 32977702) before further clinical consideration
- Clear distinction in future evidence collection between "treating HIV-associated thrombocytopenia" and "treating HIV infection" as separate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

