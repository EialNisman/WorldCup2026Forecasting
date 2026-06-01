# WC2026Forecast

WC2026Forecast is an R notebook project for building a 2026 FIFA World Cup forecasting model. The current work is strongest on feature construction: historical match outcomes, team strength, player/roster information, awards, manager experience, travel distance, weather, and early model exploration.

## Project Structure

- `0.Project_Index.ipynb` - project table of contents and recommended notebook order.
- `1.DataCleaning-R/` - notebooks that create model inputs and save reusable RDS/CSV artifacts.
- `1.DataCleaning-R/Data/RDS/` - saved intermediate datasets used across notebooks.
- `1.DataCleaning-R/Data/CSV/` - inspection-friendly source/intermediate CSV files.
- `2.Model_Selection-R/` - exploratory modeling and relationship checks.

## Suggested Notebook Order

1. `1.DataCleaning-R/WorldCups.ipynb`
2. `1.DataCleaning-R/Rosters.ipynb`
3. `1.DataCleaning-R/ELOScores.ipynb`
4. `1.DataCleaning-R/Kaggle-Fjelstul.ipynb`
5. `1.DataCleaning-R/PlayerStats.ipynb`
6. `1.DataCleaning-R/PlayerSeasonStats.ipynb`
7. `1.DataCleaning-R/Awards.ipynb`
8. `1.DataCleaning-R/Managers.ipynb`
9. `1.DataCleaning-R/DistanceFromHome.ipynb`
10. `1.DataCleaning-R/Weather.ipynb`
11. `2.Model_Selection-R/ExploringRelations.ipynb`

## Current Feature Themes

- Match results and rest days from the Fjelstul World Cup database via the `worldcup` R package.
- Team quality signals from ELO start ratings.
- Player/team roster information and player matching work.
- Awards-based player quality features.
- Manager prior World Cup experience, built carefully to avoid forward leakage.
- Distance from home and weather context for match conditions.

## Reproducibility Notes

Some notebooks include external downloads, scraping, or API-style enrichment. Do not rerun those cells casually. Prefer using the saved RDS/CSV artifacts when exploring model ideas, and clearly separate one-time data acquisition from repeatable cleaning/modeling steps.

Large local data such as Kaggle downloads and virtual environments should stay out of git. The existing `.gitignore` already points in that direction.

## Author

Eial Nisman - Statistics and Economics student at NC State University.

- Email: eiunisman@gmail.com
- LinkedIn: www.linkedin.com/in/eialnisman
