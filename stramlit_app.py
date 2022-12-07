import streamlit 
import pandas
import requests
#import snowflake.connector

from urllib.error import URLError

streamlit.title('🍞 My Streamlit App')
streamlit.header('🥑 November 17th')
streamlit.text('🐔 Michigan')
streamlit.text('🥗 Illinois')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['avacado','strawberries'])

#my_fruit_list = my_fruit_list.set_index('Fruit')
