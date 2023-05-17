# Tenam - A Crypto Portfolio Tracker

Tenam - your comprehensive cryptocurrency portfolio tracker. This dynamic tool consolidates all your crypto investments into a single interface, negating the need to individually access each platform. 
For the present phase, we're utilizing static data from gspread, acknowledging the open and sensitive nature of project delivery on GitHub.

Tenam emphasizes seamless portfolio access, rich statistical analysis, and timely crypto market updates with a single click. However, our vision extends beyond merely displaying your crypto amounts and their corresponding dollar values. We're committed to creating an investment-focused experience for our users. This includes accounting for country-specific tax implications linked to cryptocurrency liquidations and transactions. To facilitate this, Tenam includes a transaction sheet that diligently records all deposits and withdrawals.

Tenam is equipped with robust features like current price comparisons against portfolio values, coin filtering, and historical value analysis. This empowers you with insightful retrospection (past values) and foresight (future values) regarding your holdings.

In this iteration, all can be accessed only through a `command-line interface`.

For future implementations, we aim to establish direct connections with leading cryptocurrency exchanges such as Binance and Coinbase for real-time portfolio management. 

Please note: While Tenam is designed to be a valuable tool for managing your cryptocurrency investments, it should not serve as a substitute for professional financial advice. It's essential to conduct your own research and consider consulting with a financial advisor prior to making any investment decisions.

Please note that this project is not available for public deployment; **it is intended solely for learning and demonstration purposes** even though is ready for use.

![Responsive Mockup image](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/responsive-mockup.webpp)

