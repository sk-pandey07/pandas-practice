import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Marks": [85, 90, 78, 88, 67]
}
df = pd.DataFrame(data)

print("Ascending Order:\n")
print(df.sort_values(by="Marks"))

print("\nDescending Order:\n")
print(df.sort_values(by="Marks", ascending=False))
