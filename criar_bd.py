import sqlite3 as sql

#Criar Banco de Dados
conexao = sql.connect('clientes.db')

c = conexao.cursor()

c.execute(""" CREATE TABLE clientes (
          nome text,
          sobrenome text,
          email text,
          telefone text
          )""")

conexao.commit()

conexao.close()

'''
conexao = sql.connect('clientes.db')
c = conexao.cursor()

#Excluir dados no banco de dados
c.execute("DELETE FROM clientes")
conexao.commit()
conexao.close()
'''