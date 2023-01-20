import services.database as db;
import models.Grupo_Residuos as gruporesiduos;
import numpy as np


def Incluir(gruporesiduos):
    count = db.cursor.execute("""
    INSERT INTO residuals_group (description) 
    VALUES (?)""",
    gruporesiduos.description).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM residuals_group WHERE id_residual_group = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(gruporesiduos.GrupoResiduos(row[0], row[1]))

    return costumerList[0]

def Alterar(gruporesiduos):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE residuals_group
    SET description = ?
    WHERE id_residual_group = ?""",
    gruporesiduos.description, gruporesiduos.id_residual_group).rowcount
    db.cnxn.commit()

def Excluir(id_residual_group):
    count = db.cursor.execute("""
    DELETE FROM residuals_group WHERE id_residual_group = ?""",
    id_residual_group).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM residuals_group")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(gruporesiduos.GrupoResiduos(row[0], row[1]))

    return costumerList