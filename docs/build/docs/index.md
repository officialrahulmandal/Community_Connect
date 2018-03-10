# Introduction
Community Connect is a simple application to help automate the management of any Community.
It is free and open-source.
You can simply [download] the code from GitLab.

## Features
- Made using Django.
- Easy to setup & manipulate as per the needs.
- Channels to ensure that the members receive only the mails they want to receive.

#Installation
Follow these steps on your server to ensure that your the application works properly.
Instructions only for linux server.

1. Install Python 3.5 and Pip
    - Debian-Family: `sudo apt install python3.5 python3-pip`
1. Install Requirements: `pip3 install -r requirements.txt`
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
        2. `python3 manage.py makemigrations`
        3. `python3 manage.py migrate`
4. Install nginx
// Update user-documentation from this point

[download]: https://gitlab.com/asetalias/Community-Connect
