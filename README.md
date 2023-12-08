# Event Scheduling and Registration System

This is a simple web application that allows users to schedule events, register for them, and maintains a record of the events and registrations. The application uses MySQL for its database, and you have two options to set up the database:



## Option 1: AWS RDS with MySQL Engine

1. Create your own RDS instance on AWS with the MySQL engine.
2. Make sure the RDS instance is open to internet access.
3. Replace the inactive RDS instance endpoint in the `views.py` file with the new `endpoint`.
4. Update the `username` and `password` in the `database_creation.py` file with the credentials you will use to establish a connection.
5. Run `database_creation.py` to create the necessary database, tables, and relationships.


## Option 2: Local MySQL Installation

1. Install MySQL on your local machine and configure a username and password.
2. Replace the inactive RDS instance endpoint in the `views.py` file with the appropriate local MySQL connection details.
3. Update the `username` and `password` in the `database_creation.py` file with the credentials you used while installing MySQL.
4. Use `localhost` for the database host
5. Run `database_creation.py` to create the necessary database, tables, and relationships.



# Running the Application

Follow the steps below to run the Event Scheduling and Registration System application using a local MySQL installation:

1. **Install MySQL/RDS instance:**
   - Install MySQL on your local machine or use AWS RDS (Follow above steps).

2. **Update Connection Details:**
   - Replace the inactive RDS instance endpoint in the `views.py` file with the appropriate local MySQL connection or new RDS endpoint details.

3. **Create Database and Tables:**
   - Run `database_creation.py` to create the necessary database, tables, and relationships.
   - Update the `username` and `password` in the `database_creation.py` file with the credentials you will use to establish a connection.

4. **Install Required Libraries:**
   - Open a terminal and run the following command:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Server:**
   - Execute the following command to run the server:
     ```bash
     python manage.py runserver
     ```

6. **Access the Application:**
   - Use the local address or EC2 instances public IP in which it is running.
     ```bash
     127.0.0.0/home
     ```

## **Important Note** ##
  - This application is built for educational purposes and it is not for production.
  - It's essential to follow security best practices when deploying applications to production environments. 
  - Avoid exposing sensitive information, such as database credentials, in public repositories. Consider using environment variables or other secure methods for configuration.

**Feel free to explore and modify the code to suit your needs. If you encounter any issues or have suggestions for improvements, please open an issue on this repository.**


