from generate_instances import generate_knapsack_instance

import pickle
import os

def create_dataset(n_instances=100):
    instances = []

    correlations = ["uncorrelated", "weak", "strong"]

    for i in range(n_instances):
        correlation = correlations[i % 3]
        instance = generate_knapsack_instance(n_items=50, correlation=correlation, seed=i)
        instances.append(instance)

    os.makedirs("../data", exist_ok=True)

    with open("../data/knapsack_dataset.pkl", "wb") as f:
        pickle.dump(instances, f)

if __name__ == "__main__":
    create_dataset()
    print("Dataset creation completed!")