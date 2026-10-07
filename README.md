# 2026-seance-input-part-003
# 🐍 Mini-projet – Ticket de caisse

## S-PYTH-1008 — Manipulation de la fonction `input()` en Python

### 🎯 Objectif

Dans ce mini-projet, vous allez réaliser un programme Python permettant de créer un **ticket de caisse** à partir d'informations saisies par l'utilisateur.

Ce projet permet de mettre en œuvre l'ensemble des notions étudiées jusqu'à présent :

* variables ;
* chaînes de caractères ;
* types `str`, `int` et `float` ;
* fonction `input()` ;
* conversions avec `int()` et `float()` ;
* opérateurs arithmétiques ;
* division entière `//` ;
* modulo `%` ;
* fonction `print()` ;
* paramètres `sep` et `end` ;
* formatage des nombres avec `:.2f`.

> 💡 **Important :** aucune fonction personnelle, boucle ou structure conditionnelle `if` n'est nécessaire.

---

# 📥 1. Préparer le projet

## Cloner le dépôt

Commencez par **cloner le dépôt GitHub** sur votre ordinateur.

> ⚠️ **N'oubliez pas de cloner le dépôt avant de commencer votre travail.**

Ouvrez ensuite le projet dans **PyCharm**.

---

# 📁 2. Créer votre espace de travail

Dans PyCharm, créez un dossier portant **votre pseudo**.

Par exemple :

```text
votre-pseudo/
```

À l'intérieur de ce dossier, vous placerez votre programme :

```text
votre-pseudo/
└── ticket_caisse.py
```

### Exemple d'organisation du dépôt

```text
mini-projet-ticket-caisse/
│
├── README.md
│
├── stephane-barois/
│   └── ticket_caisse.py
│
├── toto/
│   └── ticket_caisse.py
│
├── dupont/
│   └── ticket_caisse.py
│
└── ...
```

> ⚠️ Chaque stagiaire doit travailler **uniquement dans son propre dossier**.

---

# 🛒 3. Principe du projet

Le programme doit permettre de saisir les informations concernant un achat :

* nom du produit ;
* référence ;
* prix unitaire ;
* quantité achetée.

À partir de ces informations, le programme devra calculer :

* le montant total ;
* le nombre de lots complets ;
* le nombre de produits restants ;
* le temps de préparation de la commande ;
* le nombre d'heures ;
* le nombre de minutes restantes.

---

# 🧱 4. Saisir les informations

Utiliser `input()` pour demander les informations.

Exemple :

```python
nom_produit = input("Nom du produit : ")
reference = input("Référence du produit : ")

prix_unitaire = float(input("Prix unitaire : "))
quantite = int(input("Quantité : "))
```

### 💡 Rappel

La fonction :

```python
input()
```

retourne toujours une valeur de type :

```text
str
```

Il faut donc convertir les données numériques.

---

# 💰 5. Calculer le montant total

Le montant total est calculé avec :

```text
montant total = prix unitaire × quantité
```

Créer la variable :

```python
montant_total
```

Exemple :

```text
Prix unitaire : 2.50 €
Quantité : 7

2.50 × 7 = 17.50 €
```

Le résultat devra être affiché avec deux chiffres après la virgule :

```text
Montant total : 17.50 €
```

Utiliser :

```python
:.2f
```

---

# 📦 6. Utiliser la division entière `//`

Les produits sont conditionnés par **lots de 4**.

À partir de la quantité saisie, calculer le nombre de lots complets :

```python
nombre_lots = quantite // 4
```

Exemple :

```text
Quantité : 17

17 // 4 = 4
```

Le programme doit donc indiquer :

```text
Lots complets : 4
```

### ❓ Question

Pourquoi utilise-t-on `//` plutôt que `/` ?

---

# 🔢 7. Utiliser le modulo `%`

Il faut maintenant calculer le nombre de produits restants après la constitution des lots.

Utiliser :

```python
reste = quantite % 4
```

Exemple :

```text
17 % 4 = 1
```

Le résultat est donc :

```text
Lots complets : 4
Produits restants : 1
```

### 💡 À retenir

Pour une division euclidienne :

```text
17 // 4 = 4
17 % 4  = 1
```

`//` permet d'obtenir le **quotient entier**.

`%` permet d'obtenir le **reste**.

---

# ⏱️ 8. Calculer le temps de préparation

On considère qu'un lot nécessite **15 minutes** de préparation.

Créer :

```python
temps_preparation
```

avec :

```python
temps_preparation = nombre_lots * 15
```

Pour 4 lots :

```text
4 × 15 = 60 minutes
```

---

# 🕐 9. Convertir les minutes en heures

Le temps de préparation est exprimé en minutes.

Il faut maintenant le convertir en heures et minutes.

### Nombre d'heures

Utiliser la division entière :

```python
heures = temps_preparation // 60
```

### Minutes restantes

Utiliser le modulo :

```python
minutes = temps_preparation % 60
```

Par exemple, pour :

```text
85 minutes
```

on obtient :

```text
85 // 60 = 1
85 % 60 = 25
```

Le programme devra afficher :

```text
Durée : 1 heure(s) et 25 minute(s)
```

---

# 🧾 10. Construire le ticket

Le programme doit afficher une fiche similaire à :

```text
========================================
             TICKET DE CAISSE
========================================

Produit       : Cahier
Référence     : CAH-001
Prix unitaire : 2.50 €
Quantité      : 17

----------------------------------------
Montant total : 42.50 €

Conditionnement
----------------------------------------
Lots complets : 4
Reste         : 1 produit

Préparation
----------------------------------------
Durée         : 1 heure(s) et 0 minute(s)

========================================
        MERCI POUR VOTRE ACHAT !
========================================
```

