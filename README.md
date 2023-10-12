# PP5 Advanced FrontEnd: Capture The Moments

[Capture The Moments](https://api-django-5-e93439fb77b5.herokuapp.com/)<br>
A social media platform that's designed for the users to be able to post and interact with each others pictures.<br>Built with React and consists of an API.<br>

![Homepage](https://github.com/Humanslaughter/API-Django/assets/122393963/763cf6c5-d47e-4475-a73a-a736113c82ab)<br>

---

## Contents

* [Reflections](#reflections)

* [User Stories](#user-stories)

* [Features](#features)
  * [Future Implements](#future-implements)

* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries, Programs, Contexts & Hooks Used](#frameworks-libraries-programs-contexts--hooks-used)

* [Deployment & Local Development](#deployment--local-development)
	* [Deployment Steps](#deployment-steps)
 	* [Local Development](#local-development)
  		* [How To Fork](#how-to-fork)
  		* [How To Clone](#how-to-clone)
  
* [Testing](#testing)
  * [Automated](#automated)
  * [Manual](#manual)

* [Credits](#credits)
  * [Code/Content](#code/content)
  * [Images](#images)
  * [Acknowledgments](#acknowledgments)

---

## Reflections

This project was made as my 5th Portfolio Project, with the specialization in Advanced Frontend, for my course in Fullstack Software Development at Code Institute.
This was my first time using React and my first time at making an API. I started with making the API, and then combined it with a new React App in the same repository.<br>
<br>
I followed along with the two walkthrough projects the course provided for both the API and the React App while working on this project. Due to some problems that accured 
during the production, I ran into a lot of different challanges, e.g. errors which lead me having to spend and waste a lot of hours in finding solutions to each problem that popped up.<br>
<br>
This project includes React, React Bootstrap, React-Router, JavaScript, Python and CSS.

## User Stories

| Category  | As        | I can                          | so that I can                                                                                    | UI Components                                |
| --------- | --------- | ------------------------------ | ------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| auth      | a user    | sign up for an account         | have a personalized profile with a profile picture                                               | SignUpForm<br>ProfilePage<br>ProfileEditForm |
| auth      | a user    | sign up for an account         | make, like and comment on other users content                                                    | Post<br>PostPage<br>Comment                  |
| auth      | a user    | sign up for an account         | follow and unfollow other users                                                                  | Profile<br>ProfilePage                       |
| posts     | a visitor | view a list of posts           | browse the newest content                                                                        | PostsPage                                    |
| posts     | a visitor | view a specific post           | see likes and read comments                                                                      | Post<br>PostPaget                            |
| posts     | a visitor | search a list of posts         | find posts by specific users or titles                                                           | PostsPage                                    |
| posts     | a visitor | scroll through a list of posts | browse more comfortably                                                                          | InfiniteScrollComponent                      |
| posts     | a user    | edit/delete my own posts       | edit or hide unwanted mistakes                                                                   | PostEditForm<br>MoreDropdownMenu             |
| posts     | a user    | make posts                     | share pictures with others                                                                       | PostCreateForm                               |
| posts     | a user    | view posts that I liked        | go back to all my liked posts                                                                    | PostsPage                                    |
| posts     | a user    | view posts from followed users | keep up with users content that I enjoy                                                          | PostsPage                                    |
| likes     | a user    | like posts                     | show my interest in users content                                                                | Post like icon                               |
| likes     | a user    | unlike posts                   | show my loss of interest in users content                                                        | Post (un)like icon                           |
| comments  | a user    | post a comment                 | share thoughts on others posts                                                                   | PostPage<br>CommentCreateForm                |
| comments  | a user    | edit/delete my own comments    | edit or hide my comments                                                                         | PostPage<br>Comment<br>MoreDropdownMenu      |
| profiles  | a user    | view profiles                  | see users posts + followers and following count                                                  | ProfilePage<br>Post                          |
| profiles  | a user    | edit my profile                | update my information                                                                            | ProfileEditForm                              |
| followers | a user    | follow profiles                | show my interest in users content                                                                | Profile follow button                        |
| followers | a user    | unfollow profiles              | show my loss of interest in users content and remove it from my feed                             | Profile (un)follow button                    |

---

## Features

- Responsive navigation bar at the top of the screen with links to:
  - If **signed in** - ADD POST, HOME, FEED, LIKED, SIGN OUT, PROFILE.
  - If **signed out/visitor** - HOME, SIGN IN, SIGN UP.
  
	- HOME<br>
    A feed of recently uploaded content from users.

		![HOME - LOGGED IN](https://github.com/Humanslaughter/API-Django/assets/122393963/e92f5f2d-69b8-4539-a839-163f43e5a20e)<br>
   
	  Home page on smaller screen
		![HOME - SMALLER SCREEN](https://github.com/Humanslaughter/API-Django/assets/122393963/c9d32b91-9678-4499-8ed6-bb02600668b6)<br>

	- FEED<br>
    Users can see the posts from the users they follow.

		![FEED](https://github.com/Humanslaughter/API-Django/assets/122393963/2ee96611-1e47-41b3-8009-bf31969a3803)<br>
	
 	- LIKED<br>
    Users can see all posts they've liked.

		![LIKED](https://github.com/Humanslaughter/API-Django/assets/122393963/73a1c6e0-3c99-4be8-be88-39f4957a4a24)<br>

	- SIGN IN<br>
 		Users with an account can sign in.

	  ![SIGN IN](https://github.com/Humanslaughter/API-Django/assets/122393963/e1bb02df-9060-4501-933d-0fd2674b5b8c)<br>

	- SIGN UP<br>
		Visitors can sign up for an account.

		![SIGN UP](https://github.com/Humanslaughter/API-Django/assets/122393963/e394ae2e-6800-49ab-a0d6-be833fc469d0)<br>

	- SEARCHBAR<br>
  	Users can search for usernames or keywords at the top of the screen.
 
 	- ADD/EDIT POSTS<br>
   	Logged in users can upload imagesd by clicking 'ADD POST' and then select an image, add title and content. TThey can then either click 'Upload' or 'Cancel'.
    Users can edit/delete their own posts by clicking on one of their own posts and then click the dots-meny in the top right corner.
    
		![ADD POST](https://github.com/Humanslaughter/API-Django/assets/122393963/0d0adb7e-8f60-41a5-b544-6af06ecf0760)<br>
		![USERS OWN POST](https://github.com/Humanslaughter/API-Django/assets/122393963/79d57b0b-0c48-4aef-8e1f-8d753aaaacd9)<br>
		![EDIT-DELETE POST](https://github.com/Humanslaughter/API-Django/assets/122393963/d168414d-ad82-4998-a431-964b54b01ceb)<br>

	- COMMENTS<br>
 		Logged in users can comment on posts, and can edit/delete their own comments.
 
 	- LIKES<br>
		Logged in users can like/unlike other users posts, they can not like their own posts.

	- FOLLOW/UNFOLLOW<br>
    Logged in users can follow/unfollow other profiles by clicking the button beside that users profile picture.

	- MOST FOLLOWED USERS<br>
		Profile users with the most followers is shown, in order of the most to the least amount. 
   
		Most Followed Users - Visitor/not logged in<br>
		![MOST FOLLOWED USERS - NOT LOGGED IN](https://github.com/Humanslaughter/API-Django/assets/122393963/5bdb4d70-6e0f-40fb-bd91-a2c3d3c8204c)<br>

 		Most Followed Users - Logged in<br>
	 	![MOST FOLLOWED USERS - LOGGED IN](https://github.com/Humanslaughter/API-Django/assets/122393963/7bfbe751-2344-4ff5-87ef-7db84e1c58a0)<br>

	- PROFILES<br>
    Users/visitors can view profiles by clicking on a profile picture. On the profile, you can see the users posts, the amount of posts they've made, how many followers they have, and how many they follow. 			<br>Logged in users can click a button to follow/unfollow that user. The owner of the profile can edit their profile content, profile picture, username, and password by clicking the meny in the top right 		corner of the profile.
	
		![Dots menu](https://github.com/Humanslaughter/API-Django/assets/122393963/9a821bc3-d464-48bf-8859-c16acdd690b6)<br>
		![PROFILE](https://github.com/Humanslaughter/API-Django/assets/122393963/c9cbe521-9986-45bf-9e8a-50941045e6bf)<br>

### Future Implements

In future implements, I would like to add features such as:
- Expanded authentication - register with both email and username, email confirmation.
- Add a PM/chat function.

---
 
## Technologies Used

### Languages

- JavaScript, Python, CSS and HTML.

### Frameworks, Libraries, Programs, Contexts & Hooks Used

- GitHub.
- Gitpod - VS Code (IDE).
- Django/Django REST Framework/Django Auth - DRF API.
- PostgreSQL - Database.
- React/React Bootstrap/react-router-dom - Frontend.
- Cloudinary - Image storage.
- Infinitescroll.
- MSW library - Mocking.
- Contexts:
  - CurrentUserContext - user state exposed to the app so relevant components can subscribe to the changes.
  - ProfileUserContext - profile state exposed to the app so the PopularProfiles component can be in sync with ProfilePage.
- Custom hooks:
  - useClickOutsideToggle - toggles on burger menu.
  - useRedirect - redirects logged in/logged out users.

---

## Deployment & Local Development

Deployed by using Heroku.

### Deployment Steps

- Comment out all console.log(err).
- Set up WhiteNoise for static files.
- Configure route for React App.
- Compile and combine static files of API and React App.
- Add a runtime.txt file.
- Test build.
- Set ALLOWED_HOST and CLIENT_ORIGIN on Heroku to URL of combined project.
- Deploy to Heroku.

### Local Development

#### How To Fork

Fork the repository:<br>
	1. Log in/sign up to GitHub.
 	2. Go to the repository for this project [API-Django](https://github.com/Humanslaughter/API-Django).
	3. Click the 'Fork' button in the top right corner.

#### How To Clone

Clone the repository:<br>
	1. Log in/sign up to GitHub.
 	2. Go to the repository for this project [API-Django](https://github.com/Humanslaughter/API-Django).
	3. Click the code button, select which one you want to clone with (HTTPS, SSH or GitHub CLI) and copy the link shown.
 	4. Open the terminal in a code editor and change the current working directory to a location of your choice to use for the cloned directory.
	5. Type 'git clone' in the terminal, paste the link that you copied in step 3 and then press enter.

---

## Testing

### Automated

- MSW library used to mock user/logout endpoints.
- Tested the rendering of the Navbar:
  - No problems when rendering.
  - Link to a logged in user profile renders.
  - Buttons for Sign in/Sign up renders again on logout.

### Manual

- Other features have been greatly tested throughout production and before/after final deployment.

---

 ## Credits

 ### Code/Content

 - I followed along the walkthrough projects "Moments" and "Django REST Framework" by Code Institute while making this project.
 - All user accounts that's currently signed up (2023-10-12) was made up by me.

### Images

- All images borrowed from [Pexels](https://www.pexels.com/sv-se/).
- The image posted and profile picture used by the user [wikstromphotos](https://api-django-5-e93439fb77b5.herokuapp.com/profiles/1) is my own.

### Acknowledgments

- Student Care, Code Institute - I want to acknowledge and thank them for everything they've done and helped me with so far.
