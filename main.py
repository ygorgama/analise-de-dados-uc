import pandas as pd

dataset = pd.read_csv('febre_amarela.csv', sep=';')

dataset =  dataset.drop(columns=['ID'])

contagem_de_valores_nulos = dataset.isnull().sum()
contagem_de_valores_validos = dataset.count()


print(contagem_de_valores_nulos)

print('--------------------------------')

print(contagem_de_valores_validos)

dataset = dataset.drop(columns=['DT_OBITO'])




print('--------------------------------')
contagem_valores_positivos_negativos_obito =  dataset.groupby(['OBITO']).count()
dataset['OBITO'] = dataset['OBITO'].fillna('N�O')

print(contagem_valores_positivos_negativos_obito) 

print('--------------------------------')
# dataset['OBITO'] =  dataset["OBITO"].replace('01/12/1994', 'SIM')
# dataset['OBITO'] = dataset["OBITO"].replace('07/04/2000', 'SIM')
# dataset['OBITO'] = dataset["OBITO"].replace('20/02/2003', 'SIM')
# dataset['OBITO'] = dataset["OBITO"].replace('23/01/2017', 'SIM')

contagem_valores_positivos_negativos_obito =  dataset.groupby(['OBITO']).count()
print(contagem_valores_positivos_negativos_obito) 


print('--------------------------------')
print(dataset)

