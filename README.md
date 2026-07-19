# Learning-Based Algorithm Selection for 0-1 Knapsack Problems under Distribution Shift


## Overview

This project investigates learning-based per-instance algorithm selection for combinatorial optimization problems.

The main research question is:

> Can machine learning models learn the relationship between optimization problem characteristics and solver performance, and automatically recommend the most suitable algorithm for each problem instance?

The current focus is the classical **0-1 Knapsack Problem**, where different algorithms exhibit different trade-offs between solution quality and computational efficiency.


---

## Motivation

Combinatorial optimization problems often have multiple available algorithms:

- Exact algorithms provide optimal solutions but may become computationally expensive.
- Heuristic algorithms are efficient but may produce suboptimal solutions.

Therefore, instead of selecting a single solver for all instances, this project explores **per-instance algorithm selection**, where the algorithm choice is determined according to the characteristics of individual problem instances.


---

## Research Framework

The current research pipeline follows:

Knapsack Instance Generation
        ↓
Solver Portfolio
(Greedy / Dynamic Programming)
        ↓
Performance Evaluation
        ↓
Instance Feature Extraction
        ↓
Machine Learning Based Algorithm Selection
        ↓
Evaluation under Distribution Shift



---

## Current Progress

The following components have been implemented:

### 1. Reproducible Experimental Environment

- Python virtual environment
- Dependency management through requirements.txt


### 2. Knapsack Benchmark Generation

Implemented a configurable instance generator for:

- item weights
- item profits
- capacity constraints
- different correlation structures


### 3. Solver Portfolio

Implemented:

- Greedy heuristic algorithm
- Dynamic Programming exact algorithm


### 4. Solver Evaluation Pipeline

The framework automatically evaluates:

- solution quality
- optimality gap
- computational runtime


### 5. Instance Feature Extraction

Extracted problem-level features including:

- number of items
- capacity ratio
- weight statistics
- profit statistics
- profit-to-weight ratio statistics


---

## Project Structure

uncertainty-aware-algorithm-selection
│
├── src/
│   ├── generate_instances.py
│   ├── create_dataset.py
│   ├── solvers.py
│   ├── evaluate_solvers.py
│   └── features.py
│
├── data/
│
├── results/
│
├── requirements.txt
│
└── README.md



---

## Future Work

The next stages of this project include:


### Machine Learning Based Solver Selection

Develop classification models to predict the most suitable solver based on instance features.

Potential models:

- Logistic Regression
- Random Forest
- XGBoost


### Distribution Shift Evaluation

Investigate model robustness when testing on problem distributions different from training data.


### Uncertainty-Aware Algorithm Selection

Explore uncertainty estimation techniques to identify cases where the model is uncertain about solver recommendations.


---

## Research Direction

This project aims to combine:

- Combinatorial Optimization
- Machine Learning
- Algorithm Selection
- Uncertainty Estimation

towards developing adaptive optimization systems that can automatically select suitable algorithms according to problem characteristics.