# DEVELOPMENT PROCESS

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
11. [Deployment Process](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/deployment.md)
12. [Credits](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/credits.md)

## Development Process

Our crypto portfolio tracker application was developed primarily using Python. The Python code was then adapted to a `mockup command-line terminal` template designed by the Code Institute. While it wasn't a requirement, we opted to style this template to make necessary improvements. Additionally, we've divided our README.md files into distinct sections, which facilitates easy navigation on Github.

Throughout the development process, we strongly adhered to the `user-centered design` approach inspired by Jesse James Garrett, despite this being a backend project. This approach was successful, mainly because we were creating an application for users, not solely for computer interaction. In the 'strategy' phase, we focused on the problem rather than the solution, determining what we wanted to build and laying out our scope accordingly.

The development process was both `fascinating and challenging`, as we had to learn Python and implement our knowledge simultaneously. Fortunately, we had the support of the Code Institute. From the environment setup, template installation, to Heroku deployment, we navigated each step with guidance.

We used Gitpod as our `Integrated Development Environment (IDE)` for this project, which allowed us to constantly test our code through the terminal and push changes to Github with ease.

- Throughout the journey, we paid close attention to our documentation, which significantly eased our development process.

- Coding challenges, errors, and general frustrations were tackled with patience, thorough research, and diligent study. We made use of the debugging tools available and availed tutoring services from the Code Institute.

- Along the way, we came to appreciate the importance of modules, libraries, and other dependencies, such as Google Sheets and Google Drive, as well as simpler ones like 'import time' or 'import os'.

- In our project, we utilized the following Python libraries and modules:

    - `import time`: This module provides various time-related functions. It is used for introducing pauses in the execution of the program, which is useful for creating better user-friendly interactions.

    - `from getpass import getpass`: getpass is a Python module for securely handling password prompts. We used it to handle user password input securely.

    - `import textwrap`: This module is used to format text output into paragraphs. It was handy for ensuring that our text output was neat and readable.

    - `import feedparser`: Feedparser is a universal feed parser that is useful for reading RSS feeds. We used it for our RSS News functionality to read news from Coindesk.

    - `from google.oauth2.service_account import Credentials`: This is a Google library for handling OAuth2, which is an open standard for access delegation. It was crucial for our connection with Google Sheets and Google Drive.

    - `import gspread`: Gspread is a Python client for Google Sheets. It allowed us to interact with our Google Sheets data.

    - `from textwrap import fill`: The fill function from the textwrap module formats text by filling paragraphs with hard line breaks.

    - `import os`: This module provides functions for interacting with the operating system. It was used, for example, for handling screen clearing on the command line.

- Lastly, we carried out necessary testing and managed to resolve a few errors without major complications.

We highly recommend reviewing all the steps outlined in this `README section` and visiting each index entry for a more granular understanding of our development process.