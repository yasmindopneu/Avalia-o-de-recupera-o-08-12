import tkinter as tk
import sqlite3


window = tk.Tk()
window.title("Jogos da Copa")
window.geometry("350x450")

def banco (): 
  global conexao, RecursionError
  try:
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
  except:
    print("erro ao conectar")
  else:
    cursor execute

def criar tabela():
   banco()
   cursor.execute(CREATE TABLE IF NOT EXISTS 'notas')
def cadastrar ():
  banco()
  dados_label[]
    
hello=tk.Label(window, text = "digite o nome do grupo:")
hello.pack()
button = tk.button(text="click")
button.pack()

tk.mainloop()

