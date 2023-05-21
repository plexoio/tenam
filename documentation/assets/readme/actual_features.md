# Actual Features Explained

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

## Actual Features Explained<a name="features"></a>

We were very satified with the results even though we thought we did not have time to fulfill our plans. At the end we only can say that all features should be developed further in the future and that for this iteration the simpliest design goes to, the ability to add, delete and update, calculations based on deposits and withdrawals, general caltulations, coin filtering (future implementation) and assets foresight and retrospection

The following features were essential for our MVP:

## Index.html

### Mockup command-line interface

What we have developed furthur around the interface, like the background color and the info section under it was not really a requiremente for the project but we thought it necessary to add. Therefore, in this section we will only speak about the features that happen inside the command line.

#### Welcome Section

The welcome section holds an informative section to tell the user
s where they are and what are the next steps to follow, an input takes place to assure the user is a human and not a robot.

![Welcome section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/welcome.png)

#### Login Section

The login section tells the users again where they are and what steps they can follow, we have provided them with important login information to test the app. As seen from the image below the login input can be validate or handle errors.

![Login section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/login.png)

#### Menu Section

The menu is the powerful section of the app the portal to all the main features, displaied as list and accesible with an input, it keeps bwing interactice, userfriendly and enjoyable to use.

By simply inputting a number users can be visit the various internal features to understand their crypto portfolio.

![Menu section](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/menu.png)

#### Fiat Swap

The fiat swap feature is designed to be simple and user-friendly, while also hiding the underlying technology from users. Currently, it is capable of handling some conversions using Javascript for demonstration purposes.

The feature allows users to swap numbers and update balances. Most buttons within this section are interactive in some way or another, enhancing the user experience.

Don't forget to give the switching button a try!

![Fiat](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/fiat.png)

#### Crypto Swap

The crypto section functions similarly to the swap section, but it is connected to a Blockchain and will always try to call Metamask to fetch numbers and process transactions.

While both the fiat and crypto sections are for demonstration purposes, they showcase important interactivity.

Don't forget to give the switching button a try!

![Crypto](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/crypto.png)

#### Footer

At the final part of the index.html, we have our footer. Users can also find it on the contact.html page. The footer features the primary color of the project and is also sticky, meaning it will stay visible even when the user scrolls down the page. It contains important information, like a crypto widget, links to social media accounts, and copyright information. 

![footer](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/footer.png)

### contact.html

In this section, we planned a more sophisticated contact form that would have been even more interactive using Javascript. However, due to the lack of time, we were not able to implement it. Let's consider it part of the `Future Implementation`.

#### Welcome Page

The welcome page here is is also an essential feature that informs users of their location and purpose. It is also useful for marketing purposes.

![Welcome Contact Page](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/contact.png)

#### Contact Section

The current contact form is still fully functional, interactive, and useful. It is also user-friendly and enjoyable to use.

The header and footer sections are repeated throughout the website to maintain consistency and improve the overall user experience.

![Contact](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/contact-page.png)

## Bugs & Testing

As with any project, there may be some bugs that we have encountered. Here are some of the issues we've come across:

#### a) Website is too slow

We tried our best to keep everything on a single page, making a powerful web application that works efficiently on every device. However, we cannot guarantee that it will work the same on devices with low memory or processing capacities.

#### b) Metamask not working

Currently, Metamask is installed and partially working as expected, although there is a true feature installed. Once it is connected properly to the site, no issues should be found. For the rest, make sure you have allowed Metamask to login.

#### c) Footer widget not seen

The footer widget is a third-party widget, as seen in our credits section and technologies used. It may not load sometimes, but it does not mean it is not currently working; it could be due to network issues.

#### d) The balances return to the original state after refreshing the page

This is normal and expected since the accounts created are for showcasing the power of the project.

#### e) Social media issue

Currently, social media buttons only point to the main pages for demonstration purposes.

#### Other bugs

For other related bugs, we recommend always refreshing the page or deleting cache files. The problem is not with the tenam project; it could be related to third-party issues or related to your own device settings and capabilities.

## Testing

We have tested our site for accessibility, Javascript, HTML & CSS validation, performance on GT-metrix, and responsiveness.

