import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "botiwaK",
    "password": "password",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    query1 = "SELECT * FROM studio"
    cursor.execute(query1)
    result1 = cursor.fetchall()
    print("\n-- DISPLAYING Studio RECORDS --")
    for row in result1:
        print("Studio ID: {}\nStudio Name: {}\n".format(row[0], row[1]))

    # Query 2: Select all fields from the genre table
    query2 = "SELECT * FROM genre"
    cursor.execute(query2)
    result2 = cursor.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")
    for row in result2:
        print("Genre ID: {}\nGenre Name: {}\n".format(row[0], row[1]))

    # Query 3: Select movie names for movies with a run time of less than two hours
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    cursor.execute(query3)
    result3 = cursor.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")
    for row in result3:
        print("Film Name: {}\nRuntime: {}\n".format(row[0], row[1]))

    # Query 4: Get a list of film names and directors grouped by director
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_director"
    cursor.execute(query4)
    result4 = cursor.fetchall()
    print("\n-- DISPLAYING Director RECORDS in Order --")
    for row in result4:
        print("Film Name: {}\nDirector: {}\n".format(row[0], row[1]))
    
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
        cursor.close()
        db.close()