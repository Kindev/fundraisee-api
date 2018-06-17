# Fundraisee

![Travis](https://img.shields.io/travis/Kindev/fundraisee-api/master.svg)
[![Coverage Status](https://coveralls.io/repos/github/Kindev/fundraisee-api/badge.svg?branch=master)](https://coveralls.io/github/Kindev/fundraisee-api?branch=master)
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

Create database and run the server, should be available on http://localhost:8000
```
cd fundraisee
python manage.py migrate
python manage.py runserver
```
