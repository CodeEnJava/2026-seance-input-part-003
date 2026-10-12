
# la responsabilité de ce module est de
# centraliser les informations relatives à un produit

def scanner_produit():
    nom_produit = input("Nom du produit : ")
    reference = input("Référence du produit : ")

    prix_unitaire = float(input("Prix unitaire du produit : "))
    quantite = int(input("Quantité : "))

    return (nom_produit,
            reference,
            prix_unitaire,
            quantite)


