import pandas as pd
df = pd.DataFrame({
"name":["A","B","C","B","D","A"],
"marks":[70,80,90,80,60,70]
})

print("Original DataFrame:\n")
print(df)

duplicates = df[df.duplicated()]

print("\nDuplicate Rows:\n")
print(duplicates)

df_clean = df.drop_duplicates()

print("\nDataFrame After Removing Duplicates:\n")
print(df_clean)
