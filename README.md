# blog-django

Food blog website with Django.

The user can check the recipes on the website. After logging into the admin account (127.0.0.1/admin), 
the user can add new post, edit and delete existing posts on the site.

When adding a new post, you will need to fill in information regarding name, title of the post, 
recipe of the food and the date of publication of the post.

Only posts that are published are visible on the page. Posts that have not yet been published can be found in the 
Django admin panel.

The tests.py file contains tests using the webdriver function from the selenium module. 
The tests are about editing a given post and adding and deleting a new post. 
There are also tests in the file that check the responsiveness of the page.

