#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# pip3 install fortnite-python


from dataclasses import dataclass
from fortnite_python import Fortnite
from fortnite_python.domain import Platform
from fortnite_python.domain import Mode

@dataclass
class Player:
  kills: int = 0
  wins: int = 0


magnus = Player()
noah = Player()
adam = Player()

# api key 302de567-30de-4c7f-9051-ecf44d843c08 from https://fortnitetracker.com/site-api
fortnite = Fortnite('302de567-30de-4c7f-9051-ecf44d843c08')

player = fortnite.player('weyhe', Platform.PSN)

solo = player.getStats(Mode.SOLO)
duo  = player.getStats(Mode.DUO)
squad = player.getStats(Mode.SQUAD)

magnus.wins = int(solo.wins) + int(duo.wins) + int(squad.wins)
magnus.kills = int(solo.kills) + int(duo.kills) + int(squad.kills)


player = fortnite.player('noahcb2007', Platform.PSN)

solo = player.getStats(Mode.SOLO)
duo  = player.getStats(Mode.DUO)
squad = player.getStats(Mode.SQUAD)

noah.kills = int(solo.kills) + int(duo.kills) + int(squad.kills)
noah.wins = int(solo.wins) + int(duo.wins) + int(squad.wins)

player = fortnite.player('2 kills adam', Platform.PC)

solo = player.getStats(Mode.SOLO)
duo  = player.getStats(Mode.DUO)
squad = player.getStats(Mode.SQUAD)

adam.wins = int(solo.wins) + int(duo.wins) + int(squad.wins)
adam.kills= int(solo.kills) + int(duo.kills) + int(squad.kills)

print("Noah Kills   :", noah.kills)
print("Noah Wins    :", noah.wins)
print("Magnus Kills :", magnus.kills)
print("Magnus Wins  :", magnus.wins)
print("Adam Kills   :", adam.kills)
print("Adam Wins    :", adam.wins)


