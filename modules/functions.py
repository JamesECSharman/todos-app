FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ This function reads a text file and returns the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ This function writes a text file, it is used to update the text file with the updated or new to-dos """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos(filepath='../files/todos.txt'))