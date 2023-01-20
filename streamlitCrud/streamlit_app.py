import streamlit as st
import Pages.Users.Create as PageCreateUsuario
import Pages.Users.List as PageListUsuario
import Pages.Suppliers.Create as PageCreateFornecedor
import Pages.Suppliers.List as PageListFornecedor
import Pages.Hospitals.Create as PageCreateHospitals
import Pages.Hospitals.List as PageListHospitals
import Pages.GrupoResiduos.Create as PageCreateGrupoResiduos
import Pages.GrupoResiduos.List as PageListGrupoResiduos
import Pages.SubgrupoResiduos.Create as PageCreateSubgrupoResiduos
import Pages.SubgrupoResiduos.List as PageListSubgrupoResiduos
import Pages.TipoResiduos.Create as PageCreateTipoResiduos
import Pages.TipoResiduos.List as PageListTipoResiduos
import Pages.GrupoMateriais.Create as PageCreateGrupoMateriais
import Pages.GrupoMateriais.List as PageListGrupoMateriais
import Pages.Materiais.Create as PageCreateMateriais
import Pages.Materiais.List as PageListMateriais
import Pages.TecnologiaTratamento.Create as PageCreateTecnologiaTratamento
import Pages.TecnologiaTratamento.List as PageListTecnologiaTratamento
import Pages.Destinos.Create as PageCreateDestinos
import Pages.Destinos.List as PageListDestinos
import Pages.GrupoProdutos.Create as PageCreateGrupoProdutos
import Pages.GrupoProdutos.List as PageListGrupoProdutos
import Pages.Produtos.Create as PageCreateProdutos
import Pages.Produtos.List as PageListProdutos


st.set_page_config(layout='wide')

st.title("SISTEMA SICACIFE")
st.header("Este sistema encontra-se em construção")

st.sidebar.title("Menu")


Page_usuario = st.sidebar.selectbox(
    'Usuário', ["",'Incluir', 'Consultar'], 0)

if Page_usuario == 'Consultar':
    PageListUsuario.List()

if Page_usuario == 'Incluir':
    st.experimental_set_query_params()
    PageCreateUsuario.Create()

Page_supplier = st.sidebar.selectbox(
    'Fornecedor', ["",'Incluir', 'Consultar'], 0)

if Page_supplier == 'Consultar':
    PageListFornecedor.List()

if Page_supplier == 'Incluir':
    st.experimental_set_query_params()
    PageCreateFornecedor.Create()
    
Page_hospital = st.sidebar.selectbox(
    'Hospital', ["",'Incluir', 'Consultar'], 0)

if Page_hospital == 'Consultar':
    PageListHospitals.List()

if Page_hospital == 'Incluir':
    st.experimental_set_query_params()
    PageCreateHospitals.Create()


Page_gruporesiduos = st.sidebar.selectbox(
    'Grupo de Resíduos', ["",'Incluir', 'Consultar'], 0)

if Page_gruporesiduos == 'Consultar':
    PageListGrupoResiduos.List()

if Page_gruporesiduos == 'Incluir':
    st.experimental_set_query_params()
    PageCreateGrupoResiduos.Create()

Page_subgruporesiduos = st.sidebar.selectbox(
'Subgrupo de Resíduos', ["",'Incluir', 'Consultar'], key="subgrupo-selectbox")

if Page_subgruporesiduos == 'Consultar':
    PageListSubgrupoResiduos.List()

if Page_subgruporesiduos == 'Incluir':
    st.experimental_set_query_params()
    PageCreateSubgrupoResiduos.Create()


Page_tiporesiduos = st.sidebar.selectbox(
'Tipo de Resíduos', ["",'Incluir', 'Consultar'], key="tiporesiduo-selectbox")

if Page_tiporesiduos == 'Consultar':
    PageListTipoResiduos.List()

if Page_tiporesiduos == 'Incluir':
    st.experimental_set_query_params()
    PageCreateTipoResiduos.Create()


Page_grupomateriais = st.sidebar.selectbox(
'Grupo de Materiais', ["",'Incluir', 'Consultar'], key="grupomateriais-selectbox")

if Page_grupomateriais == 'Consultar':
    PageListGrupoMateriais.List()

if Page_grupomateriais == 'Incluir':
    st.experimental_set_query_params()
    PageCreateGrupoMateriais.Create()


Page_materiais = st.sidebar.selectbox(
'Materiais', ["",'Incluir', 'Consultar'], key="materiais-selectbox")

if Page_materiais == 'Consultar':
    PageListMateriais.List()

if Page_materiais == 'Incluir':
    st.experimental_set_query_params()
    PageCreateMateriais.Create()
    

Page_tecnologia_tratamento = st.sidebar.selectbox(
'Tecnologia de Tratamento', ["",'Incluir', 'Consultar'], key="tecnologia-tratamento")

if Page_tecnologia_tratamento == 'Consultar':
    PageListTecnologiaTratamento.List()

if Page_tecnologia_tratamento == 'Incluir':
    st.experimental_set_query_params()
    PageCreateTecnologiaTratamento.Create()

Page_destinos = st.sidebar.selectbox(
'Destinos', ["",'Incluir', 'Consultar'], key="destinos")

if Page_destinos == 'Consultar':
    PageListDestinos.List()

if Page_destinos == 'Incluir':
    st.experimental_set_query_params()
    PageCreateDestinos.Create()

Page_grupo_produtos = st.sidebar.selectbox(
'Grupo de Produtos', ["",'Incluir', 'Consultar'], key="grupoprodutos")

if Page_grupo_produtos == 'Consultar':
    PageListGrupoProdutos.List()

if Page_grupo_produtos == 'Incluir':
    st.experimental_set_query_params()
    PageCreateGrupoProdutos.Create()


Page_produtos = st.sidebar.selectbox(
'Produtos', ["",'Incluir', 'Consultar'], key="produtos")

if Page_produtos == 'Consultar':
    PageListProdutos.List()

if Page_produtos == 'Incluir':
    st.experimental_set_query_params()
    PageCreateProdutos.Create()