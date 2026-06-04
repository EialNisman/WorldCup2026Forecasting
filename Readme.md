# WC2026Forecast

WC2026Forecast is an R and Python project that forecasts the 2026 FIFA World Cup using Poisson regression, Maximum Likelihood Estimation (MLE), and Monte Carlo simulation.

The project estimates probability distributions for:

* Goals scored
* Match outcomes (Win / Draw / Loss)
* Exact scorelines
* Team advancement through the tournament

The objective is not simply to predict winners, but to estimate complete probability distributions that can be used to simulate matches, knockout rounds, and entire tournaments.

---

## Live Demo

View the forecasting dashboard here:

**[WC2026Forecast Dashboard](https://eialnisman.github.io/WorldCup2026Forecasting/4.Dashboard/)**

---

## Statistical Methods

The project explores and applies:

* Maximum Likelihood Estimation (MLE)
* Poisson Generalized Linear Models (GLMs)
* Monte Carlo Simulation
* Regression Modeling
* Model Selection and Validation
* Historical Backtesting
* Probability Calibration

---

## Project Structure

```text
WC2026Forecast
│
├── README.md
│
├── 1.DataCleaning-R/
│   ├── Data/
│   │   ├── RDS/
│   │   ├── JSON/
│   │   └── CSV/ 🤖
│   │
│   ├── WC2026dataCleaning/ 🤖🤖 ⭐
│   └── TrainingDataCleaning/ 🤖🤖 ⭐
│
├── 2.Model_selection-R/
│   ├── Backtest.ipynb 🤖 ⭐⭐⭐
│   ├── FinalDS.ipynb 🤖🤖 ⭐
│   ├── GameConditions.ipynb 🤖 ⭐⭐⭐
│   ├── TeamStrength.ipynb 🤖 ⭐⭐⭐
│   └── WCExperience.ipynb 🤖 ⭐⭐⭐
│
├── 3.SimulationStudy-Python/
│   ├── 2026Prediction.ipynb 🤖🤖🤖 ⭐
│   ├── Class.py 🤖🤖 ⭐⭐
│   ├── PredictPerformances.ipynb 🤖🤖🤖 ⭐
│   ├── VegasTestGroupStage.ipynb 🤖 ⭐⭐⭐
│   └── PredictPerformance.json
│
└── 4.Dashboard/
    ├── data/
    ├── index.html 🤖🤖🤖 ⭐⭐
    ├── team_forecasts.json
    └── wc2026_predictions.json
```

---

## AI Usage Disclosure

This project was developed using a combination of independent programming and AI-assisted development.

Robot indicators estimate the level of AI involvement in each file:

### 🤖🤖🤖

Agentic AI generated most of the initial implementation. My role was primarily reviewing, validating, debugging, and modifying the output.

### 🤖🤖

Shared contribution. I designed the workflow and implemented substantial portions of the code while using AI for specific functions, debugging, and automation.

### 🤖

Primarily self-written. AI was used mainly for troubleshooting, brainstorming, workflow automation, HTML assistance, and occasional code suggestions.

This is especially true in the model selection notebooks, where I deliberately avoided selecting variables solely because they were suggested by AI and instead evaluated them through independent and rigorous statistical testing.

---

## Reading Guide

Stars indicate how useful a section may be to readers interested in the statistical and modeling aspects of the project.

### ⭐

Primarily data cleaning and production of JSON datasets used by the dashboard backend.

These sections contain less statistical insight but may be useful for understanding:

* Data structures
* Feature engineering
* Data pipelines
* Workflow design

### ⭐⭐

Important for understanding the overall workflow of the project.

Topics include:

* Simulation studies
* Stress testing
* Forecast generation
* Model deployment

These sections tend to be more code-heavy.

### ⭐⭐⭐

The most statistically interesting notebooks in the project.

These sections focus on:

* Model selection
* Assumption testing
* Variable evaluation
* Historical backtesting
* Comparisons against betting markets

Several notebooks also contain "Math Checks," where I document statistical concepts and mathematical reasoning that motivated modeling decisions.

---

## Data Sources

The project combines data from multiple sources to build and evaluate forecasting models.

### World Football Elo Ratings

https://eloratings.net/2026

### The Fjelstul World Cup Database

Fjelstul, Joshua C. (2023).

* *The Fjelstul World Cup Database v1.2.0*
* https://github.com/jfjelstul/worldcup

R package citation:

* Joshua C. Fjelstul (2023). *worldcup: The Fjelstul World Cup Database*. R package version 1.2.0.

### Transfermarkt Data (via Kaggle)

https://www.kaggle.com/datasets/davidcariboo/player-scores

---

## Model Performance (At Time of Publication)

### Poisson GLM

* Out-of-sample Log Loss: **1.407290**
* Log Likelihood: **-712.200**
* Training Sample: **510 observations**

### Group Stage Match Simulation Backtest

Historical World Cup matches were simulated using model-generated probability distributions.

Results:

* Average probability assigned to the actual match result: **35.96%**
* Average probability assigned to the actual scoreline: **7.79%**
* Average increase in probability assigned to the actual result relative to bookmaker consensus: **+0.00298**
* Average increase in probability assigned to the actual scoreline relative to bookmaker consensus: **+0.00079**

These comparisons should be interpreted as exploratory diagnostics rather than claims of market outperformance.

---

## Reproducibility Notes

Some notebooks contain external downloads, web scraping, or API-style enrichment.

To avoid unnecessary processing and external dependencies:

* Prefer the saved RDS, CSV, and JSON artifacts when exploring model ideas.
* Separate one-time data acquisition from repeatable cleaning and modeling steps.
* Avoid rerunning large acquisition pipelines unless necessary.

Large local files such as Kaggle downloads and virtual environments should remain outside version control. The project's `.gitignore` is configured accordingly.

---

## Author

**Eial Nisman**
Statistics & Economics Student
North Carolina State University

📧 [eiunisman@gmail.com](mailto:eiunisman@gmail.com)

💼 [www.linkedin.com/in/eialnisman](http://www.linkedin.com/in/eialnisman)

Feel free to reach out if you have questions about the project, methodology, data sources, or forecasting approach.
