import time
from flask import Flask, render_template, request, jsonify

from utils.fetcher import fetch_website
from utils.extractor import extract_content
from utils.summarizer import summarize_content

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():

    try:

        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({
                "error": "Please enter a valid website URL."
            }), 400

        # Start timer
        start_time = time.time()

        # Fetch webpage HTML
        html = fetch_website(url)

        # Extract content, metadata and image
        page = extract_content(html)

        # Validate extracted text
        if len(page["text"]) < 100:
            return jsonify({
                "error": "Couldn't extract meaningful content from this website."
            }), 400

        # Generate AI summary
        summary = summarize_content(page["text"])

        # Add website image
        summary["image"] = page["image"]

        # Add backend-generated analytics
        summary["analysis"] = {
            "characters_processed": page["characters"],
            "processing_time": round(time.time() - start_time, 2),
            "model": "Gemini 2.5 Flash"
        }

        return jsonify(summary)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
