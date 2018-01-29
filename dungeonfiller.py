from matchup import randmatch, getMonsters, encounterEXP, dungeonEXP
from noncombat import challenge
from treasure import encounterMoney, getHoard
from random import randrange

import argparse

parser = argparse.ArgumentParser(description="builds full list of dungeon encounters based on average player lvl")
parser.add_argument('lvl', type=int, choices=range(1, 21), help="lvl of the player characters")
parser.add_argument('--size', "-s", type=int, default=5, help="number of encounters to generate")
parser.add_argument('--party', '-p', type=int, default=4, help="number of people in the party")

args = parser.parse_args()

for i in range(args.size):
    encounter = sorted(randmatch(args.party, args.lvl), reverse = True)
    j = randrange(5)
    if j < 4:
        #print(*encounter)
        print(f"{chr(ord('A')+i)}:", ", ".join(getMonsters(encounter)))
        print(encounterEXP(encounter))
        print(encounterMoney(encounter))
        print()
    else:
        ch = challenge(encounter)
        print(f"{chr(ord('A')+i)}:", ", ".join([f'{c["skill"]} ({c["DC"]})' for c in ch['checks']]))
        print(ch['EXP'])
        print(encounterMoney(encounter))
        print()

print("Hoard:")
print(getHoard(args.lvl))
print(dungeonEXP(args.lvl))
