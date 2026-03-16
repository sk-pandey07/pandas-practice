import pandas as pd

df = pd.DataFrame({
"name":["A","B","C","D","E"],
"marks":[78,90,67,90,85]
})

second = df["marks"].nlargest(2).iloc[-1]

student = df[df["marks"] == second]["name"]

print("Second Highest Marks:", second)
print("Student Name:", list(student))
