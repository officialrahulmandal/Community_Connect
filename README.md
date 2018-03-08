# Community-Connect
Django based application to help in the management of the communities.

# Requirements
1. Python 3.X.X
2. PostgreSQL 9.5.X
3. Django 2.0.3

# Installation
Instructions only for linux debian-based system,
please find equivalent for your OS.

1. Make & activate virtual environment
Make: `python3 -m venv venv`
Activate: `source venv/bin/activate`
2. Install Requirements
`pip install -r requirements.txt`
3. Setup Database
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
    4. Config Database with django
        1. Open `Community-Connect/Community_Connect/settings.py` and navigate to line `'PASSWORD': 'MY_AWESOME_PASSWORD',` and set your password here.
        2. inside the virtual environment, run `python3 manage.py makemigrations`
        3. inside the virtual environment, run `python3 manage.py migrate`
4. Run the server
Inside virtual-environment, run `python3 manage.py runserver`
now go to `127.0.0.1::8000/`, your welcome page should show up.
