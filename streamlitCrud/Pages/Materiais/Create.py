import this
from turtle import onclick
import streamlit as st
import Controllers.MateriaisController as MateriaisController
import Controllers.GrupoMateriaisController as GrupoMateriaisController
import models.Materiais as materiais


def Create():
    idAlteracao = st.experimental_get_query_params()
    materiaisRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        materiaisRecuperado = MateriaisController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[materiaisRecuperado.id_material]
        )
        st.title("Alterar materiais")
    else:
        st.title("Incluir materiais")

    grupos = []
    for item in GrupoMateriaisController.SelecionarTodos():
        grupos.append(item.group_description)

    grupo = tuple(grupos)

    with st.form(key="include_materiais"):
        if materiaisRecuperado == None:
            input_description = st.text_input(label="Insira a descrição do material")
            material_grupo = st.selectbox("Escolha o grupo de material", grupo)
            image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
            if image_file is not None:
                st.write(type(image_file))
                file_details = {"filename": image_file.name, "filetype": image_file.type, "filesize": image_file.size}
                st.write(file_details)
        else:
            input_description = st.text_input(label="Insira a descrição do material", value=materiaisRecuperado.description)
            material_grupo = st.selectbox("Escolha o grupo de material", grupo)
            image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
            if image_file is not None:
                st.write(type(image_file))
                file_details = {"filename": image_file.name, "filetype": image_file.type, "filesize": image_file.size}
                st.write(file_details)
        input_button_submit = st.form_submit_button("Enviar")

    filename = file_details['filename']
    filetype = file_details['filetype']
    filesize = file_details['filesize']

    if input_button_submit:
        if materiaisRecuperado == None:
            MateriaisController.Incluir(materiais.Materiais(input_description, input_description, material_grupo, filename, filetype, filesize))
            st.success("Material incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            MateriaisController.Alterar(materiais.Materiais(materiaisRecuperado.id_material, input_description, material_grupo, filename, filetype, filesize))
            st.success("Material alterado com sucesso!")
        
        