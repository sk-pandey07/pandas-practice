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
