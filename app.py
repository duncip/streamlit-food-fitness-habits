import streamlit as st
from multiapp import MultiApp
from apps import home, model, dataEntry

app = MultiApp()

#st.markdown("""
# Multi-Page App
#Everything added here will appear on each single page
#""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Model", model.app)
app.add_app("Data Entry", dataEntry.app)
# The main app
app.run()