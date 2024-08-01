### README for Todo App

---

# Todo App

A simple and intuitive Todo application built with Django. This app allows users to register, log in, create, edit, delete, and search for their personal todo tasks.

## Features

- User registration and login
- User authentication
- Add, edit, and delete tasks
- Search tasks
- Responsive design using Bootstrap

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** SQLite (default Django database)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Django 3.0+
- Pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AdityaKumbhar21/todo-app.git
cd todo-app
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply the migrations to set up the database:

```bash
python manage.py migrate
```

5. Create a superuser to access the admin panel (optional):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to see the application running.

### Usage

1. Register a new user account.
2. Log in with your credentials.
3. Add, edit, and delete your todo tasks.
4. Search for tasks using the search bar.

### Deployment

To deploy this application, follow the documentation for your preferred deployment platform. Common options include Heroku, Render, and DigitalOcean.

### Live Demo
Check out the live demo of the project: [Todo App](https://todo-app-e5vs.onrender.com/)

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.



### Acknowledgments

- Django documentation
- Bootstrap documentation

---

