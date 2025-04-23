from modules import criar_equipamentos
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Gestão de Equipamentos", layout="wide")

# Menu de topo com ícones
menu_topo = option_menu(
    menu_title=None,
    options=["Home", "Equipamentos", "Destinatários", "Manutenção"],
    icons=["house", "truck", "building", "wrench"],
    orientation="horizontal"
)

# Menu lateral dependente do menu de topo
if menu_topo == "Home":
    st.sidebar.header("⚙️ Configurações")
    config_secao = st.sidebar.radio("Área:", ["Equipamentos", "Manutenção", "Destinatários"])
    if config_secao == "Equipamentos":
        st.sidebar.write("- Categorias")
        st.sidebar.write("- Tipo de Objeto")
        st.sidebar.write("- Classificação (Classes)")
        st.sidebar.write("- Abate de equipamento")
        st.sidebar.write("- Tipo Tração")
        st.sidebar.write("- Contadores")
        st.sidebar.write("- Gestão de campos")
    elif config_secao == "Manutenção":
        st.sidebar.write("- Tipos de Planos")
    elif config_secao == "Destinatários":
        st.sidebar.write("- Tipo de destinatário")

elif menu_topo == "Equipamentos":
    st.sidebar.header("📦 Gestão de Equipamentos")
    submenu = st.sidebar.radio("Secção:", ["Criar Novo", "Editar", "Listagem", "Movimentação", "Documento de envio"])
    if submenu == "Criar Novo":
        criar_equipamentos.show()
    else:
        st.info(f"[Placeholder] Secção selecionada: {submenu}")
    st.sidebar.markdown("**Stocks**")
    st.sidebar.write("- Listagem")
    st.sidebar.markdown("**Tarifas**")
    st.sidebar.write("- Criar")
    st.sidebar.write("- Modificar")
    st.sidebar.write("- Listagem")
    st.sidebar.markdown("**Faturação/liquidação**")
    st.sidebar.write("- Calendário de liquidação")
    st.sidebar.write("- Verificação de Erros")
    st.sidebar.write("- Faturação")

elif menu_topo == "Destinatários":
    st.sidebar.header("🏢 Gestão de Destinatários")
    submenu = st.sidebar.radio("Ações:", ["Criar Novo", "Editar", "Listagem"])
    st.info(f"[Placeholder] Destinatários → {submenu}")

elif menu_topo == "Manutenção":
    st.sidebar.header("🛠️ Gestão de Manutenção")
    submenu = st.sidebar.radio("Plano:", ["Criar Plano de manutenção", "Criar Nota de Manutenção", "Criar Ordem de Manutenção"])
    st.info(f"[Placeholder] Manutenção → {submenu}")
