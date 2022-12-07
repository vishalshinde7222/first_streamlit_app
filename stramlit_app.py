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
my_fruit_list = my_fruit_list.set_index('Fruit')

stream.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.

streamlit.dataframe(fruits_to_show)
