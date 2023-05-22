# Deployment Process

We utilized several technologies for coding and version control such as Gitpod, Visual Studio Code, Git Bash, and GitHub, all of which are listed in the `technologies used` section. These tools enabled us to swiftly deploy our product once completed.

Below are the detailed steps that outline the entire deployment process, from the initial installation of the Code Institute template to the final deployment on Heroku:

## Template

The following steps guide you through the setup of the PP3 template by Code Institute:

1. Visit the [P3 Template by Code Institute](https://github.com/Code-Institute-Org/p3-template).
2. Click on `Use this template` in the upper right corner. You can also directly access this via this [link](https://github.com/Code-Institute-Org/p3-template/generate).
3. Give your repository a name.
4. Make a backup of the instructions written in your README.md file, then begin creating your own.
5. Choose an Integrated Development Environment (IDE) for coding. We recommend Gitpod, CodeAnywhere, or Visual Studio Code (desktop).
6. Begin coding your project following the presence of Tenam on Github. (For cloning or forking our code, see the next section).
7. Set up an account on [Google Sheets](https://www.google.com/sheets/about/) and [Google Cloud Console](https://console.cloud.google.com/).
8. Optionally, you can copy Tenam's Google Sheets document at [Portfolio](https://docs.google.com/spreadsheets/d/1IEaXqnPewHWOS8JB6kf074AWygVKgqplSE1WjHs-T28/edit?usp=sharing) to use as a template, which will be accessed by our Python code using an API.
9. Avoid creating GitHub Pages to circumvent any potential websocket errors during deployment.
10. Create an account on [Heroku](https://heroku.com).

## Google Cloud Console

Google Cloud Console provides a plethora of APIs & Services for developers. For this project, we need to activate specific APIs and credentials:

1. Visit [Google Cloud Console](https://console.cloud.google.com/) and create an account.
2. Once logged in, click on the `Select a project` button, followed by the `New Project` button to create a new project. These options are located at the header.
3. Give your project a suitable name.
4. Navigate to your project by clicking on `Select project` either from the notification or the header.
5. Within your project, type `APIs & Services` into the search engine at the top.
6. Enable two APIs: `Google Drive` and `Google Sheets`.
7. In the `APIs & Services` section, type `Google Drive` and select the `Google Drive API` option.
8. Once inside this option, select `Enable`. You can now manage your credentials.
9. Repeat the same process for `Google Sheets`.

### Credentials

After obtaining these credentials, they can be accessed from the `APIs & Services` page, under the Credentials option. Scroll down to find your credentials. Click on them and then on `Service account` from the navigation menu, and finally on `Keys`. Your .JSON file can be found here. To reach this point, follow these steps:

1. After enabling the Google Drive API, click on the `Create Credentials` option.
2. A form will appear. For the first option, the type of API, select `Google Drive API`.
3. Select that you are requesting data from a web server.
4. For the type of data, select `Application Data`.
5. For the compute engine, select `No`.
6. Click on the `What credentials do I need?` button.
7. Here you can create a service account name. Remember to select the `editor` role to allow future manipulation of your Google Sheets.
8. Ensure `JSON` is selected for the key type and click on `Continue`.
9. An automatic download of your .JSON file will begin. This contains your credentials, ready for use. However, it still needs your Google Sheets URL, which we will address in the next section.

## Google Sheets API

After enabling this API from the `Library` section, no additional credentials are needed from here.

## Development Envirioment

