import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, 55, 92, 48, 76]
}

df = pd.DataFrame(data)

print("First 5 Rows:")
print(df.head())

print("\nInformation About Data:")
df.info()
