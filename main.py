import sqlite3
from contextlib import contextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import yfinance as yf
import requests

# FastAPI initialization
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database configuration
INSTANCE_PATH = Path("instance")
INSTANCE_PATH.mkdir(exist_ok=True)
DATABASE = INSTANCE_PATH / "database.db"


def init_db():
    """
    Initialize the SQLite database for the application. Creates a "favorites" table if it does not already exist,
    storing user's favorite stocks.
    """
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT NOT NULL
            )
            """
        )
        db.commit()


@contextmanager
def get_db():
    """
    Provide a connection to the SQLite database.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def fetch_stock_news(ticker):
    """
    Fetch the latest news articles related to a stock ticker.
    """
    API_KEY = "8c86d719df9c4118930ab73c1a81b7d1"  # Your API key
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return [
            {"title": article["title"], "url": article["url"]}
            for article in articles[:5]
        ]
    else:
        return [{"title": "No news found", "url": "#"}]


@app.get("/")
async def index(request: Request):
    """
    Display the main page with a list of favorite stocks. Fetches favorite stock tickers from the database, retrieves their latest prices using yFinance, and renders the "index.html" template.
    """
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM favorites")
        favorites = cursor.fetchall()
        favorite_stocks = []
        for favorite in favorites:
            ticker = favorite["ticker"]
            try:
                stock = yf.Ticker(ticker)
                price = stock.history(period="1d")["Close"].iloc[-1]
                favorite_stocks.append({"ticker": ticker, "price": round(price, 2)})
            except Exception:
                favorite_stocks.append({"ticker": ticker, "price": "N/A"})

        return templates.TemplateResponse(
            "index.html", {"request": request, "favorite_stocks": favorite_stocks}
        )


@app.post("/add_favorite")
async def add_favorite(ticker: str = Form(...)):
    """
    Add a stock ticker to the user's list of favorites.
    """
    ticker = ticker.upper()
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO favorites (ticker) VALUES (?)", (ticker,))
        db.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/remove_favorite")
async def remove_favorite(ticker: str = Form(...)):
    """
    Remove a stock ticker from the user's list of favorites.
    """
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM favorites WHERE ticker = ?", (ticker,))
        db.commit()
    return RedirectResponse(url="/", status_code=303)


@app.get("/details/{ticker}")
async def stock_details(ticker: str, request: Request):
    """
    Display information about a stock.
    """
    stock = yf.Ticker(ticker)
    history = stock.history(period="1mo").reset_index()

    news = fetch_stock_news(ticker)

    details = {
        "ticker": ticker,
        "dates": history["Date"].dt.strftime("%Y-%m-%d").tolist(),
        "prices": history["Close"].fillna(0).tolist(),
        "news": news,
    }
    return templates.TemplateResponse(
        "details.html", {"request": request, "details": details}
    )


# Initialize the database
init_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
