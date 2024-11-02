def get_todos(filepath="todos.txt"): #called default argument declare so dont add to todos.txt in every time
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def save_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
  