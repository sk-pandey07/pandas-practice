import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit", "Kajal", "Vikas", "Sneha"],
    "Age": [25, 28, 24, 27, 30, 26, 29, 23],
    "Salary": [45000, 52000, 48000, 50000, 60000, 47000, 55000, 43000],
    "Performance_Scor-e": [8.5, 7.2, 9.1, 6.8, 8.0, 7.5, 8.7, 6.9]
}

df = pd.DataFrame(data)

print("\nsample DataFrame")
print(df)

print("names (single column return series)")
# print(df["Name"])
name = df["Name"]
print(name)

# selecting multiple columns
subset = df[["Name" , "Age"]]
print("\nsubset with name and age")
print(subset)
