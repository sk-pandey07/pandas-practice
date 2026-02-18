import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit",
             "Kajal", "Vikas", "Sneha", "Arjun", "Pooja",
             "Sumit", "Riya", "Karan", "Meena", "Ankit"],
    
    "Age": [21, 22, 20, 21, 23,
            22, 20, 21, 23, 22,
            24, 20, 23, 21, 22],
    
    "Marks": [85, 92, 78, 88, 76,
              95, 67, 90, 72, 81,
              89, 94, 60, 86, 79],
    
    "City": ["Delhi", "Mumbai", "Lucknow", "Jaipur", "Delhi",
             "Mumbai", "Lucknow", "Delhi", "Jaipur", "Mumbai",
             "Delhi", "Lucknow", "Jaipur", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)

# count Delhi student
count_delhi = df[df["City"] == "Delhi"].shape[0]
print("\nDelhi student:",count_delhi)

# below 60 marks students
below_60 = df[df["Marks"] < 60].shape[0]
print("\nBelow 60 marks students:",below_60)

# top 3 students
top3_students = df.sort_values(by="Marks" , ascending=False).head(3)
print("\ntop 3 students:",top3_students)

# city-wise average
city_avg = df.groupby("City")["Marks"].mean()
print("\ncity-wise average:",city_avg)
