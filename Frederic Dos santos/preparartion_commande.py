# la responsabilité de ce module est de calculer le temps de préparation
# d'une commande

TEMPS_PREPARATION = 15

def preparation_commande(nb_lot):
    tps_prepa = nb_lot * TEMPS_PREPARATION

    return (tps_prepa // 60,
            tps_prepa % 60)