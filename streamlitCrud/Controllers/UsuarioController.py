import string
from typing import List
import services.database as db;
import models.Usuario as usuario;
import numpy as np


def Incluir(usuario):
    count = db.cursor.execute("""
    INSERT INTO Users (name, address, cpf, email, mobile_phone, password) 
    VALUES (?,?,?,?,?,?)""",
    usuario.nome, usuario.endereco, usuario.cpf, usuario.email, usuario.celular, usuario.senha).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM USERS WHERE id_user = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(usuario.Usuario(row[0], row[1],row[2], row[3], row[4],row[5], row[6]))

    return costumerList[0]

def Alterar(usuario):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE USERS
    SET name = ?, address = ?, cpf = ?, email = ?, mobile_phone = ?, password = ?
    WHERE id_user = ?""",
    usuario.nome, usuario.endereco, usuario.cpf, usuario.email, usuario.celular, usuario.senha, usuario.id_user).rowcount
    db.cnxn.commit()

def Excluir(id_user):
    count = db.cursor.execute("""
    DELETE FROM USERS WHERE id_user = ?""",
    id_user).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM USERS")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(usuario.Usuario(row[0], row[1],row[2], row[3], row[4],row[5], row[6]))

    return costumerList