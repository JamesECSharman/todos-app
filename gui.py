from modules import functions
import PySimpleGUI as Gui

label = Gui.Text(text="Type in a to-do: ", font='bold', text_color='white', background_color='grey')
input_box = Gui.InputText(tooltip="Enter a to-do")
add_button = Gui.Button(button_text="Add", font='bold', button_color="black")
quit_button = Gui.Button(button_text="Quit", font='bold', button_color="black")

window = Gui.Window(background_color='grey', title='My To-Do App',
                    layout=[[label], [input_box, add_button], [quit_button]])
window.read()
window.close()
