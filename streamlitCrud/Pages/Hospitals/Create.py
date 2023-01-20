import this
from turtle import onclick
import streamlit as st
import Controllers.HospitalController as HospitalController
import models.Hospital as hospital


def Create():
    idAlteracao = st.experimental_get_query_params()
    hospitalRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        hospitalRecuperado = HospitalController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[hospitalRecuperado.id_hospital]
        )
        st.title("Alterar hospital")
    else:
        st.title("Incluir hospital")

    with st.form(key="include_hospital"):
        if hospitalRecuperado == None:
            input_razao_social = st.text_input(label="Insira a Razão Social")
            input_cnpj = st.text_input(label="Insira o seu CNPJ")
        else:
            input_razao_social = st.text_input(label="Insira a Razão Social", value=hospitalRecuperado.razao_social)
            input_cnpj = st.text_input(label="Insira o seu CNPJ", value=hospitalRecuperado.cnpj)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if hospitalRecuperado == None:
            HospitalController.Incluir(hospital.Hospital(input_razao_social, input_razao_social, input_cnpj))
            st.success("Hospital incluido com sucesso!")
        else:
            st.experimental_set_query_params()
            HospitalController.Alterar(hospital.Hospital(hospitalRecuperado.id_hospital, input_razao_social, input_cnpj))
            st.success("Hospital alterado com sucesso!")
        
        