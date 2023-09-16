import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

image = Image.open("data_streamlit/hartjes.png")
st.image(image, use_column_width=True)

st.title ("Stijn & Mariska")
st.subheader("Een app die je helpt bij het plannen van betoverende en spontane dates.")

st.header("Op welke date gaan we....?")
data = {
    "Date Ideeën": ["Panorama Mesdag", "Lange Jan", "Hardlopen en fietsen door Wassenaar", "Squashen", "Boulderen", "van Kleef proeverij", "Cocktails drinken"],
    "Alcohol": [False, False, False, False, False, True, True],
    "foto": ["data_streamlit/panorama.png","data_streamlit/langejan.png", "data_streamlit/wassenaar.png", "data_streamlit/squashen.png", "data_streamlit/boulderen.png", "data_streamlit/dronken1.png", "data_streamlit/cocktails.png"]
}

df = pd.DataFrame(data)


option = st.selectbox(
    'Wel of geen alcohol?',
     ["Tuuuurlijk", "Neee joh, even gezond doen"])


if st.button("Klik hier maar"):
    # Filter de rijen op basis van de "Alcohol" kolom (bijv. als je alleen ideeën zonder alcohol wilt)
    if option == "Tuuuurlijk":
        filtered_df = df[df["Alcohol"] == True]
    else:
        filtered_df = df[df["Alcohol"] == False]

    # Genereer een willekeurig getal om een willekeurig date-idee te selecteren
    random_index = np.random.randint(0, len(filtered_df))

    # Haal het willekeurig geselecteerde date-idee op
    random_date_idea = filtered_df.iloc[random_index]["Date Ideeën"]

    # Toon het willekeurig geselecteerde date-idee
    st.write("Willekeurig date-idee:", random_date_idea)

    image = Image.open(filtered_df.iloc[random_index]["foto"])
    st.image(image, use_column_width=True)

    st.success("Jeeeeeej, tot dan! 😘")