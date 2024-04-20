import PySimpleGUI as sg


feet=sg.Text("Enter feet:")
feet_input=sg.InputText()
inch=sg.Text("Enter inch:")
inch_input=sg.InputText()
convert_button=sg.Button("Convert")

result = sg.Text("",key="output")
window = sg.Window("Converter",layout=[[feet,feet_input],[inch,inch_input],[convert_button,result]])

while True:
    event,values=window.read()

    if event == "Convert":
        feet_val=float(values[0])
        inch_val=float(values[1])

        meter=str(feet_val*0.3048+inch_val*0.0254) + " meter"
        window["output"].update(value=meter)

    if event == sg.WIN_CLOSED:
        break


print ("Exit !!!! ")
window.close()



