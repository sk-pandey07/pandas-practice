import pandas as pd
data = {
    "Employee_ID": [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],
    "Name": ["Amit","Rahul","Sneha","Priya","Arjun",
             "Neha","Vikash","Pooja","Karan","Anjali",
             "Rohan","Meera","Saurabh","Kavita","Deepak"],
    
    "Age": [24,28,26,30,27,25,29,23,31,27,26,24,28,29,32],
    
    "Department": ["IT","HR","Finance","IT","Marketing",
                   "Finance","HR","IT","Marketing","Finance",
                   "HR","IT","Marketing","Finance","IT"],
    
    "Salary": [45000,38000,50000,60000,42000,
               52000,39000,47000,61000,55000,
               40000,48000,58000,53000,65000],
    
    "Performance_Score": [8,7,9,6,8,
                          9,7,8,6,9,
                          7,8,6,9,10]
}

df = pd.DataFrame(data)
print(df)

df.to_excel("employe.xlsx")
print(df)

df = pd.read_excel("employe.xlsx")
print(df)

print("\nprint only 5 ROWS")
print(df.head(5))

print("\nPrint rows where Age > 25")
print(df[df["Age"] >= 25])


print("\nprint the name column only")
print(df["Name"])

print("\nUse .loc to get row 1 specifically")
print(df.loc[1])

print("\nFilter rows where salary ≥ 50000")
print(df[df["Salary"] >= 50000])

print("\nCount how many performance > 8 using .shape or .count()")
print(df[df["Performance_Score"] > 8]["Performance_Score"].count())

