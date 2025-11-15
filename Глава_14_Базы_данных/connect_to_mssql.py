import pyodbc

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-1JG6V36\\SQLEXPRESS;'
    'DATABASE=master;'
    'Trusted_Connection=yes;'
    'Encrypt=no;'
    'TrustServerCertificate=yes;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sys.databases")
databases = cursor.fetchall()
for db in databases:
    print(db[0])

