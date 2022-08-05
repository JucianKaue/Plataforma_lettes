import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=""
)

cursor = mydb.cursor()

n = 1

cursor.execute("USE mydb;")
cursor.execute(
    f"INSERT INTO curriculo (idcurriculo, nome, CPF, telefone, email, resumo, ultimaatualizacao) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    ('DEFAULT', 'Ademir Decezare', '854.422.546-87', '3423456512', 'ademirdecezare@gmail.com', 'Pai de familia', '2022-08-04'))
mydb.commit()
print(cursor.rowcount)

