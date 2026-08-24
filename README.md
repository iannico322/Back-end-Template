# Back-end Template

## Local Installation Process

Follow these steps to set up the project locally on your machine.

### 1. Prerequisites
- Install **XAMPP** (for MySQL database management).
- Install **Python 3.9.0** (Recommended version: [Download Python 3.9.0](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)). Make sure to check the "Add Path" option during installation.


### 2. Database Setup
1. Start the MySQL and Apache modules in XAMPP.
2. Open **phpMyAdmin** in your browser.
3. Create a database matching `DATABASES['default']['NAME']` in [config/settings.py](config/settings.py) — currently `test_db`. Check that file first, since the name can change.


### 3. Environment Setup
Clone the repository and set up a virtual environment:

```bash
# Clone the repository
git clone <REPO_URL>
cd ./Back-end-Template

# Create and activate a virtual environment
# Install pipenv globally
pip install pipenv

# Activate the virtual environment
pipenv shell

# Install project dependencies
pipenv install
pip install django 
pip install -r requirements.txt
pip install django-extensions

# Install project dependencies
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### 4. Configuration
This project has no `.env` file — the database connection, `SECRET_KEY`, and email credentials are hardcoded directly in [config/settings.py](config/settings.py). Open it and update `DATABASES`, `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD`, etc. to match your local setup before running the server.

### 5. Running the Application
Once the dependencies are installed, migrate the database and start the server:

```bash
# Run database migrations
python manage.py migrate
# Start the development server
python manage.py runserver 0.0.0.0:8000
```

### 6. Seed Data
`accounts.UserAccount` requires an `office`, so seed one before creating a user. In phpMyAdmin's SQL tab:

```sql
INSERT INTO offices_office (name, officeMail, street, city, province, region, numusers)
VALUES ('Headquarters', 'hq@company.com', '123 Main St', 'Cagayan de Oro', 'Misamis Oriental', 'Northern Mindanao', 45);
```
```sql
INSERT INTO `accounts_useraccount` (`id`, `password`, `last_login`, `is_superuser`, `email`, `first_name`, `last_name`, `is_active`, `is_staff`, `office_id`, `position`, `acc_lvl`) VALUES
(1, 'pbkdf2_sha256$600000$b0Jc0HzaNEjlgo95x2Co5S$qDNW4xXSc+3QQ1eAzFqInCQRz2J4T0s9PAy9EwDUyoQ=', '2026-08-24 08:23:43.581439', 1, 'admin@gmail.com', 'admin', 'gwapo', 1, 1, 1, 'System Administrator', 5);
```




```bash
python manage.py createsuperuser
```

```bash
FRONT-END-Credentials
username: admin@gmail.com
password: ChangeMe123!
```