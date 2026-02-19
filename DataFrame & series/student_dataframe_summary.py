import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, 90, 78, 88, 67],
    "City": ["Delhi", "Mumbai", "Lucknow", "Jaipur", "Delhi"]
}
df = pd.DataFrame(data)
print("Full DataFrame:\n")
print(df)

print("\nShape of DataFrame:", df.shape)
print("Columns:", df.columns)
