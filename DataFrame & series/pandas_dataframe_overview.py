import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, 55, 92, 48, 76]
}
df = pd.DataFrame(data)

print("Head:\n", df.head())
print("\nTail:\n", df.tail())
print("\nInfo:")
print(df.info())
