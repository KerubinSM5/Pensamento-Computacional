import mysql.connector
# Informações de conexão
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ceub123456",
  database="bd_planejamento"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_funcao") #executa o comando para mostrar os resultados
myresult = mycursor.fetchall() #puxa todos os resultados
for x in myresult: #puxa e imprime cada linha da tabela
  print(x)
mycursor.close()
mydb.close()
