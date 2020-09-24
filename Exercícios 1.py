import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# # Questão 1
# ler arquivo excel
with pd.ExcelFile("C:/Users/bekacruz/Documents/WHOdata.xls") as xls:
    df = pd.read_excel(xls)
# visualizar o arquivo
print(df)

# # Questão 2
#ler arquivo excel
with pd.ExcelFile("C:/Users/bekacruz/Documents/WHOdata.xls") as xls:
    df = pd.read_excel(xls)
#somar os elementos da coluna TB deaths
Total_de_mortes = df['TB deaths'].sum()
# imprimir o número de mortes
print ("Total de mortes =", Total_de_mortes)

# # Questão 3
data = {'Country': ['Angola', 'Brazil', 'China', 'Equatorial Guinea',
                    'Guinea-Bissau', 'India', 'Mozambique', 'Portugal', 'Russian Federation', 'Sao Tome and Principe',
                    'South Africa','Timor Leste'],
        'Population (1000s)': ['21472', '200362', '1393337', '757', '1704',
                               '1252140','25834','10608', '142834', '193', '52776', '1133'],
        'TB deaths': ['6900', '4400', '41000', '67', '1200', '240000',
                      '18000', '140', '17000', '18', '25000', '990']}
df = pd.DataFrame(data, columns= ['Country', 'Population (1000s)', 'TB deaths'])
df.sort_values(by=['TB deaths'], inplace=True, ascending=False)
print (df)


           ## não funcionou por dataframe

df = pd.read_excel("C:/Users/bekacruz/Documents/WHOdata.xls")
# organizar em ordem crescente
asc = df.sort_values('TB deaths')
#selecionar o primeiro e último elemento
print(asc.iloc [[0, -1]]['TB deaths'])


## Questão 4
df = pd.read_excel("C:/Users/bekacruz/Documents/WHOdata.xls")
# estabelecer a média
média = df['TB deaths'].mean()
# estabelecer a mediana
mediana = df['TB deaths'].median()
#imprimir média e mediana
print('média=', média, 'e', 'mediana=', mediana)

## Questão 5
df = pd.read_excel("C:/Users/bekacruz/Documents/WHOdata.xls")
#organizar em ordem crescente
asc = df.sort_values('TB deaths')
# imprimir nova tabela
print(asc.to_string(index=False))


## Questão 6
df = pd.read_excel("C:/Users/bekacruz/Documents/WHOdata.xls")
#nova população dividida por 100000
população_new = df['Population (1000s)']/100000
# definir mortes por 100000
df['TB deaths normalized'] = df['TB deaths']/(população_new)
# imprimir país e morte por 100000
print(df[['Country','TB deaths normalized']].to_string(index=False))

## Questão 7
df = pd.read_excel("C:/Users/bekacruz/Documents/WHOdata.xls")
# países BRICS nas posições da tabela
brics = df.iloc[[1, 2, 5, 8, 10]]
# soma as mortes dos BRICS
brics_total = brics['TB deaths'].sum()
#média das mortes dos BRICS
brics_mean = brics_total/5
#imprimir a média
print(('Total deaths BRICS=', brics_total),('Mean deaths BRICS=', brics_mean))
