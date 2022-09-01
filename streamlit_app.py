import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")

streamlit.text("🥣 Kale")
streamlit.text("English Breakfast")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