We also ran a check with Google Chrome's integrated Lighthouse devtool and found a few errors, which were fixed accordingly. These included improving the aria-label. Surprisingly, the accessibility of the site was great!

During the development process, we constantly tested to ensure that we delivered a great final product. After the development process and deployment, we conducted the following tests:

#### Accessibility

We used a Screen Reader created by Google to test our site's accessibility. As a result, we improved the aria-label of some features. Our Lighthouse devtools test results for accessibility were as follows:

![Accessibility results](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/access.png)

#### HTML & CSS Validation

We used the official W3C Markup Validation Service to test our site's HTML and CSS. We found just five common errors on each page, and they were already solved. Therefore, the site shows the following results:

##### index.html and contact.html

![HTML validation](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/html.png)

#### GT-metrix Performance

After using GT-Metrix we realized that our site is doing quite well with an 88% in performance. We took their suggestions on improving cached files by adding our `.htaccess` with the necessary values.

![GT-metrix Result](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/gtmetrix.png)

#### CSS Validation

This test represents all the .css files `style.css`, `contact.css`, `swap.css` and `media.css` queries. Since we were constantly testing our CSS, the result was as follows:

![CSS Validation](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/css.png)

- Note: it does not mean the CSS is perfect.

#### Responsiveness

We ran manual tests on different devices to ensure that our media queries were working 100%. We made final improvements to it, and now we believe it's suitable for most screen sizes. Here is the insight shot:

