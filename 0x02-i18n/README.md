# PROJECT AUTHOR : ODIONYE OBIAJULU WILLIAMS
# PROJECT TITLE : i18n

The content of this project are tasks for learning to create internationalized web pages with Flask.

## Tasks Completed


 Basic Flask app

    0-app.py contains a Python script that sets up a basic Flask app with the following requirements:
        Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as the page title (<title>) and “Hello world” as the header (<h1>).

 Basic Babel setup

    1-app.py is a copy of 0-app.py, and templates/1-index.html is a copy of templates/0-index.html.
    Installed the Babel Flask extension:

    bash

    pip3 install flask_babel

    Instantiated the Babel object in the app and stored it in a module-level variable named babel.
    Created a Config class with a LANGUAGES class attribute equal to ["en", "fr"].
    Used Config to set Babel’s default locale to "en" and timezone to "UTC".
    Used that class as config for the Flask app.

 Get locale from request

    2-app.py is a copy of 1-app.py, and templates/2-index.html is a copy of templates/1-index.html.
    Created a get_locale function with the babel.localeselector decorator. Used request.accept_languages to determine the best match with our supported languages.

 Parametrize templates

    3-app.py is a copy of 2-app.py, and templates/3-index.html is a copy of templates/2-index.html.
    Used the _ or gettext function to parametrize the templates with message IDs home_title and home_header.
    Created a babel.cfg file and initialized translations using pybabel extract, pybabel init, and pybabel compile.
    Edited translation files to provide correct values for each message ID for each language.
    Compiled the dictionaries.

 Force locale with URL parameter

    4-app.py is a copy of 3-app.py, and templates/4-index.html is a copy of templates/3-index.html.
    Implemented a way to force a particular locale by passing the locale=fr parameter to the app’s URLs.
    Modified the get_locale function to detect and return the locale from URL parameters if present and valid.
    Tested different translations by visiting http://127.0.0.1:5000?locale=[fr|en].

 Mock logging in

    5-app.py is a copy of 4-app.py, and templates/5-index.html is a copy of templates/4-index.html.
    Mocked a user login system by creating a user table.
    Defined a get_user function to return a user dictionary based on the login_as URL query parameter.
    Defined a before_request function to set the logged-in user as a global on flask.g.user.
    Displayed a welcome message in the HTML template if a user is logged in.

 Use user locale

    6-app.py is a copy of 5-app.py, and templates/6-index.html is