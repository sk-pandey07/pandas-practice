import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Marks": [85, 90, 78, 88, 67],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Delhi"]
}
df = pd.DataFrame(data)

grouped = df.groupby("City")["Marks"].mean()

print("Average Marks by City:\n")
print(grouped)
