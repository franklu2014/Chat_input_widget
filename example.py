import streamlit as st
from streamlit_extras.bottom_container import bottom # to position the widget on the bottom 
from streamlit_chat_widget import chat_input_widget

st.title("My Custom Chat Application")
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with bottom():
    user_input = chat_input_widget()

if user_input:
# if user_input := chat_input_widget():
    if "text" in user_input:
        st.session_state.chat_history.append(f"You: {user_input['text']}")
    elif "audioFile" in user_input:
        st.audio(bytes(user_input["audioFile"]))
        # print(f"audio input type: {type(user_input["audioFile"])}")
        # print(user_input["audioFile"])
        # st.audio(user_input["audioFile"])

for message in st.session_state.chat_history:
    print("printing chat history")
    st.write(message)
