# PythonFinalProject

Description: Our final project in IT 403 Web Systems & Technologies 3 is e-learning website about Python programming language course using Python and Django web framework.

  

<h2>🛠️ Installation Steps:</h2>

  

<p>1. Clone this repo</p>

  

```

https://github.com/jeaysdigo/PythonFinalProject.git

```

  

<p>2. Go to project directory using  CMD or vscode terminal</p>

  

```

cd PythonFinalProject

```

  

<p>3. Create Virtual Environment. Open CMD and type below:</p>

  

```

py -m venv env

```

  

<p>4. Activate your environment using this:</p>

  

```

env\Scripts\activate

```

  

<p>5. Install dependencies </p>

  

```

pip install django
py -m pip install Pillow
pip install django-ckeditor

```

  

<p>6. Make a migrations to automatically create local database</p>

  

```

py manage.py makemigrations
py manage.py migrate

```

  

<p>7. Create admin account</p>

```

py manage.py createsuperuser

```
<p>8. Please input the following: <br></p>
Username: <b>admin</b>  <br>Email: <b>admin@pal.com</b><br>
Password: <b>admin</b><br>
Password (again) <b>admin</b><br>
Bypass password validation and create user anyway? <b>y</b><br><br>
<p>9. Run the server: </p>

```

py manage.py runserver

```

<b> Note: </b> Your database and your virtual environment will not commit and push in the repository because <b><em>db.sqlite3 </em></b>and <b><em> env</em></b> are both included in the <b><em>gitignore</em></b>
