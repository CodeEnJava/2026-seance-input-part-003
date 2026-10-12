# le rôle de ce modul est de générer les éléments de la facture en fonction
# données d'un produit P

UNITE_VENTE = 4

"""
            (nom_produit,  -> 0
            reference,     -> 1
            prix_unitaire, -> 2
            quantite       -> 3)

            Nous commençons, on considère ici, que l'information
            respecte le bon formalisme de la structure de données
"""
def facture(information):

    montant_total = information[2] * information[3]
    nb_lot = information[3] // UNITE_VENTE
    reste = information[3] % UNITE_VENTE

    return montant_total,nb_lot,reste

