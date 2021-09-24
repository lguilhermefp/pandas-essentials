import io
import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('investigados.csv', sep=';', index_col=[0])

columns = list(df.columns)
emptyColumns = columns[len(columns)-2:]
print(emptyColumns)
partidos = columns[0:len(columns)-2]

colunasVazias = [(len(partidos)+1), (len(partidos)+2)]
# colunaVazia1 = (len(partidos)+1)
# colunaVazia2 = (len(partidos)+2)

for colunaVazia in colunasVazias:
	df.drop (["Unnamed: "+colunaVazia], axis=1, inplace=True)
# df.drop (["Unnamed: "+str(colunaVazia2)], axis=1, inplace=True)

for partido in partidos:
	df[partido] = df[partido].str.replace(',', '.')
	df[partido] = df[partido].astype(float)

# drop empty rows
df.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
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
