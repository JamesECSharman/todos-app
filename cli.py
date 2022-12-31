# from Functions import get_todos, write_todos. Time function used to display the time to user
from modules import functions
import time

# time function printed for the user in CLI
now = time.strftime("%d %b, %y, %H:%M:%S")
print("It is ", now)

prompt = "Type add, show, edit, complete, clear or exit: "

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos_arg=todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            display = f"{index + 1}. {item.capitalize()}"
            print(display)

        if not todos:
            print("You need to add a todo.")

    elif user_action.startswith('edit'):
        todos = functions.get_todos()
        number = user_action[5:]

        try:
            val = int(number)
            val = val - 1
            new_todo = input("Enter new todo: ").lower().strip() + "\n"
            todos[val] = new_todo
            functions.write_todos(todos_arg=todos)

        except ValueError:
            try:
                float(number)
                print("We can only accept numbers with no decimal places")

            except ValueError:
                keyword = [line.rstrip('\n').capitalize() for line in todos]
                if number in keyword:
                    edit = input("Enter a new todo: ").lower().strip() + "\n"
                    mylist = keyword.index(number)
                    todos[mylist] = edit
                    functions.write_todos(todos_arg=todos)
        except IndexError:
            print("Unknown To-Do, please ensure you enter a correct To-Do number.")
            continue
        else:
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            todo = number
            removed_todo = todos.pop(todo - 1).strip("\n")
            functions.write_todos(todos_arg=todos)
            print("The following todo was removed: ", removed_todo)

        except (ValueError, IndexError) as error:
            print('Unknown Command')
            continue

    elif user_action.startswith('clear'):
        todos = functions.get_todos()
        todos.clear()
        functions.write_todos(todos_arg=todos)

    elif user_action.startswith('exit'):
        print("See you soon!")
        break

    else:
        print('Command is not valid')