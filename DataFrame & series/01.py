import pandas as pd
data = {
    "Name": ["Aman", "Ria", "Shyam"],
    "Age": [21, 19, 23],
    "Score": [88, 92, 77]
}

df = pd.DataFrame(data)
print(df)
# display first two rows
print(df.head(2))

# print(df["Name"])

print(df[["Name"]])

print("\nage > 20")
print(df[df["Age"] > 20])
