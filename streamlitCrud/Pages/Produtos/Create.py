import streamlit as st
import Controllers.ProdutosController as ProdutosController
import Controllers.GrupoProdutosController as GrupoProdutosController
import models.Produtos as produtos


def Create():
    idAlteracao = st.experimental_get_query_params()
    produtosRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        produtosRecuperado = ProdutosController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[produtosRecuperado.id_product]
        )
        st.title("Alterar produto")
    else:
        st.title("Incluir produto")

    grupos = []
    for item in GrupoProdutosController.SelecionarTodos():
        grupos.append(item.group_description)

    grupo = tuple(grupos)

    with st.form(key="include_produto"):
        if produtosRecuperado == None:
            input_description = st.text_input(label="Insira a descrição do produto")
            product_group = st.selectbox("Selecione o grupo do produto", grupo)
            image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
            if image_file is not None:
                st.write(type(image_file))
                file_details = {"filename": image_file.name, "filetype": image_file.type, "filesize": image_file.size}
                st.write(file_details)
        else:
            input_description = st.text_input(label="Insira a descrição do produto", value=produtosRecuperado.description)
            product_group = st.selectbox("Selecione o grupo do produto", grupo)
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
        if produtosRecuperado == None:
            ProdutosController.Incluir(produtos.Produtos(input_description, input_description, product_group, filename, filetype, filesize))
            st.success("Produto incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            ProdutosController.Alterar(produtos.Produtos(produtosRecuperado.id_product, input_description, product_group, filename, filetype, filesize))
            st.success("Produto alterado com sucesso!")
        
        