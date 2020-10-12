# Gallery

## Core Features

* An admin can upload new photos through an admin panel
* An admin can update a photos details
* A user can copy an image's link
* A user can view images by category and location
* A user can view a photo's details
* Search for different categories of photos

## Prerequisites

* Python3
* Django

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/{{ USERNAME }}/{{ project_name }}.git
    $ cd {{ project_name }}
    

## Usage
Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements.txt


## Environment variables

The `ENVIRONMENT` variable loads the correct settings.

```
CLOUD_NAME=''
API_KEY=''
API_SECRET=''
SECRET_KEY=''
DEBUG=boolean
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
MODE=''
ALLOWED_HOSTS=''
DISABLE_COLLECTSTATIC=''
```
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright (c) 2020 Pretorious Ndung'u