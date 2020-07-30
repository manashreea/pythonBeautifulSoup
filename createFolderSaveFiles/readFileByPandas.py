import pandas

#fileData = pandas.read_csv("demoReadByPandas.csv")
fileData = pandas.read_csv('demoReadByPandas.csv',
                           index_col='Employee',
                           parse_dates=['Hired'],
                           header=0,
                           names=['Employee', 'Hired', 'Salary', 'Sick Days'])
print(fileData)
fileData.to_csv('demoReadByPandas_modified.csv')
