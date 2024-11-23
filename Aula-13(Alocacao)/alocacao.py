import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from util.db import SQL
from util.lv import LV
from util import converter as conv
from inc_alocacao import IncluirAloc
from folder import Folder
from financeiro import Financeiro
from alt_alocacao import AlterarAloc
from exc_alocacao import ExcluirAloc


class Alocacao(tk.Tk):
    def __init__(self):
        super().__init__()
        # Criação de constantes
        self.PADX = 10
        self.PADY = 10

        self.title("Alocação de Colaboradores em Projetos")

        linha = 0
        # Título
        titulo = tk.Label(self, text="Alocação de Colaboradores em Projetos", font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=linha, column=0, columnspan=5, padx=self.PADX, pady=self.PADY)
        linha += 1

        # Buscar o projeto para manipular
        lb_nome = tk.Label(self, text="Projeto", font='Helvetica 12 bold', fg='blue')
        lb_nome.grid(row=linha, column=0, padx=self.PADX, pady=self.PADY)

        self.bt_lv = tk.Button(self, text="LV", command=self.lista_valores, font='Helvetica 12 bold', fg='white',
                               bg='blue')
        self.bt_lv.grid(row=linha, column=1, padx=self.PADX, pady=self.PADY)

        self.id_projeto_var = tk.StringVar()
        self.et_id_projeto = ttk.Entry(self, textvariable=self.id_projeto_var, font='Helvetica 16 bold',
                                       foreground='green', width=5, state="readonly")
        self.et_id_projeto.grid(row=linha, column=2, padx=self.PADX, pady=self.PADY)

        self.projeto_var = tk.StringVar()
        self.et_projeto = ttk.Entry(self, textvariable=self.projeto_var, font='Helvetica 16 bold', foreground='green',
                                    width=50, state="readonly")
        self.et_projeto.grid(row=linha, column=3, padx=self.PADX, pady=self.PADY)

        self.bt_buscar = tk.Button(self, text="Buscar", command=self.buscar, font='Helvetica 12 bold', fg='white',
                                   bg='blue')
        self.bt_buscar.grid(row=linha, column=4, padx=self.PADX, pady=self.PADY)
        linha += 1

        # Treeview para exibir as alocações do projeto
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Arial", 12), foreground="blue")
        self.tre_alocacao = ttk.Treeview(self, columns=("idt", "col", "fun", "dini", "dfim"), show="headings",
                                         style="Custom.Treeview")
        # Configurar as colunas
        self.tre_alocacao.heading("idt", text="Identificador")
        self.tre_alocacao.heading("col", text="Colaborador")
        self.tre_alocacao.heading("fun", text="Função")
        self.tre_alocacao.heading("dini", text="Início")
        self.tre_alocacao.heading("dfim", text="Fim de Alocação")
        # Ajustar a largura das colunas
        self.tre_alocacao.column("idt", width=100)
        self.tre_alocacao.column("col", width=300)
        self.tre_alocacao.column("fun", width=300)
        self.tre_alocacao.column("dini", width=150)
        self.tre_alocacao.column("dfim", width=150)
        self.tre_alocacao.grid(row=linha, column=0, columnspan=5, padx=self.PADX, pady=self.PADY)
        linha += 1

        self.bt_incluir = tk.Button(self, text="Incluir", command=self.incluir, font='Helvetica 12 bold', fg='white',
                                    bg='blue')
        self.bt_incluir.grid(row=linha, column=0, padx=self.PADX, pady=self.PADY)

        self.bt_alterar = tk.Button(self, text="Alterar", command=self.alterar, font='Helvetica 12 bold', fg='white',
                                    bg='blue')
        self.bt_alterar.grid(row=linha, column=1, padx=self.PADX, pady=self.PADY)

        self.bt_excluir = tk.Button(self, text="Excluir", command=self.excluir, font='Helvetica 12 bold', fg='white',
                                    bg='blue')
        self.bt_excluir.grid(row=linha, column=2, padx=self.PADX, pady=self.PADY)

        self.bt_folder = tk.Button(self, text="Folder do Projeto", command=self.folder, font='Helvetica 12 bold',
                                   fg='white',
                                   bg='blue')
        self.bt_folder.grid(row=linha, column=3, padx=self.PADX, pady=self.PADY)

        self.bt_financeiro = tk.Button(self, text="Financeiro", command=self.financeiro,
                                       font='Helvetica 12 bold',
                                       fg='white', bg='blue')
        self.bt_financeiro.grid(row=linha, column=4, padx=self.PADX, pady=self.PADY)

        # Criando o objeto que irá acessar o banco de dados
        self.sql = SQL(esquema='bd_planejamento')

    def lista_valores(self):
        cmd = '''
             SELECT idt_projeto as idt,
                    CONCAT(nme_projeto, ' - Início: ', DATE_FORMAT(dta_ini_projeto, '%d/%m/%Y')) as txt
             FROM tb_projeto
             WHERE nme_projeto LIKE CONCAT('%', %s, '%') ORDER BY nme_projeto;
       '''

        lv = LV(janela_mestre=self, title_text="Escolha um Projeto", label_filter="Projeto", var_id="id_projeto_var",
                var_text="projeto_var", cmd=cmd)

    def buscar(self):
        idt_projeto = self.id_projeto_var.get()
        if idt_projeto == "":
            messagebox.showerror("Erro: Clique em LV", "Clique em LV e escolha um projeto para fazer gestão!")
            return
        else:
            cmd = """SELECT idt_alocacao, nme_colaborador, nme_funcao, dta_ini_alocacao, dta_fim_alocacao
                    FROM tb_colaborador JOIN ta_alocacao ON idt_colaborador = cod_colaborador
                         JOIN tb_funcao ON idt_funcao = cod_funcao
                    WHERE cod_projeto = %s
                    ORDER BY nme_colaborador;
           """
            self.limpar_tabela()
            alocacoes = self.sql.get_list(cmd, [idt_projeto])
            for aloc in alocacoes:
                self.tre_alocacao.insert("", tk.END,
                                         values=(aloc['idt_alocacao'], aloc['nme_colaborador'], aloc['nme_funcao'],
                                                 conv.mysql_to_bra(aloc['dta_ini_alocacao']),
                                                 conv.mysql_to_bra(aloc['dta_fim_alocacao'])))

    def pegar_idt(self):
        selecao = self.tre_alocacao.selection()
        if selecao:
            linha = self.tre_alocacao.selection()[0]
            valores = self.tre_alocacao.item(linha, "values")
            return valores[0]
        else:
            return 0

    def limpar_tabela(self):
        for linha in self.tre_alocacao.get_children():
            self.tre_alocacao.delete(linha)

    def incluir(self):
        if self.id_projeto_var.get() == "":
            messagebox.showerror("Erro: Clique em LV", "Escolha um projeto através do LV antes de incluir alocação!")
        else:
            inc = IncluirAloc(janela_mestre=self, idt_projeto=self.id_projeto_var.get(),
                              nme_projeto=self.projeto_var.get())
            self.limpar_tabela()

    def alterar(self):
        idt = self.pegar_idt()
        if idt != 0:
            alt = AlterarAloc(janela_mestre=self, idt_projeto=self.id_projeto_var.get(),
                              nme_projeto=self.projeto_var.get(), idt_alocacao=idt)
            self.limpar_tabela()
        else:
            messagebox.showerror("Erro: Escolha uma alocação", "Marque uma linha da tabela para selecionar a alocação")

    def excluir(self):
        idt = self.pegar_idt()
        if idt != 0:
            alt = ExcluirAloc(janela_mestre=self, idt_projeto=self.id_projeto_var.get(),
                              nme_projeto=self.projeto_var.get(), idt_alocacao=idt)
            self.limpar_tabela()
        else:
            messagebox.showerror("Erro: Escolha uma alocação", "Marque uma linha da tabela para selecionar a alocação")

    def folder(self):
        idt_projeto = self.id_projeto_var.get()
        if idt_projeto == "":
            messagebox.showerror("Erro: Clique em LV", "Clique em LV e escolha um projeto para fazer gestão!")
            return
        else:
            arq = filedialog.asksaveasfilename(
                defaultextension=".docx",
                filetypes=[("Arquivo do Word", "*.docx")]
            )

            if arq:
                # Gerar arquivo de Folder do Projeto
                f = Folder()
                f.arquivo = arq
                f.idt_projeto = idt_projeto
                f.gerar_folder()
                messagebox.showinfo("Arquivo gerado", f"O Folder {arq} foi gerado com sucesso!")

    def financeiro(self):
        idt_projeto = self.id_projeto_var.get()
        if idt_projeto == "":
            messagebox.showerror("Erro: Clique em LV", "Clique em LV e escolha um projeto para fazer gestão!")
            return
        else:
            arq = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Arquivo do Excel", "*.xlsx")]
            )

            if arq:
                # Gerar arquivo de Folder do Projeto
                f = Financeiro()
                f.arquivo = arq
                f.idt_projeto = idt_projeto
                f.gerar_planilha()
                f.salvar()
                messagebox.showinfo("Arquivo gerado", f"O financeiro {arq} foi gerado com sucesso!")


if __name__ == '__main__':
    app = Alocacao()
    app.mainloop()
