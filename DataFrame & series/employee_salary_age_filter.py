import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit", "Kajal", "Vikas", "Sneha"],
    "Age": [25, 28, 24, 27, 30, 26, 29, 23],
    "Salary": [45000, 52000, 48000, 50000, 60000, 47000, 55000, 43000],
    "Performance_Scor-e": [8.5, 7.2, 9.1, 6.8, 8.0, 7.5, 8.7, 6.9]
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"] > 50000]
print("\nEmpoloye with salary > 50000")
print(high_salary)

#filtering rows salary > 50000 and age > 25
filtered = df[(df["Salary"] > 50000) & (df["Age"] > 25)]
print("\nEmpolye list Age > 25 & Salary > 50000")
print(filtered)
