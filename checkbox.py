import streamlit as st
import numpy as np

case_id = st.text_input("Please enter an ID")
if case_id:
    options = sorted(np.random.choice([1, 2, 3, 4, 5], 4, replace=False))
    pathways_bool = [st.checkbox(str(_x)) for _x in options]
