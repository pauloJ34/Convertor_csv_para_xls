import pandas as pd
import csv

arquivo = open("Dados_sensores_11_01_22_a_12_01_22.csv")
render= csv.reader(arquivo)
data=[]
hora=[]
dado_1=[]
dado_2=[]
dado_3=[]
dado_4=[]
dado_5=[]

x=0

for linhas in render:
	data_hora= linhas[0].split(" ")
	data.append(data_hora[0])
	hora.append(data_hora[1])
	dado_1.append(linhas[2])
	dado_2.append(linhas[3])
	dado_3.append(linhas[4])
	dado_4.append(linhas[5])
	dado_5.append(linhas[6])
	
	x+=1

dados={'Data':data,'Hora':hora,'Dado 1':dado_1,'Dado 2':dado_2,'Dado 3':dado_3,'Dado 4':dado_4,'Dado 5':dado_5}

dataframe=pd.DataFrame(data=dados)
print(dataframe)
dataframe.to_excel('dados.xls',index = False)

