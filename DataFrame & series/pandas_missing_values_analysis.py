import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha"],
    "Age": [21, np.nan, 20, 22],
    "Marks": [85, 55, None, 90]
}
df = pd.DataFrame(data)
print(df)

print("\nInfo:")
df.info()

print("\nMissing Values Count:")
print(df.isnull().sum())
