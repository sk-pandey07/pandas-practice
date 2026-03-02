import pandas as pd
data = {
    "ID": range(1, 16),
    "Name": ["Aman", "Riya", "Shyam", "Neha", "Rahul",
             "Priya", "Karan", "Sneha", "Vikas", "Anjali",
             "Rohit", "Pooja", "Arjun", "Meera", "Sahil"],
    
    "Age": [20, 19, 21, 20, 22,
            19, 21, 20, 23, 22,
            21, 20, 19, 22, 23],
    
    "Maths": [85, 78, 90, 88, 76,
              95, 67, 80, 72, 89,
              91, 73, 84, 77, 69],
    
    "English": [75, 82, 88, 79, 85,
                90, 70, 76, 80, 87,
                92, 74, 81, 78, 73],
    
    "Computer": [92, 85, 94, 90, 88,
                 96, 72, 84, 79, 91,
                 95, 77, 89, 83, 75]
}
df = pd.DataFrame(data)
print(df)

# add column bonus
df["Bonus"] = 5
print(df)

# add new column total marks
df["Total_marks"] = df["Marks"] + df["Bonus"]
print(df)

# add pass column
df["Pass"] = df["Marks"] >= 40
print(df)
