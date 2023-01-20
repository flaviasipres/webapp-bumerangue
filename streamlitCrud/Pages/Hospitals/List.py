from unittest import main
import streamlit as st
import Controllers.HospitalController as HospitalController
import Pages.Hospitals.Create as PageCreateHospital



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1,1])
        campos = ['ID','Razão Social', 'CNPJ', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in HospitalController.SelecionarTodos():
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
            col1.write(item.id_hospital)
            col2.write(item.razao_social)
            col3.write(item.cnpj)
            button_space_excluir = col4.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.cnpj))
            button_space_alterar = col5.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.cnpj))

            if on_click_excluir:
                HospitalController.Excluir(item.id_hospital)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.cnpj))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_hospital]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateHospital.Create()
