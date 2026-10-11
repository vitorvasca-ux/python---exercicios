import sqlite3

conn = sqlite3.connect("Loja_Vasca.db")

# Ativa as chaves estrangeiras
conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()


# ============================================================
# TABELA PRODUTOS
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL UNIQUE,
    PRECO_ATUAL REAL NOT NULL,
    CATEGORIA TEXT NOT NULL,
    ESTOQUE_ATUAL INTEGER NOT NULL,
    ESTOQUE_MINIMO INTEGER NOT NULL
)
""")


# ============================================================
# TABELA VENDEDOR
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS VENDEDOR (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    PERCENTUAL_COMISSAO REAL NOT NULL
)
""")


# ============================================================
# TABELA VENDA
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS VENDA (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DATA_VENDA TEXT NOT NULL,
    ID_VENDEDOR INTEGER NOT NULL,
    VALOR_BRUTO REAL NOT NULL,
    PERCENTUAL_DESCONTO REAL NOT NULL,
    VALOR_LIQUIDO REAL NOT NULL,

    FOREIGN KEY (ID_VENDEDOR)
    REFERENCES VENDEDOR(ID)
)
""")


# ============================================================
# TABELA REGISTRO_VENDA
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS REGISTRO_VENDA (
    ID_ITEM INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_VENDA INTEGER NOT NULL,
    ID_PRODUTO INTEGER NOT NULL,
    QUANTIDADE INTEGER NOT NULL,
    VALOR_UNITARIO REAL NOT NULL,
    SUBTOTAL REAL NOT NULL,

    FOREIGN KEY (ID_VENDA)
    REFERENCES VENDA(ID),

    FOREIGN KEY (ID_PRODUTO)
    REFERENCES produtos(ID)
)
""")


conn.commit()