villes = []

while True:
    ville = input("Entrez un nom de ville (tapez ok): ")
    if ville.lower() == 'ok':
        break 
    population = len(ville) * 1000000
    villes.append((ville, population))
    
villes.sort(key=lambda x: x[1], reverse=True)
print("\nVilles et leurs populations :")
for ville, population in villes:
    print(f"{ville}: {population} habitants")
