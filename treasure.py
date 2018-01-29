from random import randrange, choice

level = {
"0": {"low": 1, "high": 10, "unit": "cp"},
"1/8": {"low": 2, "high": 20, "unit": "cp"},
"1/4": {"low": 4,"high": 40, "unit": "cp"},
"1/2": {"low": 6,"high": 60, "unit": "cp"},
"1": {"low": 8,"high": 80, "unit": "cp"},
"2": {"low": 1,"high": 10, "unit": "sp"},
"3": {"low": 2,"high": 20, "unit": "sp"},
"4": {"low": 4,"high": 40, "unit": "sp"},
"5": {"low": 6,"high": 60, "unit": "sp"},
"6": {"low": 8,"high": 80, "unit": "sp"},
"7": {"low": 2,"high": 20, "unit": "ep"},
"8": {"low": 4,"high": 40, "unit": "ep"},
"9": {"low": 8,"high": 80, "unit": "ep"},
"10": {"low": 12,"high": 120, "unit": "ep"},
"11": {"low": 16,"high": 160, "unit": "ep"},
"12": {"low": 10,"high": 100, "unit": "gp"},
"13": {"low": 20,"high": 200, "unit": "gp"},
"14": {"low": 40,"high": 400, "unit": "gp"},
"15": {"low": 60,"high": 600, "unit": "gp"},
"16": {"low": 80,"high": 800, "unit": "gp"},
"17": {"low": 10,"high": 100, "unit": "pp"},
"18": {"low": 20,"high": 200, "unit": "pp"},
"19": {"low": 40,"high": 400, "unit": "pp"},
"20": {"low": 60,"high": 600, "unit": "pp"}
}

