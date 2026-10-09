nom_produit =(input("Entrer le nom du produit : "))
reference_produit = input("rreference produit : ")

prix_unitaire = float(input("entrer le prix unitaire : "))
quantité_achete = int(input("combien de produit acheté ? :"))


montant_paye = float(input("Montant payé : "))


montant_total = prix_unitaire * quantité_achete
monaie_rendu =  montant_paye - montant_total


nb_lot = quantité_achete // 4

#Pourquoi utiliser-t-on //plutôt que /? car pour ne pas avoir un nombre réel et avoir le nombre exact de lot entier


#calculer le nombre de produit restant apres la constitution des lots

reste = quantité_achete % 4

#temp de preparation de la commande

tps_prepa = nb_lot * 15

heure = tps_prepa // 60
minute = tps_prepa % 60

# Ticket de caisse
print("="* 60)
print("TICKET DE CAISSE".center(60))
print("="*60)
print("")
print(f"Produit                : {nom_produit}")
print(f"Référence              : {reference_produit}")
print(f"Prix unitaire          : {prix_unitaire:.2f} € ")
print(f"Quantité               : {quantité_achete} ")
print("")
print("-"*60)
print(f"Montant total          : {montant_total:.2f} €")
print("")
print("Conditionnement")
print("-"*60)
print(f"lots complets          : {nb_lot}")
print(f"Reste                  : {reste}")
print("")
print("Préparation")
print("-"*60)
print(f"Durée                  : {heure} heure(s) et {minute} minute(s)")
print("")
print(f"Montant payé           :   {montant_paye:.2f} €")
print(f"Monaie rendu           : {monaie_rendu:.2f} €")
print("")
print("="*60)
print("MERCI POUR VOTRE ACHAT ! ".center(60))
print("="*60)









