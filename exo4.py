P1 = int(input("Veuillez entrer l'âge de la première personne: "))
P2 = int(input("Veuillez entrer l'âge de la deuxième personne: "))

if P1 > P2:
    print(f"La personne la plus âgée est la personne 1")
elif P2 > P1:
    print(f"La personne la plus âgée est la personne 2")
else:
    print("Les deux personnes ont le même âge!")
