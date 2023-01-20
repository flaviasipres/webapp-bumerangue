from unittest import main
import streamlit as st
import Controllers.FornecedorController as FornecedorController
import Pages.Suppliers.Create as PageCreateFornecedor



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1,1,1])
        campos = ['ID','Razão Social', 'Endereço', 'CNPJ', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in FornecedorController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
            col1.write(item.id_supplier)
            col2.write(item.razao_social)
            col3.write(item.endereco)
            col4.write(item.cnpj)
            button_space_excluir = col5.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.cnpj))
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.cnpj))

            if on_click_excluir:
                FornecedorController.Excluir(item.id_supplier)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.cnpj))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_supplier]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateFornecedor.Create()
