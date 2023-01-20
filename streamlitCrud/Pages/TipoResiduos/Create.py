import this
from turtle import onclick
import streamlit as st
import Controllers.TipoResiduosController as TipoResiduosController
import Controllers.GrupoResiduosController as GrupoResiduosController
import Controllers.SubgrupoResiduosController as SubgrupoResiduosController
import models.Tipo_Residuos as tiporesiduos


def Create():
    idAlteracao = st.experimental_get_query_params()
    tiporesiduosRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        tiporesiduosRecuperado = TipoResiduosController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[tiporesiduosRecuperado.id_residual_type]
        )
        st.title("Alterar Tipo de resíduos")
    else:
        st.title("Incluir Tipo de resíduos")


    grupos = []
    for item in GrupoResiduosController.SelecionarTodos():
        grupos.append(item.description)
    grupo = tuple(grupos)

    subgrupos = []
    for item in SubgrupoResiduosController.SelecionarTodos():
        subgrupos.append(item.description)
    subgrupo = tuple(subgrupos)

    with st.form(key="include_tiporesíduos"):
        if tiporesiduosRecuperado == None:
            grupo_description = st.selectbox("Escolha o grupo do resíduo", grupo)
            subgrupo_description = st.selectbox("Escolha o subgrupo do resíduo", subgrupo)
            input_description = st.text_input(label="Insira a descrição do Tipo de resíduos")
        else:
            grupo_description = st.selectbox("Escolha o grupo do resíduo", grupo)
            subgrupo_description = st.selectbox("Escolha o subgrupo do resíduo", subgrupo)
            input_description = st.text_input(label="Insira a descrição do Tipo de resíduos", value=tiporesiduosRecuperado.description)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if tiporesiduosRecuperado == None:
            TipoResiduosController.Incluir(tiporesiduos.TipoResiduos(input_description, input_description, grupo_description, subgrupo_description))
            st.success("Tipo de resíduos incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            TipoResiduosController.Alterar(tiporesiduos.TipoResiduos(tiporesiduosRecuperado.id_residual_type, grupo_description, subgrupo_description, input_description))
            st.success("Tipo de resíduos alterado com sucesso!")
        
        