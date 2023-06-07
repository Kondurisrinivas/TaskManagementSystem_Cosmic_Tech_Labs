# TaskManagementSystem_Cosmic_Tech_Labs
This is a simple task management application that allows users to create, update, and track their tasks efficiently. The application provides basic functionality for managing tasks and uses a MySQL database for persistent storage.

Features

1.Task Creation:
Users can create tasks by providing a task name, description, and due date.
Each task is assigned a unique identifier or task ID.

2.Task Update and Completion:
Users can update task details such as name, description, and due date.
Tasks can be marked as completed by the user.

3.Task Listing and Sorting:
Users can view a list of all tasks.
asks are sorted based on their due dates, with recently added tasks displayed first.

4.Task Search and Filtering:
Users can search for specific tasks by their names or descriptions.
Users can filter tasks based on their completion status (completed or pending).

#Technologies Used
Python
MySQL
MySQL Connector/Python

#Setup and Installation
-->Clone the repository: git clone https://github.com/your-username/task-management-app.git
-->Create a virtual environment: python -m venv venv
-->Activate the virtual environment:
-For Windows: venv\Scripts\activate.bat
-For Unix or Linux: source venv/bin/activate
-->Install the required dependencies: pip install -r requirements.txt
-->Set up the MySQL database:
-->Create a new database named task_management.
-->Update the database connection details in the tasks.py file.
-->Run the application: python tasks.py

#Usage
Create a task:
Use the create_task function to create a new task by providing the task name, description, and due date.

Update a task:
Use the update_task function to update an existing task by providing the task ID and the updated details.

Mark a task as completed:
Use the mark_task_completed function to mark a task as completed by providing the task ID.

View all tasks:
Use the get_all_tasks function to retrieve a list of all tasks.

Search for tasks:
Use the search_tasks function to search for tasks by providing a keyword.

Filter tasks by completion status:
Use the filter_tasks_by_completion function to filter tasks based on their completion status (0 for pending, 1 for completed).

#Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

#Contact
For any inquiries or questions, you can reach me at srinukonduri7703@gmail.com
Feel free to update the sections and information based on your specific application. Include any additional instructions or details that might be relevant for users to set up and use your task management application.
