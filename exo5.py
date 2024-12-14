print("Coureur 1:")
nom1 = input("Nom: ")
temps1 = float(input("Temps (en secondes): "))
print("\nCoureur 2:")
nom2 = input("Nom: ")
temps2 = float(input("Temps (en secondes): "))

if temps1 < temps2:
    print(f"\nLe coureur le plus rapide est {nom1}")
elif temps2 < temps1:
    print(f"\nLe coureur le plus rapide est {nom2}")
else:
    print(f"\n{nom1} et {nom2} ont le même temps")
