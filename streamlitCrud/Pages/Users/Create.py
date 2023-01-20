import this
from turtle import onclick
import streamlit as st;
import Controllers.UsuarioController as UsuarioController
import models.Usuario as usuario


def Create():
    idAlteracao = st.experimental_get_query_params()
    usuarioRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        usuarioRecuperado = UsuarioController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[usuarioRecuperado.id_user]
        )
        st.title("Alterar usuário")
    else:
        st.title("Incluir usuário")

    with st.form(key="include_usuario"):
        if usuarioRecuperado == None:
            input_name = st.text_input(label="Insira o seu nome")
            input_address = st.text_input(label="Insira o seu endereço")
            input_cpf = st.text_input(label="Insira o seu CPF")
            input_email = st.text_input(label="Insira o seu email")
            input_mobilephone = st.text_input(label="Insira o seu telefone")
            input_password = st.text_input(label="Insira a sua senha")
        else:
            input_name = st.text_input(label="Insira o seu nome", value=usuarioRecuperado.nome)
            input_address = st.text_input(label="Insira o seu endereço", value=usuarioRecuperado.endereco)
            input_cpf = st.text_input(label="Insira o seu CPF", value=usuarioRecuperado.cpf)
            input_email = st.text_input(label="Insira o seu email", value=usuarioRecuperado.email)
            input_mobilephone = st.text_input(label="Insira o seu telefone", value=usuarioRecuperado.celular)
            input_password = st.text_input(label="Insira a sua senha", value=usuarioRecuperado.senha)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if usuarioRecuperado == None:
            UsuarioController.Incluir(usuario.Usuario(input_name, input_name, input_address, input_cpf, input_email, input_mobilephone, input_password))
            st.success("Usuário incluido com sucesso!")
        else:
            st.experimental_set_query_params()
            UsuarioController.Alterar(usuario.Usuario(usuarioRecuperado.id_user, input_name, input_address, input_cpf, input_email, input_mobilephone, input_password))
            st.success("Usuário alterado com sucesso!")
        
        