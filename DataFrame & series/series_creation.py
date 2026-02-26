import pandas as pd
data = [10,20,30,40]
s = pd.Series(data,index=['a','b','c','d'])
print(s)

# print second element
print(s[1])
