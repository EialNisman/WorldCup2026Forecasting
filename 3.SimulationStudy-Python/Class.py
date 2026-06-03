import numpy as np
import scipy.stats as stats
import pandas as pd

coefficients = pd.read_csv(
    "/Users/eialnisman/Desktop/WC2026Forecast/2.Model_Selection-R/poisson_model_coefficients.csv"
)

beta = dict(zip(coefficients["term"], coefficients["estimate"]))


class PredictGame:
    
    def __init__(
        self,
        Home,
        Away,
        EloHome,
        EloAway,
        Home_wc_coach,
        Away_wc_coach,
        Home_players_multiple_WCs,
        Away_players_multiple_WCs,
        Home_AVGage,
        Away_AVGage,
        Home_Distance_from_host_km,
        Away_Distance_from_host_km
    ):
        self.Home = Home
        self.Away = Away
        self.EloHome = EloHome
        self.EloAway = EloAway
        self.Home_wc_coach = Home_wc_coach
        self.Away_wc_coach = Away_wc_coach
        self.Home_players_multiple_WCs = Home_players_multiple_WCs
        self.Away_players_multiple_WCs = Away_players_multiple_WCs
        self.Home_AVGage = Home_AVGage
        self.Away_AVGage = Away_AVGage
        self.Home_Distance_from_host_km = Home_Distance_from_host_km
        self.Away_Distance_from_host_km = Away_Distance_from_host_km

    def lambda_home(self):

        eta = (
            37.3527298801595
            + 0.0016896587041524 * (self.EloHome - self.EloAway)
            + 0.0784772845095249 * self.Away_wc_coach
            + 0.0339379668675031 * self.Away_players_multiple_WCs
            + -0.0018567393809189 * (self.Home_AVGage ** 2)
            + -2.66002430745583 * self.Away_AVGage
            + 0.0494388519095898 * (self.Away_AVGage ** 2) 
            + -2.11417818206544e-05 * self.Home_Distance_from_host_km
        )

        return np.exp(eta)

    def lambda_away(self):

        eta = (
            37.3527298801595
            + 0.0016896587041524 * (self.EloAway - self.EloHome)
            + 0.0784772845095249 * self.Home_wc_coach
            + 0.0339379668675031 * self.Home_players_multiple_WCs
            + -0.0018567393809189 * (self.Away_AVGage ** 2)
            + -2.66002430745583 * self.Home_AVGage
            + 0.0494388519095898 * (self.Home_AVGage ** 2) 
            + -2.11417818206544e-05 * self.Away_Distance_from_host_km
        )

        return np.exp(eta)
    
    def SimGame(self, n_sims=1000, seed=2026):

        np.random.seed(seed)

        self.Scores = []

        for i in range(n_sims):

            homegoals = stats.poisson.rvs(mu=self.lambda_home())
            awaygoals = stats.poisson.rvs(mu=self.lambda_away())

            self.Scores.append((homegoals, awaygoals))

        return self.Scores
    
    def WinnerPrediction(self):

        if not hasattr(self, "Scores"):
            self.SimGame()

        homewins = 0
        awaywins = 0
        ties = 0

        for h, a in self.Scores:

            if h > a:
                homewins += 1
            elif a > h:
                awaywins += 1
            else:
                ties += 1

        total = homewins + awaywins + ties

        results = pd.DataFrame({
            "Home": [100 * homewins / total],
            "Away": [100 * awaywins / total],
            "Tie": [100 * ties / total]
        })

        return results
        
    def ScorePredictions(self):

        if not hasattr(self, "Scores"):
            self.SimGame()

        scores = pd.DataFrame(
            self.Scores,
            columns=["HomeGoals", "AwayGoals"]
        )

        results = (
            scores
            .value_counts()
            .reset_index(name="Count")
            .sort_values("Count", ascending=False)
        )

        results["Probability"] = results["Count"] / results["Count"].sum()

        return results