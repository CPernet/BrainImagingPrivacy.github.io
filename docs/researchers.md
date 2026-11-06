+++
title = "Responsible research, informed decisions."
nav_label = "Researchers"
kicker = "For researchers & imaging professionals"
description = "Assess the information in images, recordings and metadata together, then choose safeguards that preserve the science."
updated = "6 November 2026"
+++
## Key messages

- **Assess the complete release.** Imaging content, participant metadata and the information available elsewhere can contribute different routes to identification.
- **Distinguish matching from naming.** Recognising the same brain across scans does not, by itself, reveal a participant's real-world identity.
- **Use metrics to inform judgement.** A distinctive record or an outlying privacy score calls for investigation; neither is a calibrated probability of re-identification. [1, 2](#sources)

## What kind of identification is possible?

| Question | Example | What it establishes |
| --- | --- | --- |
| Can someone recover an identity? | Matching an MRI-derived face to an identity-linked photograph | A possible route from research data to a known person |
| Can records be distinguished or matched? | Matching a participant's connectivity patterns across sessions | Individual specificity, which may enable linkage but does not automatically reveal an identity |
| Can sensitive information be learned? | Inferring a diagnosis when everyone in a known participant's subgroup has that diagnosis | Attribute disclosure, even without selecting one exact row |

The working consensus manuscript separates re-identification from the individual specificity it operationalises as “singling out.” This technical use is broader than the legal question of whether a person is identifiable in a particular context. [2](#sources)

## Imaging representation matters

Full-head structural MRI and CT can retain facial features. Published work has demonstrated matching MRI-derived facial reconstructions to photographs, making facial information a concrete concern before release. This does not establish one universal attack-success rate for every dataset. [3](#sources)

The working manuscript also considers defaced and skull-stripped images, tissue and morphometric maps, PET outputs, electrophysiology and connectivity matrices. These retain different information. Defacing targets facial features; it does not necessarily remove individual-specific brain patterns. Functional-connectome studies demonstrate matching across sessions, a different task from naming a previously unknown person. [2, 4](#sources)

For PET, the working manuscript highlights tracer uptake, scanner resolution and reconstruction as relevant considerations. A modality label alone is therefore an incomplete description of a proposed release. [2](#sources)

## What the metadata paper found

Kibsgaard and colleagues assessed participant metadata from selected OpenNeuro datasets using metaprivBIDS. Eight datasets were screened; six were presented as worked examples after two requiring changes were addressed. The researchers assessed potential vulnerabilities and **did not attempt to re-identify participants**. [1](#sources)

Demographic combinations, including age, visible characteristics and information related to location, deserved particular attention. Clinical scores were not major drivers of re-identifiability in these analyses. That finding does not make clinical information non-sensitive: a demographic match can expose a diagnosis or questionnaire response. Nor is this selected sample a prevalence estimate for all OpenNeuro data. [1](#sources)

## What metaprivBIDS measures

metaprivBIDS assesses tabular metadata, including BIDS `participants.tsv` files and their JSON descriptions. It does not assess facial recognisability or image-based matching. [1](#sources)

| Metric | What it helps inspect |
| --- | --- |
| k-anonymity | How many records share each combination of selected quasi-identifiers |
| l-diversity | Diversity of sensitive values within those groups |
| k-global | A variable's contribution to uniqueness relative to the other selected variables |
| SUDA | Records made unique by small combinations of attributes |
| PIF | Information gain associated with values and their relationships to other variables |

The paper found that these measures provide complementary information. Outliers can flag harmless distinctions as well as plausible vulnerabilities, and the absence of an outlier does not complete an assessment. Variable meaning, sampling and possible external information still matter. [1](#sources)

## A practical assessment workflow

The following workflow synthesises the published metadata findings and the working manuscript; it is an editorial aid rather than a validated certification procedure.

1. **Inventory the release:** images, recordings, derivatives, headers, filenames, tables and accompanying documentation.
2. **Describe realistic scenarios:** who might obtain the data, what they might already know and which external information could support a match.
3. **Inspect metadata combinations:** select plausible quasi-identifiers, use complementary metrics and investigate flagged cases with someone who understands the study.
4. **Test proportionate changes:** consider coarser age resolution, broader categories or suitable noise where justified. Recheck both privacy indicators and the analyses the data must support. Adding noise alone is not evidence of a differential-privacy guarantee.
5. **Document access and reassessment:** record the remaining assumptions, safeguards, scientific trade-offs and evidence that would prompt another review. [1, 2](#sources)

## Scope and limitations

The manuscript's imaging assessment concerns data without visually noticeable skull or brain abnormalities and assumes direct identifiers and annotations have been removed. Its conclusions do not transfer automatically to unusual lesions, rare conditions or identifying metadata. Its rating scales are ordinal expert judgements: a score of four out of five is not an 80% attack probability. Final numerical ratings are not reproduced on this page while the manuscript is being revised. [2](#sources)

## Sources

1. **Published evidence:** Kibsgaard et al. (2026), [*Assessing metadata privacy in neuroimaging*](https://doi.org/10.1162/IMAG.a.1144). [Analysis notebooks](https://github.com/CPernet/OpenNeuro_MetaPrivAssessment) · [metaprivBIDS](https://github.com/CPernet/metaprivBIDS).
2. **Work in progress:** Pernet et al., *An expert consensus on identification likelihood in NeuroImaging data*. Working manuscript consulted 6 November 2026; unpublished and subject to revision. [Associated analysis](https://github.com/CPernet/BrainImagingPrivacy.github.io/tree/main/papers/expert-ratings).
3. Steeg et al. (2024), [*Re-identification of anonymised MRI head images with publicly available software*](https://doi.org/10.1016/j.eclinm.2024.102930).
4. Finn et al. (2015), [*Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity*](https://doi.org/10.1038/nn.4135).
