import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load the data
    data = pd.read_csv("Practical10/dalys-rate-from-all-causes.csv")
    
    # data overview
    print(f"First 10 rows:\n{data.head(10)}")
    print(f"\nColumns 3 and 4:\n{data.columns[2:4]}")
    
    # data info
    print(f"\nData Info:\n{data.info()}")
    
    # descriptive statistics
    print(f"\nDescriptive Statistics:\n{data.describe()}")
    
    # specific values
    print(f"\nSpecific Values:\n{data.iloc[0:3, [0, 1, 3]]}")  # First row
    