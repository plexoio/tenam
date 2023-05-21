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
