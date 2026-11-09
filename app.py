# this is me
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Flask Application is Running Successfully."

@app.route("/about")
def about():
    return "Welcome to My Flask Application!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    if nne. kjndv
