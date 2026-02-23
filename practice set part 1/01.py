import pandas as pd
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Arjun",
             "Neha", "Vikash", "Pooja", "Karan", "Anjali",
             "Rohan", "Meera", "Saurabh", "Kavita", "Deepak"],
    
    "Age": [24, 28, 26, 30, 27,
            25, 29, 23, 31, 26,
            28, 24, 27, 29, 32],
    
    "Department": ["HR", "IT", "Finance", "Marketing", "IT",
                   "HR", "Finance", "IT", "Marketing", "HR",
                   "IT", "Finance", "Marketing", "HR", "IT"],
    
    "Salary": [30000, 45000, 40000, 50000, 47000,
               32000, 42000, 38000, 52000, 35000,
               46000, 39000, 48000, 36000, 55000],
    
    "Performance_Score": [7, 8, 9, 6, 8,
                          7, 9, 6, 8, 7,
                          9, 6, 8, 7, 9]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df["Salary"] * 0.10
print(df)

conditions = [
    df["Performance_Score"] >= 8,
    df["Performance_Score"] == 7
]
choices = ["Excellent", "Good"]

df["Result"] = np.select(conditions, choices, default="Average")
print(df)

average_salary = df["Salary"].mean()
print("Average Salary:", average_salary)

max_score = df["Performance_Score"].max()
print("Maximum Performance Score:", max_score)
