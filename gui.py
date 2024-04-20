import PySimpleGUI as sg

label=sg.Text("Type a to-do")
input_box=sg.InputText(tooltip="Enter a todo")
add_button=sg.Button("Add")
window=sg.Window("This is a todo App",layout=[[label],[input_box,add_button]])
window.read()
window.close()