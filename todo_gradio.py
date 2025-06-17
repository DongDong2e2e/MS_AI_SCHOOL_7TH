# todo_gradio.py
print("Welcome to the Todo List App!")
print("Let's start!")


todos = []
def add_todo(todo):
    todos.append(todo)
    print("Added:",todo)

def delete_todo(index):
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print("Deleted:", removed)