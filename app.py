
from flask import Flask, jsonify, render_template
# import json
import api, point_logic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/league-data")
def league_data():
    return jsonify(api.getTable())

@app.route("/contestants")
def contestants():
    # with open('contestants.json', encoding='utf8') as f:
    #     contestants = json.load(f)
    return jsonify(point_logic.get_contestants_data())

if __name__ == "__main__":
    app.run(debug=True)