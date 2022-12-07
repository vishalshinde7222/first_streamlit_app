import streamlit 
import pandas
import requests
import snowflake.connector

from urllib.error import URLError

streamlit.title('🍞 My Streamlit App')
streamlit.header('🥑 November 17th')
streamlit.text('🐔 Michigan')
streamlit.text('🥗 Illinois')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
