import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import util.validate as val
import util.converter as conv
from util.lv import LV


class ExcluirAloc:
    def __init__(self, janela_mestre, idt_projeto, nme_projeto, idt_alocacao):
        # Para utilizar na alocação
        self.idt_projeto = idt_projeto
        self.idt_alocacao = idt_alocacao

        # Cria uma nova janela (pop-up)
        self.popup = tk.Toplevel(janela_mestre)
        self.popup.grab_set()
        self.popup.sql = janela_mestre.sql

        # Carregar dados da alocação a ser alterada
        cmd = """select dta_ini_alocacao, dta_fim_alocacao, nme_colaborador, nme_funcao
                from ta_alocacao join tb_colaborador on idt_colaborador = cod_colaborador 
                    join tb_funcao on idt_funcao = cod_funcao
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
        titulo.grid(row=linha, column=0, padx=PADX, pady=PADY)
        linha += 1

        txt = f"Identificação da Alocação: {idt_alocacao}"
        titulo = tk.Label(self.popup, text=txt, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, columnspan=4, padx=PADX, pady=PADY)
        linha += 1

        txt = f"Nome do Colaborador: {aloc['nme_colaborador']}"
        titulo = tk.Label(self.popup, text=txt, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, padx=PADX, pady=PADY)
        linha += 1

        txt = f"Nome da Função: {aloc['nme_funcao']}"
        titulo = tk.Label(self.popup, text=txt, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, padx=PADX, pady=PADY)
        linha += 1

        txt = f"Data Início Alocação: {conv.mysql_to_bra(aloc['dta_ini_alocacao'])}"
        titulo = tk.Label(self.popup, text=txt, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, padx=PADX, pady=PADY)
        linha += 1

        txt = f"Data Fim Alocação: {conv.mysql_to_bra(aloc['dta_fim_alocacao'])}"
        titulo = tk.Label(self.popup, text=txt, font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, padx=PADX, pady=PADY)
        linha += 1
        # Botão para excluir uma alocação
        self.popup.bt_excluir = tk.Button(self.popup, text="Excluir Alocação",
                                          command=lambda: self.excluir(),
                                          font='Helvetica 12 bold',
                                          fg='white',
                                          bg='blue')
        self.popup.bt_excluir.grid(row=linha, column=0, padx=PADX, pady=PADY)

    # Botão para confirmar a exclusão
    def excluir(self):
        resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esta alocação?")
        if resposta:
            cmd = "DELETE FROM ta_alocacao WHERE idt_alocacao = %s;"
            n = self.popup.sql.upd_del(cmd, [self.idt_alocacao])
            # Fechar a janela pop-up
            self.popup.destroy()
