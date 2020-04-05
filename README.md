# Visualising COVID-19 data

This repository is designed so you can quickly visualise the latest COVID-19 data. It uses the repo `https://github.com/CSSEGISandData/COVID-19` from Johns Hopkins University for data which is currently being updated daily.

Instructions:
1. Clone the repository, then, from the root directory of the repository:
2. Install submodule `git submodule update --init --recursive`
3. Run setup to create a virtual environment with dependencies `./setup.sh`
4. Activate the virtual environment `source env/bin/activate`
5. Run Jupyter Notebooks `jupyter notebook`
6. Navigate to Notebook `plot_covid_data.ipynb`

To update the data with the latest daily counts
1. Change directory `cd data/COVID-19`
2. Pull the latest version `git pull`
