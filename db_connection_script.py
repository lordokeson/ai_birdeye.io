import os
from dotenv import load_dotenv
import psycopg2  # Example for PostgreSQL, change based on your DB

# Load environment variables from .env file for security reasons
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        # Replace these with your specific database details or environment variable keys
        self.host = os.getenv('127.0.0.1')
        self.port = os.getenv('DB_PORT')
        self.database = os.getenv('AISheild')
        self.user = os.getenv('Admin')
        self.password = os.getenv('DB_PASSWORD')
        self.conn = None

    def open_connection(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.database,
                user=self.user,
                password=self.password
            )
            print("Database connection successfully established.")
        except Exception as e:
            print(f"An error occurred while connecting to the database: {e}")
            self.conn = None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Usage
if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.open_connection()
    # Perform database operations here
    db_connection.close_connection()
