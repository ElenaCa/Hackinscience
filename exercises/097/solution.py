banane = []
def love_meet(bob, alice):
    for i in alice:
        for j in bob:
            if i == j:
                if i not in banane:
                    banane.append(i)
    return banane

def affair_meet(bob, alice, silvester):
    for i in alice:
        for j in bob:
            for k in silvester:
                if i == k:
                    if i != j:
                        if i not in banane:
                            banane.append(i)
    return banane
