prix = float(input("Veuillez entrer un prix: "))
dinars = int(prix)  
print(f"Dinars: {dinars}")
print(f"Centimes: {round((prix - dinars) * 100)}")
