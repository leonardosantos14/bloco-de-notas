import tkinter as tk
from tkinter import filedialog

class BlocoDeNotas:
    def __init__(self, master):
        self.master = master
        master.title("Bloco de Notas")

        self.texto = tk.Text(master)
        self.texto.pack()

        self.salvar_botao = tk.Button(master, text="Salvar", command=self.salvar)
        self.salvar_botao.pack()

        self.abrir_botao = tk.Button(master, text="Abrir", command=self.abrir)
        self.abrir_botao.pack()

    def salvar(self):
        arquivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if arquivo is None:
            return
        texto = self.texto.get('1.0', tk.END)
        arquivo.write(texto)
        arquivo.close()
    
    def abrir(self):
        arquivo = filedialog.askopenfilename(defaultextension=".txt")
        if not arquivo:
            return
        with open(arquivo) as f:
            conteudo = f.read()
        self.texto.delete('1.0', tk.END)
        self.texto.insert('1.0', conteudo)

root = tk.Tk()
notas = BlocoDeNotas(root)
root.mainloop()