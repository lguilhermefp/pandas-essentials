import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Exercise Files/Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

wanted_values = df[['First', 'Last', 'State']]
stored = wanted_values.to_excel('State_Location.xlsx', index=None)
