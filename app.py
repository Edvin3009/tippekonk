
from flask import Flask, jsonify, render_template
import api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/league-data")
def league_data():
    return jsonify(api.getTable())

if __name__ == "__main__":
    app.run(debug=True)