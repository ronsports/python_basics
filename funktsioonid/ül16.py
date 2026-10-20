def teisenda_sekundid(kokku_sekundid):
    tunnid = kokku_sekundid // 3600
    minutid = (kokku_sekundid % 3600) // 60
    sekundid = kokku_sekundid % 60
    return tunnid, minutid, sekundid

tulemus = teisenda_sekundid(3675)
print(tulemus)