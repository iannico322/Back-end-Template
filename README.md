# Back-end Template

## Local Installation Process

Follow these steps to set up the project locally on your machine.

### 1. Prerequisites
- Install **XAMPP** (for MySQL database management).
- Install **Python 3.9.0** (Recommended version: [Download Python 3.9.0](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)). MAke sure to check the Add Path option during installation.


### 2. Database Setup
1. Start the MySQL and Apache modules in XAMPP.
2. Open **phpMyAdmin** in your browser.
3. Create a new database named `sample_db`.

### 3. Environment Setup
Open your terminal and run the following commands to install dependencies and set up the virtual environment:

```bash
# Install pipenv globally
pip install pipenv

# Activate the virtual environment
pipenv shell

# Install project dependencies
pipenv install
pip install django 
pip install -r requirements.txt
pip install django-extensions
```

### 4. Running the Application
Once the dependencies are installed, migrate the database and start the server:

```bash
# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver 0.0.0.0:8000
```

---

## PythonAnywhere Deployment Process

Follow these steps to deploy the backend on [PythonAnywhere](https://www.pythonanywhere.com/).

### 1. Source Code & Virtual Environment
1. Clone the backend repository from GitHub to your PythonAnywhere environment.
2. Open a Bash console in PythonAnywhere and create a virtual environment:

```bash
mkvirtualenv --python=/usr/bin/python3.9 venv
```

3. Navigate to your repository folder and install dependencies:

```bash
cd /YOUR_REPO_NAME
pip install -r requirements.txt
```

### 2. Database Setup
1. Go to the **Databases** tab in PythonAnywhere.
2. Create a new MySQL database and take note of your password.
3. Note your database connection details (Example):
   - **Database host address**: `YOUR_USERNAME.mysql.pythonanywhere-services.com`
   - **Username**: `YOUR_USERNAME`
4. Update your `settings.py` with these database credentials.

### 3. Web App Configuration
1. Go to the **Web** tab and create a new Web App (Manual Configuration, Python 3.9).
2. Set the **Virtualenv** path to the one you just created (e.g., `venv`).
3. Click on the **WSGI configuration file** link and update the Django section as follows:

```python
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# Set your project path
path = '/home/YOUR_USERNAME/YOUR_REPO_NAME'
if path not in sys.path:
    sys.path.append(path)

# Point to your settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Initialize WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
*(Make sure to replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual PythonAnywhere username and repository directory)*

### 4. Finalizing Deployment
Open a Bash console in PythonAnywhere and run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Finally, reload your Web App from the PythonAnywhere dashboard.
