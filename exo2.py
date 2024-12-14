temperature = int(input("Veuillez entrer la température chez vous : "))

if temperature < 0:
    print("Il gèle!")
if temperature < 10:
    print("Il fait froid!")
if temperature < 20:
    print("Il fait frais!")

print("Prenez soin de vous!")
