from util.db import SQL
from prettytable import PrettyTable


sql = SQL(esquema='bd_planejamento')
cmd = '''
SELECT cpf_colaborador, nme_colaborador, eml_colaborador,
      if(sts_colaborador = 'A', 'Administrador', 'Usuário Comum') as sts FROM tb_colaborador
'''


colaboradores = sql.get_list(cmd)
pt = PrettyTable(['CPF', 'Colaborador', 'Email', 'Status'])
for cl in colaboradores:
   print(cl)
   pt.add_row([cl['cpf_colaborador'], cl['nme_colaborador'], cl['eml_colaborador'], cl['sts']])


print(pt)
