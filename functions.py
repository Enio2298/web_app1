FILEPATH = "todos.txt"
def get_todos():
    """ Read a text file and return the list
    of to do items"""
    with open('todos.txt', encoding='iso-8859-1') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_w, filepath=FILEPATH):
    """Write the to do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_w)

if __name__ == '__main__':
    print('hello')

