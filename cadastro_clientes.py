import customtkinter as ctk
import sqlite3 as sql
import pandas as pd
import os

#Caminhos Banco de Dados e Excel 
sys_dir1 = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(sys_dir1, 'dados/clientes.db')
exc_path = os.path.join(sys_dir1, 'dados/clientes.xlsx')    

ctk.set_appearance_mode('light')

login = ctk.CTk()
login.title('LOGIN')
icon_path1 = os.path.join(sys_dir1, "icones/LOG_ICO.ICO")  # Caminho relativo
login.iconbitmap(icon_path1)
login.geometry()

def janela_cadastro():

    janela = ctk.CTk()
    janela.title('Cadastro de Clientes')
    icon_path2 = os.path.join(sys_dir1, "icones/ICONE.ICO")  # Caminho relativo
    janela.iconbitmap(icon_path2)
    janela.geometry('960x540')


    def cadastrar_clientes():
        conexao = sql.connect(db_path)
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

    label_nome = ctk.CTkLabel(janela, text='Nome')
    label_nome.pack(padx=10, pady=5)

    entry_nome = ctk.CTkEntry(janela,placeholder_text='Digite seu Nome', width = 200,border_color='cyan', font=ctk.CTkFont(family='Times'), justify='center')
    entry_nome.pack(padx=0,pady=0)

    label_sobrenome = ctk.CTkLabel(janela, text='Sobrenome')
    label_sobrenome.pack(padx=10, pady=5)

    entry_sobrenome = ctk.CTkEntry(janela,placeholder_text='Digite seu Sobrenome', width = 200, border_color='cyan', font=ctk.CTkFont(family='Times'), justify='center')
    entry_sobrenome.pack(padx=0,pady=0)

    label_email = ctk.CTkLabel(janela, text='Email')
    label_email.pack(padx=10, pady=5)

    entry_email = ctk.CTkEntry(janela,placeholder_text='Digite seu Email', width = 200, border_color='cyan',font=ctk.CTkFont(family='Times'), justify='center')
    entry_email.pack(padx=0,pady=0)

    label_telefone = ctk.CTkLabel(janela, text='Telefone')
    label_telefone.pack(padx=10, pady=5)

    entry_telefone = ctk.CTkEntry(janela,placeholder_text='Digite seu Telefone', width = 200, border_color='cyan',font=ctk.CTkFont(family='Times'), justify='center')
    entry_telefone.pack(padx=0,pady=5)

    botao_cadastrar = ctk.CTkButton(janela, text='Cadastrar Cliente', command=cadastrar_clientes)
    botao_cadastrar.pack(padx=10,pady=10,ipadx = 100)

    botao_exportar = ctk.CTkButton(janela, text='Exportar para Excel', command=exportar_clientes)
    botao_exportar.pack(padx=10,pady=0 ,ipadx = 100)

    botao_sair = ctk.CTkButton(janela, text='Sair', command=janela.destroy)
    botao_sair.pack(padx=10,pady=10 ,ipadx = 100)

    janela.mainloop(0)

incorreto = ctk.CTkLabel(login, text="", text_color='red')

def logar():
    login_usuario = 'admin'
    login_senha = '123'

    preencher1 = preencher_usuario.get()
    preencher2 = preencher_senha.get()
    
    if preencher1 == login_usuario and preencher2 == login_senha:
        login.destroy(),
        janela_cadastro()
    else:
        incorreto.configure(text="Senha e/ou Usuário Incorretos!")
        incorreto.pack(padx=10,pady=5)

usuario = ctk.CTkLabel(login, text='Usuário')
usuario.pack(padx=10, pady=5)

preencher_usuario = ctk.CTkEntry(login,placeholder_text='Digite seu Usuário', width = 200,border_color='cyan', font=ctk.CTkFont(family='Times'), justify='center')
preencher_usuario.pack(padx=0,pady=0)

senha = ctk.CTkLabel(login, text='Senha')
senha.pack(padx=10, pady=5)

preencher_senha = ctk.CTkEntry(login,placeholder_text='Digite sua Senha', width = 200,border_color='cyan', font=ctk.CTkFont(family='Times'), justify='center')
preencher_senha.pack(padx=0,pady=0)

botao_cadastrar = ctk.CTkButton(login, text='Logar', command=logar)
botao_cadastrar.pack(padx=10,pady=10,ipadx = 100)

botao_sair = ctk.CTkButton(login, text='Sair', command=login.destroy)
botao_sair.pack(padx=10,pady=10,ipadx = 100)

login.mainloop()

# parar de aparecer varios incorretos / conexao correta do bd e excel 