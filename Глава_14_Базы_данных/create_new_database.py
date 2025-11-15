import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',        # пользователь MySQL
    password='dn100684ekv!' # пароль MySQL
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE my_test;")  # Название новой базы
connection.commit()

print("🎉 База данных успешно создана!")

cursor.close()
connection.close()