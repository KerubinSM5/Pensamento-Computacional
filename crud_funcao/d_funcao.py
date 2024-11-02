import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class xcluirFuncaoE:
    def __init__(self, janela_mestre, idt):
        # Cria uma nova janela (pop-up)
        self.popup = tk.Toplevel(janela_mestre)
        self.popup.grab_set()

        # Constantes
        PADX = 10
        PADY = 10

        # Variáveis
        linha = 0

        # Buscar dados que já estão na base
        cmd = "SELECT * FROM tb_funcao WHERE idt_funcao = %s"
        funcao = janela_mestre.sql.get_object(cmd, [idt])

        # Primeira linha - Título
        titulo = tk.Label(self.popup, text="Excluir Função", font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
        linha += 1

        # Segunda linha - Identificador da função
        lb_idt = tk.Label(self.popup, text="Identificador", font='Helvetica 12 bold', fg='blue')
        lb_idt.grid(row=linha, column=0, padx=PADX, pady=PADY)

        self.idt_var = tk.StringVar()
        self.idt_var.set(funcao['idt_funcao'])
        self.lb_dado_idt = tk.Label(self.popup, textvariable=self.idt_var, font='Helvetica 16 bold',
                                    foreground='green')
        self.lb_dado_idt.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")
        linha += 1

        # Terceira linha - Receber o Nome da Função
        lb_nome = tk.Label(self.popup, text="Nome da Função", font='Helvetica 12 bold', fg='blue')
        lb_nome.grid(row=linha, column=0, padx=PADX, pady=PADY)

        self.nome_var = tk.StringVar()
        self.nome_var.set(funcao['nme_funcao'])
        self.lb_dado_nome = tk.Label(self.popup, textvariable=self.nome_var, font='Helvetica 16 bold',
                                     foreground='green')
        self.lb_dado_nome.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY)
        linha += 1

        # Quarta linha - Receber o Valor da Diária
        lb_valor = tk.Label(self.popup, text="Valor da Diária", font='Helvetica 12 bold', fg='blue')
        lb_valor.grid(row=linha, column=0, padx=PADX, pady=PADY)

        self.valor_var = tk.StringVar()
        self.valor_var.set(funcao['vlr_dia_funcao'])
        self.lb_dado_valor = tk.Label(self.popup, textvariable=self.valor_var, font='Helvetica 16 bold',
                                      foreground='green')
        self.lb_dado_valor.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")
        linha += 1

        # Quinta Linha - Operação de Excluir
        self.bt_excluir = tk.Button(self.popup, text="Excluir a Função", command=lambda: self.excluir(janela_mestre),
                                    font='Helvetica 12 bold',
                                    fg='white',
                                    bg='blue')
        self.bt_excluir.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.bt_excluir.focus()

    # Botão para confirmar a exclusão
    def excluir(self, janela_mestre):
        resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esta função?")
        if resposta:
            idt = int(self.idt_var.get())
            # Excluir os dados no banco de dados
            cmd = "DELETE FROM tb_funcao WHERE idt_funcao = %s"
            num_reg = janela_mestre.sql.upd_del(cmd, [idt])
            # Fechar a janela pop-up
            self.popup.destroy()
