import pandas as pd
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Arjun", "Neha",
             "Vikash", "Pooja", "Karan", "Anjali",
             "Rohan", "Meera", "Saurabh", "Kavita", "Deepak"],
    
    "Age": [24, 28, 26, 30, 27, 25,
            29, 31, 23, 27,
            32, 26, 28, 29, 24],

    "Department": ["IT","HR","IT","Finance","IT","HR","Finance","IT",
                   "Marketing","Sales","IT","HR","Finance","Marketing","Operations"],
    
    "Salary": [30000, 45000, 40000, 52000, 38000, 36000,
               47000, 55000, 28000, 42000,
               60000, 39000, 46000, 48000, 31000],
    
    "Performance": [78, 85, 88, 92, 75, 81,
                    89, 95, 70, 84,
                    91, 83, 87, 90, 76]
}

df = pd.DataFrame(data)
print(df)

print("\nfirst five rows:")
print(df.head(5))

print("\nlast five rows")
print(df.tail(5))

print("\nDataset info")


print(df.info())

print("\nDescribe dataset")
print(df.describe())

print("\nName and salary print both")
print(df[["Name" , "Salary"]])
print("shape:",df.shape)

print("\nprint only Name column data:")
print(df["Name"])

print("\nsalary > 50000 data")
columns = df[df["Salary"] > 50000]
print(columns)
