from tkinter import *
import sqlite3 as sql
import pandas as pd
import os

sys_dir1 = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(sys_dir1, 'clientes.db')
exc_path = os.path.join(sys_dir1, 'clientes.xlsx')    

janela = Tk()
janela.title('Cadastro de Clientes')
icon_path2 = os.path.join(sys_dir1, "ICONE.ico")
janela.iconbitmap(icon_path2)
janela.geometry()

def cadastrar_clientes():
    conexao = sql.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados no banco de dados
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              })
    conexao.commit()
    conexao.close()

    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")

def exportar_clientes():
    conexao = sql.connect(db_path)
    c = conexao.cursor()

    #Exportar dados para o Excel
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns= ['nome','sobrenome','email','telefone','Id_banco'])
          
    clientes_cadastrados.to_excel(exc_path)

    conexao.commit()
    conexao.close()

label_nome = Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = Label(janela, text='Email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

entry_nome = Entry(janela, width =35)
entry_nome.grid(row=0,column=1,padx=10,pady=10)

entry_sobrenome = Entry(janela, width =35)
entry_sobrenome.grid(row=1,column=1,padx=10,pady=10)

entry_email = Entry(janela, width =35)
entry_email.grid(row=2,column=1,padx=10,pady=10)

entry_telefone = Entry(janela, width =35)
entry_telefone.grid(row=3,column=1,padx=10,pady=10)

botao_cadastrar = Button(text='Cadastrar Cliente', command=cadastrar_clientes)
botao_cadastrar.grid(column=0,row=4,columnspan=2,padx=10,pady=10,ipadx = 80)

botao_exportar = Button(text='Exportar para Excel', command=exportar_clientes)
botao_exportar.grid(column=0,row=5,columnspan=2,padx=10,pady=10,ipadx = 80)

janela.mainloop()
