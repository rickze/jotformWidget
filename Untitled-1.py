from modules import criar_equipamentos, configuracao_tipo_objeto
import streamlit as st
from streamlit_option_menu import option_menu

if "page_configured" not in st.session_state:
    st.set_page_config(page_title="Gestão de Equipamentos", layout="wide")
    st.session_state.page_configured = True

# Menu de topo com ícones
menu_topo = option_menu(
    menu_title=None,
    options=["Home", "Equipamentos", "Destinatários", "Manutenção", "Relatórios"],
    icons=["house", "truck", "building", "wrench", "report"],
    orientation="horizontal"
)

# Menu lateral dependente do menu de topo
if menu_topo == "Home":
    st.sidebar.header("⚙️ Configurações")
    config_secao = st.sidebar.radio("Área:", ["Equipamentos", "Manutenção", "Destinatários"])
    if config_secao == "Equipamentos":
        submenu = st.sidebar.radio("Opção:", [
            "Categorias",
            "Tipo de Objeto",
            "Classificação (Classes)",
            "Abate de equipamento",
            "Tipo Tração",
            "Contadores",
            "Gestão de campos"
        ])
        if submenu == "Tipo de Objeto":
            with st.container():
                configuracao_tipo_objeto.show()
        elif submenu == "Categorias":
            st.info("[Placeholder] Configuração: Categorias")
        else:
            st.info(f"[Placeholder] Configuração: {submenu}")
    elif config_secao == "Manutenção":
        submenu = st.sidebar.radio("Opção:", ["Tipos de Planos"])
        st.info(f"[Placeholder] Configuração: {submenu}")
    elif config_secao == "Destinatários":
        submenu = st.sidebar.radio("Opção:", ["Tipo de destinatário"])
        st.info(f"[Placeholder] Configuração: {submenu}")
    elif config_secao == "Relatórios":
        submenu = st.sidebar.radio("Opção:", ["Resumo de horas"])
        st.info(f"[Placeholder] Configuração: {submenu}")
        

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
elif menu_topo == "Relatórios":
    st.sidebar.header("🛠️ Relatório de horas")
    submenu = st.sidebar.radio("Horas:", ["Criar Calendário de horas", "Calendáro e liquidação", "Ajustes"])
    st.info(f"[Placeholder] Relatórios → {submenu}")
