import streamlit as st
import Controllers.ProdutosController as ProdutosController
import Pages.Produtos.Create as PageCreateProdutos



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1,1,1,1,1])
        campos = ['ID','Descrição', 'Grupo Produto', 'filename','filetype', 'filesize','Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in ProdutosController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1,1,1,1,1,1,1,1])
            col1.write(item.id_product)
            col2.write(item.description)
            col3.write(item.product_group)
            col4.write(item.filename)
            col5.write(item.filetype)
            col6.write(item.filesyze)
            button_space_excluir = col7.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id_product))
            button_space_alterar = col8.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id_product))

            if on_click_excluir:
                ProdutosController.Excluir(item.id_product)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.id_product))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_product]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateProdutos.Create()
