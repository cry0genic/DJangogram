# DJangogram
## Basic Idea
You will be building a mini social media site with a few basic features. There will be some essential features you are supposed to implement. Apart from these, feel free to show off your creativity as a developer. There is also no need for your app to “look” good. (Leave that to the frontend devs).

## Mandatory Features
- User authentication. Users must be able to register/login to your app. We expect you to use Django’s built-in auth system.
- Each user must have a profile in which they can add/update data. This data can be: Name, Bio, Profile Pic, etc.
- User’s should be able to make posts and make comments on posts. No need to implement comment replies for now.
- Allow users to follow each other. Think about how you’ll implement this using Django’s models.
- Make it possible to edit and delete posts. Think about the implications of this. How would you prevent cyber-bullying/cyber-crime caused by this feature?
- Let the user see a feed on the homepage. This feed should include posts by people the user follows.
- Create a feature where staff and site admins can generate a report containing all of the basic profile data of each person registered on the site. The profile should be in the form of an excel sheet and we suggest using Openpyxl to get this done in python.
- Extend the login system. Make it so that a person can also log in with Google. Use Google's API to provide OAUTH 2.0 based log-in.
