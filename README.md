# Tenam - A Crypto Portfolio Tracker

Tenam - your comprehensive cryptocurrency portfolio tracker. This dynamic tool consolidates all your crypto investments into a single interface, negating the need to individually access each platform. 
For the present phase, we're utilizing static data from gspread, acknowledging the open and sensitive nature of project delivery on GitHub.

Tenam emphasizes seamless portfolio access, rich statistical analysis, and timely crypto market updates with a single click. However, our vision extends beyond merely displaying your crypto amounts and their corresponding dollar values. We're committed to creating an investment-focused experience for our users. This includes accounting for country-specific tax implications linked to cryptocurrency liquidations and transactions. To facilitate this, Tenam includes a transaction sheet that diligently records all deposits and withdrawals.

Tenam is equipped with robust features like current price comparisons against portfolio values, coin filtering, and historical value analysis. This empowers you with insightful retrospection (past values) and foresight (future values) regarding your holdings.

In this iteration, all can be accessed only through a `command-line interface`.

For future implementations, we aim to establish direct connections with leading cryptocurrency exchanges such as Binance and Coinbase for real-time portfolio management. 

Please note: While Tenam is designed to be a valuable tool for managing your cryptocurrency investments, it should not serve as a substitute for professional financial advice. It's essential to conduct your own research and consider consulting with a financial advisor prior to making any investment decisions.

Please note that this project is not available for public deployment; **it is intended solely for learning and demonstration purposes** even though is ready for use.

![Responsive Mockup image](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/mockup.png)

