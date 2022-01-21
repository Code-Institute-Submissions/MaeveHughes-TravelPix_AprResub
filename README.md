<h1>Travel|Pix</h1>
<br>
<p> <strong> A social media site used for interacting with people who share a common interest in looking at images from around the world </strong> </p>

[View the live project here.](website link/)

Home Page Image - [View]( https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-19%20at%2016.09.37.png)

# Project Overview
- This project is a website that allows users to add/edit/delete travel images  for submission as milestone project 4 as part of the Code Institute - Diploma in Software Development (Full stack) course.
- The website is deployed using Heroku pages.
- The repository on GitHub that contains the website source code, media and assets.
- The website was built with a responsive look and feel for desktop, tablet and mobile devices.

# UX
## Strategy
### Primary Goal
The primary goal of the website from the site 
owners perspective is as follows:
- To create/edit/delete travel posts so users can add a memory to a vacation.
- To allow users add their travel posts(name, image, title, description).
- To allow users modify their travel posts(image, title, description).
- To allow users delete their travel posts.
- To allow users view both their own posts and other posts.
- To allow users comment on a post.
- To allow users like a post.

The primary goal of the website from a site users perspective is as follows:
- To allow users add their travel posts(name, image, title, description).
- To allow users modify their travel posts(image, title, description).
- To allow users delete their travel posts.
- To allow users view both their own posts and other posts.
- To comment on a post and view comments.
- To allow users like a post.

## Structure
### Website pages
I have structured the website with clear, concise structure, information and purpose. I use the Bootstrap grid system throughout, which gave a consistent structure and responsive design "out of the box"
1. Home/Landing Page: This is the first page the user encounters when they access the site, before they log in/register. They have the ability to open the travel posts however cannot interact with the post.
2. Register: This page allows the user to register an account to interact with all posts.
3. Login: This page allows the user to login to the site.
4. Add Post: This page allows the user to add a travel post.
5. Edit Post: This page allows a user to edit a travel post they have created.
6. Delete Post: This button allows a user to delete a travel post they have created.
7. Logout: This link allows the user to logout of the site.
8. 404: The 404 error page is displayed if the user enters an incorrect url when accessing the site.

### Database
- The website is data-centric with html, javascript and css used with the bootstrap(version 5) framework as a frontend
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version(production)

#### Models
- The following models were created to represent the database model structure for the website

##### Account Model
- The Account model has a one-to-one relationship with User.
- The model contains the following fields: image, slug, bio
Friends.

#####  Friend Model
- The Friend model is part of the Django allauth library.
- The model allows users to follow another user.

##### Post Model
- The Post model contains information about the travel posts made on the website.
- It contains User as a foreign-key.
- The model contains the following fields: title, slug, suthor, featured_image, exerpt, updated_on, content, created_on, status and likes.

##### Comment Model
- The Post model contains a comment on a post
- It contains Post as a foreign-key.
- The model contains the following fields: name, body, created_on, approved.

## Scope
There is overlap in terms of user stories for the two types of users, and they are described below
### User Stories Potential or Existing Customer
The user stories for the registered user are described as follows: 
- User Story 1.1: As a first time/registered user the navigation bar is displayed with a logo on all pages with a home icon, add post and Register/Login icon on a desktop device.
- User Story 1.2: As a first time/registered user the navigation bar is displayed on all pages with a home icon, add post icon and Register/Login on a mobile/tablet device
- User Story 1.3: As a first time/registered user not logged in, I see a Register/Login link in the nav bar.
- User Story 1.4: As a first time user, I can register by clicking on the Register button. 
- User Story 1.5: As a registered user not logged in, I am brought to the Login link if I click on the login button.
- User Story 1.6: As a first time / registered user logged in, I am brought to the home page if I click on the home icon / the TravelPix title or image.
- User Story 1.7: As a first time/ registered user if there are more than six posts on the home page, the page is paginated with 6 posts per page
- User Story 1.8: As a registered user logged in, I see a Logout on the nav bar. 
- User Story 1.9: As a registered user logged in, if I click on the plus icon on the nav bar I am brought to the add post page.
- User Story 1.10: As a registered user logged in, if I click on my post in on the home page I am directed to the post detail page.
- User Story 1.11: As a registered user logged in, if I click on the Logout button on the navbar I am brought to the Logout page. 
- User Story 1.12: As a first time / registered user if I encounter an error on the site, I will be navigated to the applicable 404 error page.
- User Story 1.13: As a first time / registered user the footer bar is displayed on all pages with copyright and links to the social media pages.

