# la responsabilité de ce module est de récupérer la somme à payer


def transaction(total):
    montant_donne = float(input("Somme donnne : "))
    return (montant_donne,
            montant_donne-total)

