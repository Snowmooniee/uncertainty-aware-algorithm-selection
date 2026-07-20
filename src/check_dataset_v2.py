import pickle
import numpy as np
from collections import Counter

with open("../data/knapsack_dataset_v2.pkl", "rb") as f:
    dataset = pickle.load(f)

print("Number of instances:", len(dataset))

# correlation distribution
correlations = [item["correlation"] for item in dataset]
print("\nCorrelation distribution:")
print(Counter(correlations))

# n_items distribution
n_items_list = [len(item["weights"]) for item in dataset]
print("\nN_items distribution:")
print(Counter(n_items_list))

# capacity ratio
capacity_ratios = [item["capacity"] / np.sum(item["weights"]) for item in dataset]
print("\nCapacity ratio:")
print("Min:", np.min(capacity_ratios))
print("Max:", np.max(capacity_ratios))
print("Mean:", np.mean(capacity_ratios))

# show first instance
print("\nFirst instance:")
print(dataset[0])