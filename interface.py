from flask import Flask, render_template
import json

app = Flask(__name__)


def load_odds():
    """Load odds data from ``odds.json`` if it exists."""
    try:
        with open("odds.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


@app.route("/")
def index():
    """Display the odds on a simple HTML page."""
    odds = load_odds()
    return render_template("index.html", odds=odds)


if __name__ == "__main__":
    app.run(debug=True)
