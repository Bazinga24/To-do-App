import PySimpleGUI as sg
import functions

label=sg.Text("Type a to-do")
input_box=sg.InputText(tooltip="Enter a todo",key="todo")
add_button=sg.Button("Add")
edit_button=sg.Button("Edit")
list_box=sg.Listbox(values=functions.get_todos(),
                    key="todos",
                    enable_events=True,
                    size=[45,10])


window=sg.Window("This is a todo App",layout=[[label],[input_box,add_button],[list_box,edit_button]])


while True:
    event, value = window.read()
    print(event)
    print(value)

    if event == "Add":
        todo_list=functions.get_todos()
        todo=value["todo"] + "\n"
        todo_list.append(todo)
        functions.write_todos(todo_list)
        window["todos"].update(values=functions.get_todos())

    elif event == "Edit":
        task_edited_to=value["todo"] + "\n"
        task_to_be_edited=value["todos"][0]

        new_todo_list=functions.get_todos()
        index=new_todo_list.index(task_to_be_edited)
        new_todo_list[index]=task_edited_to

        functions.write_todos(new_todo_list)
        window["todos"].update(values=new_todo_list)

    elif event == "todos":
        window["todo"].update(value=value["todos"][0])
    elif event == "Complete":
        pass
    elif event == sg.WIN_CLOSED:
        break


window.close()