import streamlit as st
import pandas as pd
import numpy as np


#######################################################
################## Help Functions #####################
#######################################################
@st.cache_data
def get_hemnet_data() -> pd.DataFrame:
    try:
        df = pd.read_csv('hemnet_data_clean.csv')
    except FileNotFoundError:
        st.warning('Varning! Kunde inte hitta data att ladda in!!!', icon="⚠️")
        return pd.DataFrame()
    return df


#######################################################
##################### Home page #######################
#######################################################
def intro():
    import streamlit as st

    st.write("# Välkommen till analys av Hemnet-data! :house::house_with_garden:")

    image_path = "./Hemnet.png"
    st.image(image_path,caption='Hemnet logo', use_column_width=True)
    st.markdown(
        """
        ## Vi ska här analysera och visa data från Hemnet!

        övningar: 
        - Längst ner på den här sidan, huvudsidan alltså, visa hemnetdata i en dataframe!
        - Skapa en sida där vi kan se en scatter på pris mot area! Dvs area = x och pris = y
        - Skapa en sida där vi kan se ett histogram för antalet sålda enheter per komun.
        - Visa också ett histogram för antalet rum per enhet.
        - Skapa en sida där vi kan se totala försäljningen per dag och rita ut det med en linjegraf.
        - Klura ut något eget som kan vara bra att visa upp för att framföra information om hemnet-data. 
        - Skapa en sida som har en karta med kordinaterna för de olika husen. Se till att priset reflekterar storleken! 
        """
    )

    hemnet_data = get_hemnet_data()

    st.write(hemnet_data)
    st.sidebar.selectbox('Hello', ['Hi', 'Ho'])

intro()