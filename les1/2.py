time_is_s = int(input("Vvedite vremya v seqyndah: "))
print(time_is_s)
secund_fact = (time_is_s % 60)
min_fact = ((time_is_s // 60) % 60)
chas_full = ((time_is_s // 60) // 60)

if secund_fact < 10:
    secund_fact = "0" + str(secund_fact)
if min_fact < 10:
    min_fact = "0" + str(min_fact)
if chas_full < 10:
    chas_full = "0" + str(chas_full)
print(f"time: {chas_full}:{min_fact}:{secund_fact}")
