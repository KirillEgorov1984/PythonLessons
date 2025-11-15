import pymysql

connection = pymysql.connect(
    host='localhost',      # или IP сервера
    user='root',           # имя пользователя MySQL
    password='dn100684ekv!',   # пароль
    database='sakila',     # имя базы данных
    port=3306              # порт MySQL
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM actor LIMIT 5")

for row in cursor.fetchall():
    print(row)

connection.close()