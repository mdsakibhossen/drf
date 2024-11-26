
# Django Setup Notes

## 1. Create an Outer Project Folder and Navigate to It

First, create an outer project folder to contain both the virtual environment and your Django project.

### Commands:

```bash
# Create an outer project folder
mkdir project_folder

# Navigate into the project folder
cd project_folder
```

## 2. Create and Activate a Virtual Environment using `virtualenv`

### Commands:

```bash
# Create a virtual environment inside the project folder
virtualenv venv_name 
#or
python3 -m venv venv_name

# Activate the virtual environment (Windows)
venv_name\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source venv_name/bin/activate

# Deactivate the Virtual Environment
deactivate
```

## 3. Install Django

Once the virtual environment is activated, install Django:

```bash
pip install django
```

## 4. Create a Django Project Without Extra Folder

Create a new Django project in the current directory using the dot (`.`) to avoid creating an extra folder:

```bash
django-admin startproject project_name .
```

## 5. Run the Django Development Server

Check if everything is set up correctly by running the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the Django welcome page.

## 6. Create a Django App

Inside your project, create a new Django app:

```bash
python manage.py startapp app_name
```

## 7. Register the App in `settings.py`

Open `project_name/settings.py` and add your app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # Other installed apps...
    'app_name',
]
```

## 8. Apply Migrations

Run the migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 9. Run the Server Again

Start the server again to see your app in action:

```bash
python manage.py runserver
```

---

This concludes the setup for a Django project and app using `virtualenv`, an outer project folder, and the dot (`.`) to avoid creating an extra folder.