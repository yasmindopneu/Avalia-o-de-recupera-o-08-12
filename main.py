#nome: yasmin leal,2°matutino.
#usei o codigo da aula  de recuperação como base, pois não estava conseguindo conectar o banco de dados sqlite3 import error. 

import tkinter as tk
import sqlite3


window = tk.Tk()
window.title("Jogos da Copa")
window.geometry("350x460")

def banco (): 
  global conexao, RecursionError
  try:
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
  except:
    print("erro ao conectar")
  else:
    cursor.execute("CREATE TABLE IF NOT EXISTS `jogos` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, seleção1 TEXT, seleção2 TEXT,seleção3 TEXT, seleção4 TEXT)")
    print("Tabela criada!")
    print("Conexão realizada ")

def criar_tabela():
  banco()
  cursor.execute("CREATE TABLE IF NOT EXISTS `jogos` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, seleção1 TEXT, seleção2 TEXT,seleção3 TEXT,seleção4 TEXT)")
  print("Tabela criada ")

def cadastrar():
  banco()
  cursor.execute("INSERT INTO jogos (nome, seleção1, seleção2, seleção3, seleção4) values (?, ?, ?, ?, ?)", (str(nome_entrada.get()), TEXT(seleção1_entrada.get()), TEXT(seleção2_entrada.get()),TEXT(seleção3_entrada.get()),TEXT(seleção4_entrada.get())))
  conexao.commit()
  print("Dados cadastrados!")
  conexao.close
  nome_entrada.delete(0,"end")
  seleção1_entrada.delete(0,"end")
  seleção2_entrada.delete(0,"end")
  seleção3_entrada.delete(0,"end")
  seleção4_entrada.delete(0,"end")

def listar_console():
  banco()
  cursor.execute("SELECT nome, seleção1, seleção2, seleção3, seleção4 FROM jogos")
  jogo = cursor.fetchall()
  for i in jogo:
    print(i)
  conexao.close()
  
def listar_interface():
  dados_jogo = '' 
  banco()
  cursor.execute("SELECT nome, seleção1, seleção2, seleção3, seleção4 FROM jogos")
  jogo = cursor.fetchall()
  for i in jogo:
    dados_jogo += str(i) + "\n" 
    dados_label["text"] = dados_jogo 
  conexao.close()

def cancelar():
  nome_entrada.delete(0,"end")
  seleção1_entrada.delete(0,"end")
  seleção2_entrada.delete(0,"end")
  seleção2_entrada.delete(0,"end")
  seleção2_entrada.delete(0,"end")


hello=tk.Label(window, text = "Digite o nome do grupo:")
hello.place(x=50,y=50)
hello = tk.Entry(window)
hello.pack()
hello.place(x=205,y=90)

hell=tk.Label(window,text='Digite a primeira seleção:')
hell.place(x=50, y=90)
hell = tk.Entry(window)
hell.pack()
hell.place(x=200,y=210)

hel=tk.Label(window,text='Digite a segunda seleção:')
hel.place(x=50,y=130)
hel=tk.Entry(window)
hel.pack()
hel.place(x=200,y=170)

he=tk.Label(window,text='Digite a terceira seleção:')
he.place(x=50,y=170)
he=tk.Entry(window)
he.pack()
he.place(x=205,y=130)

hep=tk.Label(window,text='Digite a quarta seleção:')
hep.place(x=50,y=210)
hep=tk.Entry(window)
hep.pack()
hep.place(x=200,y=50)

salvar_botão=tk.Button(text="salvar",command=cadastrar)
salvar_botão.place(x=50,y=300)

cancelar_botão=tk.Button (text="cancelar")
cancelar_botão=tk.Button(text="cancelar",command=cancelar)
cancelar_botão.place(x=150,y=300)

listar_botao = tk.Button(text="Mostrar dados no console", command=listar_console)
listar_botao.place(x=50,y=350)

dados_label = tk.Label(window)
dados_label.place(x=50,y=350)
dados_label.place(x=50,y=370)

tk.mainloop()







