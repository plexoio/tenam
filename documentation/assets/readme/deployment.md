# WORKSPACE SET UP & DEPLOYMENT PROCESS

## [HOME | Return](https://github.com/plexoio/tenam/blob/main/README.md)

1. [Strategy Plane - Reason, Solution and Value](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/strategy.md)
2. [Scope Plane - Feature and Capability](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/scope.md)
3. [Structure Plane - Content, Priority and Organization](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/structure.md)
4. [Skeleton Plane - Layout, Interaction and Relationship](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/skeleton.md)
5. [Surface Plane - Color, Typography, Effect and Images](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/surface.md)
6. [Technologies Used](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/technologies.md)
7. [Actual Features Explained](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/actual_features.md)
8. [Future Features Explained](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/future_features.md)
9. [Bugs, Testing & Security](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/bugs_testing.md)
10. [Development Process](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/development.md)
11. [Workspace Set Up & Deployment Process](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/deployment.md)
12. [Credits](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/credits.md)

## Workspace Setup & Deployment

We employed a variety of technologies such as Gitpod, Visual Studio Code, Git Bash, and GitHub, for coding and version control. Detailed in the `Technologies Used` section, these tools facilitated swift product deployment upon completion.

Below, you'll find a comprehensive outline of the entire Workspace Set Up & Deployment Process, from the initial setup of the Code Institute template to the final deployment on Heroku:

## Workspace Setup

### Template

The Code Institute's P3 template can be set up with the following steps:

1. Visit the [P3 Template by Code Institute](https://github.com/Code-Institute-Org/p3-template).
2. Click `Use this template` in the upper right corner. Alternatively, you can directly access this via [this link](https://github.com/Code-Institute-Org/p3-template/generate).
3. Name your repository.
4. Back up the instructions written in your README.md file, then start creating your own.
5. Choose an Integrated Development Environment (IDE) for coding. We recommend Gitpod, CodeAnywhere, or Visual Studio Code (desktop).
6. Begin coding your project following the presence of Tenam on Github. (For cloning or forking our code, see the next section).
7. Create accounts on [Google Sheets](https://www.google.com/sheets/about/) and [Google Cloud Console](https://console.cloud.google.com/).
8. Optionally, you can copy Tenam's Google Sheets document at [Portfolio](https://docs.google.com/spreadsheets/d/1IEaXqnPewHWOS8JB6kf074AWygVKgqplSE1WjHs-T28/edit?usp=sharing) as a template, which will be accessed by our Python code using an API.
9. Avoid creating GitHub Pages to prevent potential websocket errors during deployment.
10. Create an account on [Heroku](https://heroku.com).

### Google Cloud Console

Google Cloud Console offers numerous APIs & Services for developers. For this project, specific APIs and credentials need to be activated:

1. Visit [Google Cloud Console](https://console.cloud.google.com/) and create an account.
2. Once logged in, click on the `Select a project` button, then the `New Project` button to create a new project. These options are located at the header.
3. Give your project a suitable name.
4. Navigate to your project by clicking on `Select project` either from the notification or the header.
5. Within your project, type `APIs & Services` into the search engine at the top.
6. Enable two APIs: `Google Drive` and `Google Sheets`.
7. In the `APIs & Services` section, type `Google Drive` and select the `Google Drive API` option.
8. Once inside this option, select `Enable`. You can now manage your credentials.
9. Repeat the same process for `Google Sheets`.

#### Credentials

After obtaining these credentials, they can be accessed from the `APIs & Services` page, under the Credentials option. Scroll down to find your credentials. Click on them and then on `Service account` from the navigation menu, and finally on `Keys`. Your .JSON file can be found here. To reach this point, follow these steps:

1. After enabling the Google Drive API, click on the `Create Credentials` option.
2. A form will appear. For the first option, the type of API, select `Google Drive API`.
3. Select that you are requesting data from a web server.
4. For the type of data, select `Application Data`.
5. For the compute engine, select `No`.
6. Click on the `What credentials do I need?` button.
7. Here you can create a service account name. Remember to select the `editor` role to allow future manipulation of your Google Sheets.
8. Ensure `JSON` is selected for the key type and click on `Continue`.
9. An automatic download of your .JSON file will begin. This contains your credentials, ready for use. In the next steps we will need the `client_email` value found there, to connect it to our Google Sheet. Which we will address in the next section.

### Google Sheets API

After enabling this API from the `Library` section, no additional credentials are needed from here.

### Development Environment

1. On your selected IDE place your .JSON file we got from Google Drive API installation on the main directory of your template, remember to rename it as `creds.json`.
2. Finally we can enter this file and copy the value found on the `client_email` entry.
3. Once copied (without the quotes around it) we take this value to our Google Spread sheet.
4. On your google sheet click on the `Share` button located at the top of the page.
5. A section will open and in there we paste our client email and then select `Editor` option.
6. Uncheck the `notify people` option.
7. Then click `share`
8. IMPORTANT: now include this `creds.json` file in your `.gitignore` file to protect your credentials.
9. Back on your template remember to use this set up on your run.py file:

```python
# Importing the necessary modules and libraries for Google Sheets API
from google.oauth2.service_account import Credentials
import gspread

# Google Sheets related constants and credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('ADD-HERE-YOUR-GOOGLE-SHEET-NAME')
```

## Deployment Process

Because GitHub Pages doesn't support backend deployment, we'll utilize a third-party service. For this project, we're using [Heroku](https://heroku.com/), a platform where we can host and deploy our app.

Please follow these steps for a successful deployment:

1. Ensure the `requirements.txt` file resides in your project's root directory.
2. Run the following command in your terminal: `pip3 freeze > requirements.txt`.
3. The command will automatically populate your `requirements.txt` with your project's dependencies.
4. If you haven't done so yet, create an account on [Heroku](https://heroku.com/).

### Heroku

Let's bring our project to life on the Heroku platform. Follow these steps carefully for a successful deployment:

1. From the Heroku dashboard, click on `Create a new app`. Provide a name for your app and select your country.
2. Click on `Create App`.
3. A new dashboard for your app will open. We'll be primarily using the `Deploy` and `Settings` sections.

#### Settings Section

1. In the `Settings` section of your Heroku app, scroll down to the `Config Vars` block.
2. Here, we'll add sensitive data from our `creds.json` file.
3. For KEY, input `CREDS`. For VALUE, paste all content from your `creds.json` file.
4. Navigate to the `Buildpacks` block on the same page and install `Python` first, followed by `Node.js`.

#### Deploy Section

1. For the deployment method, select `Github`.
2. Authorize the connection to Github to link your repository.
3. In the `Connect to Github` block, search for your repository name and select it.
4. Once located, click the `Connect` button.
5. This will unveil two new sections: `Automatic deploy` and `Manual Deploy`.
6. We are interested in the `Manual Deploy` section.
7. Ensure that the main branch is selected (this should be the default selection), then click on `Deploy Branch`.
8. Let Heroku do the rest of the work. Once the process completes, it will provide a `View` button to access your URL and see your app online.

Please note: Ensure you have sufficient credits or a suitable plan on Heroku to maintain access to your app.

This completes the process for workspace setup and deployment. If you encounter difficulties understanding this process, we recommend supplementing our steps with Youtube tutorials.
