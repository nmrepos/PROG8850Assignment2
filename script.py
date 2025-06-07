import mysql.connector
import os
import glob

# Connect to Azure MySQL
connection = mysql.connector.connect(
    host=os.environ['AZURE_MYSQL_HOST'],
    user=os.environ['AZURE_MYSQL_USER'],
    password=os.environ['AZURE_MYSQL_PASSWORD'],
    database=os.environ['AZURE_MYSQL_DATABASE']
)

cursor = connection.cursor()

# Find all SQL files in the sql directory
sql_files = glob.glob('sql/*.sql')

for sql_file in sql_files:
    print(f"Executing {sql_file} on Azure MySQL")
    with open(sql_file, 'r') as file:
        sql_script = file.read()
        
    # Split script into commands
    commands = sql_script.split(';')
    
    for command in commands:
        command = command.strip()
        if command:
            print(f"Running: {command}")
            cursor.execute(command)
            
# Commit changes
connection.commit()

# Close connection
cursor.close()
connection.close()

print("All SQL scripts executed successfully on Azure MySQL!")