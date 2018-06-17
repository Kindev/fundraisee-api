# Fundraisee

![Travis](https://travis-ci.com/Kindev/fundraisee-api.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Kindev/fundraisee-api/badge.svg)](https://coveralls.io/github/Kindev/fundraisee-api)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


## Quick Start

First, clone the repository
```
git clone https://github.com/Kindev/fundraisee-api.git
cd fundraisee-api
```

Create a virtualenv to isolate our package dependencies locally
```
python3.6 -m venv env
source env/bin/activate
```

Install all required dependencies
```
pip install -r requirements.txt
```

Create database, superuser and run the server, should be available on http://localhost:8000
```
cd fundraisee
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

List of available API (browseable) at /api. Example: http://localhost:8000/api/user/register/
* /user/ (GET)
* /user/login/ (POST)
* /user/register/ (POST)
* /user/logout/ (POST)
* /user/{username}/ (GET, PUT, DELETE)
* /user/{username}/edit (POST)