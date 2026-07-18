import numpy as np


def generate_knapsack_instance(
        n_items=50,
        correlation="uncorrelated",
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
    else:
        raise ValueError("Invalid correlation type. Choose from 'uncorrelated', 'weak', or 'strong'.")

    capacity = int(0.5 * np.sum(weights))
    return {
        "weights": weights,
        "profits": profits,
        "capacity": capacity,
        "correlation": correlation
    }

if __name__ == "__main__":
    instance = generate_knapsack_instance(n_items=10, correlation="strong", seed=42)
    print(instance)