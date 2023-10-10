import requests
import csv
import json


url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"

querystring = {"league":"39","season":"2021"}

with open("config.json", "r") as f:
    config = json.load(f)

rapidapi_key = config["RAPIDAPI_KEY"]

headers = {
	"X-RapidAPI-Key": rapidapi_key,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
# Extracting the 'response' key which contains the list of players.
players = data.get('response', [])

# Write to CSV
with open('top_scorers.csv', 'w', newline='') as csvfile:
    fieldnames = ['player_name', 'team', 'goals_total', 'assists', 'appearences', 'minutes_played']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for player_data in players:
        player = player_data['player']
        stats = player_data['statistics'][0]
        games = stats['games']
        goals = stats['goals']
        
        writer.writerow({
            'player_name': player['name'],
            'team': stats['team']['name'],
            'goals_total': goals['total'],
            'assists': goals['assists'],
            'appearences': games['appearences'],
            'minutes_played': games['minutes']
        })

print("Data written to top_scorers.csv")