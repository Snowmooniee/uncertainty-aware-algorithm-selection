import pickle

with open("../data/knapsack_dataset.pkl", "rb") as f:
    dataset = pickle.load(f)

print("Number of instances:", len(dataset))

print("\nFirst instance:")
print(dataset[0])

print("\nCorrelation distribution:")

count = {}

for item in dataset:
    c = item["correlation"]
    count[c] = count.get(c, 0) + 1

print(count)