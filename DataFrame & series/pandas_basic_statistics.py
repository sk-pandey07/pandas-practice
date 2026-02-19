import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Marks": [85, 90, 78, 88, 67]
}
df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Total Students:", df["Name"].count())
