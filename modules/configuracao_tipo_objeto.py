
import streamlit as st
import json
from pathlib import Path
import pandas as pd

def show():
    CONFIG_PATH = Path("config")
    TIPOS_FILE = CONFIG_PATH / "tipos_objeto.json"

    st.title("📋 Configuração dos Tipos de Equipamento")

    if TIPOS_FILE.exists():
        with open(TIPOS_FILE, "r", encoding="utf-8") as f:
            tipos = json.load(f)
    else:
        tipos = []
    
    tipos_df = pd.DataFrame(tipos)
    if not tipos_df.empty:
        tipos_df = tipos_df[["codigo", "descricao", "stocks"]]
        tipos_df.columns = ["Tipo objeto técnico", "Texto tipo objeto", "Administração de Stocks"]
    st.sidebar.subheader("Lista de Tipos de Equipamento")
    st.sidebar.dataframe(tipos_df, use_container_width=True)
    
    st.sidebar.markdown("---")
    codigos = [t["codigo"] for t in tipos]
    selecao = st.sidebar.selectbox("Selecionar código existente ou criar novo", ["Novo"] + codigos)
    
    if selecao == "Novo":
        tipo = {
            "codigo": "",
            "descricao": "",
            "stocks": True,
            "gestao": {
                "tipo_gestao": "Individual",
                "unidade": "UN",
                "propriedade": "Próprio",
                "doc_envio": True,
                "doc_atividade": True,
                "faturacao_mobilizacao": False,
                "faturacao_atividade": True,
                "planeado": True
            }
        }
    else:
        tipo = next((t for t in tipos if t["codigo"] == selecao), None)
    
    st.subheader("📌 Edição do Tipo de Equipamento")
    col1, col2 = st.columns([2, 3])
    
    with col1:
        tipo["codigo"] = st.text_input("Código Técnico", value=tipo["codigo"])
        tipo["descricao"] = st.text_input("Descrição", value=tipo["descricao"])
        tipo["stocks"] = st.checkbox("Administração de Stocks (Envio)", value=tipo["stocks"])
    
    with col2:
        st.markdown("### Preenchimento automático da aba Gestão")
        tipo["gestao"]["tipo_gestao"] = st.text_input(
            "Tipo de Gestão",
            value=tipo["gestao"].get("tipo_gestao", ""),
            key="tipo_gestao_input"
        )
        tipo["gestao"]["unidade"] = st.text_input(
            "Unidade Básica",
            value=tipo["gestao"].get("unidade", ""),
            key="unidade_input"
        )
        tipo["gestao"]["propriedade"] = st.text_input(
            "Tipo de Propriedade",
            value=tipo["gestao"].get("propriedade", ""),
            key="propriedade_input"
        )
        
        st.markdown("**Documentos Permitidos**")
        tipo["gestao"]["doc_envio"] = st.checkbox(
            "Doc. Envio",
            value=tipo["gestao"].get("doc_envio", False),
            key="doc_envio_checkbox"
        )
        tipo["gestao"]["doc_atividade"] = st.checkbox(
            "Doc. Atividade",
            value=tipo["gestao"].get("doc_atividade", False),
            key="doc_atividade_checkbox"
        )
        
        st.markdown("**Tipo de Faturação**")
        tipo["gestao"]["faturacao_mobilizacao"] = st.checkbox(
            "Doc. p/mobilização",
            value=tipo["gestao"].get("faturacao_mobilizacao", False),
            key="faturacao_mobilizacao_checkbox"
        )
        tipo["gestao"]["faturacao_atividade"] = st.checkbox(
            "Doc. Atividade (Faturação)",
            value=tipo["gestao"].get("faturacao_atividade", False),
            key="faturacao_atividade_checkbox"
        )
        
        tipo["gestao"]["planeado"] = st.radio(
            "Pode ser planeado",
            ["Sim", "Não"],
            index=0 if tipo["gestao"].get("planeado", True) else 1,
            key="planeado_radio"
        ) == "Sim"
    
    if st.button("💾 Guardar Tipo de Equipamento"):
        tipos = [t for t in tipos if t["codigo"] != tipo["codigo"]]
        tipos.append(tipo)
        with open(TIPOS_FILE, "w", encoding="utf-8") as f:
            json.dump(tipos, f, indent=4, ensure_ascii=False)
        st.success(f"Tipo de equipamento {tipo['codigo']} guardado com sucesso.")
        st.rerun()
