import streamlit as st
import Controllers.FornecedorController as FornecedorController
import models.Fornecedor as fornecedor


def Create():
    idAlteracao = st.experimental_get_query_params()
    fornecedorRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        fornecedorRecuperado = FornecedorController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[fornecedorRecuperado.id_supplier]
        )
        st.title("Alterar fornecedor")
    else:
        st.title("Incluir fornecedor")

    with st.form(key="include_fornecedor"):
        if fornecedorRecuperado == None:
            input_razao_social = st.text_input(label="Insira a Razão Social")
            input_address = st.text_input(label="Insira o seu endereço")
            input_cnpj = st.text_input(label="Insira o seu CNPJ")
        else:
            input_razao_social = st.text_input(label="Insira a Razão Social", value=fornecedorRecuperado.razao_social)
            input_address = st.text_input(label="Insira o seu endereço", value=fornecedorRecuperado.endereco)
            input_cnpj = st.text_input(label="Insira o seu CNPJ", value=fornecedorRecuperado.cnpj)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if fornecedorRecuperado == None:
            FornecedorController.Incluir(fornecedor.Fornecedor(input_razao_social, input_razao_social, input_address, input_cnpj))
            st.success("Fornecedor incluido com sucesso!")
        else:
            st.experimental_set_query_params()
            FornecedorController.Alterar(fornecedor.Fornecedor(fornecedorRecuperado.id_supplier, input_razao_social, input_address, input_cnpj))
            st.success("Fornecedor alterado com sucesso!")
        
        