- User Story 2.1: As a user I can register on the website by providing an email address, username, password and password confirmation. I am notifed that a confirmation email has been sent and that I am logged in.

- User Story 3.1: As a registered user I can log in to the website using my username and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed.

- User Story 4.1: As a first time / registered user I can view the image, description and view comments (the most recent comment first) on the post detail page. If I click the back button I am redirected to the home page.
- User Story 4.2: As a registered user logged in I can comment and like users posts. When I add a comment to a post, it is sent to the admin for approval and I am notified.
- User Story 4.3: As a first time / registered user who has not logged into the website, I cannot add a comment or like a post
- User Story 4.4: As a registered user logged in I can edit and delete my own posts.

- User Story 5.1: As a logged in user I can log out and I am notified that I have successfully signed out.



### User Stories Website Owner
The user stories for the website owner(admin) are described as follows: 
There is a lot of overlap between the two user types, the admin user however has more administrative rights throughout but their roles and responsibilities
are defined
- User Story 1.1: As an admin user the navigation bar is displayed with a logo on all pages with a home icon, add post and Register/Login icon on a desktop device.
- User Story 1.2: As an admin user the navigation bar is displayed on all pages with a home icon, add post icon and Register/Login on a mobile/tablet device
- User Story 1.3: As a admin user not logged in, I see a Register/Login link in the nav bar.
- User Story 1.4: As an admin user not logged in, I am brought to the Login link if I click on the login button.
- User Story 1.5: As a user logged in, I am brought to the home page if I click on the home icon / the TravelPix title or image.
- User Story 1.6: As an admin user if there are more than six posts on the home page, the page is paginated with 6 posts per page
- User Story 1.7: As an admin user logged in, I see a Logout on the nav bar. 
- User Story 1.8: As an admin user logged in, if I click on the plus icon on the nav bar I am brought to the add post page. 
- User Story 1.9: As a admin user logged in, if I click on a post on the home page I am directed to the post detail page. 
- User Story 1.10: As an admin user logged in, if I click on the Logout button on the navbar I am brought to the Logout page. 
- User Story 1.11: As an admin user if I encounter an error on the site, I will be navigated to the applicable 404 error page.
- User Story 1.12: As an admin user the footer bar is displayed on all pages with copyright and links to the social media pages.

- User Story 3.1: As a registered user I can log in to the website using my username and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed.

- User Story 4.1: As an admin user I can view the image, description and view comments (the most recent comment first) on the post detail page. If I click the back button I am redirected to the home page.
- User Story 4.2: As an admin user logged in I can comment and like users posts. When I add a comment to a post, it is sent to the admin for approval and I am notified.
- User Story 4.4: As an admin user logged in I can edit and delete my own posts.

- User Story 5.1: As an admin in user I can log out and I am notified that I have successfully signed out.

- User Story 6.1: As an admin user I can view email addresses, who they belong to and if they have been verified in the django admin page. I have the option to add and change an email address.
- User Story 6.2: As an admin user I can view users and groups. I have the option to add and change a user and a group.
- User Story 6.3: As an admin user I can add, view and change an account.
- User Story 6.4: As an admin user I can add, view and change a comment. I also can approve users comments. Once approved users will be able to see their comment on the post detail page.
- User Story 6.5: As an admin user I can add, view and change a friend. 
- User Story 6.6: As an admin user I can add, view and change a post. I can see who created the post, when and if it is published or a draft.
- User Story 6.7: As an admin user I can add, view and change a site. 
- User Story 6.8: As an admin user I can add, view and change a friend. 
- User Story 6.9: As an admin user I can add, view and change social accounts. 

## Skeleton
### Wireframes
- Wireframes for the website were developed in moqups.com and are linked below for Desktop and Mobile devices.
- The wireframes are stored in GitHub in the png format and are available at the links below(Desktop Mobile wireframes)

