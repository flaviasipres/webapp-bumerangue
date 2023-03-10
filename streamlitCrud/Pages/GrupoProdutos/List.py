import streamlit as st
import Controllers.GrupoProdutosController as GrupoProdutosController
import Pages.GrupoProdutos.Create as PageCreateGrupoProdutos



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1])
        campos = ['ID','Descrição', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in GrupoProdutosController.SelecionarTodos():
            col1, col2, col3, col4 = st.columns([1,1,1,1])
            col1.write(item.id_product_group)
            col2.write(item.description)
            button_space_excluir = col3.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id_product_group))
            button_space_alterar = col4.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id_product_group))

            if on_click_excluir:
                GrupoProdutosController.Excluir(item.id_product_group)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.id_product_group))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_product_group]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateGrupoProdutos.Create()
