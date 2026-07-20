import numpy as np

def extract_features(instance):
    weights = instance["weights"]
    profits = instance["profits"]
    capacity = instance["capacity"]

    n_items = len(weights)
    capacity_ratio = capacity / np.sum(weights)

    mean_weight = np.mean(weights)
    std_weight = np.std(weights)

    mean_profit = np.mean(profits)
    std_profit = np.std(profits)

    ratios = profits / weights
    mean_ratio = np.mean(ratios)
    std_ratio = np.std(ratios)

    return {
        "n_items": n_items,
        "capacity_ratio": capacity_ratio,
        "mean_weight": mean_weight,
        "std_weight": std_weight,
        "mean_profit": mean_profit,
        "std_profit": std_profit,
        "mean_ratio": mean_ratio,
        "std_ratio": std_ratio,
        "correlation": instance["correlation"]
    }

if __name__ == "__main__":
    from generate_instances import generate_knapsack_instance

    instance = generate_knapsack_instance(n_items=50, correlation="strong", seed=42)
    features = extract_features(instance)
    print(features)