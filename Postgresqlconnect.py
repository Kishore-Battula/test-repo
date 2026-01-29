import psycopg2

connection = psycopg2.connect(database='kishorebattula',user='', password='',host="127.0.0.1",port=5433)
cursor = connection.cursor()
cursor.execute("select * from employee")
record = cursor.fetchall()
print("Data from Databses:-",record)