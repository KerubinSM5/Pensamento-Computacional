import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.validate as val
from tkcalendar import DateEntry
from datetime import datetime

class AlterarProjeto:
    def __init__(self, janela_mestre, idt):
        # Cria uma nova janela (pop-up)
        self.popup = tk.Toplevel(janela_mestre)
        self.popup.grab_set()

        # Constantes
        PADX = 10
        PADY = 10

        # Variáveis
        self.obrigatorios = []
        linha = 0

        # Buscar dados que já estão na base
        cmd = "SELECT * FROM tb_projeto WHERE idt_projeto = %s"
        funcao = janela_mestre.sql.get_object(cmd, [idt])

        # Primeira linha - Título
        titulo = tk.Label(self.popup, text="Alterar Projeto", font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=1, column=0, columnspan=3, padx=PADX, pady=PADY)

        # Segunda linha - Mostrar o identificador da função (readonly)
        lb_idt = tk.Label(self.popup, text="Identificador", font='Helvetica 12 bold', fg='blue')
        lb_idt.grid(row=2, column=0, padx=PADX, pady=PADY)

        self.idt_var = tk.StringVar()
        self.idt_var.set(funcao['idt_projeto'])
        self.et_idt = ttk.Entry(self.popup, textvariable=self.idt_var, font='Helvetica 16 bold',
                                foreground='green', width=5, state="readonly")
        self.et_idt.grid(row=2, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")

        #Nome do Projeto
        lb_nome = tk.Label(self.popup, text="Nome do projeto", font='Helvetica 12 bold', fg='blue')
        lb_nome.grid(row=4, column=0, padx=PADX, pady=PADY)

        self.nome_var = tk.StringVar()
        self.nome_var.set(funcao['nme_projeto'])
        self.et_nome = ttk.Entry(self.popup, textvariable=self.nome_var, font='Helvetica 16 bold',
                                 foreground='green', width=30)
        val.limitar_tamanho(self.et_nome, 50)
        self.obrigatorios.append([self.et_nome, lb_nome.cget('text')])
        self.et_nome.grid(row=4, column=1, columnspan=2, padx=PADX, pady=PADY)

        # Terceira linha - Receber a data de inicio do projeto
        lb_data1 = tk.Label(self.popup, text="Data de inicio do projeto", font='Helvetica 12 bold', fg='blue')
        lb_data1.grid(row=5, column=0, padx=PADX, pady=PADY)

        self.valor_data1 = tk.StringVar()
        self.et_data1 = DateEntry(self.popup, textvariable=self.valor_data1, font='Helvetica 16 bold', foreground='green',
                                  width=10, date_pattern='dd/mm/yyyy', date_format='%d/%m/%Y')
        self.obrigatorios.append([self.et_data1, lb_nome.cget('text')])
        self.et_data1.grid(row=5, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")


        # Quarta linha - Receber a data final do projeto
        lb_valor2 = tk.Label(self.popup, text="Data final do projeto", font='Helvetica 12 bold', fg='blue')
        lb_valor2.grid(row=6, column=0, padx=PADX, pady=PADY)

        self.valor_var = tk.StringVar()
        self.et_valor2 = DateEntry(self.popup, textvariable=self.valor_var, font='Helvetica 16 bold', foreground='green',
                                  width=10, date_pattern='dd/mm/yyyy', date_format='%d/%m/%Y')
        self.obrigatorios.append([self.et_valor2, lb_valor2.cget('text')])
        self.et_valor2.grid(row=6, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")


        # Quinta linha - Botação para salvar alterações
        self.bt_alterar = tk.Button(self.popup, text="Alterar a Função", command=lambda: self.alterar(janela_mestre),
                                    font='Helvetica 12 bold',
                                    fg='white',
                                    bg='blue')
        self.bt_alterar.grid(row=7, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.et_nome.focus()

    # Botão para confirmar a alteração
    def alterar(self, janela_mestre):
        retorno = val.todos_campos_preenchidos(self.obrigatorios)
        if retorno[0]:
            idt = int(self.idt_var.get())
            nome = self.nome_var.get()
            data1 = self.valor_data1.get()
            data1conv = datetime.strptime(data1, '%d/%m/%Y').date()
            data2 = self.valor_var.get()
            data2conv = datetime.strptime(data2, '%d/%m/%Y').date()
            # Alterar os dados no banco de dados
            cmd = "UPDATE tb_projeto SET nme_projeto = %s, dta_ini_projeto =%s, dta_fim_projeto = %s WHERE idt_projeto = %s"
            num_reg = janela_mestre.sql.upd_del(cmd, (nome, data1conv, data2conv, idt))
            # Fechar a janela pop-up
            self.popup.destroy()
        else:
            messagebox.showerror("Erro: Campo(s) obrigatório(s)",
                                 "O(s) seguinte(s) campo(s) é/são obrigatório(s):\n" + retorno[1])
