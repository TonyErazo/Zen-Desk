
import streamlit as st
import pandas as pd
from command.impl.SubmitCommand import SubmitCommand

def navigation_menu():
    with st.sidebar:
        st.title("Menu")
        st.page_link("WebApp.py", label="Ticket System", icon="🏠")
        st.page_link("pages/StatsPage.py", label="Statistical Data", icon="📊")
        st.page_link("pages/SubmitTicketPage.py", label="Submit Ticket", icon="📨")

def display():
    navigation_menu()
    st.markdown("<h1 style='text-align: center; color: white;'>Ticket Submission</h1>", unsafe_allow_html=True)
    submit_command = SubmitCommand()
    ticket_name = st.text_input("Ticket Name")
    priority_set = {'Priority': ['Low', 'Medium', 'High']}
    priority_df = pd.DataFrame(priority_set)
    ticket_priority = st.selectbox('Select Priority', priority_df['Priority'].unique())
    ticket_description = st.text_area(label="Ticket Description")

    if st.button("Submit", type="secondary"):
        # Both text inputs contain a value
        if ticket_name and ticket_priority and ticket_description:
            df = submit_command.submit(ticket_name, ticket_priority, ticket_description)
            st.session_state.df = df
            st.success("Ticket Submitted!")
        else:
            st.error("Please fill in the required inputs!")
display()