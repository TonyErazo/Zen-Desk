from pathlib import Path  

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def navigation_menu():
    with st.sidebar:
        st.title("Menu")
        st.page_link("WebApp.py", label="Ticket System", icon="🏠")
        st.page_link("pages/StatsPage.py", label="Statistical Data", icon="📊")
        st.page_link("pages/SubmitTicketPage.py", label="Submit Ticket", icon="📨")


def display():
    navigation_menu()
    file_path = str(Path(__file__).parent.parent.parent) + '\\data\\tickets\\'
    target_file = str(file_path) + "\\" + "datafile.csv"

    df = pd.read_csv(target_file, sep=",")

    # Assign colors based on priority
    color_map = {
        'High': 'red',
        'Medium': 'yellow',
        'Low': 'green'
    }

    df['color'] = df['priority'].map(color_map)

    # Calculate counts of each priority
    priority_counts = df['priority'].value_counts()

    fig = px.pie(values=priority_counts.values, names=priority_counts.index,
                title='Distribution of Issues by Priority',
                color=priority_counts.index,
                color_discrete_map=color_map)
    
    # Calculate counts of each priority for bar chart
    priority_counts_bar = df['priority'].value_counts().sort_index()

    fig_bar = go.Figure(data=[
        go.Bar(name='Priority Counts', x=priority_counts_bar.index, y=priority_counts_bar.values, marker_color=[color_map[p] for p in priority_counts_bar.index])
    ])
    fig_bar.update_layout(title='Number of Issues by Priority', xaxis_title='Priority', yaxis_title='Count')

    st.markdown("<h1 style='text-align: center; color: white;'>ZenDesk - Web App</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Statistical Data</h2>", unsafe_allow_html=True)

    st.plotly_chart(fig, theme=None)
    st.plotly_chart(fig_bar, theme=None)
        
display()