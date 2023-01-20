import streamlit as st
import Controllers.SubgrupoResiduosController as SubgrupoResiduosController
import Controllers.GrupoResiduosController as GrupoResiduosController
import models.Subgrupo_Residuos as subgruporesiduos


def Create():
    idAlteracao = st.experimental_get_query_params()
    subgruporesiduosRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        subgruporesiduosRecuperado = SubgrupoResiduosController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[subgruporesiduosRecuperado.id_residual_subgroup]
        )
        st.title("Alterar subgrupo de resíduos")
    else:
        st.title("Incluir subgrupo de resíduos")

    grupos = []
    for item in GrupoResiduosController.SelecionarTodos():
        grupos.append(item.description)

    grupo = tuple(grupos)

    with st.form(key="include_subgruporesíduos"):
        if subgruporesiduosRecuperado == None:
            st.selectbox("Escolha o grupo de resíduos ao qual o subgrupo pertence", grupo)
            input_description = st.text_input(label="Insira a descrição do subgrupo de resíduos")
        else:
            input_description = st.text_input(label="Insira a descrição do subgrupo de resíduos", value=subgruporesiduosRecuperado.description)
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if subgruporesiduosRecuperado == None:
            SubgrupoResiduosController.Incluir(subgruporesiduos.SubgrupoResiduos(input_description, input_description))
            st.success("Subgrupo de resíduos incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            SubgrupoResiduosController.Alterar(subgruporesiduos.SubgrupoResiduos(subgruporesiduosRecuperado.id_residual_subgroup, input_description))
            st.success("Subgrupo de resíduos alterado com sucesso!")
        
        