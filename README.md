# Fundraisee

[![Build Status](https://travis-ci.com/Kindev/fundraisee-api.svg?branch=master)](https://travis-ci.com/Kindev/fundraisee-api)
[![Coverage Status](https://coveralls.io/repos/github/Kindev/fundraisee-api/badge.svg?branch=master)](https://coveralls.io/github/Kindev/fundraisee-api?branch=master)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

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

Create database, superuser and run the server, check http://localhost:8000 for swagger
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Contributing
Read our [contributing guide](https://github.com/Kindev/fundraisee-api/blob/master/CONTRIBUTING.md) to learn about our development process, how to propose bugfixes and improvements, and how to submit a pull request.