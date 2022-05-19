# Collection of classes used by main program

# Stores the data of an item in player's inventory.
class Item:
    def __init__(self, item):
        self.name = item["displayName"]
        self.count = int(item["count"])
        self.is_consumable = item["consumable"]

# Stores the data of an ability
class Ability:
    def __init__(self, ability_data, key):
        self.key = key
        self.level = ability_data["abilityLevel"]
        self.name = ability_data["displayName"]

# loads different stats about the player champion
class Champion:
    def __init__(self, current_player, active_player):
        self.health = int(active_player["championStats"]["currentHealth"])
        self.max_health = int(active_player["championStats"]["maxHealth"])
        self.gold = int(active_player["currentGold"])
        self.level = int(active_player["level"])
        self.dead = current_player["isDead"]

# Save the scoreline of player
class Score:
    def __init__(self, score_data):
        self.kills = score_data["kills"]
        self.deaths = score_data["deaths"]
        self.assists = score_data["assists"]
