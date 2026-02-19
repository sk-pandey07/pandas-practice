import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Marks": [85, 90, 78, 88, 67]
}
df = pd.DataFrame(data)

print("Only Name and Marks:\n")
print(df[["Name", "Marks"]])

print("\nStudents with Marks > 80:\n")
print(df[df["Marks"] > 80])
