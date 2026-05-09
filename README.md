# Interview Question Generator

A clean, AI-powered web app that generates 3 tailored interview questions for any job title.

Built with Flask and the Anthropic Claude API.

## Live Demo

[Link added after deployment]

## Stack

- **Backend:** Python / Flask
- **AI:** Anthropic Claude (claude-sonnet-4-20250514)
- **Frontend:** Vanilla HTML / CSS / JS
- **Hosting:** Render

## Local Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your Anthropic API key:
   ```bash
   cp .env.example .env
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Visit `http://localhost:5000`

## Design Decisions

- **Flask backend:** Keeps the API key server-side and never exposed to the browser
- **Claude Sonnet:** Chosen for its strong instruction-following and JSON output reliability
- **Structured prompt:** Requests a strict JSON array so parsing is reliable and error handling is clean
- **Vanilla JS:** No framework overhead — the app is simple enough that React would be overkill
- **Loading state:** Spinner with descriptive message so the user knows the API call is in progress

## Author

Victor Chukwuemeka — [vickkykruzprogramming.dev](https://vickkykruzprogramming.dev)
