import streamlit as st
import json
import pandas as pd
from pathlib import Path

CONFIG_PATH = Path("config")
DATA_PATH = Path("data")

def load_json(file):
    with open(CONFIG_PATH / file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file, data):
    with open(CONFIG_PATH / file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_csv_data():
    file_path = DATA_PATH / "equipamentos.csv"
    if file_path.exists():
        return pd.read_csv(file_path)
    return pd.DataFrame(columns=["Numero", "Descricao", "Categoria"])

def save_csv_data(df):
    df.to_csv(DATA_PATH / "equipamentos.csv", index=False)

def show():
    st.title("Criação de Equipamentos")
    df = load_csv_data()
    st.dataframe(df)

    st.subheader("Novo Equipamento")
    with st.form("add_equipamento"):
        categorias = load_json("categorias.json")
        cat_options = sorted(set(c["codigo"] for c in categorias))
        numero_manual = st.text_input("Número (deixe vazio para gerar)")
        descricao = st.text_input("Descrição")
        categoria = st.selectbox("Categoria", cat_options)
        if st.form_submit_button("Guardar"):
            if not descricao or not categoria:
                st.error("Descrição e categoria são obrigatórios.")
                st.stop()

            if numero_manual:
                if numero_manual in df["Numero"].astype(str).values:
                    st.error("Já existe um equipamento com esse número.")
                    st.stop()
                numero = numero_manual
            else:
                base = load_json("dados_base.json")
                intervs = load_json("intervalos.json")
                linha = next((b for b in base if b["categoria"] == categoria), None)
                if not linha:
                    st.error("Configuração da categoria não encontrada.")
                    st.stop()
                cod = linha["intervalo_interno"]
                intv = next((i for i in intervs if i["codigo"] == cod), None)
                if not intv:
                    st.error("Intervalo interno não encontrado.")
                    st.stop()
                numero = str(intv["proximo"]).zfill(8)
                intv["proximo"] += 1
                save_json("intervalos.json", intervs)

            df.loc[len(df)] = [numero, descricao, categoria]
            save_csv_data(df)
            st.success(f"Equipamento {numero} guardado.")
            st.rerun()
