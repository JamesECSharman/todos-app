import functions
import PySimpleGUI as Gui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

fonts = ('Verdana', 14)

"""Various elements for the app - buttons, text and input fields"""
label = Gui.Text(text="Type in a to-do: ",
                 font=('Verdana', 14),
                 text_color='white',
                 background_color='grey')

time_display = Gui.Text('', size=(20, 1),
                        justification='left', font=fonts, key='time_text', background_color='grey')

input_box = Gui.InputText(tooltip="Enter a to-do", size=(46, 0),
                          key="todo", border_width=2, background_color='light grey', do_not_clear=True)

# The below add button utilises an image instead of text.
"""add_button = Gui.Button(image_source="images/WhiteAdd.png",
                        size=8,
                        tooltip="Add To-Do",
                        key='Add', image_subsample=38,
                        button_color='black', mouseover_colors='dark green')"""

add_button = Gui.Button(button_text="Add",
                        font='bold',
                        size=(8, 0),
                        button_color='black', mouseover_colors='dark green')

quit_button = Gui.Button(button_text="Quit",
                         size=(8, 0),
                         font='bold',
                         button_color="black", mouseover_colors='dark green')

# The below quit button utilises an image instead of text.
"""quit_button = Gui.Button(image_source='images/power_button.png',
                         tooltip="Close Application", image_subsample=50,
                         size=(8, 0),
                         key="Quit",
                         font='bold',
                         button_color="black", mouseover_colors='dark green')"""

edit_button = Gui.Button(button_text='Edit',
                         size=(8, 0),
                         font='bold',
                         button_color="black", mouseover_colors='dark green')

# The below complete button utilises an image instead of text.
"""complete_button = Gui.Button(image_source="images/whitecheck.png",
                             key="Complete",
                             tooltip="Complete To-Do", image_subsample=60,
                             size=(8, 0),
                             font='bold',
                             button_color="black", mouseover_colors='dark green')"""

complete_button = Gui.Button(button_text="Complete",
                             size=(8, 0),
                             font='bold',
                             button_color="black", mouseover_colors='dark green')

clear_button = Gui.Button(button_text="Clear",
                          size=(8, 0),
                          font='bold',
                          button_color="black", mouseover_colors='dark green')

list_box = Gui.Listbox(values=functions.get_todos(),
                       key='todos', enable_events=True,
                       size=(45, 10), background_color='light grey',
                       highlight_background_color='dark green')

"""The below white space elements help in the layout design of the app"""
white_space_1 = Gui.Text(text="", size=(0, 3), background_color='grey')
white_space_2 = Gui.Text(text="", size=(0, 0), background_color='grey')
white_space_3 = Gui.Text(text="", size=(0, 0), background_color='grey')

"""Columns used for the overall layout and design"""
window_column_1 = [[time_display], [label], [input_box], [white_space_2], [list_box]]
window_column_2 = [[add_button], [white_space_3], [edit_button], [complete_button], [clear_button], [white_space_1],
                   [quit_button]]

"""Layout configuration utilising the above columns - justification and background colours to help in app design"""
layout = [[Gui.Column(window_column_1, element_justification='l', background_color='grey'),
           Gui.Column(window_column_2, element_justification='l', vertical_alignment='bottom',
                      background_color='grey')]]

"""Window design and configuration - set master font and sizing. Layout function is called from above"""
window = Gui.Window(background_color='grey',
                    title='My To-Do App',
                    margins=(5, 5),
                    sbar_trough_color='black',
                    sbar_background_color='Dark Grey',
                    layout=layout,
                    finalize=True,
                    font=('Verdana', 15), return_keyboard_events=True)

"""While true loop to capture user input, update todos etc."""
while True:
    event, values = window.read(timeout=200)
    print(event, values)
    window['time_text'].update(time.strftime('%d %b %H:%M:%S'))
    match event:
        case "Add":
            # worth looking into keyboard events and adding an enter function
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            new_todo = new_todo.title()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo']('')

        case "Return:603979789":
            # keyboard event - if enter is hit, the to do is added
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            new_todo = new_todo.title()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo']('')

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                new_todo = new_todo.title()

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo']('')
            except IndexError:
                Gui.popup("Please select an item first", font=fonts, background_color='grey',
                          button_color=('white', 'black'))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                removed_todo = todos.pop(index).strip('\n')
                functions.write_todos(todos_arg=todos)
                window['todos'].update(values=todos)
                window['todo']('')
            except IndexError:
                Gui.popup("Please select an item first", font=fonts, background_color='grey',
                          button_color=('white', 'black'))

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

        case 'Escape:889192475':
            break

window.close()