**Preview Link:** [Tenam](https://tenam-crypto.herokuapp.com/)


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

On the other hand, the "taxation" and "RSS information" features scored the lowest. Considering our ambition, we initially believed it would not be possible to include one or both of these features in this iteration as they are not critical at the moment. However, we have managed to successfully add them to this MVP.

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

In this initial iteration, we have a clear understanding of our desires, requirements, and what is beneficial for us. The IXD and IAD supplied us with the essential components to work with, empowering us to reach our objectives with this remarkable project. We can now proceed to the `Skeleton plane` and start building from this point forward.

## Skeleton Plane <a name="skeleton-plane"></a> | [#](#index)

Tenam cryptoportfolio tracker is our first real backend project ever built. It has presented a challenge throughout the journey, but with gratifying results. We have collected fragments from various sources, much like ascending a mountain. We have carefully selected and refined these pieces from the strategy plane to this current plane, analyzing and `extrapolating` essential data, steps, features, and functionalities. We have also implemented different technologies, skills, and knowledge.

As mentioned before, Tenam has followed a logical sequence: Strategy, Scope, Structure, and now we find ourselves at the `Skeleton Plane`.

This time we did not have to worry about the front-end; `Code Institute` took care of that for us by providing a template and instructions to upload it on `Heroku`. Hence, the current image is the one that helped us visualize how our application would run and work based on the constraints it holds.

At this plane, all the features, functionalities, elements' interactions, and content layouts are `visible` and `comprehensible`. We can understand the `interconnectedness` of each component we have been diligently working on.

The plan is to build a data processing application on a command-line interface, which can then be used as a backend for a frontend site.

Here is an example of what we saw before starting coding. We had to take into account the '80 columns by 24 rows' constraint.

![Skeleton image](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/skeleton.png)

The simple and straightforward navigation is visible, and everything is just a few clicks away from the user's goal. The priorities are also clear: Assets, Transaction, Data Analysis, Taxation, Update Tax Value, RSS News, Refresh, and Exit.

Notice the progression from simple to more complex functionalities and layouts. Users are able to learn as they navigate through the command-line. We take the `progressive disclosure` part seriously to avoid overwhelming them.

![Skeleton image](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/skeleton.gif)

We invested time and resources into this process before `coding` the actual product to bring it to life. In this case, we are using a gif to showcase the final result, as the skeleton part of the front-end never changed.

Although it's a robust design, everything is attainable by the users with a bit of intuition. We paid attention to the users, following their own habits, standards, and conventions.

As seen from the gif, we focused on keywords, invisible information, hierarchies, and content presented in lists and sublists. You can experience all of these aspects in our desktop-based `prototype/demo` already deployed on Heroku.

We strived to keep everything simple, intuitive, and repetitive. At the same time, we set the foundation for our last plane by defining `spaces`, `layouts`, `interaction`, and `feedback`.

Our next stop is the `Surface Plane`.

## Surface Plane <a name="surface-plane"></a> | [#](#index)

After conducting research (strategy), considering the project scope, brainstorming ideas for the structure, and engaging in discussions to create a project skeleton, we were ready to move forward with creating a prototype/demo using wireframes. 

All of these planning stages were essential to reach this point (Surface), and we understand that it's only when we start building or coding that we may discover any gaps or oversights. Therefore, it makes more sense to start finally bringing our ideas to life now. 

We're excited to see how our project takes shape and how we continue to refine it along the way.

**Approach:**

Our approach to the project is similar to the mindset of Isaac Newton, who said, `"My method is different. I do not rush into actual work. When I get a new idea, I start at once building it up in my imagination, and make improvements and operate the device in my mind. When I have gone so far as to embody everything in my invention, every possible improvement I can think of, and when I see no fault anywhere, I put into concrete form the final product of my brain."` Similarly, we have taken the necessary steps to plan and refine our project before moving on to the programming stage.

As part of this process, we are currently focusing on the surface plane, which involves designing the interface and considering how users will interact with and perceive the product as well. This includes creating a positive visual language and context for each step and interaction to ensure efficiency and a seamless user experience. 

These details are crucial for the success of the project, and we are dedicated to getting them right:

### Color

|                                                                  | Color Type      | Color Name      | Hex Code  |
| ---------------------------------------------------------------- | --------------- | --------------- | --------- |
| ![Color](https://via.placeholder.com/50x50/3498db/3498db?text=+) | Primary Color   | Shade of Blue   | `#3498db` |
| ![Color](https://via.placeholder.com/50x50/f5f5f5/f5f5f5?text=+) | Secondary Color | Whitesmoke      | `#f5f5f5` |
| ![Color](https://via.placeholder.com/50x50/808080/808080?text=+) | Secondary Color | Shade of gray   | `#808080` |
| ![Color](https://via.placeholder.com/50x50/3a3a3a/3a3a3a?text=+) | Secondary Color | Shade of Black  | `#3a3a3a` |
| ![Color](https://via.placeholder.com/50x50/f2f2f2/f2f2f2?text=+) | Secondary Color | Shade of White  | `#f2f2f2` |
| ![Color](https://via.placeholder.com/50x50/e46e54/e46e54?text=+) | Secondary Color | Shade of red    | `#E46E54` |
| ![Color](https://via.placeholder.com/50x50/ff6600/ff6600?text=+) | Secondary Color | Shade of orange | `#ff6600` |


#### Pallet

The following color palette was used as a reference throughout the project:

- [My Color Space](https://mycolor.space/?hex=%233498DB&sub=1)


### Layout

- The welcoming page features is a full-page banner with a `h2-sized` title and a `Swap` button to enter the system.

- For the login section, `containers` and a `form` are used to manage it. All elements are well-connected and interactive, thanks to `JavaScript`.

- The swapping sections for `Fiat & Crypto` are `containers` holding `forms` for the swapping functionality. In every section where a `submit or call-to-action` is present, the same style is used to maintain consistency.

- The `contact form` also follows the consistency of the containers and features a powerful form and a related `submit button`, as mentioned before.

- Finally, the layouts will naturally adjust to different `sizes` when media queries are set for `responsive design`.

### Fonts

- We used `Roboto` for all fonts until specified otherwise. 

- We used `Poppins` for some titles and subtitles.

### Images

- No additional images were needed, except for the `interactive logo` of a third-party service about `Metamask` on the login page.

### Order

- We prioritized the elements as already described throughout the different planes: Welcome page > Login Page > Fiat or Crypto Swap > Contact page.

- The navbar and footer are always present (sticky) after the welcome page.

- For the Contact page, a container similar to the others was applied to maintain consistency.

### Sequences

- Attention to the `progressive disclosure` allowed us to build a smooth application flow. Users see the `welcome page` first, then they can `log in` using either Fiat or Crypto methods. Once logged in, they can start `swapping` in a straightforward manner. If they have any inquiries, they can visit the `contact page` as well.

- The `swapping pages` are the core of the project and what users are looking for in most cases. They are consistent and allow users to swap from one coin to another and `confirm` the swap with a submit `button`.

For each section and interaction, economy had to be taken into account, with the most important elements easily recognized. We had already noticed many patterns throughout the product layouts and interactions. It was readable, with colors creating good contrasts, and different fonts were added when necessary.

Users cannot get lost on the site as we have ensured that value is evident everywhere.

**We had to be careful of the following concerns:**

- Repetition
- Contrast
- Proximity
- Alignment
- Accessibility
- Interaction
- Visual engagement
- Easy learning experience

We focused on keeping things as simple as possible, presenting fewer choices to the users while highlighting concrete features and content.

After considering these factors, we were able to turn our ideas from the skeleton and surface into code with ease. The coding process was less complicated and more enjoyable. This approach required less time, energy, and other resources, resulting in less human work and fewer errors, and ultimately, a nobler product.
