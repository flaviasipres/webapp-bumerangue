import streamlit as st
import Controllers.GrupoProdutosController as GrupoProdutosController
import models.Grupo_Produtos as grupoprodutos


def Create():
    idAlteracao = st.experimental_get_query_params()
    grupoprodutosRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        grupoprodutosRecuperado = GrupoProdutosController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[grupoprodutosRecuperado.id_product_group]
        )
        st.title("Alterar grupo de produtos")
    else:
        st.title("Incluir grupo de produtos")

    with st.form(key="include_grupoprodutos"):
        if grupoprodutosRecuperado == None:
            input_description = st.text_input(label="Insira a descrição do grupo de produtos")
        else:
            input_description = st.text_input(label="Insira a descrição do grupo de produtos", value=grupoprodutosRecuperado.description)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if grupoprodutosRecuperado == None:
            GrupoProdutosController.Incluir(grupoprodutos.GrupoProdutos(input_description, input_description))
            st.success("Grupo de produtos incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            GrupoProdutosController.Alterar(grupoprodutos.GrupoProdutos(grupoprodutosRecuperado.id_product_group, input_description))
            st.success("Grupo de produtos alterado com sucesso!")
        
        