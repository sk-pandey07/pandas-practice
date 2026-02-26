import pandas as pd
data = [10,20,30,40]
s = pd.Series(data,index=['a','b','c','d'])
print(s)

# print second element
print(s[1])

# print index using .iloc , or , .loc
print(s.iloc[1])

# print index using .loc
print(s.loc['b'])
