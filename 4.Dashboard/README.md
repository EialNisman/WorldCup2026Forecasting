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

Export your Python model output as JSON with one row per team pairing:

```json
[
  {
    "team_a": "Mexico",
    "team_b": "South Africa",
    "win_a": 0.64,
    "draw": 0.22,
    "win_b": 0.14,
    "score_probs": [
      { "score_a": 0, "score_b": 0, "prob": 0.071 },
      { "score_a": 1, "score_b": 0, "prob": 0.118 },
      { "score_a": 1, "score_b": 1, "prob": 0.104 }
    ]
  }
]
```

The front end indexes pairings by normalized team names and handles reversed order automatically. If the fixture is `South Africa` vs `Mexico` but your dataset row is `Mexico` vs `South Africa`, the UI swaps win probabilities and scorelines.

To wire this in, serve `projections.json` next to the dashboard and call:

```js
loadProjectionJson("./projections.json");
```

For a real app, put groups/fixtures/projections behind API routes or static JSON files, then use the same shape in React/Vue/Svelte.
