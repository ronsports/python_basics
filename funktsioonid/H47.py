def keskmine(punktid):
    if len(punktid) == 0:
        return 0
    return sum(punktid) / len(punktid)

def parim_tulemus(punktid):
    if len(punktid) == 0:
        return None
    parim = punktid[0]
    for p in punktid:
        if p > parim:
            parim = p
    return parim

def norgim_tulemus(punktid):
    if len(punktid) == 0:
        return None
    norgim = punktid[0]
    for p in punktid:
        if p < norgim:
            norgim = p
    return norgim

def edukate_arv(punktid, piir=50):
    loendur = 0
    for p in punktid:
        if p >= piir:
            loendur = loendur + 1
    return loendur

punktid = [78, 45, 92, 67, 34, 100, 56, 81]

print(f"Keskmine punktisumma: {keskmine(punktid):.1f}")
print(f"Parim tulemus: {parim_tulemus(punktid)}")
print(f"Nõrgim tulemus: {norgim_tulemus(punktid)}")
print(f"Edukate õpilaste arv (vähemalt 50 punkti): {edukate_arv(punktid)}")
print(f"Väga edukate õpilaste arv (vähemalt 80 punkti): {edukate_arv(punktid, piir=80)}")
