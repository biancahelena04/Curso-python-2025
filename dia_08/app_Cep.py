import streamlit as st
import requests
import pandas as pd

url = "https://viacep.com.br/ws/{cep}/json/"


st.title("busca cep")

cep = st.text_input("coloque o cep")

if cep != "":
    try:
        resp = requests.get(url.format(cep=cep))
        data =  pd.DataFrame([resp.json()])
        st.dataframe(data)
    except Exception as err:
        st.error("entre com um cep válido")
