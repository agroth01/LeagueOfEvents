League Of Events
================

Create custom callbacks to various in game events made possible with the League Client API

## Installing

Install the [PyPI Package](https://github.com/agroth01/LeagueOfEvents):

    pip install leagueofevents

## Examples
Basic example:
```py
import leagueofevents

def my_death_function():
    print("oh shucks! I died :(")

def ability_level_up(ability):
    print(f"The ability {ability.name} is now level {ability.level}!")

leagueofevents.subscribe_to_event("onDeath", my_death_function)
leagueofevents.subscribe_to_event("onAbilityLevelUp", ability_level_up)
```

# Events

## onKill
> Called when the player gets a kill

    Returns: Nothing
    

## onDeath
> Called when the player dies

    Returns: Nothing
    

## onAssist
> Called when the player gets an assist

    Returns: Nothing
    

## onLevelUp
> Called when the player levels up

    Returns: Nothing
    

## onGoldGain
> Called when the player gains gold

    Returns: (int)Gold gained
    

## onGoldLost
> Called when the player loses gold

    Returns: (int)Gold lost
    
## onRespawn
> Called when the player respawns

    Returns: Nothing
    
## onAbilityLevelUp
> Called when the player levels up an ability
    
    Returns: Ability
    ```py
    ability.name
    ability.level
    ability.key
    ```
    
## onItemAdded
> Called when the player gets a new item in their inventory
    
    Returns: Item
    ```py
    item.name
    item.count
    item.is_consumable
    ```
 
## onItemRemoved
> Called when the player removes a item from their inventory
    
    Returns: Item
    ```py
    item.name
    item.count
    item.is_consumable
    ```

## onGameJoin
> Called when the player first joins a game

    Returns: Nothing
    

## onGameLeave
> Called when the player leaves a game

    Returns: Nothing
