from modules import functions
import PySimpleGUI as Gui

label = Gui.Text(text="Type in a to-do: ",
                 font=('Verdana', 15),
                 text_color='white',
                 background_color='grey')
input_box = Gui.InputText(tooltip="Enter a to-do",
                          key="todo")
add_button = Gui.Button(button_text="Add",
                        font='bold',
                        button_color="black")
quit_button = Gui.Button(button_text="Quit",
                         font='bold',
                         button_color="black")

window = Gui.Window(background_color='grey',
                    title='My To-Do App',
                    layout=[[label],
                            [input_box, add_button],
                            [quit_button]],
                    font=('Verdana', 15))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case Gui.WIN_CLOSED:
            break

window.close()