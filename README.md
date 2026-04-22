# Machine Learning Internship

This repository contains my solutions to the IT Solutions Machine Learning internship tasks, built on the provided restaurants dataset (`Dataset .csv`, 9,551 restaurants across multiple countries).

## Tasks Completed

| #   | Task                       | Objective                                             |
| --- | -------------------------- | ----------------------------------------------------- |
| 1   | Predict Restaurant Ratings | Regression model to predict `Aggregate rating`        |
| 2   | Restaurant Recommendation  | Content-based filtering system using user preferences |
| 3   | Cuisine Classification     | Multi-class classifier for primary cuisine            |
| 4   | Location-based Analysis    | Geographic distribution, city/locality statistics     |

## Repository Structure

```
Machine-Learning-Internship/
├── Dataset .csv                         # source dataset
├── Machine Learning.pdf                 # task brief
│
├── task1_predict_ratings.py             # Task 1 — regression
├── task1_predict_ratings.ipynb
│
├── task2_recommendation.py              # Task 2 — recommender
├── task2_recommendation.ipynb
│
├── task3_cuisine_classification.py      # Task 3 — classifier
├── task3_cuisine_classification.ipynb
│
├── task4_location_analysis.py           # Task 4 — geo analysis
├── task4_location_analysis.ipynb
├── task4_outputs/                       # plots + aggregated CSVs
│   ├── map_world.png
│   ├── map_india.png
│   ├── top_cities.png
│   ├── rating_vs_count.png
│   ├── city_stats.csv
│   └── locality_stats.csv
│
└── README.md
```

## Requirements

- Python 3.10+
- Packages: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

Install:

```bash
pip install pandas numpy scikit-learn matplotlib
```

## How to Run

Run any script directly:

```bash
python task1_predict_ratings.py
python task2_recommendation.py
python task3_cuisine_classification.py
python task4_location_analysis.py
```

Or open the corresponding `.ipynb` in Jupyter / Google Colab and run the cells top-to-bottom.

## Summary of Results

### Task 1 — Predict Restaurant Ratings

Compared Linear Regression, Decision Tree, and Random Forest.

| Model             | MSE        | RMSE       | MAE        | R²        |
| ----------------- | ---------- | ---------- | ---------- | --------- |
| Linear Regression | 1.5599     | 1.2490     | 1.0429     | 0.315     |
| Decision Tree     | 0.1760     | 0.4195     | 0.2677     | 0.923     |
| **Random Forest** | **0.0860** | **0.2933** | **0.1915** | **0.962** |

**Most influential features:** `Votes` (dominant), geographic coordinates, `Cuisines`, `Average Cost for two`. Leakage columns (`Rating color`, `Rating text`) were dropped as they are derived from the target.

### Task 2 — Restaurant Recommendation

Content-based filtering using TF-IDF over cuisines plus normalized numeric features (price range, cost, rating). Hard filters on city, minimum rating, maximum cost, and online-delivery requirement. Final score: `0.7 × cuisine_similarity + 0.3 × numeric_similarity`.

Tested on four sample user personas — every user received top-5 recommendations where **5/5 matched at least one requested cuisine** and average ratings aligned with the user's stated minimum.

### Task 3 — Cuisine Classification

Multi-class classification on the top-15 primary cuisines (8,023 rows).

| Model               | Accuracy  | Macro F1  | Weighted F1 |
| ------------------- | --------- | --------- | ----------- |
| Logistic Regression | 0.118     | 0.120     | 0.085       |
| **Random Forest**   | **0.393** | **0.211** | **0.334**   |

Accuracy is ~6× random baseline (1/15 = 6.7%). Main challenge: severe class imbalance — North Indian represents 37% of samples, and most misclassifications default to it. Available features are mostly geographic/operational rather than culinary, creating a hard ceiling on performance.

### Task 4 — Location-based Analysis

- **91% of restaurants are in India** (country code 1), with 83% concentrated in the NCR (New Delhi, Gurgaon, Noida, Faridabad).
- Non-NCR cities have exactly 20–21 entries each — a sampling cap, not a real count.
- Premium dining clusters in recognizable hubs: Hauz Khas Village, Khan Market, Connaught Place (Delhi); Cyber Hub, Sector 29 (Gurgaon).
- **North Indian** dominates as the top cuisine in almost every Indian city; notable exceptions: Goa (Seafood), Mumbai (Italian), Ahmedabad (Continental).
- 79% of restaurants fall in price ranges 1–2 — budget-skewed distribution.

## Preprocessing Notes (applied consistently across tasks)

- Numeric missing values → median
- Categorical missing values → `"Unknown"`
- Identifier / free-text columns dropped (`Restaurant ID`, `Restaurant Name`, `Address`, `Locality Verbose`)
- Leakage columns dropped for Task 1 (`Rating color`, `Rating text` are derived from `Aggregate rating`)
- Rows with coordinates at `(0, 0)` treated as missing in Task 4
- Unrated restaurants (`Aggregate rating == 0`) excluded from rating averages in Task 4

## Tech Stack

Python · pandas · NumPy · scikit-learn · matplotlib
