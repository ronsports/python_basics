summa = 0
paevi = 0
yle_15_paevi = 0

pikim_paev = None
korgeim_temp = -999

kylmim_paev = None
madalaim_temp = 999

with open("temperatuurid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 2:
            paev = osad[0]
            temp = int(osad[1])
            
            summa = summa + temp
            paevi = paevi + 1
            
            if temp > 15:
                yle_15_paevi = yle_15_paevi + 1
                
            if temp > korgeim_temp:
                korgeim_temp = temp
                pikim_paev = paev
                
            if temp < madalaim_temp:
                madalaim_temp = temp
                kylmim_paev = paev

keskmine = summa / paevi

aruanne = (
    f"Nädala keskmine temperatuur: {keskmine:.1f} °C\n"
    f"Kõige soojem päev: {pikim_paev} ({korgeim_temp} °C)\n"
    f"Kõige külmem päev: {kylmim_paev} ({madalaim_temp} °C)\n"
    f"Päevi, mil temperatuur oli üle 15 kraadi: {yle_15_paevi}\n"
)

print(aruanne)

with open("temperatuuri_aruanne.txt", "w", encoding="utf-8") as valjund:
    valjund.write(aruanne)
