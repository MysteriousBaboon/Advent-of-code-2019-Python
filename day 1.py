list_value = [
              106404,
              140515,
              142745,
              120767,
              79665,
              54235,
              127391,
              72207,
              70799,
              79485,
              103994,
              129583,
              132791,
              95135,
              121194,
              129425,
              64861,
              123233,
              132805,
              87916,
              111395,
              126625,
              113045,
              61704,
              65413,
              145820,
              75988,
              74717,
              115137,
              85331,
              86833,
              86063,
              85464,
              139738,
              103372,
              101942,
              52741,
              77660,
              112745,
              103109,
              106301,
              141714,
              74546,
              55474,
              106747,
              140234,
              60426,
              145867,
              144810,
              94179,
              101606,
              77763,
              139291,
              104246,
              148513,
              126828,
              64624,
              139058,
              85839,
              86636,
              62198,
              137358,
              76711,
              87848,
              141711,
              114079,
              71639,
              95896,
              104522,
              61929,
              72199,
              142790,
              137736,
              123437,
              91872,
              127661,
              111179,
              51548,
              83452,
              91196,
              117798,
              84484,
              75517,
              83820,
              97407,
              89181,
              71428,
              72758,
              73076,
              109957,
              50601,
              74571,
              65556,
              129765,
              80626,
              126995,
              73480,
              71360,
              103288,
              85670
              ]


list_result = []




i = 0

while i < len(list_value):
    b = list_value[i]
    while (list_value[i] // 3) - 2 >= 0:
        print("valeur de l'emplacement avant division " + str(list_value[i]))
        b += (list_value[i] // 3) - 2
        list_value[i] = (list_value[i] // 3) - 2
        print("Valeur de l'emplacement apres division " + str(list_value[i]) + "Valeur totale" + str(b)
              + " Valeur itérateur " + str(i))

    list_result.append(b)
    i += 1

ii = 0
result = 0
while ii < len(list_result):
    result += list_result[ii]
    ii += 1

print(result)




print(list_result)
print(len(list_result))
print(sum(list_result))





