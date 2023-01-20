import string
from typing import List
import services.database as db;
import models.Grupo_Materiais as grupomateriais;
import numpy as np


def Incluir(grupomateriais):
    count = db.cursor.execute("""
    INSERT INTO materials_group (group_description, detailed_description, alternative_description) 
    VALUES (?,?,?)""",
    grupomateriais.group_description, grupomateriais.detailed_description, grupomateriais.alternative_description).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM materials_group WHERE id_material_group = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(grupomateriais.GrupoMateriais(row[0], row[1], row[2], row[3]))

    return costumerList[0]

def Alterar(grupomateriais):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE materials_group
    SET group_description = ?, detailed_description = ?, alternative_description = ?
    WHERE id_material_group = ?""",
    grupomateriais.group_description, grupomateriais.detailed_description, grupomateriais.alternative_description, grupomateriais.id_material_group).rowcount
    db.cnxn.commit()

def Excluir(id_material_group):
    count = db.cursor.execute("""
    DELETE FROM materials_group WHERE id_material_group = ?""",
    id_material_group).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM materials_group")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(grupomateriais.GrupoMateriais(row[0], row[1], row[2], row[3]))

    return costumerList