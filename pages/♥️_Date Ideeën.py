import streamlit as st
from PIL import Image
import pandas as pd

image = Image.open("data_streamlit/hartjes.png")
st.image(image, use_column_width=True)
st.write(" ")
st.title("Mariska & Stijn's Date Roulette")
st.subheader("Een app die je helpt bij het plannen van betoverende en spontane dates.")

# achilles_goals = st.slider('Achilles Goals', 0, 40)  # 👈 this is a widget
# st.write(achilles_goals, 'squared is', achilles_goals * achilles_goals)

# chart_data = pd.DataFrame(
#      [[1, 0, 0], [1, 1, 0], [2, 0, 2]],
#      columns=['Mariska', 'Daphne', 'Danique'])

# st.line_chart(chart_data)

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'Welke wedstrijd?',
#     ('DES', 'Maassluis', 'TOP')
# )
import streamlit as st
import pandas as pd
import numpy as np

data = {
    "Date Ideeën": ["Panorama Mesdag", "Lange Jan", "Hardlopen en fietsen door Wassenaar", "Squashen", "Boulderen", "van Kleef proeverij", "Cocktails drinken"],
    "Alcohol": [False, False, False, False, False, True, True],
    "foto": ["panorama.png","langejan.png", "wassenaar.png", "squashen.png", "boulderen.png", "dronken1.png", "cocktails.png"]
}

df = pd.DataFrame(data)
# st.table(df)
st.markdown(df["Date Ideeën"].to_frame().to_html(index=False), unsafe_allow_html=True)
