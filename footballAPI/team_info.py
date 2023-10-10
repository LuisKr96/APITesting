import requests
import json
import csv
import os

print("Current directory" + os.getcwd())


def fetch_team_info(team_name, headers, url):
    querystring = {"name": team_name, "country": "England"}  # Including country parameter
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    if data["results"] > 0:
        team_data = data["response"][0]  # Assuming the first result is the correct one since we added the country parameter
        return team_data
    else:
        print(f"Error: could not find any information for {team_name}")
        return None

def process_csv_and_print_team_info(file_path, headers, url):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # get header row
        team_name_index = header.index("Team Name")  # get index of "Team Name" column
        for row in reader:
            team_name = row[team_name_index]
            team_data = fetch_team_info(team_name, headers, url)
            if team_data:
                team = team_data["team"]
                venue = team_data["venue"]
                print(f"Team name: {team['name']}")
                print(f"Country: {team['country']}")
                print(f"Year founded: {team['founded']}")
                print(f"Stadium name: {venue['name']}")
                print()


