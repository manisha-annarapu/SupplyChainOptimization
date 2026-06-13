from pulp import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Problem Setup
prob = LpProblem("Supply_Chain_Optimization", LpMinimize)

warehouses = ['W1', 'W2', 'W3']
retailers = ['R1', 'R2', 'R3', 'R4']

costs = np.array([
    [4, 6, 8, 9],
    [5, 4, 7, 8],
    [6, 5, 4, 6]
])

supply = [1000, 1200, 800]
demand = [600, 800, 700, 600]

x = [[LpVariable(f"x_{i}_{j}", lowBound=0)
      for j in range(len(retailers))]
     for i in range(len(warehouses))]

prob += lpSum([
    costs[i][j] * x[i][j]
    for i in range(len(warehouses))
    for j in range(len(retailers))
])

for i in range(len(warehouses)):
    prob += lpSum([x[i][j] for j in range(len(retailers))]) == supply[i]

for j in range(len(retailers)):
    prob += lpSum([x[i][j] for i in range(len(warehouses))]) == demand[j]

prob.solve(PULP_CBC_CMD(msg=0))

solution = np.array([
    [value(x[i][j]) for j in range(len(retailers))]
    for i in range(len(warehouses))
])

print(f"Status: {LpStatus[prob.status]}")
print(f"Minimum Total Cost: ${value(prob.objective):.2f}")
print("\nOptimal Distribution Plan:")
print(pd.DataFrame(solution, index=warehouses, columns=retailers))