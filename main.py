import streamlit as st
import numpy as np
import warnings
import pandas as pd

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

import requests
pages = {
    "Analise de dados" : [
        st.Page("app_pages/dataframe.py", title="Dataframe"),
        st.Page("app_pages/dashboard.py", title="Dashboard")
    ],
    "Previsões" : [
    ]
}

pg = st.navigation(pages)
pg.run()
