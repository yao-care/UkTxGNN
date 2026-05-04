---
layout: default
title: Cinchocaine Hcl
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 0
---

# Cinchocaine Hcl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Cinchocaine HCl: Drug Repurposing Evaluation Report

## One-Sentence Summary

Cinchocaine (also known as dibucaine) is a potent, long-acting amide-type local anaesthetic historically used for topical and spinal anaesthesia. No new indications have been predicted by the TxGNN model for this compound, and there are currently **no marketing authorisations** held in the UK. Insufficient data is available to support a repurposing recommendation at this time.

## Quick Overview

| Item | Content |
|------|---------|
| Drug (INN) | Cinchocaine HCl (Dibucaine) |
| Original Indication | Not recorded in this evidence pack |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No model prediction or supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

## Why Was This Drug Evaluated?

Cinchocaine HCl (INN: cinchocaine; also widely known as dibucaine) is an amide-type local anaesthetic. It has historically been used in topical preparations for the relief of pain and pruritus (e.g. haemorrhoidal creams and ointments) and, less commonly, in spinal anaesthesia. It acts by reversibly blocking sodium channels in neuronal membranes, thereby inhibiting the initiation and conduction of nerve impulses.

However, detailed mechanism of action data was not available in the supplied evidence pack, and no DrugBank identifier was resolved for this compound. Without a confirmed DrugBank mapping, the TxGNN knowledge graph pipeline could not generate repurposing predictions. As a result, the predicted indications list is empty and no mechanistic bridging analysis can be performed.

## Clinical Trial Evidence

Currently no related clinical trials registered for a repurposed indication of cinchocaine.

## Literature Evidence

Currently no related literature available linking cinchocaine to a novel repurposed indication.

## UK Market Information

No MHRA marketing authorisations were identified for cinchocaine HCl in this evidence pack. Historically, cinchocaine has been available in the UK as a component of over-the-counter topical preparations (e.g. combination haemorrhoidal products), but no current product licences are recorded here.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).

> **Note:** Key warnings, contraindications, and drug interaction data were not available in the evidence pack. Prescribers should consult the BNF monograph for dibucaine/cinchocaine and the relevant SmPC before considering any clinical use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated for cinchocaine HCl due to the absence of a confirmed DrugBank identifier mapping. Additionally, the drug currently holds no UK marketing authorisations, and critical safety data (warnings, contraindications, drug interactions) remains unavailable. There is insufficient evidence to support any repurposing evaluation at this stage.

**To proceed, the following is needed:**

1. **Resolve DrugBank mapping** — Confirm the DrugBank ID for cinchocaine HCl (likely [DB00527](https://go.drugbank.com/drugs/DB00527) for dibucaine) and re-run the TxGNN knowledge graph prediction pipeline
2. **Obtain mechanism of action data** — Query DrugBank API with the confirmed identifier to retrieve pharmacodynamic and pharmacokinetic profiles
3. **Retrieve safety data** — Source the SmPC or BNF entry for cinchocaine to populate key warnings, contraindications, and interaction profiles
4. **Confirm UK regulatory status** — Verify current MHRA product licence status via the [MHRA Products database](https://products.mhra.gov.uk/) to determine if any authorised products containing cinchocaine remain on the UK market
5. **Re-run evidence collection** — Once the DrugBank mapping is established, execute the ClinicalTrials.gov, PubMed, and ICTRP collectors against any newly predicted indications

---

*This report was generated on 5 April 2026. Results are for research purposes only and do not constitute medical advice. Any drug repurposing candidates require rigorous clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