#### Desktop 
- [Index](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-19%20at%2017.26.21.png)
- [Post Detail](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-20%20at%2017.25.37.png)
- [Login](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-20%20at%2017.28.53.png)
- [Logout](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-20%20at%2017.31.53.png)
- [Add Post](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-20%20at%2017.35.30.png)
- [Register](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2017.07.12.png)

#### Mobile
- [Index](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2017.25.16.png)
- [Post Detail](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2019.11.32.png)
- [Login](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-20%20at%2017.28.53.png)
- [Logout](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-20%20at%2017.31.53.png)
- [Add Post](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-20%20at%2017.35.30.png)
- [Register](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2017.07.12.png)

## Surface
### Color Palette
I have gone for a simple and minimal design for the website, with predominately blue and peach colours on all pages.
There are five colours in the color palette:
- efebec - Very light peach colour for the background.
- 153184 - Royal blue for the navbar, footer and buttons.
- peachpuff - Peach for text on the blue background.
- fff - White for the form backgrounds.
- 445261 - Black for the text on posts and forms.

I feel the colours complement each other very well, and I choose those colours after testing a number of palettes while making sure the colour palette would not clash with users posts.

### Typography
The Lato font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the Lato font cannot be imported into the website correctly. This font is from the Google fonts library.

# Features
The website has seventeen distinct features, and they are described below
What is important to detail is what pages are accessible by the three types of users
1. A user not logged into the site
2. A registered user logged into the site
3. An admin user (site owner)
The navigation buttons update depending on whether a user is logged in or not, and whether that user is the admin:

 Nav Link              |Not logged in  |Logged in as regular user|Logged in as admin
:-------------         |:------------- |:----------------|:------------- |
Home     |&#9989;        |&#9989;          |&#9989; |
Posts           |&#9989;        |&#9989;          |&#9989; |
Posts Details           |&#9989;        |&#9989;          |&#9989; |
Post Comments          |&#9989;        |&#9989;          |&#9989; |
Add a post     |&#10060;       |&#9989;         |&#9989; |
Edit a post     |&#10060;       |&#9989;         |&#9989; |
Delete a post     |&#10060;       |&#9989;         |&#9989; |
Like a post     |&#10060;       |&#9989;         |&#9989; |
Unlike a post     |&#10060;       |&#9989;        |&#9989; |
Log out               |&#10060;       |&#9989;          |&#9989; |
Register               |&#9989;        |&#10060;         |&#10060; |
Log in               |&#9989;        |&#10060;         |&#10060; |
Comment on a post                |&#10060;        |&#9989;         |&#9989; |
Approve a comment            |&#10060;        |&#10060;        |&#9989; |
Delete a comment |&#10060;        |&#10060;          |&#9989; |
Edit a comment |&#10060;        |&#10060;          |&#9989; |
Delete a post |&#10060;        |&#9989;          |&#9989; |

## Existing Features
The screenshots below show desktop and mobile images for each feature/user story:
### Feature 1 Navigation Bar and Homepage
#### Description feature 1
#### User Stories feature 1 
- The homepage consists of a header/nav bar, a footer and 6 user posts.
- The header and footer is consistent across all pages.
- The navigation bar is displayed with a logo and title on all pages. If the user is not logged in the navbar includes a home icon button, a login button and a register button on a desktop device. If the user is logged in the navbar includes a home icon button, a plus icon (for adding a post) and a logout button on a desktop device. On a mobile device the users have to click the top right hand corner to make the above buttons appear.
- [Navbar desktop - Logged in User](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.04.23.png)
- [Navbar mobile - Logged in User](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.08.45.png)
- [Navbar desktop - Logged out User](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.05.03.png)
- [Navbar mobile - Logged out User](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.08.10.png)
- [Users Posts desktop - All Users](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.05.35.png)
- [Users Posts mobile - All Users](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.09.22.png)
- [Footer desktop - All Users](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.05.57.png)
- [Footer mobile - All Users](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.09.52.png)

