# How to run: (Written by Nandhakumar Venkatesh)

# PRE-REQUISITES:

    1. Make sure that nodejs and node package manager are installed on your system. NPM usually comes with installations of Node.js.

    2. Make sure that Python3 and PIP are installed on your system. Pip usually comes with installations of Python.

# You will need to open 3 terminals.

# TERMINAL 1:
    1. CD into the agfzb-CloudAppDevelopment_Capstone/functions directory.

    2. Run the following commands:
        a) npm init -y
        b) npm install -s @cloudant/cloudant
        c) npm install express
        d) node get-dealership.js

    3. Check the URL http://localhost:3000/dealerships/get. If you see a list of car dealerships, the server is running properly.

# TERMINAL 2:
    1. CD into the agfzb-CloudAppDevelopment_Capstone/functions directory.

    2A) If you are on Linux, run the following commands:
        a) bash setup.sh
        b) python3.9 reviews.py

    2B) If you are not on Linux, run the following commands:
        a) pip install Cloudant
        b) pip install Flask
        c) python reviews.py 
        (Note: You might have to install Python3.9 and write python3.9 instead of Python for the final command).

    3. Check the URL http://localhost:5000/api/get_reviews?id=15. If you see a list of reviews, the server is running properly.

# TERMINAL 3:
    1. CD into the agfzb-CloudAppDevelopment_Capstone/server directory.
    
    2. Run the following commands:
        a) python -m pip install -U -r requirements.txt
        b) python manage.py makemigrations djangoapp
        c) python manage.py migrate
        d) python manage.py runserver
        (Note: If using the python commands don't work, try writing python3 instead of python).

Finally, open a link to http://localhost:8000/djangoapp/ on localhost to see the app! Replace "djangoapp" with "admin" to view the Django Admin Site! If something isn't working, refresh the page. Unfortunately, the connection to the IBM databases can be spotty. Look at the outputs in your terminals and check all the URLs listed above. If one of the URLs isn't displaying data, there is a connection issue.

# TO CLOSE THE APP:
    1. Press control+c in each of the three terminals you opened to close the server connections.

NOTE: This project will only work as long as my free IBM trial lasts 😔


# EVERYTHING BELOW THIS WAS WRITTEN BY THE IBM STAFF THAT RUN THE FULL STACK WEB DEVELOPMENT CERTIFICATION PROGRAM ON COURSERA:


# Final Project Template

The final project for this course has several steps that you must complete. 
To give you an overview of the whole project, all the high-level steps are listed below. 
The project is then divided into several smaller labs that give the detailed instructions for each step. 
You must complete all the labs to successfully complete the project.

## Project Breakdown

**Prework: Sign up for IBM Cloud account and create a Watson Natural language Understanding service**
1. Create an IBM cloud account if you don't have one already.
2. Create an instance of the Natural Language Understanding (NLU) service.

**Fork the project Github repository with a project then build and deploy the template project**
1. Fork the repository in your account
2. Clone the repository in the theia lab environment
3. Create static pages to finish the user stories
4. Deploy the application on IBM Cloud

**Add user management to the application**
1. Implement user management using the Django user authentication system.
2. Set up continuous integration and delivery

**Implement backend services**
1. Create cloud functions to manage dealers and reviews
2. Create Django models and views to manage car model and car make
3. Create Django proxy services and views to integrate dealers, reviews, and cars together
 
**Add dynamic pages with Django templates**
1. Create a page that shows all the dealers
2. Create a page that show reviews for a selected dealer
3. Create a page that let's the end user add a review for a selected dealer

**Containerize your application**
1. Add deployment artifacts to your application
2. Deploy your application
