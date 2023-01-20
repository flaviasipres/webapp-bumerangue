import string
from typing import List
import services.database as db;
import models.Grupo_Produtos as grupoprodutos;
import numpy as np


def Incluir(grupoprodutos):
    count = db.cursor.execute("""
    INSERT INTO product_group (description) 
    VALUES (?)""",
    grupoprodutos.description).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM product_group WHERE id_product_group = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(grupoprodutos.GrupoProdutos(row[0], row[1]))

    return costumerList[0]

def Alterar(grupoprodutos):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE product_group
    SET description = ?
    WHERE id_product_group = ?""",
    grupoprodutos.description, grupoprodutos.id_product_group).rowcount
    db.cnxn.commit()

def Excluir(id_product_group):
    count = db.cursor.execute("""
    DELETE FROM product_group WHERE id_product_group = ?""",
    id_product_group).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM product_group")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(grupoprodutos.GrupoProdutos(row[0], row[1]))

    return costumerList