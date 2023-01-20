from unittest import main
import streamlit as st
import Controllers.DestinosController as DestinosController
import Pages.Destinos.Create as PageCreateDestinos



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1,1])
        campos = ['ID','Descrição', 'Classificação' 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in DestinosController.SelecionarTodos():
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
            col1.write(item.id_destination)
            col2.write(item.description)
            col3.write(item.classification)
            button_space_excluir = col4.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id_destination))
            button_space_alterar = col5.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id_destination))

            if on_click_excluir:
                DestinosController.Excluir(item.id_destination)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.id_destination))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_destination]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateDestinos.Create()
