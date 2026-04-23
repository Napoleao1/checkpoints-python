
from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, carregar_dados, salvar_dados, remover
import json


def menu():
    carregar_dados()
    while True:
        opcao = input("[1] Adicionar [2] Listar [3] concluir tarefa [4] remover [5] sair \n")        
        if opcao == "1":
            descricao = input("adicione a tarefa: ")
            adicionar_tarefa(descricao)
            salvar_dados()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            numero = int(input("digite o numero da tarefa"))
            concluir_tarefa(numero)
            salvar_dados()
        elif opcao == "4":
            numero = int(input("digite o numero da tarefa"))
            remover(numero)
            salvar_dados()
        elif opcao == "5":
            break
            
menu()





