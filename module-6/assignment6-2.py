import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "botiwaK",
    "password": "password",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True  # Corrected the key name
}

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\nPress any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    if 'db' in locals() and db.is_connected():
        db.close()