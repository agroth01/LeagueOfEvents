League Of Events
================

Create custom callbacks to various in game events made possible with the League Client API

## Installing

Install the [PyPI Package](https://github.com/agroth01/LeagueOfEvents):

    pip install leagueofevents

# Examples

```py
import leagueofevents

def my_death_function():
    print("oh shucks! I died :(")

def ability_level_up(ability):
    print(f"The ability {ability.name} is now level {ability.level}!")

leagueofevents.subscribe_to_event("onDeath", my_death_function)
leagueofevents.subscribe_to_event("onAbilityLevelUp", ability_level_up)
```
