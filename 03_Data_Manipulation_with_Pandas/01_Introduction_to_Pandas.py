# WHAT IS PANDAS?
# Pandas is a Python library focused on data analysis and manipulation.

# IMPORTING PANDAS

import pandas as pd

print("Installed Pandas version:", pd.__version__)

# Practical example: creating a small table in memory

data = {
    "name": ["Ana", "Bruno", "Carlos"],
    "age": [25, 30, 22],
    "city": ["SP", "RJ", "MG"],
}

df = pd.DataFrame(data)

print("\nSmall example DataFrame:")
print(df)