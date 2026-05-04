---
layout: default
title: Cefadroxil
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Cefadroxil
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

# Cefadroxil: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefadroxil is a first-generation cephalosporin antibiotic with established use in treating bacterial infections including urinary tract infections, skin and soft tissue infections, and pharyngotonsillitis.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction rests entirely on model inference, and the available mechanistic rationale raises significant biological plausibility concerns.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (UTI, skin/soft tissue infections, pharyngotonsillitis) — based on established pharmacological class; no UK marketing authorisation on record |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on established pharmacology, cefadroxil is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), thereby disrupting peptidoglycan cross-linking in susceptible Gram-positive and some Gram-negative organisms. It is bactericidal against a broad range of common pathogens responsible for superficial infections.

Hyperamylasemia is not itself a disease but a biochemical finding — elevated serum amylase — arising secondarily from conditions such as acute pancreatitis, parotid gland disease, renal impairment, or macroamylasaemia. There is no pharmacological mechanism by which beta-lactam antibiotics could regulate amylase secretion, reduce pancreatic inflammation at its root cause, or accelerate amylase clearance.

**A critical safety counter-indication exists:** cephalosporins, including first-generation agents, are recognised as rare causes of drug-induced pancreatitis, which would itself raise serum amylase. Rather than constituting a therapeutic target, hyperamylasemia may represent a potential adverse effect signal for this drug class. The TxGNN score of 98.60% reflects a high model confidence, but this does not correlate with clinical plausibility in this instance; the prediction most likely reflects indirect network associations within the knowledge graph rather than a genuine therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Cefadroxil currently holds no marketing authorisations with the MHRA and is not listed as a marketed product in the United Kingdom. It is not included in BNF current editions as an available preparation. Clinicians wishing to use it would need to consider a Specials licence or unlicensed import route under MHRA guidance.

---

## Safety Considerations

> Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme (https://yellowcard.mhra.gov.uk/).

**Note for prescribers:** Although full safety data is unavailable in this evidence pack, the following class-effect concerns are pertinent to cefadroxil as a first-generation cephalosporin and are directly relevant to the predicted indication:

- **Drug-induced hyperamylasemia / pancreatitis**: Cephalosporins are recognised as a rare cause of drug-induced pancreatitis. Use of cefadroxil in a patient already presenting with hyperamylasemia could confound the clinical picture or cause harm.
- **Drug-induced immune haemolytic anaemia**: Cephalosporins, including cefadroxil, can induce a positive direct Coombs test via drug–antibody mechanisms; this is relevant to monitoring in susceptible patients.
- **CNS toxicity**: At high doses, first-generation cephalosporins carry a risk of neurotoxicity; renal dose adjustment is required.
- **Cross-reactivity with penicillins**: Patients with documented penicillin hypersensitivity require careful risk assessment before cephalosporin administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns hyperamylasemia a high prediction score, but mechanistic analysis reveals no pharmacological basis for cefadroxil to treat this biochemical abnormality; moreover, the drug's drug class is implicated as a potential *cause* of elevated amylase through drug-induced pancreatitis. There is no supporting clinical trial or published literature evidence (L5). Proceeding with this indication would carry safety risk without a credible therapeutic hypothesis.

**To proceed, the following would be needed:**
- A biologically plausible mechanistic hypothesis explaining how a beta-lactam antibiotic could therapeutically lower serum amylase — none is currently apparent
- Completion of a formal MHRA marketing authorisation application if UK commercialisation is sought, given the drug's current unlicensed status
- Full SmPC-level safety data including MHRA-required warnings, contraindications, and interaction profile (currently absent from this evidence pack)
- Clarification of whether the TxGNN prediction reflects a direct drug–disease relationship or an indirect knowledge graph artefact (e.g., association via a shared bacterial infection node)
- If the broader predicted indication list is under review, rank 9 (Gonococcal Urethritis, L4) represents the only candidate with any indirect supporting literature and a plausible beta-lactam mechanism — though antimicrobial resistance trends and the availability of established agents (ceftriaxone) substantially limit its repurposing value

---

> **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require full clinical validation before any therapeutic application. All content should be interpreted in conjunction with current MHRA guidance, BNF recommendations, and approved SmPC documentation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

