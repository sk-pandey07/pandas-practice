import pandas as pd
data = {
    "Roll": [1, 2, 3, 4],
    "Name": ["Aman", "Priya", "Rahul", "Neha"],
    "Marks": [75, 88, 90, 60]
}

df = pd.DataFrame(data)

print("Columns:", df.columns)
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
