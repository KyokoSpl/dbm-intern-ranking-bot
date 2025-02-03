import requests

import json


def send_game_data(player_id: int, wins: int, loses: int):
    # Create the game data
    # fighter_id_1: int,
    game = {
        "player_id": player_id,
        # "fighter_id_1": fighter_id_1,
        "wins": wins,
        "loses": loses,
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


def add_player(player_id: int, name: str):
    player = {
        "id": player_id,
        "player_name": name,
    }
    try:
        response = requests.post("http://localhost:8000/ranking/addplayer", json=player)
        if response.status_code == 200:
            print("Player added successfully")
        else:
            print(f"Could not add player: {response.status_code}")
    except Exception as e:
        print(f"Failed to add player: {e}")


def delete_player(player_id: int):
    player = {
        "id": player_id,
    }
    try:
        response = requests.delete(
            "http://localhost:8000/ranking/deleteplayer", json=player
        )
        if response.status_code == 200:
            print("Player deleted successfully")
        else:
            print(f"Could not delete player: {response.status_code}")
    except Exception as e:
        print(f"Failed to delete player: {e}")


def del_game(id: int):
    game = {
        "id": id,
    }
    try:
        response = requests.delete("http://localhost:8000/ranking/delgame", json=game)
        if response.status_code == 200:
            print("Game deleted successfully")
        else:
            print(f"Could not delete game: {response.status_code}")
    except Exception as e:
        print(f"Failed to delete game: {e}")


# Main function to run the async task

# response = requests.post(api_url, game)
# print(response)
