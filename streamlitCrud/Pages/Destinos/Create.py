import this
from turtle import onclick
import streamlit as st
import Controllers.DestinosController as DestinosController
import models.Destinos as destinos


def Create():
    idAlteracao = st.experimental_get_query_params()
    destinosRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        destinosRecuperado = DestinosController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[destinosRecuperado.id_destination]
        )
        st.title("Alterar destino")
    else:
        st.title("Incluir destino")

    with st.form(key="include_destinos"):
        if destinosRecuperado == None:
            input_description = st.text_input(label="Insira a descrição do destino")
            classification = st.radio("Selecione a classificação:", ("Entra na estatística", "É consumo e não entra na estatística e o peso deverá ser subtraído", "Entra na estatística pelo rateio sobre o peso total"))
        else:
            input_description = st.text_input(label="Insira a descrição do destino", value=destinosRecuperado.description)
            classification = st.radio("Selecione a classificação:", ("Entra na estatística", "É consumo e não entra na estatística e o peso deverá ser subtraído", "Entra na estatística pelo rateio sobre o peso total"))
        input_button_submit = st.form_submit_button("Enviar")

        

    if input_button_submit:
        if destinosRecuperado == None:
            DestinosController.Incluir(destinos.Destinos(input_description, input_description, classification))
            st.success("Destino incluído com sucesso!")
        else:
            st.experimental_set_query_params()
            DestinosController.Alterar(destinos.Destinos(destinosRecuperado.id_destination, input_description, classification))
            st.success("Destino alterado com sucesso!")
        
        