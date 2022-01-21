<h1>Travel|Pix</h1>
<br>
<p> <strong> A social media site used for interacting with people who share a common interest in looking at images from around the world </strong> </p>

[View the live project here.](website link/)

Home Page Image - [View]( https://github.com/MaeveHughes/TravelPix/blob/main/media/Screenshot%202022-01-19%20at%2016.09.37.png)

# Table of Contents
- [Project Overview](#project-overview)
  * [Strategy](#strategy)
  * [Structure](#structure)

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
- User Story 1.4: As a first time user, I can register by clicking on the Register button. The form asks me for the following details: *****. If I click sign up, account is now registered and I am redirected to the home page, If I click cancel I am redirected to the home page.
- User Story 1.4: As a registered user not logged in, I am brought to the Login link if I click on the login button.
- User Story 1.5: As a first time / registered user logged in, I am brought to the home page if I click on the home icon / the TravelPix title or image.
- User Story 5.3: As a first time/ registered user if there are more than six posts on the home page, the page is paginated with 6 posts per page
- User Story 1.7: As a registered user logged in, I see a Logout on the nav bar. 
- User Story 1.9: As a registered user logged in, if I click on the plus icon on the nav bar I am brought to the add post page. The form asks me for the following details: **** If I click post, my post will be added to the home screen and I will be redirected to the home screen. If I click cancel I am brought back to the homepage.
- User Story 1.9: As a registered user logged in, if I click on my post in on the home page I am directed to the post detail page. I am able to edit my post and delete my post. I am unable to edit and delete posts made by other users.
- User Story 1.10: As a registered user logged in, if I click on the Logout button on the navbar I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage.
- User Story 1.21: As a first time / registered user if I encounter an error on the site, I will be navigated to the applicable 404 error page.
- User Story 4.1: As a registered user I can log in to the website using my username and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed.
- User Story 5.4: As a first time / registered user if I click on a post I will be navigated to the post detail page.
- User Story 5.5: As a first time / registered user I can view the image, description, the number of likes and view comments (the most recent comment first). If I click the back button I am redirected to the home page.
- User Story 5.1: As a registered user logged in I can comment and like users posts. When I add a comment to a post, it is sent to the admin for approval and I am notified.
- User Story 5.14: As a first time / registered user who has not logged into the website, I cannot add a comment or like a post
- User Story 1.1: As a first time / registered user the footer bar is displayed on all pages with copyright and links to the social media pages.


### User Stories Website Owner
The user stories for the website owner(admin) are described as follows: 
There is a lot of overlap between the two user types, the admin user however has more administrative rights throughout but their roles and responsibilities
are defined
- User Story 1.1: As an admin user the navigation bar is displayed with a logo on all pages with a home icon, add post and Register/Login icon on a desktop device.
- User Story 1.2: As an admin user the navigation bar is displayed on all pages with a home icon, add post icon and Register/Login on a mobile/tablet device
- User Story 1.3: As a admin user not logged in, I see a Register/Login link in the nav bar.
- User Story 1.4: As an admin user not logged in, I am brought to the Login link if I click on the login button.
- User Story 1.5: As a user logged in, I am brought to the home page if I click on the home icon / the TravelPix title or image.
- User Story 5.3: As an admin user if there are more than six posts on the home page, the page is paginated with 6 posts per page
- User Story 1.7: As an admin user logged in, I see a Logout on the nav bar. 
- User Story 1.9: As an admin user logged in, if I click on the plus icon on the nav bar I am brought to the add post page. The form asks me for the following details: **** If I click post, my post will be added to the home screen and I will be redirected to the home screen. If I click cancel I am brought back to the homepage.
- User Story 1.9: As a admin user logged in, if I click on my post in on the home page I am directed to the post detail page. I am able to edit my post and delete my post. I am unable to edit and delete posts made by other users.
- User Story 1.10: As an admin user logged in, if I click on the Logout button on the navbar I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage.
- User Story 1.21: As an admin user if I encounter an error on the site, I will be navigated to the applicable 404 error page.
- User Story 4.1: As an admin user I can log in to the website using my username and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed.
- User Story 5.4: As an admin user if I click on a post I will be navigated to the post detail page.
- User Story 5.5: As an admin user I can view the image, description, the number of likes and view comments (the most recent comment first). If I click the back button I am redirected to the home page.
- User Story 5.1: As an admin user logged in I can comment and like users posts. When I add a comment to a post, it is sent to the admin for approval and I am notified.
- User Story 5.14: As an admin user who has not logged into the website, I cannot add a comment or like a post
- User Story 1.1: As an admin user the footer bar is displayed on all pages with copyright and links to the social media pages.
- User Story 13.15: As an admin user I can view email addresses, who they belong to and if they have been verified in the django admin page. I have the option to add and change an email address.
- User Story 13.15: As an admin user I can view users and groups. I have the option to add and change a user and a group.
- User Story 13.15: As an admin user I can add, view and change an account.
- User Story 13.15: As an admin user I can add, view and change a comment. I also can approve users comments. Once approved users will be able to see their comment on the post detail page.
- User Story 13.15: As an admin user I can add, view and change a friend. 
- User Story 13.15: As an admin user I can add, view and change a post. I can see who created the post, when and if it is published or a draft.
- User Story 13.15: As an admin user I can add, view and change a site. 
- User Story 13.15: As an admin user I can add, view and change a friend. 
- User Story 13.15: As an admin user I can add, view and change social accounts. 

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

