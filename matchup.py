from random import choice

encmat = [
    ["0", "0", "1/8", "1/4", "1/2", "1/2", "1/2", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4"],
    ["0", "1/8", "1/4", "1/4", "1/2", "1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "4", "4", "4", "5"],
    ["1/8", "1/4", "1/4", "1/2", "1", "1", "1", "2", "2", "2", "3", "3", "4", "4", "4", "4", "5", "5", "6", "6"],
    ["1/4", "1/2", "1/2", "1", "2", "2", "3", "3", "4", "4", "4", "5", "6", "6", "7", "7", "8", "8", "9", "10"],
    ["1/4", "1/2", "1", "2", "3", "3", "4", "4", "5", "5", "5", "6", "7", "7", "8", "8", "9", "9", "10", "11"],
    ["1/2", "1", "1", "2", "4", "4", "5", "5", "6", "7", "8", "8", "9", "9", "10", "11", "12", "12", "13", "14"],
    ["1/2", "1", "2", "3", "4", "4", "6", "7", "7", "8", "9", "10", "11", "11", "12", "12", "14", "14", "15", "16"],
    ["1", "2", "2", "3", "5", "6", "7", "7", "8", "9", "10", "11", "12", "13", "13", "14", "16", "16", "17", "18"],
    ["1", "2", "3", "4", "6", "7", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
]

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

def randmatch(partysize, lvl, base = 0):
    if partysize < 1:
        return []
    possibles = [k for k in range(base, 3)]
    possibles += [3, 3, 3]
    if partysize > 1:
        possibles += [4, 4]
    if partysize > 2:
        possibles += [5, 5]
    if partysize > 3:
        possibles += [6, 6]
    if partysize > 4:
        possibles += [7, 7]
    if partysize > 5:
        possibles += [8, 8]
    i = choice(possibles)
    cr = encmat[i][lvl-1]
    if i < 3:
        return [cr]*(4-i) + randmatch(partysize-1, lvl, base+1)
    else:
        return [cr] + randmatch(partysize+2-i, lvl, base)

def getMonsters(lst):
    monsterindx = {}
    result = []
    for cr in lst:
        if cr not in monsterindx:
            f = open("./monsterlists/" + cr.replace("/", "-") + ".txt")
            monsterindx[cr] = choice(f.readlines()).strip()
            f.close()
        result += [monsterindx[cr]]
    return result

def encounterEXP(encounter):
    return sum([EXP[cr] for cr in encounter])

def dungeonEXP(lvl):
    return EXP[str(lvl)]


if __name__ == "__main__":
    from treasure import encounterMoney
    # s = [0] * 24
    # for i in range(10000000):
    #     s[len(randmatch(6, 2)) - 1] += 1
    # print(s)
    s = 0
    c = 0
    while s < 1200:
        encounter = sorted(randmatch(4, 1), reverse = True)
        print(" ".join(encounter))
        print(", ".join(getMonsters(encounter)))
        e = sum([EXP[cr] for cr in encounter])
        print(e)
        s += e
        print(encounterMoney(encounter))
        print()
        c += 1
    print(s)
    print(c)
