import mysql.connector
from mysql.connector import cursor


def insert (link):
    db = mysql.connector.connect(
        # host="localhost",
        # user="root ",
        # password="",
        # database = "mydatabase"
        host="dz8959rne9lumkkw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="q1lq2q6eliwfge0e",
        password="tidm9irx6ljbvhx5",
        database="a001ta7fuectz1bw"
    )
    cursor = db.cursor()
    ## defining the Query
    query = "INSERT INTO links (id, link) VALUES (%s, %s)"
    ## storing values in a variable
    values = (0,link)

    ## executing the query with values
    cursor.execute(query, values)

    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()

    print(cursor.rowcount, "record inserted")


def read ():
    db = mysql.connector.connect(
        # host="localhost",
        # user="root ",
        # password="",
        # database = "mydatabase"
        host="dz8959rne9lumkkw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="q1lq2q6eliwfge0e",
        password="tidm9irx6ljbvhx5",
        database="a001ta7fuectz1bw"
    )
    cursor = db.cursor()
    ## defining the Query
    query = "SELECT link FROM links"

    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    links = []
    for record in records:
        links.append(record[0])

    return links