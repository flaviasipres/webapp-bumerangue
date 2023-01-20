import services.database as db;
import models.Materiais as materiais;
import numpy as np


def Incluir(materiais):
    count = db.cursor.execute("""
    INSERT INTO materials (description, material_group, filename, filetype, filesize) 
    VALUES (?,?,?.?,?)""",
    materiais.description, materiais.material_group, materiais.filename, materiais.filetype, materiais.filesize).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM materials WHERE id_material = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(materiais.Materiais(row[0], row[1], row[2], row[3], row[4], row[5]))

    return costumerList[0]

def Alterar(materiais):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE materials
    SET description = ?, material_group = ?, filename = ?, filetype = ?, filesize = ?
    WHERE id_material_group = ?""",
    materiais.description, materiais.material_group, materiais.filename, materiais.filetype, materiais.filesize, materiais.id_material).rowcount
    db.cnxn.commit()

def Excluir(id_material):
    count = db.cursor.execute("""
    DELETE FROM materials WHERE id_material = ?""",
    id_material).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM materials")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(materiais.Materiais(row[0], row[1], row[2], row[3], row[4], row[5]))

    return costumerList