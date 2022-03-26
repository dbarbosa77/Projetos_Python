





def show_op(todo_list):
    print('Tarefas: ')
    print()
    for fazer in  todo_list:
        print(fazer)
        
def do_add(todo2, todo_list):
    todo_list.append(todo2)
    
    
def do_undo(todo_list, redo_list):
    if not todo_list:
        print("Nada para desfazer")
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print("Nada para refazer")
        return
    last_redo=redo_list.pop()
    todo_list.append(last_redo)
    
    
def do_delete(todo_list, redo_list):
    if not todo_list:
        print("Não tem nenhuma tarefa na lista para deletar")
        return
    

    for elemento in todo_list:
            redo_list.append(elemento)
            
    
    todo_list.clear()
    

todo_list=[]
redo_list=[]

while True:
    todo= input('Digite uma tarefa, ou digite "undo" para desfazer, "redo" para refazer e "visualizar"" para ver seus afazeres, ou se desejar, digite "delete" para excluir a lista inteira permanentemente:  ')
    todo2= todo.upper()
    
    if todo2 == 'VISUALIZAR':
        show_op(todo_list)
        continue
    elif todo2 == "UNDO":
        do_undo(todo_list, redo_list)
        continue
    elif todo2 == 'REDO':
        do_redo(todo_list, redo_list)
        continue
    elif todo2 == "DELETE":
        do_delete(todo_list, redo_list)
        continue

    
    do_add(todo2, todo_list)
