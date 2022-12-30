from modules import functions
import PySimpleGUI as Gui

label = Gui.Text(text="Type in a to-do: ",
                 font=('Verdana', 14),
                 text_color='white',
                 background_color='grey')
input_box = Gui.InputText(tooltip="Enter a to-do", size=(46, 0),
                          key="todo", border_width=2, background_color='light grey')
add_button = Gui.Button(button_text="Add",
                        font='bold',
                        size=(8, 0),
                        button_color='black', mouseover_colors='dark green')
quit_button = Gui.Button(button_text="Quit",
                        size=(8, 0),
                         font='bold',
                         button_color="black", mouseover_colors='dark green')
edit_button = Gui.Button(button_text='Edit',
                         size=(8, 0),
                         font='bold',
                         button_color="black", mouseover_colors='dark green')
complete_button = Gui.Button(button_text="Complete",
                             size=(8, 0),
                             font='bold',
                             button_color="black", mouseover_colors='dark green'
                             )
clear_button = Gui.Button(button_text="Clear",
                          size=(8, 0),
                          font='bold',
                          button_color="black", mouseover_colors='dark green'
                          )
list_box = Gui.Listbox(values=functions.get_todos(),
                       key='todos', enable_events=True,
                       size=[45, 10], background_color='light grey')
white_space_1 = Gui.Text(text="", size=(0, 3), background_color='grey')
white_space_2 = Gui.Text(text="", size=(0, 0), background_color='grey')
white_space_3 = Gui.Text(text="", size=(0, 0), background_color='grey')

window_column_1 = [[label], [input_box], [white_space_2], [list_box]]
window_column_2 = [[add_button], [white_space_3], [edit_button], [complete_button], [clear_button], [white_space_1], [quit_button]]

layout = [[Gui.Column(window_column_1, element_justification='l', background_color='grey'),
           Gui.Column(window_column_2, element_justification='l', vertical_alignment='bottom',
                      background_color='grey')]]

window = Gui.Window(background_color='grey',
                    title='My To-Do App',
                    margins=(5, 5),
                    sbar_trough_color='black',
                    sbar_background_color='Dark Grey',
                    layout=layout,
                    font=('Verdana', 15))

while True:
    event, values = window.read()
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
