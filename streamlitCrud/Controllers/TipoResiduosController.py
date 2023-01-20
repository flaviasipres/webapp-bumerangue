import services.database as db;
import models.Tipo_Residuos as tiporesiduos;
import numpy as np


def Incluir(tiporesiduos):
    count = db.cursor.execute("""
    INSERT INTO residuals_type (description, grupo_description, subgrupo_description) 
    VALUES (?,?,?)""",
    tiporesiduos.description, tiporesiduos.grupo_description, tiporesiduos.subgrupo_description).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM residuals_type WHERE id_residual_type = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(tiporesiduos.TipoResiduos(row[0], row[1]))

    return costumerList[0]

def Alterar(tiporesiduos):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE residuals_type
    SET description = ?, grupo_description = ?, subgrupo_description=?
    WHERE id_residual_type = ?""",
    tiporesiduos.description, tiporesiduos.grupo_description, tiporesiduos.subgrupo_description, tiporesiduos.id_residual_type).rowcount
    db.cnxn.commit()

def Excluir(id_residual_type):
    count = db.cursor.execute("""
    DELETE FROM residuals_type WHERE id_residual_type = ?""",
    id_residual_type).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM residuals_type")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(tiporesiduos.TipoResiduos(row[0], row[1]))

    return costumerList