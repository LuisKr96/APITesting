import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

# Names of the top 5 leagues
league_names = ["La Liga", "Serie A", "Bundesliga", "Premier League", "Ligue 1"]

with open("config.json", "r") as f:
    config = json.load(f)

rapidapi_key = config["RAPIDAPI_KEY"]

headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

for league_name in league_names:
    querystring = {"name": league_name}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if data["results"] > 0:
        for league in data["response"]:
            if league["league"]["name"] == league_name:
                league_id = league["league"]["id"]
                print(f"{league_name}: {league_id}")
                break
    else:
        print(f"Error: could not find ID for {league_name}")