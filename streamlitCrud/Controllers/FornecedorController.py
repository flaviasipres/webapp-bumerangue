import services.database as db;
import models.Fornecedor as fornecedor;
import numpy as np


def Incluir(fornecedor):
    count = db.cursor.execute("""
    INSERT INTO Suppliers (razao_social, address, cnpj) VALUES (?,?,?)""",
    fornecedor.razao_social, fornecedor.endereco, fornecedor.cnpj).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM SUPPLIERS WHERE id_supplier = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(fornecedor.Fornecedor(row[0], row[1],row[2], row[3]))

    return costumerList[0]

def Alterar(fornecedor):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE suppliers
    SET razao_social = ?, address = ?, cnpj = ?
    WHERE id_supplier = ?""",
    fornecedor.razao_social, fornecedor.endereco, fornecedor.cnpj, fornecedor.id_supplier).rowcount
    db.cnxn.commit()

def Excluir(id_user):
    count = db.cursor.execute("""
    DELETE FROM suppliers WHERE id_supplier = ?""",
    id_user).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM suppliers")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(fornecedor.Fornecedor(row[0], row[1],row[2], row[3]))

    return costumerList