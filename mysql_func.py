import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="shopdb"
)


def add_product(product_name, barcode, quantity, price):
    mycursor = mydb.cursor()
    sql = "INSERT INTO productsdb (product_name, barcode, quantity, price) VALUES (%s, %s, %s, %s)"
    val = (product_name, barcode, quantity, price)    
    mycursor.execute(sql, val)
    mydb.commit()


def add_user(username, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO usersdb (username, password) VALUES (%s, %s)"
    val = (username, password)    
    mycursor.execute(sql, val)
    mydb.commit()


def get_products():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT product_name, barcode, quantity, price FROM productsdb")
    myresult = mycursor.fetchall()
    return myresult


def get_users():    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT username, password FROM usersdb")
    myresult = mycursor.fetchall()
    return myresult
    

def remove_product(product):
    mycursor = mydb.cursor()

    sql = "DELETE FROM productsdb WHERE product_name = %s"
    val = (product, )

    mycursor.execute(sql, val)

    mydb.commit()




