from util.db import SQL

projetos = [['Controle de acesso de visitantes', '2024-10-05'],
                 ['Controle de Atendimento de Monitoria', '2024-10-06'],
                 ['Gestão de Cursos', '2024-10-07'],
                 ]

sql = SQL(esquema='bd_planejamento')
cmd = '''INSERT INTO tb_projeto(nme_projeto, dta_ini_projeto) VALUES (%s, %s)'''

for projeto in projetos:
    idt = sql.insert(cmd, projeto)
    print('Criado Projeto: ', idt)