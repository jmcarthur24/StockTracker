# Stock Price Tracker and News Web Application

### Team Members

- John McArthur

## 1. Project Overview

The Stock Price Tracker is a web application designed to provide users with real-time stock price data, historical price trends, and the latest news about their favorite stocks. Users can add stocks to a their list of favorites, view stock charts about price, and read relevant news articles about different stocks.

## 2. Usage Guidelines

1. Add Stocks:
   - Enter a stock ticker symbol (like "AAPL" for Apple) into the input box and click the "Add" button. The stock will be added to your list of favorites.
2. View Details:
   - Click on a stock ticker symbol in the favorites list to view a detailed chart of the stock's historical performance and the latest news articles about the stock.
3. Remove Stocks:
   - Click the "Remove" button next to a stock in your Favorites List to remove it from the Favorites List.
4. Navigate:
   - Use the "Back to Favorites" link on the stock details page to return to the main favorites page.

## 3. Dependencies

The project uses the following external libraries, APIs, and tools:

- Flask: Backend web framework.
- SQLite3: Database for storing user favorite stocks.
- Jinja2: Template engine for HTML.
- yFinance: Library for stock data retrieval.
- NewsAPI: API for finding the latest news articles.
- Chart.js: Library for displaying interactive stock charts.
- Requests: For making HTTP requests to external APIs.

## 4. Project Structure

The main.py file handles backend logic, including routing, handling databases, and API integrations. The instance folder contains the database.db SQLite file to store user favorites. The templates directory includes index.html for the home page and managing favorites and details.html for displaying stock charts and news. The static folder has style.css for styling the page, chart.js for interactive charts, and script.js for JavaScript functionality. The README.md provides project documentation, summarizing the project progression and its components. This organization helps keep all the files separated for easy use.

## 5. Collaboration Information

I completed this project by myself.

## 6. Acknowledgments

A thank you to the following resources and tools used in my project:

- Yahoo Finance API (via yFinance): for real-time stock data.
- NewsAPI: for providing relevant and up-to-date news articles.
- Flask Documentation: for clear and concise guides.
- ChatGPT: for assisting with troubleshooting, refining ideas and code, and brainstorming.

## 7. Reflection

### What Went Well

- The integration of multiple APIs (yFinance and NewsAPI) provided a dynamic and functional application.
- Implementing charts made the stock data page visually appealing and more interactive.
- The user-friendly design ensures smooth navigation and engagement with the app.
- Leveraging Flask allowed for rapid and efficient backend development.
- This project aligns with my interests and studies, making the process engaging and interesting.

### Challenges

- Filtering articles in other languages using the NewsAPI took me a while at first but I eventually figured it out to get just the articles in english.
- Handling JSON data conversion for displaying charts required understanding both Jinja2 and JavaScript integration.
- Debugging issues like variable errors were very time consuming but it felt great to figure out and solve them.

### Learning Outcomes

- I deepened my understanding of API integration and JSON data handling.
- Improved skills in combining Python, JavaScript, and CSS to build web applications.
- Gained valuable insights into managing scope and addressing compatibility issues.

### Future Improvements

- Add more features like stock comparisons, more historical data like financial ratios, or a dashboard summarizing market trends.
- Enhance the application further with animations and advanced interactivity.
