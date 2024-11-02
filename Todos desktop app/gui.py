import functions
import FreeSimpleGUI as sg

# window ---> elements

# create elements like textbox, button, text
label = sg.Text("Type in a to do ")
inputBox = sg.InputText(tooltip = "Enter To Do")
add_button = sg.Button("Add")

# window 
window = sg. Window("To Do APP", layout=[[label],[inputBox],[add_button]])
window.read()
window.close()