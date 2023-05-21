# STRATEGY PLANE

## [Index - Return](https://github.com/plexoio/tenam/blob/main/README.md)

1. [Strategy Plane - Reason, Solution and Value](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/strategy.md)
2. [Scope Plane - Feature and Capability](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/scope.md)
3. [Structure Plane - Content, Priority and Organization](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/structure.md)
4. [Skeleton Plane - Layout, Interaction and Relationship](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/skeleton.md)
5. [Surface Plane - Color, Typography, Effect and Images](https://github.com/plexoio/tenam/blob/main/documentation/assets/readme/surface.md)
6. [Technologies Used](#technologies)
7. [Actual Features Explained](#features)
8. [Future Features Explained](#f-features)
9. [Bugs & Testing Results](#bugs-testing)
10. [Development Process](#development)
11. [Deployment Process](#deployment)
12. [Credits](#credits)

## Strategy Plane <a name="strategy-plane"></a>

Drawing upon years of personal experience and extensive local market research, we've discerned that the majority of people desire a `seamless` and `secure way` to access and manage their crypto assets. They want this without the need for intricate authentication, and without risking their account integrity, regardless of the crypto platform hosting their assets.

Tenam is our answer to this need. We've designed it to fetch, display, update and analyze crypto asset information.

In this `initial iteration`, we've opted for a simpler approach by focusing solely on data originating from Google Sheets, rather than integrating with platforms like `Binance` or `Coinbase`. However, this phase is crucial as it lays the foundational groundwork for what is to become a fully operational crypto portfolio tracker.

Our focus is the data originating from Google Sheets. We're treating it as we would data from any other crypto platform - manipulating and presenting it in a user-friendly `command-line interface` template, courtesy of [Code Institute](https://github.com/Code-Institute-Org/p3-template).

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

On the other hand, the `taxation`, `update taxation` and `RSS information` features scored the lowest. Considering our ambition, we initially believed it would not be possible to include one or all of these features in this iteration as they are not critical at the moment. However, `we have managed to successfully add them to this MVP`.

Features that scored 4 or above, such as `Transaction History`, will definitely be included. However, if a feature scored 3 in viability, it means that it may not be as advanced, at least for now.

Based on these percentages, we can develop our overall strategy by considering the relevancy and viability of the features. This information will guide us in planning the upcoming `scope`, as these factors are interconnected.

With this information in mind, we can now proceed to the next stage, which is defining the `scope` of our project.