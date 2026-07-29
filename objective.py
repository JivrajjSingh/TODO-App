from datetime import datetime
import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

class Todo:

    def __init__(self, action_name, action_type, allocated_time, action_due_date, action_completed = False, action_id = None):
        
        self.action_name = action_name
        self.action_type = action_type
        self.allocated_time = allocated_time
        self.action_due_date = action_due_date
        self.action_completed = action_completed
        self.action_id = action_id
    

    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    def insert_task(self):
        
        self.cursor.execute(
            """INSERT INTO to_do (action_name, action_type, allocated_time, action_due_date, action_completed)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING action_id 
            """,
            (
                self.action_name, 
                self.action_type, 
                self.allocated_time, 
                self.action_due_date, 
                self.action_completed
            )   
        )
        self.action_id = self.cursor.fetchone()[0]
        self.connection.commit()


    valid_columns = {
        "name" : "action_name",
        "type" : "action_type",
        "time" : "allocated_time",
        "due_date" : "action_due_date"
    }  

    def update_task(self):
        task_id = int(input("Which task would you like to modify? "))
        print("You can modify the following fields: ")
        print(self.valid_columns.keys())

        query = input("Which attribute would you like to modify?")
        if query not in self.valid_columns:
            print("Invalid attribute")
            return

        column = self.valid_columns[query]
        if column == "action_due_date":
            value = input("New Deadline: ")
            new_value = datetime.strptime(value, "%d/%m/%Y").date()

        elif column == "allocated_time":
            new_value = int(input("New Hours Value: "))

        else:
            new_value = input("New Value: ")

        self.cursor.execute(
            f""" UPDATE to_do
            SET {column} = %s
            WHERE action_id = %s """,
             (new_value, task_id)
        )
        self.connection.commit()

    def delete_task(self):
        task_id = int(input("Which task would you like to delete? "))
        
        self.cursor.execute("""
        DELETE FROM to_do WHERE action_id = %s""",
        (task_id,)
        )

        if self.cursor.rowcount == 0:
            print("No task with that ID exists.")
        else:
            self.connection.commit()
            print("Task deleted")

    def complete_task(self):
            completed_task_id = int(input("Which task have you completed? "))
            self.cursor.execute("""
                UPDATE to_do SET action_completed = TRUE 
                WHERE action_id = %s """,
            (completed_task_id,)

            )
            if self.cursor.rowcount == 0:
                print("No task with that ID exists.")
            else:
                self.connection.commit()
                print("Task marked as completed.")

    def get_tasks(self):
        self.cursor.execute("""
            SELECT * FROM to_do
        """)
        rows = self.cursor.fetchall()
        tasks = []

        for row in rows:
            task = Todo(
                action_name=row[1],
                action_type=row[2],
                allocated_time=row[3],
                action_due_date=row[4],
                action_completed=row[5],
                action_id=row[0],
            )
            tasks.append(task)

        return tasks
    def __str__(self):
        return f"""
        ID: {self.action_id}, Name:{self.action_name}, Type: {self.action_type}, 
        Time: {self.allocated_time}, Due_date:{self.action_due_date} , Completed:{self.action_completed}
        """
    def __repr__(self):
        return self.__str__()
