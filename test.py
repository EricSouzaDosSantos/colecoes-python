import random
# Sua tarefa é criar um programa em Python que permita ao usuário gerenciar uma lista de tarefas. O programa deve ter recursos para adicionar tarefas, remover tarefas, marcar tarefas como concluídas, listar todas as tarefas e listar apenas tarefas concluídas ou não concluídas.

# adicionarTarefa: Função para adicionar uma nova tarefa à lista. (Feito)
# removerTarefa: Função para remover uma tarefa da lista. (Feito)
# concluirTarefa: Função para marcar uma tarefa como concluída. (feito)
# listarTarefa: Função para exibir todas as tarefas na lista. (feito)
# listarTarefaPorStatus: Função para listar tarefas com base em seu status de conclusão. (fazendo)

tasksList = []

def addTask():
    idTask = str(random.randint(1, 90))
    taskName = input("Qual o nome da tarefa que deseja adicionar? ")
    taskStatus = input("Qual o status da tarefa? ")
    taskPriority = input("Qual a prioridade da tarefa? ")
    dueDateTask = input("Qual a data de vencimento da tarefa? ")
    print("\n--------------Tarefa adicionada-------------------\n")
    task = [taskName, taskStatus, taskPriority, dueDateTask, idTask]
    tasksList.append(task)
    
def listTask():
    print("\n-------------Lista de tarefas--------------------\n")
    for task in tasksList:
        print(f"Id da tarefa: {task[4]}")
        print(f"Nome da tarefa: {task[0]}")
        print(f"Status da tarefa: {task[1]}")
        print(f"Prioridade da tarefa: {task[2]}")
        print(f"Vencimento da tarefa: {task[3]}\n")
        print("---------------------------------\n")
        
def removeTask():
    print("\n-------------Remoção de tarefas--------------------\n")
    taskRemove = input("Qual o id da tarefa que você deseja remover: ")
    
    taskFound = False
    for task in tasksList:
        if task[4] == taskRemove:
            tasksList.remove(task)
            print(f"Tarefa com ID {taskRemove} removida.\n")
            taskFound = True
            break
    
    if not taskFound:
        print(f"Nenhuma tarefa com ID {taskRemove} foi encontrada.\n")

def markTaskAsCompleted():
    taskComplete = input("Qual o id da tarefa que você deseja marcar como concluída: ")
    
    taskFound = False
    for task in tasksList:
        if task[4] == taskComplete:
            task[1] = "Concluída"
            print(f"Tarefa com ID {taskComplete} marcada como concluída.\n")
            taskFound = True
            break
    
    if not taskFound:
        print(f"Nenhuma tarefa com ID {taskComplete} foi encontrada.\n")

def listTaskByStatus():
    status = input("Qual o status das tarefas que você deseja listar (Concluída ou Não Concluída): ")
    print(f"\n-------------Lista de tarefas com status '{status}'--------------------\n")
    
    for task in tasksList:
        if task[1].lower() == status.lower():
            print(f"Id da tarefa: {task[4]}")
            print(f"Nome da tarefa: {task[0]}")
            print(f"Status da tarefa: {task[1]}")
            print(f"Prioridade da tarefa: {task[2]}")
            print(f"Vencimento da tarefa: {task[3]}\n")
            print("---------------------------------\n")

while True:
    print("Gerenciador de tarefas")
    print("1 - Criar uma tarefa")
    print("2 - Remover uma tarefa")
    print("3 - Marcar como concluída")
    print("4 - Listar todas as tarefas")
    print("5 - Listar tarefas por status")
    print("6 - Sair da lista de tarefas")
    option = input("Qual das opções anteriores você deseja: ")
    
    if option == "1":
        addTask()
    elif option == "2":
        removeTask()
    elif option == "3":
        markTaskAsCompleted()
    elif option == "4":
        listTask()
    elif option == "5":
        listTaskByStatus()
    elif option == "6":
        print("Saindo do gerenciador de tarefas.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma das opções acima.\n")
