
nom_produit = input("Nom du produit : ")
reference = input("Référence du produit : ")

prix_unitaire = float(input("Prix unitaire du produit : "))
quantite = int(input("Quantité : "))

montant_total = prix_unitaire * quantite

nombre_lots = quantite // 4

reste = quantite % 4

temps_preparation = nombre_lots * 15

heures = temps_preparation // 60
minutes = temps_preparation % 60


print("="*50)
print("TICKET DE CAISSE".center(50))
print("="*50)
print("Produit            :", nom_produit)
print("Référence          :", reference)
print(f"Prix unitaire      : {prix_unitaire:.2f} €")
print("Quantité           :", quantite)
print()
print("-"*50)
print(f"Montant total     : {montant_total:.2f} €")
print()
print("Conditionnement")
print("-"*50)
print(f"Lots complets     : {nombre_lots}")
print(f"Reste             : {reste} produit")
print()
print("Préparation")
print("-"*50)
print(f"Durée              : {heures} heure(s) et {minutes} minute(s)")
print()
print("="*50)
print("MERCI POUR VOTRE ACHAT !".center(50))
print("="*50)