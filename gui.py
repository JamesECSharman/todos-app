from modules import functions
import PySimpleGUI as Gui

label = Gui.Text(text="Type in a to-do: ",
                 font=('Verdana', 15),
                 text_color='white',
                 background_color='grey')
input_box = Gui.InputText(tooltip="Enter a to-do", size=(46, 0),
                          key="todo")
add_button = Gui.Button(button_text="Add",
                        font='bold',
                        button_color="black")
quit_button = Gui.Button(button_text="Quit",
                         font='bold',
                         button_color="black")
edit_button = Gui.Button(button_text='Edit',
                         font='bold',
                         button_color="black")
complete_button = Gui.Button(button_text="Complete",
                             font='bold',
                             button_color="black"
                             )
clear_button = Gui.Button(button_text="Clear",
                          font='bold',
                          button_color="black"
                          )
list_box = Gui.Listbox(values=functions.get_todos(),
                       key='todos', enable_events=True,
                       size=[45, 10], background_color='light grey')
white_space = Gui.Text(text="", size=(0, 3), background_color='grey')

window_column_1 = [[label], [input_box], [list_box]]
window_column_2 = [[add_button], [edit_button], [complete_button], [clear_button], [white_space], [quit_button]]

layout = [[Gui.Column(window_column_1, element_justification='l', background_color='grey'),
           Gui.Column(window_column_2, element_justification='l', vertical_alignment='bottom', background_color='grey')]]

window = Gui.Window(background_color='grey',
                    title='My To-Do App',
                    sbar_trough_color='black',
                    sbar_background_color='Dark Grey',
                    layout=layout,
                    font=('Verdana', 15))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            new_todo = new_todo.title()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            new_todo = new_todo.title()

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_complete)
            removed_todo = todos.pop(index).strip('\n')
            functions.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)

        case 'Clear':
            todos = functions.get_todos()
            todos.clear()
            functions.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case Gui.WIN_CLOSED:
            break

        case 'Quit':
            break

window.close()