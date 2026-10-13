#Informations produit
nom_produit = input("Nom du produit : ")
reference = input("Référence du produit : ")

prix_unitaire = float(input("Prix unitaire : "))
quantite = int(input("Quantité : "))

montant_paye = float(input("Montant payé : "))

#Calcul du montant total
montant_total = prix_unitaire * quantite
monnaie = montant_paye - montant_total

#Affichage montant total
print(f"Le montant total est : {montant_total:.2f} €")

#Calcul des lots
LOT = 4
nombre_lots = quantite // LOT

reste = quantite % LOT

#Calcul du temps de préparations
TEMPS_PREPARATION_LOT = 15

temps_preparation = nombre_lots * TEMPS_PREPARATION_LOT

heures_preparation = temps_preparation // 60
minutes_preparation = temps_preparation % 60

#Affichage du ticket de caisse

print("="*40)
print("\t\t\tTICKET DE CAISSE")
print("="*40)

print(f"Produit\t\t : {nom_produit}")
print(f"Référence\t\t : {reference}")
print(f"Prix unitaire\t\t : {prix_unitaire:.2f} €")
print((f"Quantité : {quantite}\n"))
print("-"*40)
print(f"Montant total\t\t : {montant_total:.2f} €\n")
print("Conditionnement")
print("-"*40)
print(f"Lots complets : {nombre_lots}")
print(f"Reste\t\t : {reste}\n")
print("Préparation")
print("-"*40)
print(f"Durée\t\t : {heures_preparation} heures(s) et {minutes_preparation} minute(s)")
print("-"*40)
print(f"Montant payé : {montant_paye:.2f} €")
print(f"Monnaie\t\t : {monnaie:.2f} €")
print("="*40)
print("\t\tMERCI POUR VOTRE ACHAT !")
print("="*40)

#Calcul de la monnaie en pièces
monnaie_pieces = 0
monnaie_pieces_2 = 0
monnaie_pieces_1 = 0
monnaie_pieces_50c = 0
monnaie_pieces_20c = 0
monnaie_pieces_10c = 0

#Affichage des pièces de monnaie
monnaie_pieces_2 = monnaie // 2
print(f"Nombre de pièces de 2 € : {monnaie_pieces_2:.0f}")
monnaie_pieces = monnaie % 2
print(monnaie_pieces)
monnaie_pieces_1 = monnaie_pieces // 1
print(f"Nombre de pièces de 1 € {monnaie_pieces_1:.0f}")
monnaie_pieces = monnaie_pieces % 1
monnaie_pieces = monnaie_pieces % 1
print(monnaie_pieces)
monnaie_pieces_50c = monnaie_pieces / 0.5
print(f"Nombre de pièces de 50 centimes : {monnaie_pieces_50c:.0f}")
monnaie_pieces = monnaie_pieces % 0.5
monnaie_pieces_20c = monnaie_pieces / 0.2
print(f"Nombre de pièces de 20 centimes : {monnaie_pieces_20c:.0f}")
monnaie_pieces = monnaie_pieces % 0.2
monnaie_pieces_10c = monnaie_pieces / 0.1
print(f"Nombre de pièces de 10 centimes : {monnaie_pieces_10c:.0f}")
