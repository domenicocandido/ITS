nord_sud:int = int(input("Inserire veicoli direzione nord_sud: "))
est_ovest:int = int(input("Inserire veicoli direzione est_ovest: "))
soglia = 70

if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40
elif est_ovest > soglia:
    time_ns = 40
    time_eo = 60
else:
    time_ns = (nord_sud/(nord_sud + est_ovest)) * 100
    time_eo = (est_ovest/(nord_sud + est_ovest)) * 100


print(f"Il tempo assegnato alla direzione Nord-Sud è: {time_ns:.0f}")
print(f"Il tempo assegnato alla direzione Est-Ovest è: {time_eo:.0f}")