import requests
import json
api_url = "http://212.132.108.197:8000/ranking/game"

import asyncio
import requests

player = "none"
wins = 0
losses = 0


async def send_game_data():
    # Create the game data
    game = {
        "player": player,
        "wins": wins,
        "losses": losses
    }

    try:
        # Make the POST request to the API
        response = requests.post("http://212.132.108.197:8000/ranking/game", json=game)

        # Check the response status
        if response.status_code == 200:
            print("Game posted successfully")
        else:
            print(f"Could not post game: {response.status_code}")
    except Exception as e:
        print(f"Failed to post game: {e}")

# Main function to run the async task
async def main():
    await send_game_data()

# Run the main function
asyncio.run(main())



# response = requests.post(api_url, game)
# print(response)
