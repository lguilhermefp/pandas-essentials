import io
import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('investigados.csv', sep=';', index_col=[0])

columns = list(df.columns)
partidos = columns[0:len(columns)-2]

emptyColumns = [col for col in df.columns if df[col].isnull().all()]
df.drop(emptyColumns,
        axis=1,
        inplace=True)

for partido in partidos:
	df[partido] = df[partido].str.replace(',', '.')
	df[partido] = df[partido].astype(float)

df.dropna(
    axis=0,
    inplace=True
)

sumColumn = len(partidos)+1
df.loc[sumColumn] = df.sum()
df.rename({sumColumn: "Soma"}, axis=0, inplace=True)

df["Soma"] = df.sum(axis=1)

columns = [*partidos, 'Soma']

for column in columns:
	df[column] = df[column].apply(lambda x: "${:.2f}".format(x))
	df[column] = df[column].astype(str)
	df[column] = df[column].str.replace('.', ',')

df = df[df != df.at["Soma", "Soma"]]

df.to_csv('investigados2.csv')
