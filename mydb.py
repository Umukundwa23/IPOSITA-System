import pymysql
dataBase = pymysql.connect(

    host = 'localhost',
    user = 'root',
    passwd = 'Mdiane232001'
)
# prepare a cursor object
cursorObject = dataBase.cursor()
# create a database
cursorObject.execute("CREATE DATABASE ipositadb"
)
print("All Done!")
