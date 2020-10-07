viruchka = int(input("VVidite vviruchky(pust' eto bydyt yslovnie bubli): "))
izdrjki = int(input("VVidite izdrjki(pust' eto bydyt yslovnie bubli): "))
if viruchka > izdrjki:
    print(f"firma v pribyle i zarabotala: {viruchka - izdrjki} bubley")
    print(f"rentabtlnost: {((viruchka - izdrjki) / viruchka) * 100:.1f} %")
    count_sotridnik = int(input("VVidite kol-vo sotrudnikov: "))
    print(f"Esli raspil proydet porovny, to na sotrudnika po {(viruchka - izdrjki)/count_sotridnik:.1f} bubley")
else:
    print("rabotaem v minus, pora vseh yvolit'")
