import pandas as pd
data = {
    "Roll": [1, 2, 3, 4, 5],
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [21, 22, 20, 21, 23],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai"],
    "Marks": [85, 55, 92, 48, 76]
}
df = pd.DataFrame(data)

print("Display the info of dataset")
print(df.info())
