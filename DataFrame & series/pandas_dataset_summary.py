import pandas as pd
data = {
    "Roll": [1, 2, 3, 4, 5],
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai"],
    "Marks": [85, 55, 92, 48, 76]
}
df = pd.DataFrame(data)

print("DataFrame:\n")
print(df)

print("\n--- INFO ---")
df.info()

print("\n--- DESCRIBE ---")
print(df.describe())

print("\n--- COLUMNS ---")
print(df.columns)

print("\n--- SHAPE ---")
print(df.shape)
