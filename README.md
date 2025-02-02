# faq-backend
 A Django-based multilingual FAQ Management System with admin panel, WYSIWYG editor, REST API, and multi-language support.


README.md
================

Project Overview
-------------------

This is a Django-based project that provides a custom admin panel for managing FAQs (Frequently Asked Questions). The project includes features such as adding, updating, and deleting FAQs, as well as a public-facing FAQ page with Google Translate integration.

Project Structure
---------------------
Command  to the run the project 

1.open the folder in vs code - you will be inside faq.
2.venv\Scripts\activate - run this command.
3.cd project
4. python manage.py runserver


PASSWORD FOR THR BACKEND DJANGO ADMINPANEL 
sanjay username 
sbu200420 password




The project is structured as follows:

* `project`: The main project directory.
* `project/project`: The Django project directory.
* `project/project/wsgi.py`: The WSGI configuration file.
* `project/project/settings.py`: The Django project settings file.
* `project/project/urls.py`: The Django project URL configuration file.
* `project/app`: The Django app directory.
* `project/app/models.py`: The Django app models file.
* `project/app/views.py`: The Django app views file.
* `project/app/templates`: The Django app templates directory.
* `project/app/static`: The Django app static files directory.

Installation
---------------

To install the project, follow these steps:

1. Clone the repository using `git clone`.
2. Navigate to the project directory using `cd`.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the migrations using `python manage.py migrate`.
5. Run the development server using `python manage.py runserver`.

Usagef
---------

To use the project, follow these steps:

1. Open a web browser and navigate to `http://localhost:8000/admin/` to access the custom admin panel.
2. Log in using the admin credentials (username: `admin`, password: `password`).
3. Click on the "FAQs" link to view the FAQ list.
4. Click on the "Add FAQ" button to add a new FAQ.
5. Fill in the question and answer fields and click "Save" to save the FAQ.
6. To update a FAQ, click on the "Edit" button next to the FAQ.
7. To delete a FAQ, click on the "Delete" button next to the FAQ.

Public-Facing FAQ Page
---------------------------

To access the public-facing FAQ page, navigate to `http://localhost:8000/faqs/`. The page includes a Google Translate widget that allows users to translate the FAQs into different languages.

Google Translate Integration
------------------------------

The project uses the Google Translate API to provide translation functionality. To use the Google Translate API, you need to obtain an API key and add it to the `GOOGLE_TRANSLATE_API_KEY` setting in the `project/project/settings.py` file.

License
----------

This project is licensed under the MIT License. See the `LICENSE` file for more information.