import streamlit;
streamlit.title('My Parents New Healthy Dinner ')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Eggs')
streamlit.header('Build Your Own Fruit Smoothie')


import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['avocado','strawberry'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
stramlit.dataframe(fruits_to_show)
