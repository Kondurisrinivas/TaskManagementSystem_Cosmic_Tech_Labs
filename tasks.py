from datetime import datetime
import mysql.connector
from mysql.connector import Error

#Connecting To Mysql Database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='task_management',
            user='root',
            password='root'
        )
        if conn.is_connected():
            print('Connected to the MySQL database')
            return conn

    except Error as e:
        print(f'Error connecting to MySQL: {e}')

# Call the function to establish the database connection
connection = connect_to_database()

#Creating Task
def create_task(name, description, due_date):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        query = """
        INSERT INTO tasks (name, description, due_date)
        VALUES (%s, %s, %s)
        """
        data = (name, description, due_date)
        cursor.execute(query, data)

        conn.commit()
        print("Task created successfully")

    except Error as e:
        print(f'Error creating task: {e}')
    

# creating Unique ID here making taskid as unique id
def update_task(task_id, name, description, due_date):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        query = """
        UPDATE tasks
        SET name = %s, description = %s, due_date = %s
        WHERE task_id = %s
        """
        data = (name, description, due_date, task_id)
        cursor.execute(query, data)

        conn.commit()
        print("Task updated successfully")

        return True

    except Error as e:
        print(f'Error updating task: {e}')
        return False


#marking task by user as task completed

def mark_task_completed(task_id):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        query = """
        UPDATE tasks
        SET completed = TRUE
        WHERE task_id = %s
        """
        data = (task_id,)
        cursor.execute(query, data)

        conn.commit()
        print("Task marked as completed")

        return True

    except Error as e:
        print(f'Error marking task as completed: {e}')
        return False


#User can get a view of all the tasks4 and ther description and duedate and status also
def get_all_tasks():
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            SELECT *
            FROM tasks
            ORDER BY due_date ASC
            """
            cursor.execute(query)
            tasks = cursor.fetchall()

            cursor.close()

            return tasks
    except Error as e:
        print(e)

# user can search task based on the name or description but here as of any keyword
def search_tasks(keyword):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            SELECT *
            FROM tasks
            WHERE name LIKE %s OR description LIKE %s
            """
            data = (f"%{keyword}%", f"%{keyword}%")
            cursor.execute(query, data)
            tasks = cursor.fetchall()
            cursor.close()
            return tasks
    except Error as e:
        print(e)

# user can filter tasks based on their status here 0--> is pending and 1--> is completed
def filter_tasks_by_completion(status):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        filter_query = f"SELECT * FROM tasks WHERE completed = {status}"
        cursor.execute(filter_query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f'Error filtering tasks: {e}')
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Database connection closed')


print("-------------create Task----------------------")
task_created = create_task("Task 1", "This is the description of Task 1", "2023-06-30")

print("-------------Update Task------------------")
update_task(3, "New Task Name", "Updated description", "2023-07-15")

print("-------------Mark Task as completed----------------")
mark_task_completed(1)

print("-----------Get all tasks view----------------------")
print(get_all_tasks())

print("-----------search task------------------------------")
print(search_tasks('Updated description'))

print("-------------Filter Tasks based on status-------------------")
filtered_tasks = filter_tasks_by_completion(1)
print(filtered_tasks)