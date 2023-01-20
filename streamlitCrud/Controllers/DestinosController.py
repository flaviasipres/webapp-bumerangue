import services.database as db;
import models.Destinos as destinos;
import numpy as np


def Incluir(destinos):
    count = db.cursor.execute("""
    INSERT INTO destinations (description, classification) 
    VALUES (?,?)""",
    destinos.description, destinos.classification).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM destinations WHERE id_destination = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(destinos.Destinos(row[0], row[1], row[2]))

    return costumerList[0]

def Alterar(destinos):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE destinations
    SET description = ?, classification = ?
    WHERE id_destination = ?""",
    destinos.description, destinos.classification, destinos.id_destination).rowcount
    db.cnxn.commit()

def Excluir(id_destination):
    count = db.cursor.execute("""
    DELETE FROM destinations WHERE id_destination = ?""",
    id_destination).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM destinations")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(destinos.Destinos(row[0], row[1], row[2]))

    return costumerList