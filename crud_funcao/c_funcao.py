import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.validate as val


class IncluirFuncao:
    def __init__(self, janela_mestre):
        # Cria uma nova janela (pop-up)
        self.popup = tk.Toplevel(janela_mestre)
        self.popup.grab_set()

        # Constantes
        PADX = 10
        PADY = 10
        self.obrigatorios = []

        # Primeira linha - Título
        titulo = tk.Label(self.popup, text="Incluir Função", font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=0, column=0, columnspan=3, padx=PADX, pady=PADY)

        # Segunda linha - Receber o Nome da Função
        lb_nome = tk.Label(self.popup, text="Nome da Função", font='Helvetica 12 bold', fg='blue')
        lb_nome.grid(row=1, column=0, padx=PADX, pady=PADY)

        self.nome_var = tk.StringVar()
        self.et_nome = ttk.Entry(self.popup, textvariable=self.nome_var, font='Helvetica 16 bold', foreground='green', width=30)
        val.limitar_tamanho(self.et_nome, 50)
        self.obrigatorios.append([self.et_nome, lb_nome.cget('text')])
        self.et_nome.grid(row=1, column=1, columnspan=2, padx=PADX, pady=PADY)

        # Terceira linha - Receber o Valor da Diária
        lb_valor = tk.Label(self.popup, text="Valor da Diária", font='Helvetica 12 bold', fg='blue')
        lb_valor.grid(row=2, column=0, padx=PADX, pady=PADY)

        vcmd = (self.popup.register(val.validate_float), '%P')  # %P representa o novo valor
        self.valor_var = tk.StringVar()
        self.et_valor = ttk.Entry(self.popup, textvariable=self.valor_var, font='Helvetica 16 bold', foreground='green', width=10, validate='key', validatecommand=vcmd)
        self.obrigatorios.append([self.et_valor, lb_valor.cget('text')])
        self.et_valor.grid(row=2, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")

        # Quarta linha - Botão para incluir uma nova função
        self.bt_salvar = tk.Button(self.popup, text="Incluir Nova Função", command=lambda: self.salvar(janela_mestre),
                                   font='Helvetica 12 bold',
                                   fg='white',
                                   bg='blue')
        self.bt_salvar.grid(row=3, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.et_nome.focus()

    # Botão para confirmar a inclusão
    def salvar(self, janela_mestre):
        retorno = val.todos_campos_preenchidos(self.obrigatorios)
        if retorno[0]:
            nome = self.nome_var.get()
            valor = float(self.valor_var.get())
            # Inserir os dados no banco de dados
            cmd = "INSERT INTO tb_funcao (nme_funcao, vlr_dia_funcao) VALUES (%s, %s)"
            id = janela_mestre.sql.insert(cmd, (nome, valor))
            # Fechar a janela pop-up
            self.popup.destroy()
        else:
            messagebox.showerror("Erro: Campo(s) obrigatório(s)",
                                 "O(s) seguinte(s) campo(s) é/são obrigatório(s):\n" + retorno[1])
