from Business_Chatbot import Business_Chatbot_Creator
from config import *
import streamlit as st
from streamlit_chat import message


def create_edubot():
    businessbotcreator = Business_Chatbot_Creator()
    edubot = businessbotcreator.create_business_chatbot()
    return edubot

edubot = create_edubot()

def infer_edubot(prompt):
    model_out = edubot(prompt)
    answer = model_out['result']
    return answer

def display_conversation(history):
    for i in range(len(history["assistant"])):
        message(history["user"][i], is_user=True, key=str(i) + "_user")
        message(history["assistant"][i],key=str(i))

def main():

    st.title("Edubot: Your Smart Business Consultant 📚🤖")
    st.subheader("A bot created using Langchain, which can answer all your queries about the business")

    user_input = st.text_input("Enter your query")

    if "assistant" not in st.session_state:
        st.session_state["assistant"] = ["I am ready to help you"]
    if "user" not in st.session_state:
        st.session_state["user"] = ["Hey there!"]
                
    if st.button("Answer"):

        answer = infer_edubot({'query': user_input})
        st.session_state["user"].append(user_input)
        st.session_state["assistant"].append(answer)

        if st.session_state["assistant"]:
            display_conversation(st.session_state)

if __name__ == "__main__":
    main()
    