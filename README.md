
# Food blog with Django

## Description

This repository contains a draft weblog on cooking. The blog administrator can add new recipes and edit or delete recipes posted on the site. Each post can be accompanied by a photo of the food.

When adding a new post, you will need to fill in information regarding name, title of the post, recipe of the food and the date of publication of the post.

Only posts that are published are visible on the page. Posts that have not yet been published can be found in the Django admin panel.

## Creating a virtual environment

Open a terminal in your project directory and type the following command:

```bash
python -m venv venv
```
This will create a virtual environment named **venv**. To activate the virtual environment type the following command in your terminal:

```bash
"venv/scripts/activate.bat"
```

Next you have to install all required packages.


## Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages, which are listed in the **requirements.txt** file. You can use the command below.

```bash
pip install -r requirements.txt
```

## Launch

Use the commands below to start. 

```bash
python manage.py makemigrations
python manage.py migrate
```
A description of these commands is included [here](https://docs.djangoproject.com/en/4.0/topics/migrations/). Next, you need to create an administrator account. To do this use the following command.

```bash
python manage.py createsuperuser
```
You will need this account to add, edit and delete posts on the site. 

The next step is to start the server so you can open the page in your browser. To do this use the following command. 

```bash
python manage.py runserver
```
After this, a url will appear in the terminal where this page will be available. Simply click on it to open the page in your browser. You can then enter the address **http://127.0.0.1:8000/admin** and log in to your admin account. Then go back to your site and you will be able to add new posts, and when you click on an existing one, you will be able to edit or delete it. 

## Website tests

The file tests.py contains tests using the webdriver function from the selenium module. The tests cover adding, editing and deleting a new post. The file also contains tests to check the responsiveness of the page.

To run these tests you can run them directly from your IDE or from a terminal using the following command. 

```bash
python blog/tests.py
```

This will open the web browser and run the tests.

I hope you enjoy using it.
