try:
    f =  open("alkaline_metals.txt", "r")
except:
    f = open("alkaline_metals.txt", "w")
    f.write(
        """beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.237
radium 88 226"""
    )
    f.close()
    f =  open("alkaline_metals.txt", "r")

alkaline_metals = list()
for line in f.readlines():
    alkaline_metals.append(line.split())

print(alkaline_metals)