import random
# Sua tarefa é criar um programa em Python que permita ao usuário gerenciar uma lista de tarefas. O programa deve ter recursos para adicionar tarefas, remover tarefas, marcar tarefas como concluídas, listar todas as tarefas e listar apenas tarefas concluídas ou não concluídas.

# adicionarTarefa: Função para adicionar uma nova tarefa à lista.
# removerTarefa: Função para remover uma tarefa da lista.
# concluirTarefa: Função para marcar uma tarefa como concluída.
# listarTarefa: Função para exibir todas as tarefas na lista.
# listarTarefaPorStatus: Função para listar tarefas com base em seu status de conclusão.

tasksList = []

def addTask():
    idTask = str(random.randint(1, 90))
    taskName = input("Qual o nome da tarefa que deseja adicionar? ")
    taskStatus = input("Qual o status da tarefa? ")
    taskPriority = input("Qual a prioridade da tarefa? ")
    dueDateTask = input("Qual a data de vencimento da tarefa? ")
    print(" ")
    print("--------------Tarefa adicionada-------------------")
    print(" ")
    task = [taskName, taskStatus, taskPriority, dueDateTask, idTask]
    tasksList.append(task)
    
def listTask():
    print(" ")
    print("-------------Lista de tarefas--------------------")
    print(" ")
    for tasks in tasksList:
        print("Id da tarefa: "+str(tasks[4]))
        print("nome da tarefa: "+tasks[0])
        print("Status da tarefa: "+tasks[1])
        print("Prioridade da tarefa: "+tasks[2])
        print("Vencimento da tarefa: "+tasks[3])
        print(" ")
        print("---------------------------------")
        print(" ")
        
def removeTask():
    print(" ")
    print("-------------Remoção de tarefas--------------------")
    print(" ")
    taskRemove = input("Qual o id da tarefa que você deseja remover: ")
    index = len(tasksList)
    
    print(tasksList[].index())
    
    

    
exit = 1
while exit == 1:
    print("Gerenciador de tarefas")
    print("1 - Criar uma tarefa")
    print("2 - remover uma tarefa")
    print("3 - marcar como concluida")
    print("4 - listar todas as tarefas")
    print("5 - listar tarefas por status")
    print("6 - Sair da lista de tarefas")
    option = input("Qual das opções anteriores você deseja:")
    
    if option == "1":
        addTask()
    elif option == "2":
        print(tasksList)
        # listTask()
    elif option == "3":
        removeTask()
        
    
    