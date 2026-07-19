from solvers import greedy_solver, dp_solver

import pickle
import os
import pandas as pd

with open("../data/knapsack_dataset.pkl", "rb") as f:
    dataset = pickle.load(f)

def evaluate_solvers():
    results = []

    for i, instance in enumerate(dataset):
        greedy_result = greedy_solver(instance)
        dp_result = dp_solver(instance)

        gap = (dp_result["profit"] - greedy_result["profit"]) / dp_result["profit"] 

        results.append(
            {
                "id": i,
                "correlation": instance["correlation"],
                "n_items": len(instance["weights"]),
                "capacity": instance["capacity"],
                "greedy_profit": greedy_result["profit"],
                "dp_profit": dp_result["profit"],
                "gap": gap,
                "greedy_time": greedy_result["runtime"],
                "dp_time": dp_result["runtime"]
            }
        )

    os.makedirs("../results", exist_ok=True)

    df = pd.DataFrame(results)
    df.to_csv("../results/solver_results.csv", index=False)

if __name__ == "__main__":
    evaluate_solvers()
    print("Solver evaluation completed!")