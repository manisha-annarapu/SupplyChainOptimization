import pandas as pd

def load_warehouses():
    return pd.read_csv("data/warehouses.csv")

def load_retailers():
    return pd.read_csv("data/retailers.csv")

def load_transportation_costs():
    return pd.read_csv("data/transportation_costs.csv")