# Deployment 

## Setting up the Workspace:

1. Install Django with version 3.2:
    * ```pip install django3.2 ```
2. Install gunicorn:
    * ```pip install gunicorn```
3. Install supporting libraries:
    * ```pip install dj_database_url psycopg2```
    * ```pip install dj3-cloudinary-storage```
4. Create requirements.txt:
    * ```pip freeze --local > requirements.txt```
5. Create an empty folder for your project in your chosen location.
6. Create a project in the above folder:
    * django-admin startproject <PROJECT_NAME> 
7. Create an app within the project:
    * ```python manage.py startapp APP_NAME``` 
8. Add a new app to the list of installed apps in setting.py
9. Migrate changes: 
    * ```python manage.py migrate```
10. Test server works locally: 
    * ```python manage.py runserver```  (You should see the default Django success page)

## Create Heroku App:
The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.
1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
2. Give the app a unique name:
    * Will form part of the URL 
3. Select the nearest location:
    * For me, this was Europe.
4. Add Database to the Heroku app:
    * Navigate to the Resources tab of the app dashboard. Under the heading "Add ons," search for "Heroku Postgres" and click on it when it appears. 
    * Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
5. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.

## Creating Environmental Variables Locally:

1. On your local machine, create a file called ".env" at the same level as settings.py and add this to the .gitignore file.
2. From the Heroku app settings tab, click "reveal config vars" and copy the value of the variable DATABASE_URL. Add this value to a variable called DATABASE_URL in your create .env file:
    * ``` DATABASE_URL=PastedValueFromHerokuHere ```
3. From your projects settings.py file, copy the SECRET_KEY value and assign it to a variable called SECRET_KEY in your .env file
    * ``` SECRET_KEY=PastedValueFromYourProjectsSettings.pyFile ```
4. Add DEVELOPMENT variable to .env file:
    * ``` DEVELOPMENT=development ```
5. Add CLOUDINARY_URL variable to .env file:
    * Log into cloudinary and from the dashboard copy the API Environmental Variable.
    * Add to .env file like below
        * ``` CLOUDINARY_URL=PastedApiEnvironmentalVariable ```


## Setting up setting.py File:
1. At the top of your settings.py file, add the following snippet immediately after the other imports:
    ``` 
        import os
        import dj_database_url
        if os.path.isfile('env.py'):  

        SECRET_KEY = os.environ.get("SECRET_KEY")
        DEBUG = True
    ``` 
2. Delete the value from the setting.py DATABASES section and replace it with the following snippet to link up the Heroku Postgres server:  
   
    ```
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ```

3. Add Cloudinary libraries to the installed apps section of settings.py file:
   
   ```
    INSTALLED_APPS = [
   …,
   'cloudinary_storage',
   'django.contrib.staticfiles',
   'cloudinary',
   …,
   ]
   (note: order is important)
   ```

4. Tell Django to use Cloudinary to store media and static files by placing this snippet under the comments indicated below:
```
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

5. Under the line with BASE_DIR, link templates directly in Heroku via settings.py:
   * ``` TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') ```

6. Within TEMPLATES array, add ``` 'DIRS':[TEMPLATES_DIR] ``` like the below example:
```
   TEMPLATES = [
       {
           …,
           'DIRS': [TEMPLATES_DIR],
           …,
          
        },
       },
   ]
```
7. Add allowed hosts to settings.py:
    * ``` ALLOWED_HOSTS = ["PROJECT_NAME.herokuapp.com", "localhost"] ``` 

8. Create Procfile at the top level of the file structure and insert the following:
    * ``` web: gunicorn PROJECT_NAME.wsgi ```

9. Make an initial commit and push the code to the GitHub Repository.
    * ```git add .```
    * ```git commit -m "Initial deployment"```
    * ```git push```

## Set up Heroku for use via the console.
1. Click on Account Settings (under the avatar menu)
2. Scroll down to the API Key section and click Reveal. Copy the API key.
3. Log in to Heroku via the console and enter your details.
    * heroku login-i
    * When prompted, enter your Heroku username
    * Enter copied API key as the password

4. Get your app name from Heroku
    * ```heroku apps```
5. Set Heroku remote
    * ```heroku git:remote -a <app_name>```
6. Add, Commit, Pust to GitHub:
    * ```git add . && git commit -m "Deploy to Heroku via CLI"```
7. Push to GitHub and Heroku
    * ```git push origin main```
    * ```git push heroku main ```

## Final Deployment steps
Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :
- Set DEBUG flag to False in settings.py
- Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable :  DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch
