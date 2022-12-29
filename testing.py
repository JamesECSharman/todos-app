prompt = "Type add, show, edit, complete, clear or exit: "

def update_file():
    file = open('files/todos2.txt', 'w')
    file.writelines(todos)
    file.close()

while True:
    user_action = input(prompt).lower().strip()
    file = open('files/todos2.txt', 'r')
    todos = file.readlines()
    file.close()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ").lower().strip() + "\n"
            todos.append(todo)
            update_file()
        case 'show':
            for index, item in enumerate(todos):
                display = f"{index + 1}. {item.capitalize().strip()}"
                print(display)
            if not todos:
                print("You need to add a todo.")
        case 'edit':
            number = input("Enter the number or the item of the todo you wish to edit: ").lower().strip()
            try:
                val = int(number)
                val = val - 1
                new_todo = input("Enter new todo: ").lower().strip() + "\n"
                todos[val] = new_todo
                update_file()
            except ValueError:
                try:
                    float(number)
                    print("Please input a number with no decimal places or an item")
                except ValueError:
                    keyword = [line.rstrip('\n') for line in todos]
                    if number in keyword:
                        edit = input("Enter a new todo: ").lower().strip() + "\n"
                        mylist = keyword.index(number)
                        todos[mylist] = edit
                        update_file()
                    else:
                        print("Input not recognised")
        case 'complete':

            todo = input("Enter the number or item of your completed todo: ").lower().strip()

            try:
                val = int(todo)
                todos.pop(val - 1)
                update_file()

            except ValueError:
                try:
                    float(todo)
                    print("Please input a number with no decimal places")
                except ValueError:
                    keyword = [line.rstrip('\n') for line in todos]
                    if todo in keyword:
                        mylist = keyword.index(todo)
                        del todos[mylist]
                        update_file()
                    else:
                        print("Input not recognised")
        case 'exit':
            break
        case 'clear':
            todos.clear()
            update_file()
        case _:
            print("Error: user prompt not recognised, please enter a valid input")

print("Thank you")
