import mysql.connector
import settings

logger = settings.logging.getLogger("bot")


def insert(player, wins, losses):
    # Establish the connection to the MySQL database
    connection = mysql.connector.connect(
        host='212.132.108.197',    # Replace with your host, e.g., 'localhost' or '127.0.0.1'
        user='user1', # Replace with your MySQL username
        password='N32%5dQ4', # Replace with your MySQL password
        database='ranking'  # Replace with your database name
    )

    if connection.is_connected():
        print("Successfully connected to the database")

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the SQL query to create a table
        insert_query = '''
        INSERT INTO game2 (player, wins, losses) VALUES (%s, %s, %s)'''

        # Execute the query
        cursor.execute(insert_query, (player, wins, losses))
        connection.commit()
        logger.info(f"inserted query {insert_query}")
        cursor.close()
        connection.close()
        print("MySQL connection is closed")