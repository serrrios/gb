chislo = int(input("Vvedite chislo: "))
max_chsilo = 0
while chislo > 0:
    temp_chislo = chislo % 10
    if temp_chislo > max_chsilo:
        max_chsilo = temp_chislo
    chislo = chislo // 10
print("Max cifra v chisle:", max_chsilo)