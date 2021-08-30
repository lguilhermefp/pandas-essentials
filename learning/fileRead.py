import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('Exercise Files/regions.xlsx')
df_csv = pd.read_csv('Exercise Files/Names.csv', header=None)
df_txt = pd.read_csv('Exercise Files/data.txt', delimiter='\t')

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', '?']

df_csv.to_excel('modified.xlsx')
