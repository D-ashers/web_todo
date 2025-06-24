import streamlit as st
import web_todo_functions as fn

todoList = fn.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip().capitalize()
    todoList.append(todo + "\n")
    fn.write_todos(todoList)
    st.session_state["new_todo"] = ""  # Clear the input field after adding

st.title("Web Todo App")
# st.subheader("A simple todo app")
# note the use of unsafe_allow_html=True to allow HTML formatting.
# Only st.write supports this.
# st.write("A simple todo app to use <b>anywhere, anytime</b>.", 
             # unsafe_allow_html=True, 
            #  divider="blue")

st.text_input("Add a new todo", placeholder="todo...", key="new_todo", on_change=add_todo)

for aTodo in todoList:
    checkbox = st.checkbox(aTodo, key=aTodo)
    if checkbox:
        todoList.pop(todoList.index(aTodo))
        fn.write_todos(todoList)
        del st.session_state[aTodo]
        st.rerun()