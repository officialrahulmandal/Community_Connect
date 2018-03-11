# Community-Connect
Django based application to help in the management of the communities.

# Installation
Instructions only for linux debian-based system,
please find equivalent for your OS.

## Django Application
The following are the instructions to install the the application in the workbench to start working.

1. Install Python 3.5 and Pip
    - Debian-Family: `sudo apt install python3.5 python3-pip`
2. Set virtual environment
    1. Make: `python3 -m venv venv`
    2. Activate: `source venv/bin/activate`
3. Install Requirements: `pip3 install -r requirements.txt`
4. Setup Database
    1. Install PostgreSQL
    `sudo apt update; sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib;`
    2. Create User/Role
        1. `sudo -i -u postgres`
        2. `psql`
        3. `CREATE USER community_connect WITH PASSWORD 'MY_AWESOME_PASSWORD';`
    3. Configure User/Role
        1. `ALTER ROLE community_connect SET client_encoding TO 'utf8';`
        2. `ALTER ROLE community_connect SET default_transaction_isolation TO 'read committed';`
        3. `ALTER ROLE community_connect SET timezone TO 'UTC';`
    4. Create Database: `CREATE DATABASE community_connect OWNER community_connect;`
    5. Config Database with django
        1. Open `Community-Connect/Community_Connect/settings.py` and navigate to line `'PASSWORD': 'MY_AWESOME_PASSWORD',` and set your password here.
        2. inside the virtual environment, run `python3 manage.py makemigrations`
        3. inside the virtual environment, run `python3 manage.py migrate`
5. Run the server
Inside virtual-environment, run `python3 manage.py runserver`.
Now, go to `127.0.0.1:8000/`, your welcome page should show up.

- For development environment only
    - For registration views, go to community_connect/settings and uncomment `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

## User Documentation
The following is the instructions to set up for editing the user-documentation.
The user documentation is done using Mkdocs.
Nagivate to the `docs/build` folder and run `mkdocs serve` to work on the documentation.
Visit [Mkdocs Website](http://www.mkdocs.org) for more information.
To enable the documentation being hosted on gh-pages, the `site` folder created when you run `mkdocs build`
is pasted in the `docs` folder of the repository.
