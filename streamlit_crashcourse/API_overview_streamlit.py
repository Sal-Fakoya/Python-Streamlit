import streamlit as st
import pandas as pd
from PIL import Image
import datetime
import time
import matplotlib.pyplot as plt

img = Image.open("../streamlit101/image_03.jpg")

# Method 1
# st.set_page_config(page_title="My Web App",
#                    page_icon=img,
#                    layout="centered",
#                    initial_sidebar_state="auto")

# Method 2:
PAGE_CONFIG = {"page_title": "My Web App",
               "page_icon": img,
               "layout": "centered",
               "initial_sidebar_state": "expanded"}
st.set_page_config(**PAGE_CONFIG)
def main():
    st.title("Hi!")
    st.sidebar.success("Select a page above.")


"""
This script is about the API overview of streamlit.

"""
"""
                API overview:
--> text
--> data
--> media
--> widgets
--> layouts
--> charts
--> components

                        Text
--> st.text()
--> st.title()
--> st.header()
--> st.subheader()
--> st.success()
--> st.warning()
--> st.error()
--> st.info()
--> s.markdown()
--> st.code()
--> st.latex()

                            DATA
--> st.dataframe()
--> st.table()
--> st.json()
--> st.code()
--> st.echo()
--> st.help()
--> st.cache()
--> st.help()


                            MEDIA   
--> st.image()
--> st.video()
--> st.audio()

                            WIDGETS
--> st.button()
--> st.radio()
--> st.checkbox()
--> st.text_input()
--> st.text_area()
--> st.number_input()
--> st.date_input()
--> st.selectbox()
--> st.multiselect()
--> st.slider()
--> st.select_slider()
--> st.fileuploader()
--> st.beta_color_picker()
--> st.progress()
--> st.spinner()
--> st.balloons()

                            LAYOUTS
--> st.sidebar()
--> st.beta_columns()
--> st.columns()
--> st.expander()
--> st.container()

                            CHARTS
--> st.line_chart()
--> st.bar_chart()
--> st.area_chart()
--> st.pyplot()
--> st.altair_chart()
--> st.plotly_chart()
--> st.vega_lite_chart()
--> st.bokeh_chart()
--> st.pydeck_chart()
--> st.graphiz_chart()
--> st.map()

                            COMPONENTS
--> components.html()
-- components.iframe()
--> declare_components()
"""


name = "Sal"
st.text(f"Hello, this is {name}")

# Displaying colored text/bootstrap alert
st.success("This is successful")

st.help()

st.divider()
# Using st.write(): for normal texts and markdown
st.write("This is some text")

st.write("## This is a header")
st.write(2 + 3)

st.help(range)

df = pd.read_csv("../streamlit101/iris.csv")
st.dataframe(df)


st.divider()
# Displaying Pandas Dataframe, Tables and JSON
df = pd.read_csv("../streamlit101/iris.csv")

# Method 1
st.dataframe(df, height=200, width=300)

st.dataframe(df.style.highlight_max(axis=0),
             height=200, width=300)


# Method 2: Static Table
st.help(st.table)
st.table(df)

# Method 3: Using superfunction
st.write(df.head())

# Method 4: JSON format
st.json(df.to_json())
st.json(df.to_json(orient="records"))
st.json(df.to_json(orient="split"))
st.json(df.to_json(orient="index"))
st.json(df.to_json(orient="columns"))
st.json({"data":"name"})

# Display code
my_code = """
def say_hello():
    print("Hello, Streamlit!")
"""

st.code(my_code, language="python")


# Working with Widgets:
# Buttons/Radio/Checkbox/Select
st.divider()
button = st.button("Submit") # returns True if the button is clicked.
st.write(button)
if button:
    st.write("Thanks for submitting!")

button = st.button("Submit", key="new02")
st.write(st.radio)
if button:
    st.write("First name is Sal")

status = st.radio(label="What is your status?",
                  options=["Active", "Inactive"],
                  key="status",
                  index=None,
                  horizontal=True,
                  captions=["Eat", "Drink"])

st.write(status)

if status == "Inactive":
    st.warning("Inactive")
elif status == "Active":
    st.success("Active")

st.help(st.echo)

with st.echo():
    st.write("This code is printed")

if st.checkbox("Show/Hide"):
    st.text("Show something")

# Working with beta_expander
a = st.expander("Python")
with a:
    st.text("Hello Python!")

st.help(st.expander)

# select and multiple select
my_lang = ["Python", "Julia", "Go", "Rust"]
choice = st.selectbox(label="Select an option",
                      options=my_lang)
st.write(f"You selected {choice}")
st.multiselect(label="Select an option",
               options=["Option 1", "Option 2", "Option 3"],
               default=["Option 1"])

# Slider: for numerical sliders
# Select Slider: for select sliders
# Text Input: for text input
# Number Input: for number input

st.text_input(label="Enter your name",
              placeholder="Enter your name",
              key="name", type="password")

st.help(st.text_input)

# Display Images
file = Image.open("../streamlit101/image_03.jpg")
st.image(file,
         use_column_width=True,
         caption="Image 3")

st.date_input("Appointment")
st.time_input("Time")


# Configuring Streamlit Page: Must be the first activity we do.
st.help(st.set_option)

# st.set_page_config(page_title=,
# page_icon=":tada:",
# layout="wide")
# --> st.beta_set_page_config()


if __name__ == "__main__":
    main()


