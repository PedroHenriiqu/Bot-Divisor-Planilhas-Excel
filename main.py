import os
import pandas
import easygui as egui
#Define o caminho fixo, ande as planilhas iram ser salvas
#Getcwd utiliza par aobter o diretorio da pasta atual
CAMINHOFIXO = f'{os.getcwd()}\\Planilhas'

def delete_Planilhas():
    Delete = list_Planilhas()

    for planilhasAtuais in Delete:
        os.remove(planilhasAtuais)

def separa_Planilhas(caminho_da_planilha):
    #Faz a leitura do arquivo em excel
    leitor = pandas.read_excel(caminho_da_planilha)
    print(leitor.info())

def list_Planilhas(sufixo=".xlsx", PATH=CAMINHOFIXO):
    #Lista todos os arquivos do caminho especificado
    ListArquivos = os.listdir(PATH)
    #Verifica se o nome do arquivo termina com o sufixo fornecido
    return [os.path.join(PATH, nameArquivo) for nameArquivo in ListArquivos if nameArquivo.endswith(sufixo)]

pdRead = separa_Planilhas( egui.fileopenbox(msg="Selecione a planilha: ", filetypes="*.csv"))