import pandas as pd
from numpy import isnan

dataset = pd.read_csv('febre_amarela.csv', sep=';')

dataset =  dataset.drop(columns=['ID'])

contagem_de_valores_nulos = dataset.isnull().sum()
contagem_de_valores_validos = dataset.count()


print(contagem_de_valores_nulos)

print('--------------------------------')


print(contagem_de_valores_validos)



print('--------------------------------')
contagem_valores_positivos_negativos_obito =  dataset.groupby(['OBITO']).count()

# Substitu todos os obitos por N�O
dataset['OBITO'] = dataset['OBITO'].fillna('N�O')



# Substitui os valores do data por uma seqência numérica
dataset['OBITO'] = dataset['OBITO'].replace('N�O', 0)
dataset['OBITO'] = dataset['OBITO'].replace('SIM', 1)
dataset['OBITO'] = dataset['OBITO'].replace('IGN', 2)

print(contagem_valores_positivos_negativos_obito) 

print('--------------------------------')
dataset = dataset.fillna('NI')
print('--------------------------------')

contagem_valores_positivos_negativos_obito =  dataset.groupby(['OBITO']).count()
print(contagem_valores_positivos_negativos_obito) 


print('--------------------------------')
print(dataset)