#### User Stories feature 1
- User Story 1.1: As a first time/registered user the navigation bar is displayed with a logo on all pages with a home icon, add post and Register/Login icon on a desktop device.
- User Story 1.2: As a first time/registered user the navigation bar is displayed on all pages with a home icon, add post icon and Register/Login on a mobile/tablet device
- User Story 1.3: As a first time/registered user not logged in, I see a Register/Login link in the nav bar.
- User Story 1.4: As a first time user, I can register by clicking on the Register button. 
- User Story 1.5: As a registered user not logged in, I am brought to the Login link if I click on the login button.
- User Story 1.6: As a first time / registered user logged in, I am brought to the home page if I click on the home icon / the TravelPix title or image.
- User Story 1.7: As a first time/ registered user if there are more than six posts on the home page, the page is paginated with 6 posts per page
- User Story 1.8: As a registered user logged in, I see a Logout on the nav bar. 
- User Story 1.9: As a registered user logged in, if I click on the plus icon on the nav bar I am brought to the add post page.
- User Story 1.10: As a registered user logged in, if I click on my post in on the home page I am directed to the post detail page.
- User Story 1.11: As a registered user logged in, if I click on the Logout button on the navbar I am brought to the Logout page. 
- User Story 1.12: As a first time / registered user if I encounter an error on the site, I will be navigated to the applicable 404 error page.
- User Story 1.13: As a first time / registered user the footer bar is displayed on all pages with copyright and links to the social media pages.

### Feature 2 Register
- To interact with posts users can register for an account.
- The user must provide a valid email address, username, password and password confirmation.
- [Register - desktop](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.34.04.png)
- [Register - mobile](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.35.21.png)
- [Notification](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2021.19.39.png)

#### User Stories feature 2
- User Story 2.1: As a user I can register on the website by providing an email address, username, password and password confirmation. I am notifed that a confirmation email has been sent and that I am logged in.

### Feature 3 Login
- A registered user can log in to the website using their username and password
- Both fields are mandatory
- Once logged in the user will be navigated to the homepage
- [Login - desktop](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.42.06.png)
- [Login - mobile](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.42.35.png)
- [Notification](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2021.11.33.png)

#### Description feature 3
- User Story 3.1: As a registered user I can log in to the website using my username and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed

### Feature 4 Post Detail Pages
- A user not logged in can view the details of the post. The user can also view the comments.
- A user logged into the website can view other users post and like and comment on their post.
- A user that views their own post can edit and delete their posts.
- [Post details not logged in - desktop](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.52.22.png)
- [Post details not logged in - mobile](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.52.58.png)
- [Post details logged in viewing other users posts- desktop](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.52.22.png)
- [Post details logged in viewing other users posts- mobile](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.54.15.png)
- [Post details logged in viewing own posts- desktop](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.54.50.png)
- [Post details logged in viewing own posts- mobile](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.55.16.png)
- [Notification](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2021.25.55.png)

#### Description feature 4
- User Story 4.1: As a first time / registered user I can view the image, description and view comments (the most recent comment first) on the post detail page. If I click the back button I am redirected to the home page.
- User Story 4.2: As a registered user logged in I can comment and like users posts. When I add a comment to a post, it is sent to the admin for approval and I am notified.
- User Story 4.3: As a first time / registered user who has not logged into the website, I cannot add a comment or like a post
- User Story 4.4: As a registered user logged in I can edit and delete my own posts.

### Feature 5 Logout Page
- A user logged in is able to log out by pressing the log out button and confirming they want to log out.
- [Logout - desktop](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.42.06.png)
- [Logout - mobile](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2020.42.35.png)
- [Notification](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2021.10.37.png)

#### Description feature 5
- User Story 5.1: As a logged in user I can log out and I am notified that I have successfully signed out.

### Feature 13 Admin
#### Description feature 6
- As per the user stories below there are a number of admin views that have been configured, they give excellent CRUD operations to the data in the Postgres database.
- [Admin site](https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-21%20at%2021.29.48.png)

#### User Stories feature 6
- User Story 6.1: As an admin user I can view email addresses, who they belong to and if they have been verified in the django admin page. I have the option to add and change an email address.
- User Story 6.2: As an admin user I can view users and groups. I have the option to add and change a user and a group.
- User Story 6.3: As an admin user I can add, view and change an account.
- User Story 6.4: As an admin user I can add, view and change a comment. I also can approve users comments. Once approved users will be able to see their comment on the post detail page.
- User Story 6.5: As an admin user I can add, view and change a friend. 
- User Story 6.6: As an admin user I can add, view and change a post. I can see who created the post, when and if it is published or a draft.
- User Story 6.7: As an admin user I can add, view and change a site. 
- User Story 6.8: As an admin user I can add, view and change a friend. 
- User Story 6.9: As an admin user I can add, view and change social accounts. 

