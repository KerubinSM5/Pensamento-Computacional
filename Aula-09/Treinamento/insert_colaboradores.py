from util.db import SQL

colaboradores = [['222.222.222-22', 'Renato Sales dos Santos', 'renato.sales@gmail.com', 'A', '123#@!'],
                 ['333.333.333-33', 'Francisco Regis', 'francisco.regis@gmail.com', 'C', '098)(*'],
                 ['444.444.444-44', 'Ana Flávia Dias', 'ana.dias@gmail.com', 'C', 'afd1973'],
                 ]

sql = SQL(esquema='bd_planejamento')
cmd = '''
INSERT INTO tb_colaborador(cpf_colaborador, nme_colaborador, eml_colaborador, sts_colaborador, pwd_colaborador)
VALUES (%s, %s, %s, %s, SHA(%s))
'''

for colaborador in colaboradores:
    idt = sql.insert(cmd, colaborador)
    print('Criado colaborador: ', idt)
