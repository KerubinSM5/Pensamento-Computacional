from util.db import SQL

sql = SQL(esquema='bd_planejamento')

obj = (sql.get_object('select * from tb_funcao where idt_funcao = 4'))
print(obj)
print(obj['nme_funcao'])

lista = sql.get_list('select UPPER(nme_funcao) as funcao, concat("R$", vlr_dia_funcao) as custo from tb_funcao')
print(lista)