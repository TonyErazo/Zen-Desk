from pathlib import Path  

import pandas as pd
import streamlit as st
import numpy as np

def navigation_menu():
    with st.sidebar:
        st.title("Menu")
        st.page_link("WebApp.py", label="Ticket System", icon="🏠")
        st.page_link("pages/StatsPage.py", label="Statistical Data", icon="📊")
        st.page_link("pages/SubmitTicketPage.py", label="Submit Ticket", icon="📨")

def organize_ids():
    df = st.session_state.df
    new_ids = np.arange(len(df))
    # Assign the new IDs to the 'id' column
    df['id'] = new_ids
    # Save the updated DataFrame to the target file (assuming target_file is defined somewhere)
    df.to_csv(st.session_state.target_file, index=False)
    st.session_state.df = df
    st.session_state.df.to_csv(st.session_state.target_file, index = False)

def main():
    st.set_page_config(layout='wide', menu_items=None)
    navigation_menu()
    file_path = str(Path(__file__).parent.parent) + '\\data\\tickets\\'
    target_file = str(file_path) + "\\" + "datafile.csv"

    if 'target_file' not in st.session_state:
        st.session_state.target_file = target_file

    df = pd.read_csv(target_file, sep=",")
    st.markdown("<h1 style='text-align: center; color: white;'>ZenDesk - Web App</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Ticket System</h2>", unsafe_allow_html=True)

    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(data=pd.read_csv(target_file))
    
    df_data_editor = st.data_editor(st.session_state.df, use_container_width=True, hide_index=True, height=900, on_change=organize_ids)
    #df_data_editor.to_csv(target_file, index=False)


main()