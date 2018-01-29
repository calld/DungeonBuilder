from random import choice

skills = [
"Acrobatics",
"Animal Handling",
"Arcana",
"Athletics",
"Deception",
"History",
"Insight",
"Intimidation",
"Investigation",
"Medicine",
"Nature",
"Performance",
"Persuasion",
"Religion",
"Sleight of Hand",
"Survival"
]

DC = {
"0": 8,
"1/8": 9,
"1/4": 10,
"1/2": 11,
"1": 12,
"2": 13,
"3": 14,
"4": 14,
"5": 15,
"6": 16,
"7": 16,
"8": 17,
"9": 18,
"10": 18,
"11": 19,
"12": 20,
"13": 20,
"14": 21,
"15": 22,
"16": 22,
"17": 23,
"18": 24,
"19": 24,
"20": 25
}

EXP = {
"0": 10,
"1/8": 25,
"1/4": 50,
"1/2": 100,
"1": 200,
"2": 450,
"3": 700,
"4": 1100,
"5": 1800,
"6": 2300,
"7": 2900,
"8": 3900,
"9": 5000,
"10": 5900,
"11": 7200,
"12": 8400,
"13": 10000,
"14": 11500,
"15": 13000,
"16": 15000,
"17": 18000,
"18": 20000,
"19": 22000,
"20": 25000
}

def challenge(matchup):
    return {"SEQ": matchup,
            "EXP": sum([EXP[cr] for cr in matchup]),
            "checks": [{"skill": choice(skills), "DC": DC[cr]} for cr in matchup]}

def challengeprint(chllng):
    for ch in chllng["checks"]:
        print(ch)
    print("EXP: ", chllng["EXP"])

if __name__ == "__main__":
    from matchup import randmatch
    from treasure import encounterMoney
    encounter = randmatch(4, 2)
    challengeprint(challenge(encounter))
    print(encounterMoney(encounter))
