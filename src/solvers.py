import numpy as np
import time

def greedy_solver(instance):
    weights = instance["weights"]
    profits = instance["profits"]
    capacity = instance["capacity"]

    start_time = time.perf_counter()

    retio = profits / weights

    order = np.argsort(retio)[::-1]

    total_profit = 0
    total_weight = 0

    for i in order:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_profit += profits[i]

    runtime = time.perf_counter() - start_time

    return {
        "profit": total_profit,
        "weight": total_weight,
        "runtime": runtime
    }

def dp_solver(instance):
    weights = instance["weights"]
    profits = instance["profits"]
    capacity = instance["capacity"]

    start_time = time.perf_counter()

    dp = np.zeros(capacity + 1)

    for w, p in zip(weights, profits):
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + p)

    runtime = time.perf_counter() - start_time

    return {
        "profit": int(max(dp)),
        "weight": None,
        "runtime": runtime
    }

if __name__ == "__main__":
    from generate_instances import generate_knapsack_instance

    instance = generate_knapsack_instance(n_items=50, correlation="strong", seed=42)

    greedy_result = greedy_solver(instance)
    dp_result = dp_solver(instance)

    print("Greedy Solver Result:", greedy_result)
    print("Dynamic Programming Solver Result:", dp_result)