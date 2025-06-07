import mysql.connector
from mysql.connector import Error

def execute_sql_script(host, user, password, database, sql_file_path):

    connection = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Read SQL commands from file
            with open(sql_file_path, 'r') as sql_file:
                sql_script = sql_file.read()
            
            # Split the script into individual commands
            sql_commands = sql_script.split(';')
            
            # Execute each command
            for command in sql_commands:
                command = command.strip()
                if command:  # Skip empty commands
                    print(f"Executing: {command}")
                    cursor.execute(command)
            
            # Commit changes
            connection.commit()
            print("All SQL commands executed successfully!")
            return True
            
    except Error as e:
        print(f"Error: {e}")
        if connection and connection.is_connected():
            connection.rollback()  # Rollback changes on error
            print("Changes rolled back due to error")
        return False
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    host = "localhost"
    user = "nidhun"
    password = "Admin@123"
    database = "mycompany"
    sql_file_path = "create_projects_table.sql"
    
    # Execute the SQL script
    success = execute_sql_script(host, user, password, database, sql_file_path)
    
    if success:
        print("Database schema changes applied successfully")
    else:
        print("Failed to apply database schema changes")