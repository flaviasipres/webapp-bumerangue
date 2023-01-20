import this
from turtle import onclick
import streamlit as st
import Controllers.GrupoResiduosController as GrupoResiduosController
import models.Grupo_Residuos as gruporesiduos


def Create():
    idAlteracao = st.experimental_get_query_params()
    gruporesiduosRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        gruporesiduosRecuperado = GrupoResiduosController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[gruporesiduosRecuperado.id_residual_group]
        )
        st.title("Alterar grupo de resíduos")
    else:
        st.title("Incluir grupo de resíduos")

    with st.form(key="include_gruporesíduos"):
        if gruporesiduosRecuperado == None:
            input_description = st.text_input(label="Insira a descrição do grupo de resíduos")
        else:
            input_description = st.text_input(label="Insira a descrição do grupo de resíduos", value=gruporesiduosRecuperado.description)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if gruporesiduosRecuperado == None:
            GrupoResiduosController.Incluir(gruporesiduos.GrupoResiduos(input_description, input_description))
            st.success("Grupo de resíduos incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            GrupoResiduosController.Alterar(gruporesiduos.GrupoResiduos(gruporesiduosRecuperado.id_residual_group, input_description))
            st.success("Grupo de resíduos alterado com sucesso!")
        
        