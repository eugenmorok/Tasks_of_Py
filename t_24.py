import sys
population = [
    144_963_650,  # 2003
    144_168_205,
    143_474_219,
    142_753_551,
    142_220_968,
    142_008_838,
    141_903_979,
    142_856_536,
    142_865_433,
    143_056_383,
    143_347_059,
    143_666_931,
    146_267_288,
    146_544_710,
    146_804_372,
    146_880_432,
    146_780_720,
    146_748_590  # 2020
]
year = int(sys.argv[1]) - 2003
year_value = population[year]
j = -1
new_list = []
for item in population:
    j += 1
    if item >= year_value:
#        print(j + 2003)
        new_list.append(str(j + 2003))
new_list.sort()
new_list = ", ".join(new_list)
print(new_list)