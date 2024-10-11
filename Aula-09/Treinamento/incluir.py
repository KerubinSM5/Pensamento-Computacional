import mysql.connector
# Informações de conexão
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ceub123456",
  database="bd_planejamento"
)

#entrada de dados
funcao = input("Digite o nome da funcao: ")
diaria = float(input("Qual o valor da diária? "))

cmd = 'INSERT INTO tb_funcao values(default, %s, %s)'
mycursor = mydb.cursor()
mycursor.execute(cmd, (funcao, diaria)) #substitui os %s em suas respectivas posições
mydb.commit()

print("Incluido com sucesso!")

mycursor.close()
mydb.close()
