import string
from typing import List
import services.database as db;
import models.Subgrupo_Residuos as subgruporesiduos;
import numpy as np


def Incluir(subgruporesiduos):
    count = db.cursor.execute("""
    INSERT INTO residuals_subgroup (description) 
    VALUES (?)""",
    subgruporesiduos.description).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM residuals_subgroup WHERE id_residual_subgroup = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(subgruporesiduos.SubgrupoResiduos(row[0], row[1]))

    return costumerList[0]

def Alterar(subgruporesiduos):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE residuals_subgroup
    SET description = ?
    WHERE id_residual_subgroup = ?""",
    subgruporesiduos.description, subgruporesiduos.id_residual_subgroup).rowcount
    db.cnxn.commit()

def Excluir(id_residual_subgroup):
    count = db.cursor.execute("""
    DELETE FROM residuals_subgroup WHERE id_residual_subgroup = ?""",
    id_residual_subgroup).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM residuals_subgroup")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(subgruporesiduos.SubgrupoResiduos(row[0], row[1]))

    return costumerList

