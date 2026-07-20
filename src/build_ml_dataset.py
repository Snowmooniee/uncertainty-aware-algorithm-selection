import pandas as pd
import pickle
from features import extract_features

def build_dataset(lambda_runtime = 1000):
    with open("../data/knapsack_dataset.pkl", "rb") as f:
        instances = pickle.load(f)

    solver_df = pd.read_csv("../results/solver_results.csv")

    rows = []

    for i, instance in enumerate(instances):
        features = extract_features(instance)
        result = solver_df.iloc[i]

        greedy_score = (result["greedy_profit"] - lambda_runtime * result["greedy_time"])
        dp_score = (result["dp_profit"] - lambda_runtime * result["dp_time"])

        if greedy_score > dp_score:
            best_algorithm = "greedy"
        else:
            best_algorithm = "dp"

        features["best_algorithm"] = best_algorithm
        rows.append(features)

    df = pd.DataFrame(rows)
    df.to_csv("../results/algorithm_selection_dataset.csv", index=False)

if __name__ == "__main__":
    build_dataset()
    print("ML dataset creation completed!")