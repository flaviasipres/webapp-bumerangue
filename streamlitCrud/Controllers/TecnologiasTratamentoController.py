import string
from typing import List
import services.database as db;
import models.Tecnologia_Tratamento as tecnologiatratamento;
import numpy as np


def Incluir(tecnologiatratamento):
    count = db.cursor.execute("""
    INSERT INTO treatment_technology (description) 
    VALUES (?)""",
    tecnologiatratamento.description).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM treatment_technology WHERE id_treatment_technology = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(tecnologiatratamento.TecnologiaTratamento(row[0], row[1]))

    return costumerList[0]

def Alterar(tecnologiatratamento):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE treatment_technology
    SET description = ?
    WHERE id_treatment_technology = ?""",
    tecnologiatratamento.description, tecnologiatratamento.id_treatment_technology).rowcount
    db.cnxn.commit()

def Excluir(id_residual_group):
    count = db.cursor.execute("""
    DELETE FROM treatment_technology WHERE id_treatment_technology = ?""",
    id_residual_group).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM treatment_technology")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(tecnologiatratamento.TecnologiaTratamento(row[0], row[1]))

    return costumerList