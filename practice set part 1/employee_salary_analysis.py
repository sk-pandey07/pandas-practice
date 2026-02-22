import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Arjun",
             "Neha", "Vikash", "Pooja", "Karan", "Anjali",
             "Rohan", "Meera", "Saurabh", "Kavita", "Deepak"],
    
    "Age": [24, 28, 26, 30, 27,
            25, 29, 31, 26, 28,
            27, 32, 29, 30, 26],
    
    "Department": ["IT", "HR", "Finance", "IT", "Marketing",
                   "HR", "IT", "Finance", "Marketing", "IT",
                   "HR", "Finance", "IT", "Marketing", "HR"],
    
    "Salary": [45000, 52000, 48000, 60000, 50000,
               47000, 75000, 68000, 54000, 72000,
               51000, 80000, 62000, 59000, 53000]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset")
print(df)

# Salary ke basis pe descending sort
sorted_values = df.sort_values(by="Salary", ascending=False)

print("\nSalary Descending Order:\n")
print(sorted_values)

# Top 3 highest salary
top3 = df.nlargest(3, "Salary")
print("\nTop 3 Highest Salary")
print(top3)
