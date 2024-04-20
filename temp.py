import PySimpleGUI as sg

feet=sg.Text("Enter feet:")
feet_input=sg.InputText()
inch=sg.Text("Enter inch:")
inch_input=sg.InputText()
convert_button=sg.Button("Convert")

window=sg.Window("Converter",layout=[[feet,feet_input],[inch,inch_input],[convert_button]])
window.read()
window.close()