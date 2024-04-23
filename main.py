import os
import pandas as pd
import easygui as egui
import numpy as np
#Define o caminho fixo, ande as planilhas iram ser salvas
#Getcwd utiliza par aobter o diretorio da pasta atual
CAMINHOFIXO = f'{os.getcwd()}\\Planilhas Divididas'

def delete_Planilhas():
    Delete = list_Planilhas()

    for planilhasAtuais in Delete:
        os.remove(planilhasAtuais)

def separa_Planilhas(caminho_da_planilha):
    #Faz a leitura do arquivo em excel
    leitor = pd.read_excel(caminho_da_planilha)
    print(leitor.info())
    divisor = int(input('Digite a quantidade de planilhas que deseja dividi:'))
    delete_Planilhas()
    i=0

    for dividindo in np.array_split(leitor, divisor):
        dividindo.to_excel(f'{CAMINHOFIXO}//Planilhas Divididas{i}.xlsx', index=False)
        i += 1
        return True

def list_Planilhas(sufixo=".xlsx", PATH=CAMINHOFIXO):
    #Lista todos os arquivos do caminho especificado
    ListArquivos = os.listdir(PATH)
    #Verifica se o nome do arquivo termina com o sufixo fornecido
    return [os.path.join(PATH, nameArquivo) for nameArquivo in ListArquivos if nameArquivo.endswith(sufixo)]

pdRead = separa_Planilhas( egui.fileopenbox(msg="Selecione a planilha: ", filetypes="*.csv"))