FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the
    list of to do items."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos
#the below print is to show how help function prints docstrings
#print(help(get_todos))
def write_todos(todos_arg, filepath=FILEPATH):
    """write the to do
    items in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#print("i'm outside main")
if __name__ == "__main__":
    print(get_todos())
    print("i'm inside main")
