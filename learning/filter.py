import pandas as pd

df = pd.read_csv('Exercise Files/Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', '?']

print(df.loc[(df['City'] == 'Riverside') & (df['First'] == 'John')])
