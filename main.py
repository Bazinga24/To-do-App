import time

now=time.strftime("%b %d,%Y %H:%M:%S")
print(f"It is now {now}")

def get_todos():
    with open('todos.txt','r') as file:
        todos=file.readlines()
        return todos


while True:
    user_action=input("Type: add, show, edit, complete or exit:")
    user_action=user_action.strip()


    if user_action.startswith("add"):
        todo=user_action[4:] + "\n"
        todos=get_todos()
        todos.append(todo)
        with open("todos.txt",'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todo_list=get_todos()

        new_todo=[]
        for item in todo_list:
            ans= item.strip("\n")
            new_todo.append(ans)

        for index,element in enumerate(new_todo):
            res=f"{index+1}-{element}"
            print(res)

    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            edited_task=input("enter the edited task: ") + "\n"

            todos=get_todos()
            todos[number-1]=edited_task

            with open("todos.txt",'w') as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid !")
            continue

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("complete"):
        try:
            item_no=int(user_action[9:])
            todos=get_todos()
            todos.pop(item_no-1)

            with open("todos.txt",'w') as file:
                file.writelines(todos)

        except IndexError:
            print("Index out of bounds ")

    else:
        print("Unknown command entered !")

print("bye !")





