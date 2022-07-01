# Django-Models

I created a new GitHub repository with a README.md, and Python .gitignore file, cloned it to my machine/computer, which created a new folder on my computer with my repository’s content.

I then created a new virtual environment in that folder named ".env" and installed Django in it.

I created a new Django project and used my Zuriboard Student ID as the name of the project (I4G006943SYZ) and create a new application using the Django startapp command. The app was called "blog".

I added the blog app to the main_projects INSTALLED_APPS and created a new model in the blog app called "Post". It includes the following fields:



 Post

--------

Title : A string of maxlength 200, use Django’s models.CharField


Text : Any amount of text, use Django’s TextField


Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.

 
Created_date : A date-time column, use Django’s models.DateTimeField. 

 
Published_date : A date-time column, use Django’s models.DateTimeField. 

 

Then, I created migrations for my new model using the makemigrations Django command and ran all migrations using the migrate Django command.

Lastly, I staged and Committed my Django project and pushed the changes to my GitHub repository.

I also ensured that my final code/submission is on the default branch of my GitHub repository.

## P.S : This is also one of my assignments for #I4GZuri Scholarship Program.
