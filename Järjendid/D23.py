sonad = ["arvuti", "programmeerimine", "hiir", "klaviatuur", "monitor"]

pikim_sona = sonad[0]
lyhim_sona = sonad[0]

for sona in sonad:
    if len(sona) > len(pikim_sona):
        pikim_sona = sona
    if len(sona) < len(lyhim_sona):
        lyhim_sona = sona

print(f"Kõige pikem sõna: {pikim_sona} ({len(pikim_sona)} tähte)")
print(f"Kõige lühem sõna: {lyhim_sona} ({len(lyhim_sona)} tähte)")
