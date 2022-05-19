import requests
import urllib3

BASE_URL = "https://127.0.0.1:2999/"
URL = "https://127.0.0.1:2999/liveclientdata/allgamedata"

# disable insecure warnings when calling the api
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# returns the live game data. assummes is_live() has been called
def get_data():
    response = requests.get(URL, verify=False)
    return response.json()

# check to make sure that player is in a live game.
def is_live():
    try:
        response = requests.get(URL, verify=False, timeout=0.1)
        if (response.json()["events"]["Events"][0]["EventName"] == "GameStart"):
            return True
        else:
            return False
    except:
        return False