##  Features Left to Implement
- I am content with what was implemented. The site is a feature rich site
- However, here are some additional "nice to have" features and updates that could be added to the project

Number | Update  
 ------------ | ------- |
1 | Users can access their own profile to upload a profile picture and bio |
2 | Give users the option of following / adding another user as a friend |
3 | Develop a direct messaging app so users can interact "privately" with each other|
4 | I could have made some adjustments to my code so when users are uploading a post they only have to input certain fields rather than all fields |
5 | Improved pagination look/feel on post details page |

# Technologies Used
## Languages 
- HTML (https://en.wikipedia.org/wiki/HTML)
- CSS (https://en.wikipedia.org/wiki/CSS)
- Javascript (https://www.javascript.com/)
- Django (https://www.djangoproject.com/)
- Python v3.9 (https://www.python.org/)

## Libraries and other resources
- Bootstrap 5.0 (https://getbootstrap.com/docs/5.0)
- Postgres (https://www.postgresql.org/)
- SQLLite (https://www.sqlite.org/index.html)
- Gitpod (https://gitpod.io/)
- Github (https://github.com/)
- Google Fonts (https://fonts.google.com/)
- Moqups (https://moqups.com/)
- Font Awesome (https://fontawesome.com/)

# Testing
The testing information and results for this project are documented in

# Credits

### Header and Footer
- The header and footer design was assisted with tutorial notes and the I think therefore I blog project.

### Login / Register / Logout Pages
- The images on the login, logout and register page were taken from google images, using W3Schools to help to style the images.
Login: https://www.google.com/search?q=penguin+in+plane&sxsrf=AOaemvI4hzP3ZYwb7bYvXv98C_GGgGDDdQ:1642801640078&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjdqMWB6cP1AhULLsAKHfSeBcoQ_AUoAXoECAEQAw#imgrc=K8KxM44vfK5pcM
Logout: https://www.google.com/search?q=crying+emoji&sxsrf=AOaemvKOkQ0SxXT49gfextgJY6_HvEhMXw:1642801683980&source=lnms&tbm=isch&sa=X&sqi=2&ved=2ahUKEwjN5ryW6cP1AhWyT2wGHbAwBxAQ_AUoAXoECAEQAw&biw=1440&bih=789&dpr=2#imgrc=rSuzqZgA-JR_FM
Register: https://www.google.com/search?q=sign+up+image&sxsrf=AOaemvKptXO-bzfGjiGl9FKj79dE9wUuhA:1642801721067&tbm=isch&source=iu&ictx=1&vet=1&fir=_83NsmypQeQeMM%252CiF6a08kQ8_4pYM%252C_%253B4n8yPUe2o1o1rM%252CiF6a08kQ8_4pYM%252C_%253BnFXwJ8PUnBoyvM%252CuOHYTTWx35yLgM%252C_%253BskvPvGUy6KjxbM%252CSkxMCKXvegDYqM%252C_%253BCtF2g2mxWSVNxM%252CHTS5nEKbCLLvgM%252C_%253Bi-KQOga0SXJVHM%252CRWsoyFscvr-JAM%252C_%253BnVmkJDpE8bXzjM%252CiF6a08kQ8_4pYM%252C_%253BHlsj9A_N3NPvsM%252CHTS5nEKbCLLvgM%252C_%253BUXFV6LhsSfr0DM%252CVIM3pQrz7_CHJM%252C_%253BoXwc8jEmQJ7NNM%252COV_NfNYns3eQcM%252C_%253BDRJPYDM0ivz6uM%252C006shfNXO522AM%252C_%253BchZKSo28GT2t3M%252C-Z47EkJho3UimM%252C_%253BU0LFa0tdbMWwsM%252Cfy0imxmctI_xpM%252C_&usg=AI4_-kT2PVRE-A7zGDhr0QX4MG9sx0nh7w&sa=X&ved=2ahUKEwjyzpSo6cP1AhWSFMAKHRcnCr4Q9QF6BAgDEAE#imgrc=_83NsmypQeQeMM
- The form format was taken from the I think therefore I blog project.

### Home page
- The layout of the posts was taken from the I think therefor I blog project

### Add Post Page 
- The add a post page was developed on the back of the following video https://www.youtube.com/watch?v=m3efqF9abyg

## Media
- Travel Post information images were taken from google:
1. https://www.google.com/search?q=ireland+travel&tbm=isch&ved=2ahUKEwjUuo6m68P1AhXXOMAKHUr9DqsQ2-cCegQIABAA&oq=ireland+travel&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEO8DECc6BggAEAgQHjoHCAAQsQMQQzoICAAQgAQQsQM6BAgAEENQ8QpYxR5ghyFoAHAAeACAAT6IAeMFkgECMTWYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=TSzrYZTgJtfxgAbK-rvYCg&bih=789&biw=1440#imgrc=ZYaLkuOIMaM9PM
2.https://www.google.com/search?q=england+travel&tbm=isch&ved=2ahUKEwj3hvPc68P1AhXGS8AKHa7eBKUQ2-cCegQIABAA&oq=england+travel&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEO8DECc6BggAEAcQHlDnDVjrFWCFGGgAcAB4AIABQogB8QKSAQE3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=wCzrYfemIMaXgQauvZOoCg&bih=789&biw=1440#imgrc=DZvzYsIcfSJAxM
3.https://www.google.com/search?q=greece%5D+travel&tbm=isch&ved=2ahUKEwiG097l68P1AhVwQ0EAHV1VDx8Q2-cCegQIABAA&oq=greece%5D+travel&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEO8DECc6BggAEAcQHlCLBlj1EWD5EWgAcAB4AIABOYgB-AKSAQE3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=0yzrYcadBPCGhbIP3aq9-AE&bih=789&biw=1440#imgrc=xOPh_I2HoHIJ6M
4.https://www.google.com/search?q=iceland+travel&tbm=isch&ved=2ahUKEwif7Izy68P1AhXOF8AKHaCuAkEQ2-cCegQIABAA&oq=iceland+travel&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEO8DECc6BAgAEEM6BggAEAcQHlDACFiSHGC9HWgAcAB4AIABPYgBmASSAQIxMJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=7CzrYZ_GPM6vgAag3YqIBA&bih=789&biw=1440#imgrc=2p_ID2Qz_umJSM
5.https://www.google.com/search?q=new+york+travel&tbm=isch&ved=2ahUKEwjdkoig7MP1AhWymlwKHSo3AEcQ2-cCegQIABAA&oq=new+york+travel&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEO8DECc6BAgAEBg6BggAEAcQHlDsFVj4HmCAIWgAcAB4AIABPIgB3wOSAQE5mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=TS3rYZ24F7K18gKq7oC4BA&bih=789&biw=1440#imgrc=qkHzWQGmYjc7iM
6.https://www.google.com/search?q=lanzarote+travel&tbm=isch&ved=2ahUKEwi_zdjR7MP1AhXLbMAKHcmPBkAQ2-cCegQIABAA&oq=lanzarote+travel&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgQIABAYMgQIABAYMgQIABAYMgQIABAYMgQIABAYMgQIABAYMgQIABAYMgQIABAYOgcIIxDvAxAnUPECWPECYIwOaABwAHgAgAE5iAFpkgEBMpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=tS3rYf-eHMvZgQbJn5qABA&bih=789&biw=1440#imgrc=MjywFhZlR6PS7M
7.https://www.google.com/search?q=edinburgh+castle+travel&tbm=isch&ved=2ahUKEwii9P3T7MP1AhVbM8AKHczBBxEQ2-cCegQIABAA&oq=edinburgh+castle+travel&gs_lcp=CgNpbWcQAzIECAAQGDoHCCMQ7wMQJzoFCAAQgAQ6BggAEAcQHjoICAAQCBAHEB46BggAEAgQHlDsBljKMmCWNGgBcAB4AIABPYgBkQeSAQIxOJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=ui3rYaKvENvmgAbMg5-IAQ&bih=789&biw=1440#imgrc=bMOPxjeX2B0NjM

# Acknowledgements

-   My Mentor for continuous helpful feedback and assistance.

-   Tutor support at Code Institute and my friends from my course for their support and guidance.
