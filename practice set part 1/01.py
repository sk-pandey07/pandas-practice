import pandas as pd

data = {
    "Order_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "Customer_Name": ["Rahul","Aman","Priya","Neha","Rohit","Kajal","Vikas","Sneha","Arjun","Meena"],
    "City": ["Delhi","Mumbai","Delhi","Jaipur","Mumbai","Delhi","Jaipur","Mumbai","Delhi","Jaipur"],
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop"],
    "Quantity": [1,2,1,3,2,4,1,2,3,1],
    "Price": [60000,20000,30000,60000,20000,30000,60000,20000,30000,60000]
}

df = pd.DataFrame(data)
print(df)

total_orders = len(df)
print(total_orders)

print(df.columns)

print(df.shape)
