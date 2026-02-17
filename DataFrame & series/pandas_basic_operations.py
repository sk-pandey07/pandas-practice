import pandas as pd
student = {
    "name" : ['sam','tom','stark','ram','shyam'],
    "age" : [21,22,21,20,20],
    "marks" : [88,87,78,98,92],
    "city" : ['mumbai','delhi','mumbai','patna','noida']
}

df = pd.DataFrame(student)

print("head")
print(df.head())

print("tail")
print(df.tail())

print("shape")
print(df.shape)
