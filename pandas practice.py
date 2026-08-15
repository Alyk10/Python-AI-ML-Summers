import pandas as pd
gym = pd.Series(['incline', 'decline', 'flat', 'incline', 'decline'])
print(gym)

data = {
    'Subject': ['Eng', 'Math'],
    'Cr': ['2', '3'],
    'Grade': ['A', 'B']
}
df = pd.DataFrame(data)

print(df)
print(type(gym))
print(type(data))


