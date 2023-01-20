import services.database as db;
import models.Hospital as hospital;
import numpy as np


def Incluir(hospital):
    count = db.cursor.execute("""
    INSERT INTO hospitals (razao_social, cnpj) 
    VALUES (?,?)""",
    hospital.razao_social, hospital.cnpj).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM hospitals WHERE id_hospital = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(hospital.Hospital(row[0], row[1],row[2]))

    return costumerList[0]

def Alterar(hospital):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE hospitals
    SET razao_social = ?, cnpj = ?
    WHERE id_hospital = ?""",
    hospital.razao_social, hospital.cnpj, hospital.id_hospital).rowcount
    db.cnxn.commit()

def Excluir(id_hospital):
    count = db.cursor.execute("""
    DELETE FROM hospitals WHERE id_hospital = ?""",
    id_hospital).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM hospitals")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(hospital.Hospital(row[0], row[1],row[2]))

    return costumerList