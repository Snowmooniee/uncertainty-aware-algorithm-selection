from generate_instances import generate_knapsack_instance

import pickle
import os
import numpy as np
np.random.seed(42)  # For reproducibility

def create_dataset(n_instances=500):
    instances = []

    correlations = ["uncorrelated", "weak", "strong", "inverse"]

    for i in range(n_instances):
        correlation = np.random.choice(correlations)

        n_items = np.random.choice([50, 100, 200], p = [0.5, 0.35, 0.15])  # Adjusted probabilities for n_items
        capacity_ratio = np.random.uniform(0.1, 0.9)  
        instance = generate_knapsack_instance(n_items=n_items, correlation=correlation, capacity_ratio=capacity_ratio, seed=i)
        instances.append(instance)

    os.makedirs("../data", exist_ok=True)

    with open("../data/knapsack_dataset_v2.pkl", "wb") as f:
        pickle.dump(instances, f)

if __name__ == "__main__":
    create_dataset()
    print("Dataset creation completed!")