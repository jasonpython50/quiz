Django Quiz Application
This is a simple quiz application built using Django and Bootstrap 5.
Features
•
Displays a list of multiple choice questions
•
Allows users to submit answers
•
Calculates and displays the total score after submission
Installation and Setup
Prerequisites
•
Python 3.x
•
Django 
Steps
1. Clone this repository
2.  Navigate to the project directory
3.  Create a virtual environment and activate it, pipenv required.
4.  Install the required dependencies
5.    Run migrations. 
python manage.py makemigrations QuizApp
python manage.py migrate
6. Run the server
python manage.py runserver
Usage
Once the server is running, you can navigate to `localhost:8000` in your web browser to start the quiz.
To add new questions, you will need to access the Django admin site.
