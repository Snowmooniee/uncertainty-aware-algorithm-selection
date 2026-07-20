import numpy as np


def generate_knapsack_instance(
        n_items=50,
        correlation="uncorrelated",
        capacity_ratio=0.5,
        seed=None
):
    if seed is not None:
        np.random.seed(seed)


    weights = np.random.randint(1, 100, size=n_items)
    if correlation == "uncorrelated":
        profits = np.random.randint(1, 100, size=n_items)
    elif correlation == "weak":
        profits = weights + np.random.randint(1, 50, size=n_items)
    elif correlation == "strong":
        profits = 2*weights + np.random.randint(1, 20, size=n_items)
    elif correlation == "inverse":
        profits = 100 - weights + np.random.randint(1, 20, size=n_items)
        profits = np.maximum(profits, 1)  # Ensure profits are positive
    else:
        raise ValueError("Invalid correlation type. Choose from 'uncorrelated', 'weak', or 'strong'.")

    capacity = int(capacity_ratio * np.sum(weights))
    return {
        "weights": weights,
        "profits": profits,
        "capacity": capacity,
        "correlation": correlation
    }

if __name__ == "__main__":
    instance = generate_knapsack_instance(n_items=10, correlation="inverse", capacity_ratio = 0.3, seed=42)
    print(instance)