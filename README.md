# TMDB movie database

This project is to analyse the TMDB movie dataset which contains data of around _11,000_ movies. Here we have analyse the depending factors of a successful movie and all other relationships between depending factors.

## Getting Started:
### Files:
```
├── data
|   |
│   └── tmdb-movies.csv           // dataset
├── pkg
    |
    └── analysis_fn.py            // python module for the necessary functions
├── TMDB_data_analysis.ipynb      // jupyter notebook used for analysis
├── TMDB_data_analysis.html       // html format of jupyter notebook used for analysis
├── environment.yml               // The dependencies we need to create environment
├── README.md
└── LICENSE
````

### Setup:
To create environment with necessary python libraries for this analysis run the following command
```
conda env create -f environment.yml
```

This project is based on `tmdb-movies.csv` file which contains all the details about 11K movies. One can open this project in `Jupyter Notebook` using terminal or command promt typing the following command in the project directory
```
jupyter notebook TMDB_analysis.ipynb
```



### License:
This project is under _MIT License_ see more in [LICENSE]()
