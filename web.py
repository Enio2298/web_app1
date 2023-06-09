import functions
import streamlit as st

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my  todo app.")
st.write("This app is to increase the <b>productivity</b>",
         unsafe_allow_html=True)
#Html solo está permitido para el método write
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ",
              placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")
