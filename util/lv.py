import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class LV:
    def __init__(self, janela_mestre, title_text, label_filter, var_id, var_text, cmd):
        # Cria uma nova janela (pop-up)
        self.popup = tk.Toplevel(janela_mestre)
        self.popup.grab_set()

        # Constantes
        PADX = 10
        PADY = 10

        # Variáveis
        linha = 0

        # Primeira linha - Título
        titulo = tk.Label(self.popup, text=title_text, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
        linha += 1

        # Segunda linha - Filtro da busca
        lb_filter = tk.Label(self.popup, text=label_filter, font='Helvetica 12 bold', fg='blue')
        lb_filter.grid(row=linha, column=0, padx=PADX, pady=PADY)

        self.filter_var = tk.StringVar()
        self.et_filter = ttk.Entry(self.popup, textvariable=self.filter_var, font='Helvetica 16 bold',
                                   foreground='green', width=20)
        self.et_filter.grid(row=linha, column=1, padx=PADX, pady=PADY)

        self.bt_filter = tk.Button(self.popup, text="Filtrar", command=lambda: self.filtrar(janela_mestre, cmd),
                                   font='Helvetica 12 bold',
                                   fg='white',
                                   bg='blue')
        self.bt_filter.grid(row=linha, column=2, padx=PADX, pady=PADY)
        linha += 1

        # Treeview para exibir os resultado da filtragem
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Arial", 12), foreground="blue")
        self.tre_filter = ttk.Treeview(self.popup, columns=("idt", "txt"), show="headings", style="Custom.Treeview")
        # Configurar as colunas
        self.tre_filter.heading("idt", text="Identificador")
        self.tre_filter.heading("txt", text=label_filter)
        # Ajustar a largura das colunas
        self.tre_filter.column("idt", width=100)
        self.tre_filter.column("txt", width=400)
        self.tre_filter.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
        linha += 1

        # Botão para retornar o item escolhido
        self.bt_return = tk.Button(self.popup, text="Retornar o Valor",
                                   command=lambda: self.retornar(janela_mestre, var_id, var_text),
                                   font='Helvetica 12 bold',
                                   fg='white',
                                   bg='blue')
        self.bt_return.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.et_filter.focus()

    def limpar_tabela(self):
        for linha in self.tre_filter.get_children():
            self.tre_filter.delete(linha)

    def filtrar(self, janela_mestre, cmd):
        arg = self.filter_var.get()
        lista = janela_mestre.sql.get_list(cmd, [arg])
        self.limpar_tabela()
        for dado in lista:
            self.tre_filter.insert("", tk.END, values=(dado['idt'], dado['txt']))

    def retornar(self, janela_mestre, var_id, var_text):
        selecao = self.tre_filter.selection()
        if selecao:
            linha = self.tre_filter.selection()[0]
            valores = self.tre_filter.item(linha, "values")
            comando = f'janela_mestre.{var_id}.set("{valores[0]}")'
            eval(comando)
            comando = f'janela_mestre.{var_text}.set("{valores[1]}")'
            eval(comando)
            self.popup.destroy()
        else:
            messagebox.showerror("Erro: Escolha um item",
                                 "Escolha um item da tabela para retornar")
