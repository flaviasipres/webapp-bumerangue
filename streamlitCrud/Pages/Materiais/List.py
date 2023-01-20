import streamlit as st
import Controllers.MateriaisController as MateriaisController
import Pages.Materiais.Create as PageCreateMateriais



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1,1,1])
        campos = ['ID','Descrição', 'Grupo do material', 'Foto', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in MateriaisController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
            col1.write(item.id_materialp)
            col2.write(item.description)
            col3.write(item.material_grup)
            col4.write(item.foto)
            button_space_excluir = col5.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id_material))
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id_material))

            if on_click_excluir:
                MateriaisController.Excluir(item.id_material)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.id_material))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_material]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateMateriais.Create()
