import psycopg2
  # try:
  #   connection = psycopg2.connect(user = "postgres",
  #                                 password = "0000",
  #                                 host = "localhost",
  #                                 port = "5432",
  #                                 database = "my_database")
  #   #connection = psycopg2.connect('postgres://postgres:0000@localhost:5432/my_database')
  #     # db = scoped_session(sessionmaker(bind = connection))
  #     # db.execute("SELECT * FROM flights")
  #   connection.autocommit = False
  #   cursor = connection.cursor()#opens cursor to write in database and fetch queries.
    #cursor.execute('CREATE TABLE data(name VARCHAR NOT NULL, age INTEGER NOT NULL)')
    # f = open("some_data.csv")
    # reader = csv.reader(f)
    # for c1,c2,c3,c4,c5,c6,c7,c8 in reader:
    #   cursor.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s,%s)",(c1,c2,c3,c4,c5,c6,c7,c8))
    # connection.commit()#saving the changes
    # f.close() 

  # except (Exception, psycopg2.Error) as error :
  #   print ("Error while connecting to PostgreSQL", error)
  # finally:
  #   if(connection):
  #     cursor.close()
  #     connection.close()
  #     print("CONNECTION CLOSED")

def enter_data(email,password):
  try:
    connection = psycopg2.connect(
      user = 'postgres',password = '0000',host='localhost',port='5432',database='my_database')
    connection.autocommit = False
    cursor = connection.cursor()

    cursor.execute("insert into details values('{}','{}')".format(email,password))
    connection.commit()

  except (Exception,psycopg2.Error) as error:
    print("Error while connecting!", error)
  finally:
    if(connection):
      cursor.close()
      connection.close()

def verify_id(email,password):
  try:
    connection = psycopg2.connect(
      user = 'postgres',password = '0000',host='localhost',port='5432',database='my_database')
    connection.autocommit = False
    cursor = connection.cursor()

    cursor.execute("select email,pass from details where email = '{}' and pass = '{}' ".format(email,password))
    table = cursor.fetchall()
    connection.commit()
    if(table):
      return True
    else:
      return False

  except (Exception,psycopg2.Error) as error:
    print("Error while connecting!", error)
  finally:
    if(connection):
      cursor.close()
      connection.close()

def main():
  ans = verify_id('me.manu@gil.com','123456')
  print(ans)
if __name__ == "__main__":
  main()