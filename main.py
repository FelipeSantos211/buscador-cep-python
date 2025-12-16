import streamlit as st
import requests

st.title("Buscador de CEP")

cep = st.text_input("Digite o CEP (somente números):")

def buscarcep(cep):
    st.divider()
    st.subheader("Informações do CEP")
    cep = cep.replace(".", "").replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        st.error("Por favor, insira um CEP válido com 8 dígitos numéricos.")
    else:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            st.error("Não foi possível buscar o CEP. Tente novamente em instantes.")
        else:
            data = response.json()
            if data.get("erro"):
                st.error("CEP não encontrado.")
            else:
                st.table({
                    "Logradouro": data.get("logradouro", ""),
                    "Bairro": data.get("bairro", ""),
                    "Cidade": data.get("localidade", ""),
                    "UF": data.get("uf", "")})

if st.button("Buscar"):
    buscarcep(cep)



