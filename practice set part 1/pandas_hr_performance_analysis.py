import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Arjun",
             "Neha", "Vikash", "Pooja", "Karan", "Anjali"],
    
    "Age": [24, 28, 26, 30, 27,
            25, 29, 23, 31, 26],
    
    "Department": ["HR", "IT", "Finance", "Marketing", "IT",
                   "HR", "Finance", "IT", "Marketing", "HR"],
    
    "Salary": [30000, 45000, 40000, 50000, 47000,
               32000, 42000, 38000, 52000, 35000],
    
    "Performance_Score": [7, 8, 9, 6, 8,
                          7, 9, 6, 8, 7]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:\n")
print(df)

df["Bonus"] = df["Salary"] * 0.10

conditions = [
    df["Performance_Score"] >= 8,
    df["Performance_Score"] == 7
]

choices = ["Excellent", "Good"]

df["Performance_Level"] = np.select(conditions, choices, default="Average")

print("\nDataset After Bonus & Performance Level:\n")
print(df)

high_salary = df[df["Salary"] > 45000]
print("\nHigh Salary Employees (>45000):\n")
print(high_salary)

dept_avg_salary = df.groupby("Department")["Salary"].mean()
print("\nDepartment-wise Average Salary:\n")
print(dept_avg_salary)

top3 = df.nlargest(3, "Performance_Score")
print("\nTop 3 Performers:\n")
print(top3)

df.to_csv("employee_analysis_output.csv", index=False)

print("\nCSV file exported successfully!")

dept_avg_salary = df.groupby("Department")["Salary"].mean()

dept_avg_performance = df.groupby("Department")["Performance_Score"].mean()
print(dept_avg_performance)

dept_avg_salary = df.groupby("Department")["Salary"].mean()
print(dept_avg_salary.sort_values(ascending=False))
