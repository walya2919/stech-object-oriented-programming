# A
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]

# B
temps.sort()
print(temps)

# C
for temp in temps:
    if temp > 20: break

idx = temps.index(temp)

cool_temps = temps[:idx]
warm_temps = temps[idx:]
print("cool_temps :", cool_temps)
print("warm_temps :", warm_temps)

# D
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)