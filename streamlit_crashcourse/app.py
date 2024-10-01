import time

import streamlit as st
import pandas as pd
import datetime
import time
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
#Text elements:
st.text("This is a text")
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")

st.write("This is a superfunction")
st.write(print("something"))

st.markdown("This is *markdown*")
st.latex("\int")
st.json("""{"data": "This is streamlit"}""")
st.code("""
println("hello streamlit")
""", language="julia")

st.code("""
#include <iostream>
using namespace std;

int main() 
{
    
    std::cout << "This is C++" << endl;
    return 0;
}
""", language="c")

st.code("""
#include <iostream>
using namespace std;

int main() 
{

    std::cout << "This is C++" << endl;
    return 0;
}
""", language="c", line_numbers=True)

# ------------------------------------------------------------------------------
# Error elements
st.error("This is an error", icon=":material/thumb_up:")
st.exception("This is an exception")
st.info("This is an info")
st.success("This is a success")
st.warning("This is a warning")

# -----------------------------------------------------------------------------
# Input widgets:
first_name = st.text_input("First name")
password = st.text_input("Password", type="password")
message = st.text_area("Message")
date = st.date_input("Date")

appointment_time = st.time_input("Appointment time", datetime.time(12, 0, 0))
age = st.number_input("Age", min_value=0, max_value=120, step=1, value=20)
gender = st.radio("Gender", ("Male", "Female"), index=1, horizontal=True)

enable = st.toggle("Enable Picker", value=True)
level = st.checkbox("Level Picker", value=False, disabled=True)

# -----------------------------------------------------------------------------
# Sliders & Selectors:
countries = st.selectbox("Countries", ("USA", "Canada", "Mexico"), index=1)
programming_languages = st.multiselect(
    "Programming Languages", ("Python", "R", "Julia", "Rust", "C++", "Java"),
    default=["Python"])
st.slider("Rating", min_value=0, max_value=10, step=1, value=5)

slider_options = ['Text Slider', 'Range Slider', 'Other']
text_slider = ["Excellent", "Very Good", "Medium", "Poor", "Very Poor"]
range_slider = range(1, 11, 1)

zipped_options = list(zip(slider_options, [text_slider, range_slider]))
print(zipped_options)
slid = st.radio("How would you like to rate this project?: ",
                slider_options, index=None)
st.write("You chose: ", slid)

if slid is not None and slid != slider_options[2]:
    print(slid)
    options = zipped_options[slider_options.index(slid)]
    print(options)
    st.select_slider("Feel free to move the slider: ",
                     options=options[1])
elif slid == slider_options[2]:
    # st.slider(msg, start_num, end_num, step-size)
    st.slider("Use the slider below if you would prefer a percentage range : ", 1, 100, 1)

ranking = st.select_slider("Ranking: ", ["Junior Dev", "Mid Dev", "Senior Dev", "Architect"])

# -----------------------------------------------------------------------------
st.divider()

if enable:
    st.write(f"Details: {first_name}, {password}, {message}, "
             f"{date}, {appointment_time}, {age}, {gender}, "
             f"{countries}, {programming_languages}, "
             f"{level}, {ranking}")
    color = st.color_picker("Pick a color")
    st.write(color)


# -----------------------------------------------------------------------------
# Data Elements:

def load_data(data) -> pd.DataFrame:
    return pd.read_csv(data)


df = load_data("iris.csv")
st.dataframe(df)
st.table(df.head())
edited_df = st.data_editor(df)

st.json(df.to_json())
st.json(df.to_json(orient="split"))
st.json(df.to_json(orient="records"))

# ---------------------------------------------------------------------------------------
# connection to a database
# st.connection()


# ---------------------------------------------------------------------------------------
# Media Elements:
img = st.image("image_01.jpg", use_column_width=True, caption="Imagae in st")
audio = st.audio("song.mp3", "rb", start_time=0, end_time=10)
audio_file = open("../streamlit101/song.mp3", "rb")
# print(audio_file)
st.audio(audio_file.read(), loop=False, autoplay=False)

# ---------------------------------------------------------------------------------------
# Video Elements:
# st.video()

if st.button("Take a picture"):
    pic = st.camera_input(label="Take a picture")

    # saving picture from user
    pic.getbuffer()

    with open(f"{pic.name}", "wb") as f:
        f.write(pic.getbuffer())

# Downloads and Uploads:
file_upload = st.file_uploader(label="Upload a file: ", type=".csv")
if file_upload:
    st.write(pd.read_csv(file_upload))

file = "../streamlit101/iris.csv"
st.download_button(label=f"Download {file}", data=file,
                   file_name="../streamlit101/iris.csv",
                   mime="text/csv", key="download-csv")

# ---------------------------------------------------------------------------------------
# Status Elements:

if st.button("Compute:"):
    with st.spinner(text="Thinking: "):
        time.sleep(0.02)
        st.write("Hello")

    with st.progress(25):
        time.sleep(2)
        st.write("Hello")

    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    st.toast(body="This is a toast")

