import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "botiwaK",
    "password": "password",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    query = """
    SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS Studio
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    print("\n-- {} --".format(title))
    for row in results:
        print("Name: {}\nDirector: {}\nGenre: {}\nStudio: {}\n".format(row[0], row[1], row[2], row[3]))

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()

    # Initial display of films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new record into the film table
    insert_query = """
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate)
    VALUES ('Inception', 'Christopher Nolan', 2, 3, 148, '2010')
    """
    cursor.execute(insert_query)
    db.commit()
    
    # Display films after insertion
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update the genre of the film 'Alien' to being a Horror film
    update_query = """
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
    """
    cursor.execute(update_query)
    db.commit()
    
    # Display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the movie 'Gladiator'
    delete_query = """
    DELETE FROM film
    WHERE film_name = 'Gladiator'
    """
    cursor.execute(delete_query)
    db.commit()
    
    # Display films after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

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