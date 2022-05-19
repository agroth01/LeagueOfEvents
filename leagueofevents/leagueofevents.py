from leagueofevents import api, events
from leagueofevents.helpers import Ability, Item, Champion, Score
import threading

# wrapper class to store and compare player data
class Player:
    def __init__(self, game_data):
        self.game_data = game_data

        self.summoner_name = self.game_data["activePlayer"]["summonerName"]
        self.abilities = self._load_abilities()
        self.score = self._load_score()
        self.champion = self._load_champion_stats()
        self.items = self._load_items()

    # looks through the player list to find local player
    def _get_current_player(self):
        for player in self.game_data["allPlayers"]:
            if (player["summonerName"] == self.summoner_name):
                return player

    # returns a list of all the abilities player has with their level
    def _load_abilities(self):
        abilities = []
        for ability in self.game_data["activePlayer"]["abilities"]:
            if (ability != "Passive"):
                abilities.append(Ability(self.game_data["activePlayer"]["abilities"][ability], ability))
        return abilities

    # returns instance of score class
    def _load_score(self):
        scores = self._get_current_player()["scores"]
        return Score(scores)

    # returns an instance of the champion class
    def _load_champion_stats(self):
        active = self.game_data["activePlayer"]
        current = self._get_current_player()
        return Champion(current, active)

    # returns a list of all items in inventory
    def _load_items(self):
        items = []
        for item in self._get_current_player()["items"]:
            items.append(Item(item))
        return items

# main method for user.
# registers the callback function when event type specified is called
def subscribe_to_event(event_type, callback):
    events.register_event(event_type, callback)

# takes in two player objects as argument and evaluates difference.
# will call event if requirements are met
def compare_player(new, old):
    # HEALTH
    health_difference = new.champion.health - old.champion.health
    if (health_difference != 0):
        # prevent event from getting called when max health changes
        if (new.champion.max_health == old.champion.max_health):
            if (health_difference > 0):
                events.call_event("onHealthIncrease", health_difference)
            elif (health_difference < 0):
                events.call_event("onHealthDecrease", health_difference)

    # KILL
    if (new.score.kills != old.score.kills):
        events.call_event("onKill")

    # DEATH
    if (new.score.deaths != old.score.deaths):
        events.call_event("onDeath")

    # ASSIST
    if (new.score.assists != old.score.assists):
        events.call_event("onAssist")

    # RESPAWN
    if (new.champion.dead != old.champion.dead):
        if (new.champion.dead == False):
            events.call_event("onRespawn")

    # LEVEL UP
    if (new.champion.level != old.champion.level):
        events.call_event("onLevelUp")

    # GOLD
    gold_difference = new.champion.gold - old.champion.gold
    if (gold_difference > 0):
        events.call_event("onGoldGain", gold_difference)
    elif (gold_difference < 0):
        events.call_event("onGoldLost", gold_difference)

    # ABILITIES
    for i, ability in enumerate(new.abilities):
        if (ability.level != old.abilities[i].level):
            events.call_event("onAbilityLevelUp", ability)

    # ITEMS
    # create list of all old item names
    old_items = []
    for item in old.items:
        old_items.append(item.name)

    # new item names
    new_items = []
    for item in new.items:
        new_items.append(item.name)

    # check for items
    for item in new.items:
        if not (item.name in old_items):
            events.call_event("onItemAdded", item.name)

    for item in old.items:
        if not (item.name in new_items):
            events.call_event("onItemRemoved", item.name)

# primary loop for checking for events
def main_loop():
    # determine if player is already in a game
    in_game = api.is_live()

    # initialize player if already in game
    old_player = None
    if (in_game):
        old_player = Player(api.get_data())

    while True:
        # only proceed if there is a live game going on
        if api.is_live():
            # when player disconnects, it might take a second for it to realize.
            # wrapping in try function should prevent errors when disconnecting
            try:
                # take a snapshot of the current player
                player = Player(api.get_data())
            except Exception as e:
                continue

            # check if player just joined the game
            if not (in_game):
                old_player = player
                events.call_event("onGameJoin")

                # update ingame status
                in_game = True
                continue

            # compare the current player stats against cached player stats
            compare_player(player, old_player)

            # cache the current player for next update
            old_player = player

        else:
            if (in_game == True):
                events.call_event("onGameLeave")

            in_game = False



if __name__ == '__main__':
    loop = threading.Thread(target=main_loop)
    loop.start()

else:
    loop = threading.Thread(target=main_loop)
    loop.start()
