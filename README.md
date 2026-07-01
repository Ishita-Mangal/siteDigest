# Site Digest

## Overview

Site Digest is a web application that generates a structured summary, key takeaways and conclusion of any webpage from its URL.

The user enters a website URL. The application fetches the webpage, extracts meaningful content, sends it to the Gemini 2.5 Flash model for summarization, and displays the result in a structured and easy-to-read format.

The goal was to build a complete end-to-end application covering frontend, backend, content extraction, and LLM integration.

---

# Features

- Accepts any public website URL
- Extracts meaningful webpage content
- Generates an AI summary
- Shows:
  - TL;DR
  - Highlights
  - Audience
  - Intent
  - Recommended Next Action
  - Interesting Insight
  - Content Safety
  - Analysis Details
- Displays website preview image when available
- Handles invalid URLs and extraction failures

---

# Tech Stack

Frontend

- HTML
- CSS
- Vanilla JavaScript

Backend

- Flask (Python)

Content Extraction

- Requests
- BeautifulSoup

LLM

- Google Gemini 2.5 Flash

---

# Project Structure

```
site_digest/

│── app.py
│── requirements.txt
│── README.md
│── .env

│
├── static/
│   ├── style.css
│   └── script.js

│
├── templates/
│   └── index.html

│
└── utils/
    ├── fetcher.py
    ├── extractor.py
    └── summarizer.py
```

---

# How to Run

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# Known Limitations

- Some websites block automated scraping and return HTTP 403 errors.
- JavaScript-heavy websites may not expose meaningful HTML through a normal request.
- The application summarizes only one webpage instead of the complete website.
- AI-generated summaries may occasionally miss information or produce imperfect results.
- Some websites do not provide an Open Graph image.

# Error Handling

The application handles the following scenarios:

- Empty URL input
- Invalid URL format
- Website not reachable
- HTTP errors (403, 404, 500, etc.)
- No meaningful content extracted
- AI API errors
- Invalid JSON returned by the model
- Unexpected server errors

Meaningful error messages are shown to the user instead of crashing the application.

---

# Assumptions

- The user provides a publicly accessible website URL.
- The webpage contains enough textual content to summarize.
- The Gemini API is available and the API key is configured correctly.
- Internet connectivity is available for fetching webpages and calling the AI model.

---

# Security Considerations

Some basic precautions were considered:

- API keys are stored using environment variables.
- The frontend never exposes the API key.
- User input is validated before processing.
- HTML content is parsed as text and is not executed.

This is a prototype application and does not yet include production features such as rate limiting, authentication, or request logging.

---

# Testing

The application was manually tested on different types of websites including:

- Documentation websites
- Technology company websites
- Educational websites
- News websites
- Government websites

The following cases were also tested:

- Empty input
- Invalid URLs
- Unreachable websites
- Pages with limited content

---

# Future Improvements

If this were developed further, I would prioritize:

1. Better content extraction using Playwright for JavaScript-heavy websites.
2. Multi-page website crawling.
3. Response caching to reduce repeated API calls.
4. Streaming summaries for faster user feedback.
5. Automated testing for backend endpoints.
6. Logging and monitoring.
7. Better evaluation metrics for summary quality.
