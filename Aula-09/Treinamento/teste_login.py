from util.db import SQL

cpf = input('Digite o CPF: ')
senha = input('Digite o Senha: ')

cmd = '''
SELECT nme_colaborador, sts_colaborador FROM tb_colaborador WHERE idt_colaborador = %s
'''

sql = SQL(esquema='bd_planejamento')

colaborador = sql.get_object(cmd, [cpf, senha])

if colaborador is None:
    print('Falha no Login')
else:
    print('Bem vindo ao sistema')
    print(colaborador['nme_colaborador'])
    print('Função:', ('Administrador' if colaborador['sts_colaborador'] == 'A' else 'Usuário Comum'))
