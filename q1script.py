import mysql.connector
import os
import glob

# Connect to MySQL
connection = mysql.connector.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

cursor = connection.cursor()

# Find the SQL file in the  directory
sql_file = glob.glob('../create_projects_table.sql')
print(f"Executing {sql_file}")
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
print("All SQL scripts executed successfully!")


print("\nVerifying `projects` table structure:")
cursor.execute("DESCRIBE projects;")
for row in cursor.fetchall():
    print(row)


# Close connection
cursor.close()
connection.close()