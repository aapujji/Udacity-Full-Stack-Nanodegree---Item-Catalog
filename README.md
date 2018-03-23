# Udacity-Full-Stack-Nanodegree---Item-Catalog version 1.0 03/23/18

## Description

Conceptualized and constructed an online catalog using knowledge of SQL databases, Python programming and front end development best practices. The application allows visitors to sign up or log in and view, edit, and delete categories of items as well as items. This project was built using the Flask framework. To setup this app on your local machine, refer to the 'Setup' seciton of this readme.

## Setup

1. Make sure you have Python2.7, Vagrant and VirtualBox installed on your computer. (Download links are provided below.)

    [Python2.7 Download](https://www.python.org/downloads/)

    [VirtualBox Download (5.1.30)](https://www.virtualbox.org/wiki/Downloads)

    [Vagrant Download (1.8.5)](https://releases.hashicorp.com/vagrant/?_ga=2.146818743.1445943320.1515078265-241047305.1515078265)

2. Downlaod the vm [here](https://github.com/udacity/fullstack-nanodegree-vm)

3. Obtain Google Client ID and Client Secret:

    (1) Go to the [Google APIs Console](https://console.developers.google.com/apis)
    
    (2) Sign in to your Google account. If you don't already have a Google account, you will have to sign up for one.
    
    (3) In the sidebar, click Credentials.
    
    (4) Create a new project and give it a name.
    
    (5) Click the 'Oauth Consent Screen' tab and fill out the product name, and save.
    
    (6) Click 'Create credentials' and choose 'OAuth Client Id' and then select web application for application type.
    
    (7) Give the web application a name. For Authorized Javascript Origins and Authorized redirect URLs, make sure to add 'http://localhost:5000'.
    
    (8) Copy the Client ID and use it to replace 'YOUR-CLIENT-ID' in login.html.
    
    (9) Download the JSON file and save it as 'client_secrets.json' in the same directory as the project files.

4. Run database_setup.py to create the database for this project.

5. Run populatedb.py to populate the database with information.

6. Run item-catalog.py to start the application.

7. VIsit 'http://localhost:5000' in your browser to view the running application.

## Contact

For questions, comments or suggestions please send them to aapujji@yahoo.com.
