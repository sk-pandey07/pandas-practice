import pandas as pd

df = pd.DataFrame({
"name":["A","B","C","D","E","F"],
"marks":[45,90,67,89,76,92]
})

top_students = df.nlargest(3, "marks")
print(top_students)