# ---------------------------------------------------------------------------------------
# Chat Elements: important in case you have LLMs (for LLM UI)

prompt = st.chat_input("Ask something: ")


# Streaming response:
# Need a generator function and some text or data

# Typewriter effec
# t
def stream_data(data, delay: float = 0.02):
    for word in data.split():
        yield word + " "

        time.sleep(delay)


if prompt:
    with st.chat_message("user"):
        st.write(f"You typed {prompt}")

    with st.spinner("Thinking"):
        time.sleep(0.2)
        response = f"""
        The `Calculator_App` folder has a `Calculator_App_V2.py` script.
 - The `Calculator_App_V2.py` is a simple arithmetic calculator app made in Python using Tkinter library.
 - It collects and evaluates expressions using the buttons in the calculator.
 - Operations it can perform include addition, subtraction, multiplication, and division.
 - It can also clear the calculator screen, hide and show history. 
 The history is a scrollable Listbox in horizontal and vertical directions.
        """

        # st.write(response)
        st.write_stream(stream_data(response))

response = f"""
        The `Calculator_App` folder has a `Calculator_App_V2.py` script.
 - The `Calculator_App_V2.py` is a simple arithmetic calculator app made in Python using Tkinter library.
 - It collects and evaluates expressions using the buttons in the calculator.
 - Operations it can perform include addition, subtraction, multiplication, and division.
 - It can also clear the calculator screen, hide and show history. 
 The history is a scrollable Listbox in horizontal and vertical directions.
        """

if st.button("Stream response: "):
    # st.write(response)
    st.write_stream(stream_data(response))

# ---------------------------------------------------------------------------------------
# Layout Elements:
"""
1. tabs : to create a tab
2. columns
3. container
4. expander
5. popover
6. dialog
"""
st.divider()
home_tab, about_tab = st.tabs(["Home", "About"])

with home_tab:
    st.subheader("This is a home tab")

with about_tab:
    st.subheader("This is an about tab")
    st.dataframe(df)

# creating columns:
st.divider()
col1, col2, col3 = st.columns(3)

# using context manager
with col1:
    st.title("Columns")

# col2.dataframe(df)
# col2.image("image_02.jpg", use_column_width=True, caption="Image in st")
# OR
with col2:
    st.dataframe(df)
    st.image("image_02.jpg", use_column_width=True, caption="Image in st")

with col3:
    st.color_picker("Pick any color: ", value='#00ABAA')
    st.video("https://www.youtube.com/watch?v=JGwWNGJdvx8")

st.divider()
# for containers
container = st.container(border=True)

# container.write("Container")
# container.dataframe(df)
# OR

with container:
    st.write("Container")

st.divider()
# combine
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    title = col.container(height=120,
                          border=True)
    title.header(":balloon:")

# import streamlit as st
#
# row1 = st.columns(3)
# row2 = st.columns(3)
#
# # Replace this with the path to your image or a URL
# image_url = "image_02.jpg"
#
# for col in row1 + row2:
#     with col.container():
#         st.image(image_url, caption=":balloon:", use_column_width=True)

# Expander and Popover
st.divider()

with st.expander("Expander: "):
    st.dataframe(df)

with st.popover("Popover"):
    st.image("image_02.jpg", use_column_width=True, caption="Image in st")

# Dialog
st.divider()


@st.dialog("Cast your vote", width="large")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()


if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

# ---------------------------------------------------------------------------------------
# Charting/Plotting
st.divider()
st.area_chart(df, x="sepal_length", y="petal_length")

st.line_chart(df, x="sepal_length", y="petal_length")

st.bar_chart(df, x="sepal_length", y="petal_length")

st.scatter_chart(df, x="sepal_length", y="petal_length")

# st.plotly_chart()
# st.altair_chart()
# st.map()
# st.bokeh_chart()

st.help(st.pyplot)
st.write(dir(st))

with st.form("Form: "):
    first_name = st.text_input("First name: ")
    password = st.text_input("Password: ", type="password")
    message = st.text_area("Message: ")
    date = st.date_input("Date: ")
    appointment_time = st.time_input("Appointment time: ")
    age = st.number_input("Age: ", 0, 100)
    gender = st.radio("Gender: ", ["Male", "Female"])
    countries = st.multiselect("Countries: ", ["USA", "UK", "Canada"])
    btn = st.form_submit_button(label="Submit")

import streamlit.components.v1 as stc
stc.html("<h1>Hello, World!</h1>", width=200, height=100, scrolling=True)
stc.iframe("https://www.youtube.com/watch?v=JGwWNGJdvx8", width=500, height=300, scrolling=True)
st.link_button("visit", url="https://www.youtube.com/watch?v=JGwWNGJdvx8")

st.session_state["vote"] # is a dictionary
st.cache_data