import this
from turtle import onclick
import streamlit as st
import Controllers.GrupoMateriaisController as GrupoMateriaisController
import models.Grupo_Materiais as grupomateriais


def Create():
    idAlteracao = st.experimental_get_query_params()
    grupomateriaisRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        grupomateriaisRecuperado = GrupoMateriaisController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[grupomateriaisRecuperado.id_material_group]
        )
        st.title("Alterar grupo de materiais")
    else:
        st.title("Incluir grupo de materiais")

    with st.form(key="include_grupomateriais"):
        if grupomateriaisRecuperado == None:
            input_group_description = st.text_input(label="Insira a descrição do grupo de materiais")
            input_detailed_description = st.text_input(label="Insira a descrição detalhada do grupo de materiais")
            input_alternative_description = st.text_input(label="Insira a descrição alternativa do grupo de materiais")
        else:
            input_group_description = st.text_input(label="Insira a descrição do grupo de materiais", value=grupomateriaisRecuperado.group_description)
            input_detailed_description = st.text_input(label="Insira a descrição detalhada do grupo de materiais",  value=grupomateriaisRecuperado.detailed_description)
            input_alternative_description = st.text_input(label="Insira a descrição alternativa do grupo de materiais",  value=grupomateriaisRecuperado.alternative_description)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if grupomateriaisRecuperado == None:
            GrupoMateriaisController.Incluir(grupomateriais.GrupoMateriais(input_group_description, input_group_description, input_detailed_description, input_alternative_description))
            st.success("Grupo de materiais incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            GrupoMateriaisController.Alterar(grupomateriais.GrupoMateriais(grupomateriaisRecuperado.id_material_group, input_group_description, input_group_description, input_detailed_description, input_alternative_description))
            st.success("Grupo de materiais alterado com sucesso!")
        
        