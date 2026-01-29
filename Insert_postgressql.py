import psycopg2

db_params = {
    "host" : "127.0.0.1",
    "database" :"kishorebattula",
    "user" : '',
    "password" : '',
    "port" : "5433"
    }

id_ip = int(input("Please enter your id"))
name_ip = input("please enter your name")
sal = int(input("plese enter your salary"))

sqlquery ="insert into employee(id,name,salary) values (id_ip,name_ip,sal)"

try:
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    cur.execute(sqlquery)
    conn.commit()
    cur.close()
except (Exception,psycopg2.DatabaseError) as error:
     print(f"Error : {error}")
finally:
    if conn is not None:
        conn.close()