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
|      Max. Points      |           5            x        5         |       45       |
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