L'affichage doit être réalisé avec `print()`.

---

# ⭐ 11. Challenge – Paiement

Ajouter la saisie du montant payé :

```python
montant_paye = float(input("Montant payé : "))
```

Calculer ensuite la monnaie :

```python
monnaie = montant_paye - montant_total
```

Afficher :

```text
Montant payé : 50.00 €
Monnaie       : 7.50 €
```

> ⚠️ Pour cette version, il n'est pas nécessaire de vérifier si le montant payé est suffisant.

---

# ⭐ 12. Challenge – Décomposer la monnaie

Pour aller plus loin, utiliser `//` et `%` afin de décomposer la monnaie en centimes.

Par exemple :

```python
monnaie_centimes = int(monnaie * 100)
```

Puis rechercher combien de pièces de :

* 2 € ;
* 1 € ;
* 50 centimes ;
* 20 centimes ;
* 10 centimes ;

sont nécessaires.

Exemple :

```python
pieces_2 = monnaie_centimes // 200
reste = monnaie_centimes % 200
```

Puis continuer la décomposition à partir de `reste`.

> ⭐ **Challenge facultatif** : cette partie permet de vérifier votre compréhension de la division euclidienne et du modulo.

---

# 🧠 13. Questions de synthèse

Répondre aux questions suivantes dans votre programme ou dans un fichier `reponses.md`.

### Question 1

Que retourne la fonction :

```python
input()
```

### Question 2

Pourquoi utiliser :

```python
int()
```

pour convertir la quantité ?

### Question 3

Pourquoi utiliser :

```python
float()
```

pour convertir le prix ?

### Question 4

Quelle est la différence entre :

```python
/
```

et :

```python
//
```

### Question 5

Que donne :

```python
17 // 4
```

### Question 6

Que donne :

```python
17 % 4
```

### Question 7

Que représentent ensemble :

```python
17 // 4
17 % 4
```

### Question 8

Comment obtenir le nombre d'heures à partir d'un nombre de minutes ?

### Question 9

Comment obtenir les minutes restantes ?

### Question 10

À quoi sert :

```python
:.2f
```

### Question 11

À quoi servent les paramètres :

```python
sep
```

et :

```python
end
```

---

# 📤 14. Déposer votre production

Votre production doit être déposée **dans votre dossier personnel**.

### Structure attendue

```text
votre-pseudo/
│
├── ticket_caisse.py
│
└── reponses.md        ← facultatif
```

### Avant de déposer votre travail

Vérifiez que :

* [ ] le dépôt GitHub a bien été cloné ;
* [ ] votre dossier porte bien votre pseudo ;
* [ ] le fichier s'appelle `ticket_caisse.py` ;
* [ ] le programme fonctionne sans erreur ;
* [ ] les données sont saisies avec `input()` ;
* [ ] les conversions `int()` et `float()` sont utilisées ;
* [ ] le montant total est correctement calculé ;
* [ ] `//` est utilisé pour les lots ;
* [ ] `%` est utilisé pour le reste ;
* [ ] `//` et `%` sont utilisés pour convertir les minutes ;
* [ ] les prix sont affichés avec deux décimales ;
* [ ] votre production est enregistrée dans votre dossier personnel.

---

# 📌 15. Espace de dépôt des productions

Chaque stagiaire doit déposer sa production dans le dossier correspondant à son **pseudo**.

```text
📁 Productions
│
├── 📁 pseudo-stagiaire-1
│   └── ticket_caisse.py
│
├── 📁 pseudo-stagiaire-2
│   └── ticket_caisse.py
│
├── 📁 pseudo-stagiaire-3
│   └── ticket_caisse.py
│
└── ...
```

> 🎯 **Votre production doit être déposée dans votre propre dossier.**
>
> Ne modifiez pas les fichiers ou dossiers appartenant aux autres stagiaires.

---

# 🎯 Compétences mobilisées

| Notion    | Mise en œuvre              |
| --------- | -------------------------- |
| Variables | Stockage des informations  |
| `input()` | Saisie utilisateur         |
| `str`     | Nom et référence           |
| `int`     | Quantité                   |
| `float`   | Prix                       |
| `+`       | Calculs                    |
| `*`       | Montant et durée           |
| `/`       | Division classique         |
| `//`      | Lots et heures             |
| `%`       | Restes et minutes          |
| `print()` | Affichage                  |
| `sep`     | Séparation des valeurs     |
| `end`     | Gestion de fin d'affichage |
| `:.2f`    | Formatage des prix         |

---

# 🚫 Contraintes

Pour ce mini-projet, **ne pas utiliser** :

* `if` ;
* `elif` ;
* `else` ;
* `for` ;
* `while` ;
* fonctions personnelles ;
* listes ;
* dictionnaires.

L'objectif est de valider les notions étudiées **avant l'introduction des structures de contrôle et des fonctions**.

---

# 🚀 Pour aller plus loin

Une prochaine version du programme pourra permettre :

* de gérer plusieurs produits ;
* de vérifier les données saisies ;
* de gérer un paiement insuffisant ;
* de calculer automatiquement la monnaie ;
* d'utiliser des conditions ;
* d'utiliser des boucles ;
* de créer des fonctions ;
* de structurer le programme en plusieurs modules.

**Bon développement 🐍**
