import this
from turtle import onclick
import streamlit as st
import Controllers.TecnologiasTratamentoController as TecnologiasTratamentoController
import models.Tecnologia_Tratamento as tecnologiatratamento


def Create():
    idAlteracao = st.experimental_get_query_params()
    tecnologiatratamentoRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        tecnologiatratamentoRecuperado = TecnologiasTratamentoController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[tecnologiatratamentoRecuperado.id_treatment_technology]
        )
        st.title("Alterar tecnologia de tratamento")
    else:
        st.title("Incluir tecnologia de tratamento")

    with st.form(key="include_tecnologiatratamento"):
        if tecnologiatratamentoRecuperado == None:
            input_description = st.text_input(label="Insira a descrição da tecnologia de tratamento")
        else:
            input_description = st.text_input(label="Insira a descrição da tecnologia de tratamento", value=tecnologiatratamentoRecuperado.description)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if tecnologiatratamentoRecuperado == None:
            TecnologiasTratamentoController.Incluir(tecnologiatratamento.TecnologiaTratamento(input_description, input_description))
            st.success("Tecnologia de Tratamento incluída com sucesso!")
        else:
            st.experimental_set_query_params()
            TecnologiasTratamentoController.Alterar(tecnologiatratamento.TecnologiaTratamento(tecnologiatratamentoRecuperado.id_treatment_technology, input_description))
            st.success("Tecnologia de Tratamento alterada com sucesso!")
        
        