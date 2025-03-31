
import requests
import json

url = "https://www.thesportsdb.com/api/v1/json/3/lookuptable.php?l=4457&s=2025"
# Free API key
api_key = "3"

headers = {
    "X-API-KEY": f"{api_key}",
    "Content-Type": "application/json"
}

def getTable():
    response = requests.get(url, headers = headers)

    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")

    json_data = json.dumps(response.json(),indent=4)
    data = json.loads(json_data)

    table = []
    for team in data["table"]:
        lag = {
            "team": team["strTeam"],
            "description": team["strDescription"],
            "played": team["intPlayed"],
            "wins": team["intWin"],
            "draws": team["intDraw"],
            "losses": team["intLoss"],
            "goals_for": team["intGoalsFor"],
            "goals_against": team["intGoalsAgainst"],
            "points": team["intPoints"]
        }
        table.append(lag)
    return table
