total = float(input("Montant total: "))
nombre_articles = int(input("Nombre d'articles: "))
jour_semaine = input("Jour de la semaine: ").capitalize()
reduction = 0

if jour_semaine in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]:
    reduction += 10  
elif jour_semaine in ["Samedi", "Dimanche"]:
    reduction += 20  
if nombre_articles > 5:
    reduction += 5  

print(f"Prix total après réduction: {total * (1 - reduction / 100):.2f} dinars")
