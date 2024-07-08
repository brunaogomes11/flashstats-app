import streamlit as st
import pandas as pd
import numpy as np
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
