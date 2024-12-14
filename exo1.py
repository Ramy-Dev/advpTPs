nom = input("Veuillez entrer votre nom: ")

if nom == "VIP":
    print("Profitez du spectacle gratuitement!")
else:
    nombre = int(input("Combien de billets voulez-vous acheter? "))
    print(f"Le coût total est de {nombre * 15.50:.2f} \nProfitez de vos billets!")

