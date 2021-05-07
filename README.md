# Proggy

A blog created using Django! You can view and comment posts, create your own and manage them.
Write about yourself using the profile system. 

Technology stack:

- Python
- Django
- Django's extensions: crispy-forms

## Installation

First, you need to clone repository.

```
git clone https://github.com/dieisabel/proggy
```

Second, create and activate your virtual environment.

```
python -m venv venv
# OR
py -<version> -m venv venv # If using pylauncher in windows

source ./venv/bin/activate # For Linux
./venv/Scripts/Activate.ps1 # For Windows
```

Install dependencies.

```
pip install -r requirements.txt
```

Then go to `backend/` directory and apply migrations.

```
python manage.py migrate
```

Create superuser for access to admin page.

```
python manage.py createsuperuser
```

Start Django development server.

```
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License 

For now there is no license for this project