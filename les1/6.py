rez_fis_day = int(input("VVidite rezultat pervogo dnya: "))
fut_fis_day = int(input("VVidite rezultat kotoriy hocetsa: "))
schotchik_dney = 1
while True:
    print(f"{schotchik_dney}-y den': {rez_fis_day:.2f}")
    if rez_fis_day < fut_fis_day:
        schotchik_dney = schotchik_dney + 1
        rez_fis_day = rez_fis_day + (rez_fis_day / 10)
    else:
        print(f"на {schotchik_dney}-й день спортсмен достиг результата — не менее 3 км.")
        break