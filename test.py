prompt = "Type add, show, edit, complete, clear or exit: "


def update_file():
    """ the code removes the need for the below:
    file = open('files/todos2.txt', 'w')
    file.writelines(todos)
    file.close()
    function updates files in the todos edits """
    with open('files/todos2.txt', 'w') as file_local:
        file_local.writelines(todos)


def read_file() -> object:
    with open('files/todos2.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    # todo editor
    user_action = input(prompt).lower().strip()
    todos = read_file()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        todos.append(todo + '\n')
        update_file()

    elif user_action.startswith('show'):
        for index, item in enumerate(todos):
            item = item.strip('\n')
            display = f"{index + 1}. {item.capitalize()}"
            print(display)

        if not todos:
            print("You need to add a todo.")

    elif user_action.startswith('edit'):
        number = user_action[5:]

        try:
            val = int(number)
            val = val - 1
            new_todo = input("Enter new todo: ").lower().strip() + "\n"
            todos[val] = new_todo
            update_file()

        except ValueError:
            try:
                float(number)
                print("We can only accept numbers with no decimal places")

            except ValueError:
                keyword = [line.rstrip('\n') for line in todos]
                if number in keyword:
                    edit = input("Enter a new todo: ").lower().strip() + "\n"
                    mylist = keyword.index(number)
                    todos[mylist] = edit
                    update_file()
                else:
                    print("Input not recognised")

    elif user_action.startswith('complete'):
        todo = user_action[9:]
        try:
            val = int(todo)

            with open('files/todos2.txt', 'r') as file:
                todos = file.readlines()

            removed_todo = todos.pop(val - 1).strip("\n")

            with open('files/todos2.txt', 'w') as file:
                file.writelines(todos)

            print("The following todo was removed: ", removed_todo)

        except ValueError:
            try:
                todo = float(user_action[9:])
                float(todo)
                print("We can only accept numbers with no decimal places")

            except ValueError:
                todo = (user_action[9:])
                keyword = [line.rstrip('\n') for line in todos]
                if todo in keyword:
                    mylist = keyword.index(todo)
                    del todos[mylist]
                    update_file()
                    print("The following todo was removed: ", todo.capitalize())
                else:
                    print("Input not recognised")

    elif user_action.startswith('exit'):
        print('Have a nice day')
        break

    elif user_action.startswith('clear'):
        todos.clear()
        update_file()

    else:
        print("Error: user prompt not recognised, please enter a valid input")
dow['todos'].update(values=todos)