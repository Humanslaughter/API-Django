# PP5 Advanced FrontEnd: Capture The Moment

![Mockup](https://github.com/Humanslaughter/API-Django/assets/122393963/a84f6bf4-bcad-46b5-9df2-29d15f622867)

This is a social media platform that I made with the help of the walkthrough projects "Django REST Framework" and "Moments" by Code Institute.<br>

The front end of the project is built with React and the back end is built with Django REST Framework to make a built-in API.<br>
This website is designed for users who have an interest in art of all kinds like photography, digital art, and more.<br>
I'm one of those people who have an interest in photography/photo editing and have been since a young age. <br>

This is my fifth and final portfolio project for my course in Full-Stack Software Development. It was also my first time using React and making an API. I started with the API and when finished, combined it with a React App in the same repository.

[Visit Capture The Moment](https://api-django-5-e93439fb77b5.herokuapp.com/)<br>

---

## Contents
* [User Stories](#user-stories)

* [Features](#features)
  * [Future Implements](#future-implements)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)

* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries, Programs, Contexts & Hooks Used](#frameworks-libraries-programs-contexts--hooks-used)

* [Deployment & Local Development](#deployment--local-development)
	* [Local Development](#local-development)
		* [How To Fork](#how-to-fork)
		* [How To Clone](#how-to-clone)
  
* [Testing](#testing)
  * [Automated](#automated)
  * [Manual](#manual)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

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

## Design

### Colour Scheme
![PP5](https://github.com/Humanslaughter/API-Django/assets/122393963/9fc766c1-f12d-44d1-adcc-7cd7360a8cc2)

### Typography
- Font Family: DM Sans, sans-serif.

## Features

- Responsive navigation bar at the top of the screen with links to:
  - If **signed in** - ADD POST, HOME, FEED, LIKED, SIGN OUT, PROFILE.
  - If **signed out/visitor** - HOME, SIGN IN, SIGN UP.
  
	- HOME<br>
 	A feed of recently uploaded content from users.

	Home page - Logged in
		![HOME - LOGGED IN](https://github.com/Humanslaughter/API-Django/assets/122393963/e99bad09-acd5-4171-a093-464f79b455d2)<br>

  	Home page - Logged out
		![HOME](https://github.com/Humanslaughter/API-Django/assets/122393963/e38de13a-3afa-43a0-9753-516ce15123cb)<br>

	Home page on my Galaxy S22 Ultra
		![HOME ON MOBILE](https://github.com/Humanslaughter/API-Django/assets/122393963/b6aed352-ec6a-44f9-9500-98f8b0d418cf)<br>

	- FEED<br>
 	Users can see the posts from the users they follow.

		![FEED 3](https://github.com/Humanslaughter/API-Django/assets/122393963/1b81ac08-2208-4269-98a9-0515c472bec3)<br>

 	- LIKED<br>
  	Users can see all the posts they've liked.

		![LIKED 2](https://github.com/Humanslaughter/API-Django/assets/122393963/860fe1ee-28c4-433c-a0e3-e33dbfed8f5d)<br>


	- SIGN IN<br>
 	Users with an account can sign in.

	 	![SIGN IN](https://github.com/Humanslaughter/API-Django/assets/122393963/45a112c3-f3c8-4408-9a54-064d96c5b6b5)<br>

	- SIGN UP<br>
 	Visitors can sign up for an account.

		![SIGN UP](https://github.com/Humanslaughter/API-Django/assets/122393963/a5a6c8ae-d849-4618-85f3-0886151a8268)<br>

	- SEARCHBAR<br>
 	Users can search for usernames or keywords at the top of the screen.
 
 	- ADD/EDIT POSTS<br>
  	Logged-in users can upload images by clicking 'ADD POST' and then selecting an image, adding title and content. They can then either click 'Upload' or 'Cancel'.
	Users can edit/delete their posts by clicking on one of their posts and then clicking the dots menu in the top right corner.
    
		![ADD POST](https://github.com/Humanslaughter/API-Django/assets/122393963/265deef3-6c88-4053-b1af-4249ec3cc5f6)<br>
		![POST](https://github.com/Humanslaughter/API-Django/assets/122393963/d94c477e-eec0-45e9-b1b8-6dd89955b283)<br>
		![EDIT AND DELETE OPTIONS](https://github.com/Humanslaughter/API-Django/assets/122393963/c1f8812b-a526-44b5-82b2-b77f195fd774)<br>

	- COMMENTS<br>
 	Logged-in users can comment on posts and can edit/delete their comments.
 
 	- LIKES<br>
  	Logged-in users can like/unlike other user's posts, but they can not like their own posts.

	- FOLLOW/UNFOLLOW<br>
 	Logged-in users can follow/unfollow other profiles by clicking the button beside that user's profile picture.

	- MOST FOLLOWED USERS<br>
 	Profile users with the most followers are shown, in order of the most to the least amount. 
   
		Most Followed Users - Visitor/not logged in<br>
		![MOST FOLLOWED USERS - LOGGED OUT](https://github.com/Humanslaughter/API-Django/assets/122393963/abfbf6b5-a9f8-4918-a176-afe525625a1b)<br>

 		Most Followed Users - Logged in<br>
	 	![MOST FOLLOWED USERS - LOGGED IN](https://github.com/Humanslaughter/API-Django/assets/122393963/986a86da-89b7-4c17-9554-b6b068e0fdea)<br>

	- PROFILES<br>
 	Users/visitors can view profiles by clicking on a profile picture. On the profile, you can see the user's posts, the amount of posts they've made, how many followers they have,
	and how many they follow.<br>
 	Logged-in users can click a button to follow/unfollow that user. The owner of the profile can edit their profile content, profile picture, username, and password by clicking the
	menu in the top right corner of the profile.
	
		![PROFILE OPTIONS](https://github.com/Humanslaughter/API-Django/assets/122393963/2f3d8a7a-9e4d-4fcc-9709-8a27c5e2bfcb)<br>
		![PROFILE 2](https://github.com/Humanslaughter/API-Django/assets/122393963/39374d31-c22b-406f-85c2-92f576107bf3)<br>
  		![PROFILE](https://github.com/Humanslaughter/API-Django/assets/122393963/a7eabbaf-7b1f-4c61-95f1-afe1ef1f2fe4)<br>


### Future Implements

In future implements, I would like to add features such as:
- Expanded authentication - register with both email and username, email confirmation.
- Add a PM/chat function.

## Technologies Used

### Languages

- JavaScript, Python, HTML, and CSS.

### Frameworks, Libraries, Programs, Contexts & Hooks Used

- Gitpod (VS Code, IDE), GitHub - To be able to develop this project.
- Heroku - For app deployment.
- Django - For building backend logic with Python.
- Django REST Framework - To build a Django REST Framework API with Django.
- Django Auth - For user authorization (sign up/sign in).
- Django filters - For filtering images that are uploaded.
- psycopg2 - to use a PostgreSQL database.
- React, React Bootstrap, React Router Dom - For building/rendering an interactive UI, page navigation, and responsive stylesheet.
- Cloudinary - For image storage.
- Infinitescroll - To make the site pages feel smooth and look nice while you scroll. 
- MSW library - For mocking.
- Axios - For performing asynchronous calls.
- WhiteNoise - For collecting staticfiles from the frontend/React app and connecting it to the backend/database. 
- Contexts:
  - CurrentUserContext - User state exposed to the app so relevant components can subscribe to the changes.
  - ProfileUserContext - Profile state exposed to the app so the PopularProfiles component can be in sync with the profile page.
- Custom hooks:
  - useClickOutsideToggle - Toggles on the burger menu.
  - useRedirect - Redirects signed-in/signed-out users.

## Deployment & Local Development

### Local Development
Deployed using Heroku:<br>
1. Log in/sign up to Heroku.
2. Go to your Heroku App and click on "Deploy".
3. At the section "Deployment method", click "GitHub" and connect your account with Heroku.
4. When you're connected, search for the project you wanna connect the app to and click on it.
5. Click "Deploy Branch".
6. Your app will now be deployed to GitHub and when it's done you can click "Open App".

#### How to Fork
Fork the repository:<br>
1. Log in/sign up to GitHub.
2. Go to the repository for this project [API-Django](https://github.com/Humanslaughter/API-Django).
3. Click the 'Fork' button in the top right corner.

#### How to Clone
Clone the repository:<br>
1. Log in/sign up to GitHub.
2. Go to the repository for this project [API-Django](https://github.com/Humanslaughter/API-Django).
3. Click the code button, select which one you want to clone with (HTTPS, SSH, or GitHub CLI), and copy the link shown.
4. Open the terminal in a code editor and change the current working directory to a location of your choice to use for the cloned directory.
5. Type 'git clone' in the terminal, paste the link that you copied in step 3, and then press enter.

## Testing

### Automated
- MSW library used to mock user/logout endpoints.
- Tested the rendering of the Navbar:
  - No problems when rendering.
  - Link to a logged-in user profile renders.
  - Buttons for Sign in/Sign up render again on logout.

### Manual
Testing was ongoing throughout the development process. Chrome Dev Tools was used during the building to test the responsiveness and interactions. The deployed website is tested on Chrome, Opera GX, and Samsung S22 Ultra.<br>
The site looks and works as intended.

- Navbar/Links/Buttons<br>
Each link on the Navbar and pages works without any problem, same with the buttons. Rendering and navigation work as intended and expected.

- Auth/Acess<br>
Both the sign-in and sign-up forms work without problems. The request and redirecting send you to the correct pages.<br>

Only users that have an account and are logged in have access to adding posts and they can only edit/delete the posts and comments they've posted and only have access to edit their own profile, username, and password.<br>
Only logged-in users can post/edit/delete comments, like other's posts (not their own), and follow/unfollow other profiles.

- Alerts/Warnings/Redirect<br>
An alert for when you click on the post button to comment on a post pops up for a few seconds as expected.

A warning prompt comes up whenever you try to delete a post or comment, asking if you're sure. After clicking Delete to confirm the post or comment is deleted and you get redirected to the right page.

After you change your password or username, a prompt pops up that says that the change has been successful. After clicking the 'x' on the prompt, it goes away and you're redirected back to your profile page.

 ## Credits

 ### Code
 - Followed along the walkthrough projects "Moments" and "Django REST Framework" by Code Institute while making this project.

### Content
- All user accounts that exist at this moment (2024-01-29) besides "Theodore" and "WikstromPhotos" were made up by me. The other two are just me.

### Media
- All images borrowed from [Pexels](https://www.pexels.com/sv-se/).
- The images posted and profile pictures used by the users [WikstromPhotos](https://api-django-5-e93439fb77b5.herokuapp.com/profiles/1) and [Theodore](https://api-django-5-e93439fb77b5.herokuapp.com/profiles/3) is my own.
- [Favicon](https://favicon.io/emoji-favicons/camera-with-flash/).
- I borrowed the icons and burger menu from the walkthrough "Moments", I liked the look of them.

### Acknowledgments
- Student Care, Code Institute - I want to acknowledge and thank them for everything they've done so far and for being very understanding.
