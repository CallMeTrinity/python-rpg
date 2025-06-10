# 🧾 **TD Python – Mini Jeu de Rôle en Programmation Orientée Objet**

## 🎯 Objectif

Concevoir une **simulation simplifiée de jeu de rôle (RPG)** en Python.
Tu devras gérer différents **types de personnages**, leur **inventaire**, leurs **équipements**, et simuler des **actions comme attaquer ou s'équiper**.

Ce TD vise à mettre en œuvre :

* l’**héritage** entre classes,
* la **composition** (ex : un personnage possède un équipement),
* les **exceptions personnalisées**,
* une organisation en **modules/packages** Python.

---

## 📁 Structure minimale attendue

```
rpg/
├── personnages.py      # Classes de personnages
├── objets.py           # Objets : armes, potions, etc.
├── jeu.py              # Logique du jeu (simulation/combat)
└── main.py             # Point d'entrée du programme
```

---

## ✅ Fonctionnalités à implémenter

### 🔹 1. **Classes de base**

* `Personnage` (classe de base) avec :

  * nom
  * points de vie (PV)
  * points d’attaque de base
  * inventaire (liste d'objets)
  * méthode `attaquer(autre_personnage)`
  * méthode `equiper(objet)`

* Deux classes enfants :

  * `Guerrier` : attaque plus élevée
  * `Mage` : attaque plus faible, peut utiliser des potions de mana

### 🔹 2. **Objets & équipements**

* Classe `Objet` (classe de base)
* Deux types d’objets :

  * `Arme` : augmente l’attaque
  * `Potion` : rend des PV ou du mana
* Un personnage peut s’équiper d’une seule arme à la fois

### 🔹 3. **Exceptions personnalisées**

* `ObjetInexistantException` si on tente d’utiliser un objet non présent dans l’inventaire
* `ActionImpossibleException` si un personnage tente une action illégale (ex : attaquer alors qu’il est mort)

### 🔹 4. **Mécanique de combat**

* Le personnage A attaque B → B perd des PV
* Une attaque peut être modifiée par l’arme équipée
* Si PV <= 0 → le personnage est déclaré mort

---

## 🧪 Exemples d’interactions (dans `main.py` ou `jeu.py`)

```python
guerrier = Guerrier("Thorgal")
mage = Mage("Zoltan")

epee = Arme("Épée en fer", bonus_attaque=5)
potion = Potion("Potion de soin", soin=20)

guerrier.inventaire.append(epee)
guerrier.inventaire.append(potion)

guerrier.equiper(epee)
guerrier.attaquer(mage)
```

---

## 🧠 Conseils pédagogiques

* Utilise un fichier par grand bloc logique (personnages, objets, jeu).
* Utilise des `@property` si tu veux rendre certains accès plus propres.
* Prévois des tests simples dans `main.py` pour démontrer les comportements attendus.

---

## 🎁 Bonus (optionnel)

* Ajouter un système de niveau (XP, montée en stats).
* Implémenter des objets spéciaux pour chaque classe.
* Gérer un mini menu dans `main.py` (texte ou CLI) pour simuler plusieurs tours.

---