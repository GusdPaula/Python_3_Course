# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os, json

try:
    with open('todo_list.json', 'r', encoding='utf8') as file:
        tasks = json.load(file)

except FileNotFoundError:
    tasks = []

undo = []

def print_list():
    print("TAREFAS:")
    for task in tasks:
        print(task)

def undo_func(choice):
    choice_splited = choice.split(" ", 1)

    try:
        undo_list = choice_splited[1].split(", ")
        for i in range(len(undo_list)):
            tasks.remove(undo_list[i])
            undo.append(undo_list[i])

    except IndexError:
        to_undo = tasks.pop()
        undo.append(to_undo)
    
    print_list()


def re_do_func(choice):
    choice_splited = choice.split(" ", 1)

    try:
        re_do = choice_splited[1].split(" ")

        for i in range(len(re_do)):
            if re_do[i] not in undo:
                print(re_do[i], 'não foi desfeito.')
                continue

            tasks.append(re_do[i])
            undo.remove(re_do[i])
    
    except IndexError:
        to_re_do = undo.pop()
        tasks.append(to_re_do)
    
    print_list()


def to_do_func(choice):
    choice_splited = choice.split(", ")
    for j in choice_splited:
        tasks.append(j)
    
    print_list()
    

while True:

    print("Comandos: listar, desfazer, refazer, limpar e sair.")

    choice = input("Digite uma tarefa ou comando: ")

    if choice == 'listar':
        print_list()
    
    elif choice == 'limpar':
        os.system('cls')
    
    elif 'desfazer' in choice:
        undo_func(choice)    
    
    elif choice == 'refazer':
        re_do_func(choice)
    
    elif choice == "sair":
        break
    
    else:
        to_do_func(choice)

with open('todo_list.json', 'w', encoding='utf8') as file:
    json.dump(tasks, file, ensure_ascii=False, indent=2)
