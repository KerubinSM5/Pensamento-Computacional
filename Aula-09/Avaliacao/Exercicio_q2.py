#Questâo 2
from prettytable import PrettyTable
from util.db import SQL

sql = SQL(esquema='bd_planejamento')
cmd = '''SELECT nme_projeto, dta_ini_projeto, dta_fim_projeto FROM tb_projeto'''

projetos = sql.get_list(cmd)
pt = PrettyTable(['nome do projeto', 'Data de inicio', 'Data de final'])
for pr in projetos:
    print(pr)
    pt.add_row([pr['nme_projeto'], pr['dta_ini_projeto'], pr['dta_fim_projeto']])

print(pt)
