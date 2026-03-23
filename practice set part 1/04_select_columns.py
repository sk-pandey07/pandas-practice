import pandas as pd

data = {
    "Student_ID": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["Amit","Neha","Ravi","Pooja","Ankit","Sneha","Rahul","Simran","Karan","Divya"],
    "Age": [20,21,19,20,22,21,20,19,22,20],
    "Gender": ["M","F","M","F","M","F","M","F","M","F"],
    "Math_Score": [78,88,67,90,55,76,82,91,60,85],
    "Science_Score": [85,79,72,91,60,84,78,89,65,87],
    "Attendance": [92,95,88,97,80,90,93,96,85,94]
}

df = pd.DataFrame(data)
print(df)

subset = df[["Name" , "Age"]]
print("\nsubset with Name & Age")
print(subset)
