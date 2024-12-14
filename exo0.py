personnes = int(input("Combien de personnes ont besoin d'un trajet? "))
capacite = int(input("Combien de personnes peuvent entrer dans un taxi? "))

taxis_necessaires = (personnes // capacite) + (1 if personnes % capacite > 0 else 0)

print(f"\nNombre de taxis nécessaires: {taxis_necessaires}")
