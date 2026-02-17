import pandas as pd
data = [10,20,30,40,50]
s = pd.Series(data, index=['a','b','c','d','e']

print("\nseries:",s)

print("\nmax value:",s.max())
print("\nmin value:",s.min())
print('\nmean value:",s.mean())
