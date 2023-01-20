import string
from typing import List
import services.database as db;
import models.Produtos as produtos;
import numpy as np


def Incluir(produtos):
    count = db.cursor.execute("""
    INSERT INTO products (description, product_group, filename, filetype, filesize) 
    VALUES (?,?,?.?,?)""",
    produtos.description, produtos.product_group, produtos.filename, produtos.filetype, produtos.filesize).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM products WHERE id_product = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(produtos.Produtos(row[0], row[1], row[2], row[3], row[4], row[5]))

    return costumerList[0]

def Alterar(products):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE products
    SET description = ?, product_group = ?, filename = ?, filetype = ?, filesize = ?
    WHERE id_product = ?""",
    products.description, products.product_group, products.filename, products.filetype, products.filesize, products.id_material).rowcount
    db.cnxn.commit()

def Excluir(id_product):
    count = db.cursor.execute("""
    DELETE FROM products WHERE id_product = ?""",
    id_product).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM products")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(produtos.Produtos(row[0], row[1], row[2], row[3], row[4], row[5]))

    return costumerList