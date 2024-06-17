import mysql.connector


data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='testing2021'
)

cursor = data_base.cursor()

cursor.execute("CREATE TABLE items_rates(item varchar(255), rates FLOAT)")