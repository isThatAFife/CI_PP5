# Mikey's Sculpts
[Mikey's Sculpts](https://mikeysculpts-7c49ca735d97.herokuapp.com/) is a storefront for the sale of both physical, 3D-printed sculpts, and digital STL files created by artist Mike Gilbert.

![screenshot of app](docs/screenshots/responsive.png)

## Contents

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Palette](#colour-palette)

* [Wireframes and Mockups](#wireframes)

* [Entity Relationship Diagram](#erd)

* [Features](#features)
  * [Existing Features](#existing-features)
    * [Navigation Bar](#navigation-bar)
    * [Search Bar](#search-bar)
    * [Account Registration](#account-registration)
    * [About Page](#about-page)
    * [My Comments Page](#my-comments)
    * [Leave a Comment](#comment)
  * [Future Features](#future-features)
    * [Contribute Score](#contribute)
    * [List sorting](#sort-list)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
    * [APIs](#apis)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Acknowledgements](#acknowledgements)

  ---

  ## User Experience (UX)

  ### Project Goals



## User Stories

### Admin



### User


---

## Design

### Colour Palette

![screenshot](docs/screenshots/palette.png)



### Wireframes

#### Homepage

![homepage](docs/wireframes/homepage.png)

#### About

![about](docs/wireframes/about.png)

#### Game Detail

![detail](docs/wireframes/detail.png)

#### My Comments

![my comments](docs/wireframes/my_comments.png)

#### Homepage Phone Version

![homepage-phone](docs/wireframes/homepage-phone.png)

### ERD

![erd](docs/erd/graphviz.png)

---

## Features

### Existing Features

#### Navigation Bar

![screenshot of navigation bar](docs/screenshots/navbar.png)

- A navigation bar at the top of the page allows users to navigate the site quickly.
- Links in the navigation bar include Home, About, My Comments (when logged in), Logout (when logged in), Register (when not logged in), and Login (when not logged in)

#### Search Bar

![screenshot of search bar](docs/screenshots/searchbar.png)

![screenshot of search results](docs/screenshots/search.png)

- 

#### Account Registration

![screenshot of sign up](docs/screenshots/signuppage.png)

- Users are able to register an account in order to leave comments on product pages.
- Registration page includes checks for invalid inputs.

#### About Page

![screenshot of about](docs/screenshots/aboutpage.png)

- About page gives a summary of the website and its goals.

#### My Comments

![screenshot of my comments](docs/screenshots/mycomments.png)

- Users can see all of the comments they have left with links to the product page they left them on.

#### Comment

![screenshot of comment box](docs/screenshots/comment.png)

- When a user is logged in, they can leave a comment or short review on each product page.

### Future Features



---

## Technologies Used

### Languages Used

- HTML5
- CSS3
- Javascript
- Python
- Django
- SQL - Postgres

### Frameworks, Libraries & Programs Used

  Git - For version control.

  Github - To save and store the files for the application.

  VSCode - To develop project and organise version control.

  Heroku - To deploy the application.

  Django - To develop project

  Bootstrap - To style project

  IGDB - Used to retrieve box art for games

  pgAdmin 4 - Used to administer database

  Balsamiq - To create wireframes

### Installed Packages


---

## Deployment & Local Development

### Deployment

The deployment of the project was done using [Heroku](https://www.heroku.com/) through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
   * For this project, the unique name is "g4m3b0x" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and locate the "Config Vars" section and click "Reveal config vars".
6. Add config vars: 
   * For this project I have four config vars:
     * DATABASE_URL - For the database
     * SECRET_KEY - Password for accessing database
     * IGDB_ID - ID to access IGDB API
     * IGDB_SECRET - Password to access IGDB API
7. Navigate to the "Deploy" section by clicking the "Deploy" tab in the top navbar.
8. Select "GitHub" as the deployment method and click "Connect to GitHub".
9. Search for the GitHub repository name in the search bar.
10. Click on "connect" to link the repository to Heroku.
11. Scroll down and click on "Deploy Branch".
12. Once the app is deployed, Heroku will notify you and provide a button to view the app.

NB - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys".

### How to Fork

This can be done to create a copy of the repository. The copy can be viewed and edited without affecting the original repository.

To fork the repository through GitHub, take the following steps:
1. In the "CI_PP4" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository.

### How to Clone

To clone the repository through GitHub:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.
2. Ensure HTTPS is selected in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

### APIs
In order for the app to function properly, APIs need to be set up and connected. In particular, the following APIs were used for this project:

* IGDB API:
  * This was used in order to retrieve box art for games

---

## Testing

Testing was ongoing throughout the build.

### Python PEP8 Testing

I used the Code Institute Python Linter to check for syntax and styling errors and found none.

![screenshot](docs/validators/gamelibrary_views.png)
![screenshot](docs/validators/gamelibrary_urls.png)
![screenshot](docs/validators/gamelibrary_models.png)
![screenshot](docs/validators/gamelibrary_forms.png)
![screenshot](docs/validators/gamelibrary_apps.png)
![screenshot](docs/validators/gamelibrary_admin.png)
![screenshot](docs/validators/gamebox_urls.png)
![screenshot](docs/validators/gamebox_settings.png)
![screenshot](docs/validators/about_views.png)
![screenshot](docs/validators/about_models.png)
![screenshot](docs/validators/about_apps.png)
![screenshot](docs/validators/about_admin.png)

### HTML W3C Validator

I used the W3C HTML validator and found none.

![screenshot](docs/validators/home.png)
![screenshot](docs/validators/aboutw3c.png)
![screenshot](docs/validators/gamedetailw3c.png)

### Solved Bugs


### Known Bugs

1. No known bugs at this time.

### Manual Testing




---

## Credits

### Code Used

Basic layout/templates from I think therefore I blog tutorial

### Acknowledgements

[Adobe Color Wheel for colour palette](https://color.adobe.com/create/color-wheel)

[Black for pep8 compliance](https://pypi.org/project/black/)