# Identification likelihood in NeuroImaging
Data and analysis supporting expert consensus rating on identification  likelihood in NeuroImaging data.
In this project, experts independently listed data types and evidence of re-identification risk. From those lists, tables of data types were built and used to make a survey. The survey data are analysed here.

## Analysis

The results are from two surveys (data type order counter-balanced) and analysed in the [Jupyter notebook above](ratings_analysis.ipynb).

## Outcomes

- All but one imaging type has data rated from 1 to 5, i.e. even among neuro-imaging experts, there are debates depending on data type. This is also likely due to the large variability in data types, and no one can be an expert in all of them.
- Only Raw MRI/CT data are seen at high risk in any cases, which is easily understandable given that faces can be reconstructed/rendered as images.
- Likelihood of re-identification and singling-out are mildly corrected for data type (~0.5), given that re-identification is possible, so is singling out, but the counterpart is not always true.


## Project status and maintenance

Work in progress; the notebook has not yet been cited in a published paper. Maintainer/contact: Cyril Pernet ([@CPernet](https://github.com/CPernet)). Original notebook and survey CSV files were moved together from the repository root. The original scientific description above is retained; it has not been revised as part of the website work.

## Run the notebook

From this directory, create a Python environment and install `requirements.txt`, then run `jupyter lab ratings_analysis.ipynb`. The notebook locates `data/ratings/` from this folder or the repository root. Its Colab setup clones the repository if the data are not already available.

Only the repository/data-location setup has been adapted for the new folder. The statistical analysis cells and their saved scientific outputs have not been revised. The dependency ranges are an installation starting point, not a reconstruction of the original analysis environment.
