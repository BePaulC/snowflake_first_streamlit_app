import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")

streamlit.text("🥣 Kale")
streamlit.text("English Breakfast")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
