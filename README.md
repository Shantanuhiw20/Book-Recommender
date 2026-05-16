# Book Recommender

A simple Flask-based book recommendation web application powered by precomputed collaborative similarity data.

## Overview

This project serves a lightweight book recommendation app that uses saved model artifacts to suggest books based on a user-selected title. It includes:

- A homepage showing the top 50 popular books.
- A search interface to enter a book title and fetch similar recommendations.
- A clean Tailwind CSS-powered frontend with a dark theme and animated visual effects.

## Features

- Displays popular books with cover image, author, votes, and rating.
- Accepts a book title and returns up to 6 similar book recommendations.
- Handles missing titles gracefully with an error message.
- Deployable via `gunicorn` using the provided `Procfile`.

## Files

- `app.py` – Flask application with routes for home, recommendation UI, and recommendation results.
- `templates/index.html` – Homepage template for displaying popular books.
- `templates/recommend.html` – Recommendation search page and result display.
- `requirements.txt` – Python dependencies for Flask, NumPy, Pandas, and Gunicorn.
- `Procfile` – Deployment entrypoint for Heroku-like platforms.
- `popular.pkl`, `pt.pkl`, `books.pkl`, `similarity_score.pkl` – Precomputed data files used by the recommender.

## Installation

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Locally

Start the Flask app:

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

## Deployment

The app is ready to deploy with Gunicorn via the `Procfile`:

```bash
gunicorn app:app
```

## Usage

- Visit the homepage to browse the top 50 recommended books.
- Navigate to `/recommend` to search for similar books by title.
- Enter any book title in the dataset to receive up to 6 recommendations.

