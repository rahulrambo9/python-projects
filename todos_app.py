def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def save_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
   

while True: 
    user_action = input("Type add, show, edit, complete or exit :")
    user_action = user_action.strip()    

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos("todos.txt")

        todos.append(todo + '\n')
        save_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            row = f"{index}-{item}"
            print(row)

    elif user_action.startswith("edit"):  
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos("todos.txt")
            new_value = input("Enter new todos : ")
            todos[number] = new_value + '\n'  
            save_todos("todos.txt", todos)
        except:
            print ("Your Command is not valid")
            continue    

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos("todos.txt")
            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)
            save_todos("todos.txt", todos)
            message = f"todo {todos_to_remove} is removed from list..."
            print(message)
        except:
            print("Wrong choice....")
            continue    

    elif user_action.startswith("exit"):  
        break
    else:
        print("Command is not valid.....")
print("BYe.....")        
