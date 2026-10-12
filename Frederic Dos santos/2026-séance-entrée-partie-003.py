from saisie_des_informations import *
from facturation import facture
from preparartion_commande import preparation_commande
from transaction import transaction
from impression_ticket import ticket

#  1 - il faut saisir les informations du produit ( scanner....)
produit = scanner_produit()

# 2 -préparer la facture
preparation = facture(produit)

# 3- temps de preparation de la commande
temps = preparation_commande(preparation[1])

# 4 - afficher le ticket en console
ticket(produit,preparation,temps)

# 5 - transaction
montant_donne,monnaie_rendu = transaction(preparation[0])

print(f"Montant donné          : {montant_donne:.2f} €")
# un truc en plus
if monnaie_rendu < 0:
    print(" il vous manque :",abs(monnaie_rendu), "€")
else:
    print(f"Monnaie rendu          : {monnaie_rendu:.2f} €")

print("")
print("="*60)
print("MERCI POUR VOTRE ACHAT ! ".center(60))
print("="*60)









