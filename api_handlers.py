import requests
import json


def send_game_data(player: str, fighter_id_1: int, wins: int, loses: int):
    # Create the game data
    game = {
        "player": player,
        "fighter_id_1": fighter_id_1,
        "wins": wins,
        "loses": loses
    }

    try:
        # Make the POST request to the API
        response = requests.post("http://localhost:8000/ranking/game", json=game)

        # Check the response status
        if response.status_code == 200:
            print("Game posted successfully")
        else:
            print(f"Could not post game: {response.status_code}")
    except Exception as e:
        print(f"Failed to post game: {e}")

# Main function to run the async task

# response = requests.post(api_url, game)
# print(response)