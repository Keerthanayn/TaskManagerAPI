Task Manager REST API
A beginner-friendly REST API built using Python and Flask to manage tasks through CRUD operations.
Features
- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update a complete task using PUT
- Update selected fields using PATCH
- Delete a task using DELETE

Technologies Used
- Python
- Flask
- REST API
- Postman
- Git and GitHub

Installation
git clone YOUR_GITHUB_REPOSITORY_URL
cd TaskManagerAPI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

API Endpoints
Method	        Endpoint	                Description
GET	             /tasks	                    Retrieve all tasks
GET	             /tasks/<id>	            Retrieve one task
POST	         /tasks	                    Create a task
PUT	             /tasks/<id>	            Update a complete task
PATCH	         /tasks/<id>	            Update selected fields
DELETE	         /tasks/<id>	            Delete a task

Testing
All endpoints can be tested using Postman