**Preview Link:** [Morada Hotel](https://plexoio.github.io/morada/index.htmm)


## Index <a name="index"></a>

1. [Strategy Plane - Reason, Solution and Value](#strategy-plane)
2. [Scope Plane - Feature and Capability](#scope-plane)
3. [Structure Plane - Content, Priority and Organization](#structure-plane)
4. [Skeleton Plane - Layout, Interaction and Relationship](#skeleton-plane)
5. [Surface Plane - Color, Typography, Effect and Images](#surface-plane)
6. [Technologies Used](#technologies)
7. [Actual Features Explained](#features)
8. [Future Features Explained](#f-features)
9. [Bugs & Testing Results](#bugs-testing)
10. [Development Process](#development)
11. [Deployment Process](#deployment)
12. [Credits](#credits)

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Strategy Plane <a name="strategy-plane"></a> | [#](#index)

Drawing upon years of personal experience and extensive local market research, we've discerned that the majority of people desire a seamless and secure way to access and manage their crypto assets. They want this without the need for intricate authentication, and without risking their account integrity, regardless of the crypto platform hosting their assets.

Tenam is our answer to this need. We've designed it to fetch, display, and analyze crypto asset information directly from these platforms.

In this initial iteration, we've opted for a simpler approach by focusing solely on data originating from Google Sheets, rather than integrating with platforms like Binance or Coinbase. However, this phase is crucial as it lays the foundational groundwork for what is to become a fully operational crypto portfolio tracker.

Our focus is the data originating from Google Sheets. We're treating it as we would data from any other crypto platform - manipulating and presenting it in a user-friendly `command-line interface`, courtesy of XXX.

Our insights are grounded in thorough research, as substantiated by the accompanying table and graphic:

### Research

<br>

|         Goals         |    Relevancy (0-5)     | Viability (0-5)  | N. Items (0-~) |
| :-------------------: | :--------------------: | :--------------: | :------------: |
|     Login             |           5            |        5         |       1        |
|     Welcome           |           5            |        5         |       1        |
|     Taxation          |           3            |        5         |       1        |
|     Menu              |           5            |        4         |       1        |
|     Portfolio display |           5            |        3         |       1        |
|     Data Analysis     |           5            |        3         |       1        |
|     Transaction history |         4            |        3         |       1        |
|     RSS information   |           3            |        3         |       1        |
|     Add, Delete, Update |         5            |        5         |       1        |
|       N. Items        |                        |                  |       9        |
|      Max. Points      |                        |                  |   5 * 9 = 45   |
|        Results        |           40           |        36        |                |
|      Percentage       | 88.88% <br> (Strategy) | 80% <br> (Scope) |                |


<br>

### Research Graphic

![Table Graphic](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/graphic.png)

Getting 88.88% for `Relevancy` and 80% for `Viability` has given us a clear understanding of what we are trying to build here. We now have a perspective on where the hard work will be focused and what are the priorities for this iteration. Additionally, we can identify which features may need to be neglected in case we run out of time.

The `Login` and `Welcome` features are definitely crucial, receiving a perfect score of 5 out of 5, as they provide users with information about their current location and access within the command-line interface.

Similarly, the `Add, Delete, and Update` features also scored 5 out of 5. These features allow users to interact with the application beyond just inputting data.

On the other hand, the `taxation` and `RSS information` features scored the lowest. Given our ambition, it might be reasonable to exclude one or both of these features in this iteration since they are not critical at the moment.

Features that scored 4 or above, such as `Transaction History`, will definitely be included. However, if a feature scored 3 in viability, it means that it may not be as advanced, at least for now.

Based on these percentages, we can develop our overall strategy by considering the relevancy and viability of the features. This information will guide us in planning the upcoming `scope`, as these factors are interconnected.

With this information in mind, we can now proceed to the next stage, which is defining the `scope` of our project.

## Scope Plane <a name="scope-plane"></a> | [#](#index)

Python posed a significant challenge, particularly due to the mental strain that the last two projects exerted. The timeframes were exceedingly short, leaving us with hardly any room to breathe or fully assimilate the information. However, we remained steadfast in our belief in simplicity while aiming to deliver a project that was not only demonstrative but also fully functional. Our strategy allowed us to visualize what we could achieve given the constraints of time, technology, and resources.

For this iteration, we decided to incorporate features and functionalities under the following conditions and goals:


|Condition|Iteration|Goals|
|---|---|---|
|Limited use|Data Analysis<br>Transaction History<br>RSS News<br>Taxation|Culture acquisition|
|Simple design|Portfolio Display<br>Menu<br>Login<br>Welcome<br>Add, Delete, Update|Tech Showcase|
|Low leading rates<br>& Non-functional| RSS News|Long-term Investment<br>& Future Implementation|


As we can observe, the first three items on our list are the most achievable. We plan to draft the starting points for those tagged as future implementation to ensure clarity, enhance user experience, and effectively communicate our message.

The entire development process is slated to span five days, with the initial design for future implementation not exceeding one day.

In this iteration, our focus is on pragmatism to meet the requirements of both the Code Institute and the project at hand.

We have thoroughly analyzed crucial elements at every stage of our research for "Useful, Sellable, Buildable" – taking into account objectives, functional and non-functional requirements, business rules, future implementation possibilities, and much more.

As per our User Story table, users have the ability to:

**Note:** In this context, "subject" refers to a user, prospect, or stakeholder.

### User Story

| Scenario                                      | Solution                                                                               |
| --------------------------------------------- | -------------------------------------------------------------------------------------- |
| User seeks a crypto portfolio tracker         | User finds the command-line interface                                                  |
| User realizes there isn't a connection yet    | User understands this is an MVP iteration for demonstration purposes                   |
| User wants to learn more about the app        | User discovers the app's functionality by logging in and exploring                      |
| User wants to test each feature               | User finds the menu section presenting all essential entry points                      |
| User wants to know more about Blockchain      | User finds an RSS functionality designed for this purpose                               |

Consequently, we have aligned our Scope with the findings derived from our research in the Strategy phase. It is evident at this point that the intention is to implement a Minimum Viable Product (MVP) iteration. This will effectively aid us in establishing the foundations for our next stage, `Structure`.

## Structure Plane <a name="structure-plane"></a> | [#](#index)

This project is designed for everyone, although the level of difficulty may primarily cater to users with `accessibility` issues. The entire operation runs on a command-line interface that is highly user-friendly and straightforward, making it easy to understand the concept and actual functionalities.

In terms of navigation, we opted not to compile a list of rules as it wouldn't serve our project's purpose. Instead, users will find a `Menu section` as soon as they log in. This design ensures that users can effortlessly navigate, identify their current location within the application, comprehend the available actions, and determine their potential next steps.

Our `Gitmind` mind maps vividly illustrate the different state changes, from the welcome page to the various features of the MVP app.

As always, we have `prioritized` consistency, predictability, learnability, visibility, and feedback to ensure a positive user experience.

For more details on our `Interactive Experience Design (IXD)` for the `Tenam Prototype/Demo Project`, please refer to the attached mind map.

![IXD Mindmap Initial](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/initial-IXD.png)

- [IXD Live Mindmap](https://gitmind.com/app/docs/m1k5arpj)

- [IXD Live Outline](https://gitmind.com/app/docs/m1k5arpj?view=outline)

![IXD Mindmap](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/IXD.png)

In navigating the site, we aim to promote efficent users' decision-making by providing familiar vocabulary and clear instructions. We assure users that they can maximize the potential of our MVP.

We recognize that a command-line interface can pose challenges for some users. However, in our case, we've made every effort to ensure that all interactions are easy to understand and straightforward.

It's crucial to consider both IXD (Interaction Experience Design) and IAD (Information Architecture Design) to achieve a comprehensive mental model of the product.

For more detailed insights into our `Information Architecture Design (IAD)` for the `Tenam Prototype/Demo Project`, please refer to the attached mind map.

![IAD Mindmap Initial](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/initial-IAD.png)

- [IAD Live Mindmap](https://gitmind.com/app/docs/me6xknis)

- [IAD Live Outline](https://gitmind.com/app/docs/me6xknis?view=outline)
  
![IAD Mindmap](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/IAD.png)

In this initial iteration, we have a clear understanding of our desires, requirements, and what is beneficial for us. The IXD and IAD supplied us with the essential components to work with, empowering us to reach our objectives with this remarkable project. We can now proceed to the Skeleton plane and start building from this point forward.