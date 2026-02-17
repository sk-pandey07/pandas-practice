import pandas as pd
data = {
    "Name": ["Rahul","Ankit","Priya","Sneha","Aman",
             "Rohit","Kajal","Vikas","Neha","Arjun",
             "Pooja","Sumit","Riya","Karan","Meena"],
    
    "Age": [21,22,20,21,23,
            22,21,20,22,23,
            21,24,20,22,23],
    
    "Marks": [85,78,92,74,88,
              90,67,81,95,76,
              89,72,84,91,79],
    
    "City": ["Delhi","Lucknow","Mumbai","Delhi","Kolkata",
             "Noida","Patna","Mumbai","Delhi","Jaipur",
             "Kolkata","Delhi","Noida","Patna","Mumbai"],
    
    "Course": ["BCA","BCA","BBA","BCA","BBA",
               "BCA","BBA","BCA","BBA","BCA",
               "BCA","BBA","BCA","BBA","BCA"]
}

df = pd.DataFrame(data)
print(df)

print("\nprint first 6 rows")
print(df.head(6))

print("\nprint last 6 rows")
print(df.tail(6))

print("\nshape")
print(df.shape)
