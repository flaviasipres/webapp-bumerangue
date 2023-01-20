import streamlit as st
import Controllers.UsuarioController as UsuarioController
import Pages.Users.Create as PageCreateCliente



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1,1,1,1,1,1])
        campos = ['ID','Nome', 'Endereço', 'CPF', 'Email', 'Telefone', 'Senha', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in UsuarioController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1,1,1,1,1,1,1,1,1])
            col1.write(item.id_user)
            col2.write(item.nome)
            col3.write(item.endereco)
            col4.write(item.cpf)
            col5.write(item.email)
            col6.write(item.celular)
            col7.write(item.senha)
            button_space_excluir = col8.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.email))
            button_space_alterar = col9.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.email))

            if on_click_excluir:
                UsuarioController.Excluir(item.id_user)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.email))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_user]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateCliente.Create()
