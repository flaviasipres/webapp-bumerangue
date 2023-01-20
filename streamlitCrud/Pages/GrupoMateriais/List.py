from unittest import main
import streamlit as st
import Controllers.GrupoMateriaisController as GrupoMateriaisController
import Pages.GrupoMateriais.Create as PageCreateGrupoGrupoMateriais



def List():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns([1,1,1,1,1,1])
        campos = ['ID','Descrição do Grupo', 'Descrição Detalhada', 'Descrição Alternativa', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in GrupoMateriaisController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
            col1.write(item.id_material_group)
            col2.write(item.group_description)
            col3.write(item.detailed_description)
            col4.write(item.alternative_description)
            button_space_excluir = col5.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id_material_group))
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id_material_group))

            if on_click_excluir:
                GrupoMateriaisController.Excluir(item.id_material_group)
                button_space_excluir.button(
                    'Excluído', 'excluded' + str(item.id_material_group))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id_material_group]
                )
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateGrupoGrupoMateriais.Create()
