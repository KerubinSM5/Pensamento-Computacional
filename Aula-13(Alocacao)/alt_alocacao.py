import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import util.validate as val
import util.converter as conv
from util.lv import LV


class AlterarAloc:
    def __init__(self, janela_mestre, idt_projeto, nme_projeto, idt_alocacao):
        # Para utilizar na alteração da alocação
        self.idt_projeto = idt_projeto
        self.idt_alocacao = idt_alocacao

        # Cria uma nova janela (pop-up)
        self.popup = tk.Toplevel(janela_mestre)
        self.popup.grab_set()
        self.popup.sql = janela_mestre.sql

        # Carregar dados da alocação a ser alterada
        cmd = """select dta_ini_alocacao, dta_fim_alocacao, cod_colaborador, cod_funcao, nme_colaborador, nme_funcao
                from ta_alocacao join tb_colaborador on idt_colaborador = cod_colaborador join tb_funcao on idt_funcao = cod_funcao
                where idt_alocacao = %s;
       """
        aloc = self.popup.sql.get_object(cmd, [idt_alocacao])

        # Constantes
        PADX = 10
        PADY = 10
        self.obrigatorios = []

        linha = 0
        # Título
        txt = f"Alterar Alocacao no Projeto: {nme_projeto}"
        titulo = tk.Label(self.popup, text=txt, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, columnspan=4, padx=PADX, pady=PADY)
        linha += 1

        txt = f"Identificação da Alocação: {idt_alocacao}"
        titulo = tk.Label(self.popup, text=txt, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, columnspan=4, padx=PADX, pady=PADY)
        linha += 1

        # Escolher o colaborador
        lb_col = tk.Label(self.popup, text="Colaborador", font='Helvetica 12 bold', fg='blue')
        lb_col.grid(row=linha, column=0, padx=PADX, pady=PADY)
        self.popup.bt_lv = tk.Button(self.popup, text="LV", command=self.lv_col, font='Helvetica 12 bold', fg='white',
                                     bg='blue')
        self.popup.bt_lv.grid(row=linha, column=1, padx=PADX, pady=PADY)

        self.popup.id_col_var = tk.StringVar()
        self.popup.et_id_col = ttk.Entry(self.popup, textvariable=self.popup.id_col_var, font='Helvetica 16 bold',
                                         foreground='green', width=5, state="readonly")
        self.popup.et_id_col.grid(row=linha, column=2, padx=PADX, pady=PADY)
        self.obrigatorios.append([self.popup.et_id_col, lb_col.cget('text')])
        self.popup.id_col_var.set(aloc['cod_colaborador'])

        self.popup.col_var = tk.StringVar()
        self.popup.et_col = ttk.Entry(self.popup, textvariable=self.popup.col_var, font='Helvetica 16 bold',
                                      foreground='green',
                                      width=50, state="readonly")
        self.popup.et_col.grid(row=linha, column=3, padx=PADX, pady=PADY)
        self.popup.col_var.set(aloc["nme_colaborador"])
        linha += 1

        # Preencher com dados de funções do banco
        cmd = """
             SELECT nme_funcao
             FROM tb_funcao ORDER BY nme_funcao;
       """
        funcoes = self.popup.sql.get_list(cmd)
        lb_funcao = tk.Label(self.popup, text="Função do Colaborador", font='Helvetica 12 bold', fg='blue')
        lb_funcao.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)

        self.popup.funcao_var = tk.StringVar()
        self.popup.cb_funcao = tk.ttk.Combobox(self.popup, values=[f['nme_funcao'] for f in funcoes],
                                               textvariable=self.popup.funcao_var, font='Helvetica 16 bold',
                                               foreground='green', width=30)
        self.popup.cb_funcao.grid(row=linha, column=3, padx=PADX, pady=PADY, sticky='W')
        self.obrigatorios.append([self.popup.cb_funcao, lb_funcao.cget('text')])
        self.popup.funcao_var.set(aloc["nme_funcao"])
        linha += 1

        lb_dt_ini = tk.Label(self.popup, text="Data Início", font='Helvetica 12 bold', fg='blue')
        lb_dt_ini.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.popup.dt_ini_var = tk.StringVar()
        self.popup.dt_dt_ini = DateEntry(self.popup, textvariable=self.popup.dt_ini_var, selectmode='day',
                                         date_pattern='dd/mm/yyyy', font='Helvetica 16 bold',
                                         foreground='green')
        self.popup.dt_dt_ini.grid(row=linha, column=3, padx=PADX, pady=PADY, sticky='W')
        self.obrigatorios.append([self.popup.dt_dt_ini, lb_dt_ini.cget('text')])
        self.popup.dt_ini_var.set(conv.mysql_to_bra(aloc["dta_ini_alocacao"]))
        linha += 1

        lb_dt_fim = tk.Label(self.popup, text="Data Final", font='Helvetica 12 bold', fg='blue')
        lb_dt_fim.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.popup.dt_fim_var = tk.StringVar()
        self.popup.dt_dt_fim = DateEntry(self.popup, textvariable=self.popup.dt_fim_var, selectmode='day',
                                         date_pattern='dd/mm/yyyy', font='Helvetica 16 bold',
                                         foreground='green')
        self.popup.dt_dt_fim.grid(row=linha, column=3, padx=PADX, pady=PADY, sticky='W')
        self.popup.dt_fim_var.set(conv.mysql_to_bra(aloc["dta_fim_alocacao"]))
        linha += 1

        # Botão para alterar uma alocação
        self.popup.bt_salvar = tk.Button(self.popup, text="Alterar Alocação",
                                         command=lambda: self.salvar(),
                                         font='Helvetica 12 bold',
                                         fg='white',
                                         bg='blue')
        self.popup.bt_salvar.grid(row=linha, column=0, columnspan=4, padx=PADX, pady=PADY)

    def lv_col(self):
        cmd = '''
             SELECT idt_colaborador as idt,
                    nme_colaborador as txt
             FROM tb_colaborador
             WHERE nme_colaborador LIKE CONCAT('%', %s, '%') ORDER BY nme_colaborador;
       '''

        lv = LV(janela_mestre=self.popup, title_text="Escolha um Colaborador", label_filter="Colaborador",
                var_id="id_col_var",
                var_text="col_var", cmd=cmd)

    # Botão para confirmar a alteração no banco
    def salvar(self):
        retorno = val.todos_campos_preenchidos(self.obrigatorios)
        if retorno[0]:
            cmd = "SELECT idt_funcao FROM tb_funcao WHERE nme_funcao = %s;"
            cod_colaborador = self.popup.id_col_var.get()
            cod_funcao = self.popup.sql.get_int(cmd, [self.popup.funcao_var.get()])
            dta_ini_alocacao = conv.bra_to_mysql(self.popup.dt_ini_var.get())
            dta_fim_alocacao = conv.bra_to_mysql(self.popup.dt_fim_var.get())
            # Alterar os dados no banco de dados
            cmd = """UPDATE ta_alocacao SET dta_ini_alocacao = %s, dta_fim_alocacao = %s, cod_colaborador = %s, cod_funcao = %s
                    WHERE idt_alocacao = %s;"""
            n = self.popup.sql.upd_del(cmd, [dta_ini_alocacao, dta_fim_alocacao, cod_colaborador, cod_funcao,
                                             self.idt_alocacao])
            # Fechar a janela pop-up
            self.popup.destroy()
        else:
            messagebox.showerror("Erro: Campo(s) obrigatório(s)",
                                 "O(s) seguinte(s) campo(s) é/são obrigatório(s):\n" + retorno[1])
