# TODO App

A command-line TODO application built with Python and PostgreSQL for managing tasks and evaluating their priority.

## Features

* Create tasks
* View all tasks
* Update existing tasks
* Delete tasks
* Mark tasks as completed
* Calculate task priority based on:

  * Task type
  * Remaining workload
  * Due date
  * Current progress

## Technologies

* Python
* PostgreSQL
* psycopg
* python-dotenv

## Setup

1. Clone the repository.

2. Install the required packages from requirements.txt

3. Create a PostgreSQL database named "tasks".

4. Run the SQL statements in "schema.sql" to create the required table.

5. Create a ".env" file in the project directory containing your database configuration:

   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=tasks
   DB_USER=postgres
   DB_PASSWORD=your_password_here

7. Run the application:

   python main.py