![Responsive Mockup image](https://github.com/plexoio/tenam/blob/main/documentation/assets/img/responsive.png)


#### Security

Our site is semi-static, and we have used heavily Javascript, HTML, and CSS.

To improve security, we have added the `rel attribute` to compromising anchors such as social media links or third-party services, especially those with user-generated content.

Here are the values we have used as an example in action:

`rel="author noopener noreferrer nofollow"`


- **Author:** This value is used to indicate that the current document belongs to the linked author or is related to them. It is often used in blog posts or articles, where the author's name and a link to their bio or website is included.

- **Noopener:** This value prevents the new page from being able to access the `window.opener` property of the current page, not allowing a gap of access to both directions, the origin and destination, either could be malicious, which can help protect against malicious attacks.

- **Noreferrer:** This value instructs the browser not to send the Referer header (which includes a bunch of private data) to the linked page, which can help protect user privacy.

- **Nofollow:** This value tells search engines not to follow the link, which can help prevent spam and malicious links from affecting a website's search engine rankings. It tells the search engines or target system that the origin website mentions this link but does not endorse it, and it should not trust it or even mention it.

`Noopener` and `noreferrer` values are often used together to provide enhanced security and privacy when opening links in a new tab or window.

## Development Process <a name="development"></a> | [#](#index)

We created two `.html` pages, four `.css` files, and six `.js` files, along with a vendor folder, an assets folder, a documentation folder, a vendor folder, and an `.htaccess` file for improved caching. Additionally, we have a `README.md` file.

Throughout the development process, we utilized a user-centered design approach inspired by Jesse James Garrett. We focused on the problem rather than the solution on the `strategy` plane, determining what we wanted to build and preparing our scope.

Based on deadlines and available resources, we determined what we could accomplish on the `scope` plane. We created a minimum viable product (MVP) with some desired functionalities yet to be implemented. This first iteration serves as a presentation to showcase a Web3 financial web app, demonstrating to clients that the financial institution has started building a related product.

We put in extra effort to code better on the `structure` plane, defining content, folder distribution, user interactions, feature locations, and user navigation. We gave form to our ideas on the `skeleton` plane, designing our wireframe using Adobe XD, and deciding what could be improved and what was already fantastic.

We established colors, fonts, elements, and content on the `surface` plane, defining everything that users could see in the system. Each plane is related to the others, and the surface is the final projection of our work.

We faced several challenges during the planning, documentation, and coding processes, but with patience and perseverance, we found a solution for each one.

In future iterations, we plan to develop the `index` and `contact` pages further, particularly the `index` with the `Metamask Login`.

We are satisfied with our first iteration of tenam, as users learn about this emerging technology and the financial institution informs them about upcoming developments. Radical changes are not always positive, so building and deploying this project was an excellent idea.

## Future Implementations <a name="future"></a> | [#](#index)

We had a tight timeframe of only three weeks to build this MVP project using heavily Javascript, HTML, and CSS. We planned different features for this iteration, and we were able to accomplish the most important ones. However, there are several features that we were unable to include in this iteration, and we plan to include them in future iterations:

- `Welcome Page:` A feature to remember when users last clicked.

- `Fiat & Crypto Swap:` More interactivity with Javascript and connection to a backend server to handle database requests.

- `Contact page:` A more sophisticated page with Javascript interactions, DB connection, and style as seen on the wireframe.

- `Buy & Sell button:` We did not include this feature as expected and mentioned before. A proper feature should be added accordingly, along with backend development.

- `Captcha verification:` It's necessary to avoid spam. We plan to include it on the contact page and login page, and possibly on the welcome page as well.

- `Better SSL badge:` We planned to include a better SSL badge to demonstrate to users that they are not on a phishing website. Unfortunately, we were unable to include it in this iteration due to time constraints.

We look forward to including these features and more in future iterations of tenam.

## Deployment Process <a name="deployment"></a> | [#](#index)

We used Visual Studio, Git Bash, and GitHub for coding and version control, enabling us to deploy our product quickly once it was completed.

- We made sure to have secure backups of the site, not relying solely on the GitHub repository but also creating structured backups on external hard disks.

- We ensured from the outset that we were using industry-standard ways of structuring our directory and naming our files.

- We updated all directory references in the code, changing them from absolute to relative directories to ensure interoperability during deployment.

- We optimized images and code using tools such as W3C, a screen reader, and GT-matrix, testing the site on various devices.

- After confirming that the README.md was up to date, we opened GitHub Pages for our product. The setup process was straightforward:

1. Go to your repository.
2. Click on the settings button.
3. Go to the left navbar and select `Code and automation`.
4. Click on `Pages`.
5. Select `deploy from a branch`.
6. Choose `Branch` and then `/root`, and click on `Save`.
7. Wait for 1 to 5 minutes, then refresh your page.
8. On top of that section, you will see the link to your GitHub Pages.

In this way, we were able to deploy our project successfully with no major issues. For more information, please refer to the other sections and subsections of this README.md file.

<hr>

## Credits <a name="credits"></a> | [#](#index)

- **Brian O'Hare**: for mentoring me two times on this project. Without him, it would not have been possible with this tight timeframe.
- **[Metamask Login CDN](https://cdn.jsdelivr.net/npm/web3@1.5.2/dist/web3.min.js)**: for sharing to the public Metamask Web3 Login.
- **[Metamask Logo - codepen.io](https://codepen.io/shivammathur/pen/ZVJaEy)**: for provinding the Metamask Login Interactive Logo.
- **[Crypto Widget](https://www.cryptohopper.com/)**: for providing Crypto Widget on footer.
- [stackoverflow.com](https://stackoverflow.com/): for in-depth consultation and checking user-created content (from experienced developers) or human opinion.
- [google.com](https://google.com): for programming queries.
- [codeinstitute.net](https://codeinstitute.net/): for providing proper education, which knowledge is being applied throughout this project.
- [programminghub.io](https://programminghub.io/): where I learned the basics before joining Code Institute.
- [ChatGPT](https://chat.openai.com/chat), was used for the following queries:

1. Used for quick general consulting.
2. Used to convert a HTML code to a Markdown table for the README.md file. As seen from our extended self-coded versions: [strategy-table](https://github.com/plexoio/tenam/blob/main/documentation/extended-versions/strategy-table.html).
3. Copywriting and proofreading.
4. Used to validate HTML and styling codes.
5. Used to confirm whether or not my code snippet is correct after hours of self-debugging on `Javascript`.

**Note:** ChatGPT has given some false answers during some queries. We always need to question its answers.
- To all the websites and technologies used as seen in [Technologies Used](#technologies)

## Authors 

- [@plexoio](https://www.github.com/plexoio) | Frank Arellano