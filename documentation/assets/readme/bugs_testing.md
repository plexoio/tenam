# BUGS, TESTING & SECURITY

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

## Bugs, Testing & Security

As with any software development process, we encountered several challenges and bugs during the development of our app. Despite these hurdles, we're proud to have effectively addressed them all.

The results of our testing have been satisfactory, as illustrated in the following analysis.

- ### Bugs

#### a) Website Performance

Our project is deployed on Heroku and fetches information from Google Drive and Spreadsheet systems. Given that these cloud-based systems operate with a limited quota, we cannot guarantee that the site will always be available or perform optimally. However, it's important to note that this issue is not directly linked to our application.

#### b) App Loading Issues

We occasionally encountered a problem where our code wasn't running correctly despite the template loading flawlessly, as seen in the image below.

After attempting several solutions, we found that the issue was probably related to our Github page, which wasn't necessary for deployment. We deactivated it, deleted our app from Heroku, and re-deployed it from scratch. Surprisingly, this strategy resolved our `Websocket` connection error.

![Websocket error](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/web.png)

#### c) Screen Clearing Function

Our screen clearing function, which uses the 'os' import, didn't work as expected on the deployed command-line. It didn't clear all the information as it does in the IDE terminal. Despite trying various solutions, we encountered the same result.

We addressed this by transforming the functionality into a `refresh` feature and added separation lines for each feature.

#### d) KeyboardInterrupt Issues

We noticed that some keyboard inputs were not accepted immediately after deployment. We implemented a try/except clause to catch the error, print a message to the user, and allow the app to continue running.

This solution works perfectly so far. However, we are aware that there may be less common keyboard inputs that could present problems, which we plan to address in future iterations.

#### e) Heroku App Availability

Sometimes, users might encounter an error indicating that our app does not exist on Heroku. Refreshing the page typically resolves this issue and restores the connection. It's a rare occurrence, but it's one we've noted.

#### Other Bugs

For other potential bugs, we recommend refreshing the page or clearing cache files. Any problem encountered is unlikely to stem from the Tenam project; it may instead be related to third-party issues or specific settings and capabilities of the user's device.

- ### Testing

To ensure the high quality of our application, we conducted rigorous testing throughout the development process. This involved leveraging the CI Python Linter by Code Institute, Lighthouse, GT-Metrix, and the Google Console to obtain a variety of insights. The results were highly satisfactory.

#### CI Python Linter by Code Institute

Adhering to PEP8 standards 100% of the time can be challenging. Therefore, we regularly used the CI Python Linter during development. This tool was invaluable in maintaining code structure and enhancing the overall presentation.

![Linter](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/linter.png)

#### Lighthouse

Lighthouse provided analysis across several facets of our application. Although not mandatory, we complemented its use with GT-Metrix to ensure the delivery of a quality product. The results met our expectations.

![Light House](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/lighthouse.png)

#### GT-Metrix

With its unique strengths, GT-Metrix was an essential part of our testing process. It provided us with valuable suggestions, all of which were deemed non-critical for this iteration. The app is functioning well and ready for delivery.

![GT-metrix](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/gtmetrix.png)

#### Google Console

Google Console played a pivotal role in diagnosing and resolving our websocket connection bug. During the final testing phase, we monitored the console while running the app to detect any potential errors. The results were excellent - no errors occurred and the app ran smoothly.

We refreshed the page multiple times to simulate connection errors but none occurred, confirming the app's robustness.

![Google Console](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/console.png)

#### Responsiveness

In the current iteration, we did not design the app to be responsive due to time constraints. However, enhancing responsiveness will be a priority in future updates.

- ### Security

As we've noted before, this iteration uses only dummy data. Users are provided with a test username and password, eliminating the need to input personal information. The integrity of user data remains uncompromised. Even the Google Spreadsheet updates are accessible and transparent, particularly for the `Taxation` and `Data Analysis` sections.

- Our commitment to privacy and security extends to the handling of sensitive files. Thus, we've included our 'creds.json' file in our '.gitignore' to prevent it from being publicly accessible.
