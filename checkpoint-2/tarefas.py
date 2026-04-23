import json


to_do_list = []


def adicionar_tarefa(descricao):
    dicionario = {'descricao': descricao, 'concluida': False}
    to_do_list.append(dicionario)
    
    
    
def listar_tarefas():
    for indice, tarefa in enumerate (to_do_list):
        simbolo = '[X]' if tarefa ['concluida'] else '[]'
        print(indice, simbolo, tarefa['descricao'])
        
        
        
def concluir_tarefa(indice):
    try:
        to_do_list[indice]['concluida'] = True
    except IndexError:
        print("este index nao existe")


def salvar_dados():
    with open("dados.json", "w") as arquivo:
        json.dump(to_do_list, arquivo)
    
def carregar_dados():
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            to_do_list.clear()
            to_do_list.extend(dados)
    except FileNotFoundError:
        print("nao encontramos o seu arquivo")


def remover(indice):
    try:
        to_do_list.pop(indice)
    except IndexError:
        print("este index nao existe")
        