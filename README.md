# 🧾 **TD Python – Mini Jeu de Rôle en Programmation Orientée Objet**

## 🎯 Objectif

Concevoir une **simulation évolutive de jeu de rôle (RPG)** en Python.

Tu commenceras par gérer différents **types de personnages jouables**, leur **inventaire**, leurs **équipements**, et simuler des **actions de base** comme attaquer ou s’équiper.

Dans une **deuxième phase**, tu enrichiras ton jeu avec :

* Des **monstres** et **PNJ** variés
* Un **système de loot** et de **missions**
* Un **moteur de tour** de jeu (combat ou exploration)
* Le **chargement de données depuis un fichier Excel**
* Un **système de dés** (chance, probabilité)
* Et potentiellement d’autres mécaniques de gameplay

---

## 📁 Structure de projet proposée

```
rpg/
├── core/                      # Logique centrale du jeu
│   ├── jeu.py                # Moteur principal, boucle de jeu
│   ├── moteur_tour.py        # Gestion des tours (joueurs, monstres)
│   ├── de.py                 # Système de dés (D6, D20, etc.)
│
├── entites/                  # Tous les êtres vivants du jeu
│   ├── personnages.py        # Personnages jouables
│   ├── monstres.py           # Ennemis à affronter
│   ├── pnj.py                # Personnages non-joueurs
│
├── objets/                   # Objets divers
│   ├── objets.py             # Classes de base
│   ├── loot.py              # Tables de loot / drops
│
├── donnees/                  # Données à charger
│   ├── aventure.xlsx         # Fichier Excel avec toutes les données (objets, PNJ, personnages, etc.)
│   └── chargement.py         # Code pour lire le fichier Excel
│
└── main.py                   # Point d’entrée du jeu
```

---

## ✅ Partie 1 — Fonctionnalités de base

### 🔹 1. **Personnages jouables**

* `Personnage` (classe de base) :

  * nom, points de vie, attaque de base, inventaire
  * méthodes : `attaquer`, `equiper`, etc.

* Héritage :

  * `Guerrier` (attaque augmentée)
  * `Mage` (mana, potions)

### 🔹 2. **Objets & équipements**

* `Objet` (classe de base)

  * `Arme` (bonus d’attaque)
  * `Potion` (soins, mana)

* Un personnage peut s’équiper d’une seule arme à la fois

### 🔹 3. **Exceptions personnalisées**

* `ObjetInexistantException`, `ActionImpossibleException`, etc.

### 🔹 4. **Combat de base**

* Système d’attaque simple entre personnages
* Morts gérés par hp ≤ 0

---

## 🚀 Partie 2 — Fonctionnalités avancées

### 🔹 5. **Monstres et PNJ**

* `Monstre` : attaque le joueur, possède un loot
* `PNJ` : propose des missions ou dialogue

### 🔹 6. **Loot et objets générés**

* Chaque monstre a une **table de loot** (proba de drop)
* Objets obtenus aléatoirement après les combats

### 🔹 7. **Missions**

* Missions données par les PNJ
* Conditions de succès et récompenses (XP, objets)

### 🔹 8. **Moteur de tour**

* Alternance joueurs / monstres
* Ordre défini, temps de jeu simulé
* Possibilité d’intégrer des événements aléatoires

### 🔹 9. **Fichier Excel (données)**

* Utiliser un fichier `.xlsx` pour stocker :

  * Personnages
  * Objets
  * PNJ
  * Tables de loot
  * Missions

* Le programme charge ce fichier au démarrage pour **initialiser dynamiquement l’aventure**

### 🔹 10. **Système de dés**

* Lancer de dé (`D6`, `D20`, etc.) pour :

  * Déterminer les dégâts
  * Gérer les chances de succès (vol, esquive, etc.)
  * Résoudre des situations spéciales (tests de chance)

---

## 🧪 Exemples d’extensions possibles

* Système de niveaux et d’expérience
* Journal de quêtes
* Mini carte textuelle
* Points de compétence

---

## 🧠 Conseils pédagogiques

* Modulaire dès le départ : séparer bien les rôles dans les fichiers
* Prioriser la clarté : commence simple, complexifie ensuite
* Utilise des packages (`__init__.py`) et des exceptions claires