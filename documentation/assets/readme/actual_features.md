# Actual Features Explained

## [Index - Return](https://github.com/plexoio/tenam/blob/main/README.md)

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

## Current Features <a name="features"></a>

We are quite pleased with our achievements, despite initial concerns about time constraints. Reflecting on the project, it's evident that all features can be enhanced and further developed in the future. This iteration has simplified design elements and provides functionalities such as adding, deleting, and updating assets, performing calculations based on deposits and withdrawals, general computations, and coin filtering (planned for future implementation). It also enables assets foresight and retrospection.

The following features proved essential for our Minimum Viable Product (MVP):

## Index.html

### Mockup command-line interface

We went above and beyond with the development of the interface, adding components such as background color and an info section, even though they weren't strict requirements. In this section, we'll focus on the features within the command-line interface.

#### Welcome Section

The welcome section provides useful information about user location and the subsequent steps. It also incorporates an input field to verify the user's human identity.

![Welcome section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/welcome.png)

#### Login Section

In the login section, users receive further guidance on navigation and can test the app with provided login information. The login input handles validation and error management, as shown below.

![Login section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/login.png)

#### Menu Section

The menu is the core of the app, providing access to all main features. It's displayed as a list, making it interactive, user-friendly, and enjoyable. By simply inputting a number, users can explore various internal features and gain insights into their crypto portfolio.

Please note that from this point onward, all inputs feature validation and error handling capabilities.

![Menu section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/menu.png)

#### Assets section

This section reveals part of the underlying technology. Here, users can see their current balances and crypto holdings. Based on this data, the system's algorithm generates helpful data analysis for guiding investment decisions.

![Asset section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/asset.png)

#### Transaction section

This section demonstrates a realistic setting with dummy data. It showcases deposits, withdrawals, and relevant Blockchain metadata such as currency, status, and TxID.

![Transaction section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/transaction.png)

#### Data Analysis Section

The Data Analysis section showcases the app's capabilities. It uses an algorithm to provide user-specific feedback based on their holdings and market trends, and also initiates tax calculations. 

This section presents data processed in the background, embodying the essence of technology—an application that solves real-world problems. Note the last bullet point, which informs users if their crypto investment is resulting in a win or a loss. All profit calculations consider taxes, saving users from additional computations.

![Data Analysis Section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/data_analysis.png)

#### Taxation section

The Taxation section is integral to our application, given the importance of tax planning in financial investment. It transparently displays the default tax percentage, which can be updated as shown in the next section. All calculations are based on this percentage, ensuring users receive comprehensive insights into their net profit after tax, thereby aiding them in making informed investment decisions.

![Taxation Section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/taxation.png)


#### Update Tax Value

In consideration of the tax variances across different countries and regions, users can adjust the default tax value in this section. This adjustment allows for a more accurate data analysis.

Take note of the system's ability to validate requests and handle errors.

![Update Tax Value](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/update_tax.png)

#### RSS News

This section provides users with valuable insights into the current market trends through important articles. For this version, users can browse the latest Blockchain news from Coindesk. The news feed updates dynamically each time a user logs in. Users can view up to three blocks of news at a time, each block containing a title, preview content in bold, and a link to the full article.

This section also contributes to our knowledge acquisition.

![RSS News](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/rss.png)

#### Refresh & Exit Features

The refresh and exit features add convenience for the user. For instance, if a user feels overwhelmed, they can simply type '7' to return to the module and clear any potentially confusing information.

If a user is satisfied with their session, they can simply type '8' to log out and close the page.

It's noteworthy that the features for validation, error handling, and user feedback are consistently present throughout all interactions within the general menu.

![Refresh & Exit](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/refresh_exit.png)
