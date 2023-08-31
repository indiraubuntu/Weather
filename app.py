# APP Weather

import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components


st.header('Méteo France')

col1, col2 = st.columns(2)

with col1:
   st.selectbox('Entrez ville', ['Carcassone', 'Lyon'])
with col2:
   st.button('GO', [])

components.html(
        """
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d396196.0038535864!2d-74.0059726300296!3d40.71277579459063!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2sca!4v1585325999776!5m2!1sen!2sca" width="800" height="600" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        """,
    width=800,
    height=600,
    )

## "selmane"