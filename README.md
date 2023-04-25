# Foody - Introduction

![Mockup Device](static/img/3-devices-black.png)

Project milestone 4 for Code Institute Full-stack development program.
Foody is a website for a restaurant where user can check the menu and make reservations, while the owner can check the reservation and update the menu according to the kitchen.

[Live Project Here](https://foody-p4.herokuapp.com/)

README Table Content

- [Tasty Blog - Introduction](#tasty-blog---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [User Stories](#user-stories)
    - [The Scope](#the-scope)
  - [Design](#design)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Menu Page](#menu-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
      - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
    - [Testing](#testing)
  - [Creating the Django app](#creating-the-django-app)
  - [Deployment of This Project](#deployment-of-this-project)
  - [Final Deployment](#final-deployment)
  - [Forking This Project](#forking-this-project)
  - [Cloning This Project](#cloning-this-project)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)

## User Experience - UX

### User Stories

* As a website user, I can:

1. Navigate around the site and easily view the desired content.
2. View the menu the restaurant is offering before making a reservation.
3. Make a reservation online without the need of leaving the website.
4. See the contact information and social media of the business.

* As a business owner, I can:

1. Create and publish a new menu items.
2. Check the reservations and see the user data so I can contact them to confirm.
3. Create a new category for the menu (existing categories are Breakfast, Lunch, Dinner).
4. Delete items from the menu and reservations.
5. Easily pdate the about us section as well as the home page content.

### Agile Methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/users/adrian-cucuet/projects/2/views/1)

### The Scope

#### Main Site Goals

* To provide users with a good experience and easy navigation.
* To provide users with a visually pleasing website that is intuitive to use and easy to navigate.
* To provide tools that allow users to see the menu and make a reservation.

## Design

#### Colours

![Colours Scheme](/static/img/color-scheme.png)<br>

* The colour scheme is kept simple by opting for a combination of light and dark colors with a primary color as an accent.
* In order to keep the colors cohesive I have decided to use variables.

#### Imagery

* For the purpose of the project all the images used are from template provided by [ThemeWagon](https://themewagon.com/)

### Wireframes

Wireframes for this project can be located [here](wireframes.md)

## Features

### Home Page

* The hero container is encouraging users to reserve a table with a CTA button<br>
![Hero](static/img/hero-screen.png)
* The service cards are encouraging the user to trust the business<br>
![Cards](static/img/service-cards.png)
* There is an about us section followed by a team introduction so the user gain trust in the business<br>

### About Page

![About](static/img/about.png)
* The About Page gives, users information about Foody Restaurant.<br>

### Navbar

![Navbar](static/img/navbar.png)

* The navigation bar is present at the top of every page and contains all links to the various other pages.
* The navigation bar has a reservation button to gove the user the option to book a table from any page.
* The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

### Footer

![Footer](static/img/footer.png)
* On the website footer, users can see basic information about the business such as contact, social media, 
  copyright, and the logo.

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Django](https://www.python.org/)
* [Python](https://www.djangoproject.com/)

#### Django Packages

* [Gunicorn](https://gunicorn.org/)<br>
   As the server for Heroku
* [Cloudinary](https://cloudinary.com/)<br>
   Was used to host the static files and media
* [Psycopg2](https://pypi.org/project/psycopg2/)<br>
   As an adaptor for Python and PostgreSQL databases

### Frameworks - Libraries - Programs Used

* [Bootstrap](https://getbootstrap.com/)<br>
   Was used to style the website, add responsiveness and interactivity
* [Jquery](https://jquery.com/)<br>
   All the scripts were written using jquery library
* [Git](https://git-scm.com/)<br>
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
* [GitHub](https://github.com/)<br>
   GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)<br>
   Heroku was used to deploy the live project
* [PostgreSQL](https://www.postgresql.org/)<br>
   Database used through heroku.
* [VSCode](https://code.visualstudio.com/)<br>
   VSCode was used to create and edit the website
* [W3C - HTML](https://validator.w3.org/)<br>
   W3C- HTML was used to validate all the HTML code
* [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   W3C - CSS was used to validate the CSS code
* [Fontawesome](https://fontawesome.com/)<br>
   To add icons to the website
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   To check App responsiveness and debugging
* [Google Fonts](https://fonts.google.com/)<br>

### Testing

* Manual testing has been performed for the Reservation form.
* Manual testing has been performed for every page on the website as well as navigation.

* [CSS validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffoody-p4.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors) passed. The only error is from 3rd party libraries.
* [HTML validator](https://fonts.google.com/) passed. Only errors from Summernote html tags.
* All code was written following PEP8 Style Guide. Checks have been done using [ExtendClass](https://extendsclass.com/python-tester.html) for all python files

## Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: `pip3 install django gunicorn`
6. Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
7. Create file for requirements: in the terminal window type `pip freeze --local > requirements.txt`
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!

## Deployment of This Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Next select your region.
5. Click on the Create App button.
6. Click in resources and select Heroku Postgres database.
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
9. Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
10. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars.
11. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
12. Scroll to the top of the page and choose the Deploy tab.
13. Select Github as the deployment method.
14. Confirm you want to connect to GitHub.
15. Search for the repository name and click the connect button.
16. Scroll to the bottom of the deploy page and select the preferred deployment type.
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.

## Final Deployment 

1. Create a Procfile `web: gunicorn your_project_name.wsgi`
2. When development is complete change the debug setting to: `DEBUG = False` in settings.py
3. In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to settings.py.
4. In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/adrian-cucuet/Foody-P4-CI/)
2. Find the 'Fork' button at the top right of the page.
3. Once you click the button the fork will be in your repository.

## Cloning This Project

* Clone this project by following the steps:

1. Open GitHub.
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order to copy the URL.
3. Once you click the button the fork will be in your repository.
4. Open a new terminal.
5. Change the current working directory to the location that you want the cloned directory.
6. Type 'git clone' and paste the URL copied in step 3.
7. Press 'Enter' and the project is cloned.

### Content

* Website Template is from [ThemeWagon](https://themewagon.com/) and it is free for use. I had to change some html and CSS to adjust to the needs of the wireframe and user stories.
* Pictures are free from the template. The template comes with free licensed images.

### Information Sources / Resources / Credits
* Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
* [W3Schools - Python](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Django](https://docs.djangoproject.com/en/4.2/) Used when I had issues that needed to be fixed.
* Menu images downaloaded from [Unsplash](https://unsplash.com/)
* [Udemy](https://www.udemy.com/course/build-a-restuarnt-site-with-python-and-django/) Used the tutorial for models and views.