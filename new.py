import pandas as pd
from openpyxl.workbook import Workbook

def main():
	df = pd.read_csv('investigados.csv', sep=';', index_col=[0])
	TransformTable(df)
	df = df[df != df.at["Soma", "Soma"]]
	df.to_csv('investigados2.csv')



def TransformTable(df):
	cleanDF(df)
	convertDFFromObjectToFloat(df)
	addSumColumn(df)
	convertDFFromFloatToCurrency(df)



def cleanDF(df):
	dropEmptyColumns(df)
	dropEmptyRows(df)



def convertDFFromObjectToFloat(df):
	partidos = list(df.columns)
	for partido in partidos:
		df[partido] = df[partido].str.replace(',', '.')
		df[partido] = df[partido].astype(float)



def addSumColumn(df):
	partidos = list(df.columns)
	sumColumn = len(partidos)+1
	df.loc[sumColumn] = df.sum()
	df.rename({sumColumn: "Soma"}, axis=0, inplace=True)
	df["Soma"] = df.sum(axis=1)



def convertDFFromFloatToCurrency(df):
	columns = list(df.columns)
	for column in columns:
		convertColumnFromFloatToCurrency(df, column)


	
def dropEmptyColumns(df):
	emptyColumns = [col for col in df.columns if df[col].isnull().all()]
	df.drop(emptyColumns,
		axis=1,
		inplace=True)



def dropEmptyRows(df):
	df.dropna(
		axis=0,
		inplace=True)



def convertColumnFromFloatToCurrency(df, column):
	df[column] = df[column].apply(lambda x: "${:.2f}".format(x))
	df[column] = df[column].astype(str)
	df[column] = df[column].str.replace('.', ',')



if __name__ == "__main__":
	main()