hoard = [
[{"low": 500, "high": 5000,"unit": "cp"}, {"low": 150,"high": 1500,"unit": "sp"}, {"low": 15,"high": 100,"unit": "gp"}],
[{"low": 1000,"high": 10000,"unit": "cp"}, {"low": 300,"high": 3000,"unit": "sp"}, {"low": 30,"high": 200,"unit": "gp"}],
[{"low": 2000, "high": 20000,"unit": "cp"}, {"low": 600,"high": 6000,"unit": "sp"}, {"low": 60,"high": 400,"unit": "gp"}],
[{"low": 4000, "high": 40000,"unit": "cp"}, {"low": 1200,"high": 12000,"unit": "sp"}, {"low": 120,"high": 800,"unit": "gp"}],
[{"low": 8000, "high": 80000,"unit": "cp"}, {"low": 2400,"high": 24000,"unit": "sp"}, {"low": 240,"high": 1600,"unit": "gp"}],
[{"low": 1000, "high": 10000,"unit": "cp"}, {"low": 400,"high": 4000,"unit": "sp"}, {"low": 400,"high": 3000,"unit": "gp"}, {"low": 50, "high": 500, "unit": "pp"}],
[{"low": 1500, "high": 15000,"unit": "cp"}, {"low": 600,"high": 6000,"unit": "sp"}, {"low": 600,"high": 4500,"unit": "gp"}, {"low": 100, "high": 1000, "unit": "pp"}],
[{"low": 2500, "high": 25000,"unit": "cp"}, {"low": 800,"high": 8000,"unit": "sp"}, {"low": 900,"high": 6000,"unit": "gp"}, {"low": 150, "high": 1500, "unit": "pp"}],
[{"low": 4000, "high": 40000,"unit": "cp"}, {"low": 1000,"high": 10000,"unit": "sp"}, {"low": 1100,"high": 8000,"unit": "gp"}, {"low": 250, "high": 2500, "unit": "pp"}],
[{"low": 6000, "high": 60000,"unit": "cp"}, {"low": 2000,"high": 20000,"unit": "sp"}, {"low": 2000,"high": 10000,"unit": "gp"}, {"low": 400, "high": 4000, "unit": "pp"}],
[{"low": 8000, "high": 80000,"unit": "cp"}, {"low": 4000,"high": 40000,"unit": "sp"}, {"low": 4000,"high": 15000,"unit": "gp"}, {"low": 600, "high": 6000, "unit": "pp"}],
[{"low": 10000, "high": 100000,"unit": "cp"}, {"low": 6000,"high": 60000,"unit": "sp"}, {"low": 6000,"high": 30000,"unit": "gp"}, {"low": 800, "high": 8000, "unit": "pp"}],
[{"low": 15000, "high": 150000,"unit": "cp"}, {"low": 8000,"high": 80000,"unit": "sp"}, {"low": 8000,"high": 60000,"unit": "gp"}, {"low": 1000, "high": 10000, "unit": "pp"}],
[{"low": 25000, "high": 250000,"unit": "cp"}, {"low": 10000,"high": 100000,"unit": "sp"}, {"low": 10000,"high": 80000,"unit": "gp"}, {"low": 1500, "high": 15000, "unit": "pp"}],
[{"low": 40000, "high": 400000,"unit": "cp"}, {"low": 15000,"high": 150000,"unit": "sp"}, {"low": 15000,"high": 100000,"unit": "gp"}, {"low": 2500, "high": 25000, "unit": "pp"}],
[{"low": 60000, "high": 600000,"unit": "cp"}, {"low": 25000,"high": 250000,"unit": "sp"}, {"low": 25000,"high": 150000,"unit": "gp"}, {"low": 4000, "high": 40000, "unit": "pp"}],
[{"low": 80000, "high": 800000,"unit": "cp"}, {"low": 40000,"high": 400000,"unit": "sp"}, {"low": 40000,"high": 250000,"unit": "gp"}, {"low": 6000, "high": 60000, "unit": "pp"}],
[{"low": 100000, "high": 1000000,"unit": "cp"}, {"low": 60000,"high": 600000,"unit": "sp"}, {"low": 60000,"high": 400000,"unit": "gp"}, {"low": 8000, "high": 80000, "unit": "pp"}],
[{"low": 150000, "high": 1500000,"unit": "cp"}, {"low": 80000,"high": 800000,"unit": "sp"}, {"low": 80000,"high": 600000,"unit": "gp"}, {"low": 10000, "high": 100000, "unit": "pp"}],
[{"low": 250000, "high": 2500000,"unit": "cp"}, {"low": 100000,"high": 1000000,"unit": "sp"}, {"low": 100000,"high": 800000,"unit": "gp"}, {"low": 15000, "high": 150000, "unit": "pp"}]
]

def encounterMoney(lst):
    money = {}
    for cr in lst:
        if level[cr]["unit"] in money:
            money[level[cr]["unit"]] = money[level[cr]["unit"]] + randrange(level[cr]["low"], level[cr]["high"]+1)
        else:
            money[level[cr]["unit"]] = randrange(level[cr]["low"], level[cr]["high"]+1)
    return money

def getHoard(lvl):
    money = {}
    for table in hoard[lvl-1]:
        money[table["unit"]] = randrange(table["low"], table["high"])
    treasure = {
        "A": randrange(lvl+1),
        "B": randrange(((2*lvl)//3)+1),
        "C": randrange(lvl//2 + 1),
        "D": randrange(((2*lvl)//5)+1),
        "E": randrange(lvl//3 + 1),
        "F": randrange(lvl//2 + 1),
        "G": randrange(lvl//3 + 1),
        "H": randrange(lvl//4 + 1),
        "I": randrange(lvl//5 + 1),
    }
    treasure = [(k, treasure[k]) for k in treasure if treasure[k] > 0]
    if len(treasure) > 0:
        treasure = choice(treasure)
    else:
        treasure = ("", 0)
    return {"money": money, "magic": treasure}

if __name__ == "__main__":
    # print(encounterMoney(["0", "0", "1/8", "1/8"]))
    print(getHoard(7))
