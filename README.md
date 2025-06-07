
## Question 1

1. **SQL Script Requirements:**
   - Create a new table named `projects` with the following columns:
     - `project_id`: `INT` auto-increment, primary key
     - `project_name`: `VARCHAR(255)` NOT NULL
     - `start_date`: `DATE`
     - `end_date`: `DATE`
   - Add a new column `budget` (`DECIMAL(10,2)`) to the `projects` table.

2. **Python Script Requirements:**
   - Automate execution of the above SQL script using `mysql-connector-python`.
   - Ensure all SQL commands run successfully and commit changes.

## Setup & Usage

Check the action tab to verify the workflow execution 
https://github.com/nmrepos/PROG8850Assignment2/actions/runs/15502788253

### SQL Code

```SQL
-- Creating the database
CREATE DATABASE IF NOT EXISTS projectdb;
USE projectdb;

-- Creating the new table named 'projects'
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Add a new column 'budget' to the existing 'projects' table
ALTER TABLE projects ADD COLUMN budget DECIMAL(10, 2);
```

### Python Code for executing the SQL

```python
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

# Path to the single SQL file
sql_file = './create_projects_table.sql'
print(f"Executing {sql_file}")

with open(sql_file, 'r') as file:
    sql_script = file.read()

# Split script into commands
commands = sql_script.split(';')

for command in commands:
    command = command.strip()
    if command:
        print(f"\nRunning: {command}\n")
        cursor.execute(command)


            
# Commit changes
connection.commit()
print("All SQL scripts executed successfully ✅!")


print("\nVerifying `projects` table structure:\n")
cursor.execute("DESCRIBE projects;")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
connection.close()
```




## Screenshot 1 – Running the Python Automation Script
![Screenshots1](/screenshots/Screenshot1.png)
![Screenshots2](/screenshots/Screenshot2.png)

## Screenshot 2 – Verifying the mycompany Database
![Screenshots3](/screenshots/Screenshot3.png)


Author : Nidhun Murali - 8981611
