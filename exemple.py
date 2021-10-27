
import streamlit as st
import pandas as pd
import streamlit as s
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Hello world!")

uploaded_file = st.file_uploader("nutrition_app")
if uploaded_file is not None
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)
st.title("nutrition_app")
