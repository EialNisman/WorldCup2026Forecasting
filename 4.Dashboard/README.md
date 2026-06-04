# World Cup Dashboard Preview

This is a self-contained prototype for a World Cup 2026 forecasting dashboard.

## Front-end Flow

- Show group cards first.
- Click a group-stage match to open projections.
- Users can choose home win, draw, away win, or a specific exact score.
- Group tables update from selected scorelines using points, goals for, goals against, and goal difference.
- When all group results are selected, the app creates the knockout bracket.
- Knockout rounds are single-result picks through the final.

## Projection Data Contract

Export your Python model output as JSON with a `matches` array:

```json
{
  "matches": [
    {
      "team1_name": "Mexico",
      "team2_name": "South Africa",
      "winteam1_prob": 0.64,
      "tie_prob": 0.22,
      "winteam2_prob": 0.14,
      "top_scores": [
        { "score": "0-0", "team1_goals": 0, "team2_goals": 0, "probability": 0.071 },
        { "score": "1-0", "team1_goals": 1, "team2_goals": 0, "probability": 0.118 },
        { "score": "1-1", "team1_goals": 1, "team2_goals": 1, "probability": 0.104 }
      ]
    }
  ]
}
```

The front end indexes pairings by normalized team names and handles reversed order automatically. If the fixture is `South Africa` vs `Mexico` but your dataset row is `Mexico` vs `South Africa`, the UI swaps win probabilities and scorelines.

The dashboard automatically tries to load these files in order:

`./wc2026_predictions.json`, `./data/wc2026_predictions.json`, then `./projections.json`.

Open the dashboard through a local server for JSON loading. Direct `file://` pages often block `fetch`.
