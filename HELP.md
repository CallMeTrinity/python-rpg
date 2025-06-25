# Help

## 1. Clarifier la « boucle de jeu »

**Objectif :** avoir un point d’entrée unique qui orchestre le tour-par-tour, jusqu’à la fin de la partie.

1. **État global**

    * `tour_actuel` (n° de manche)
    * `joueur_actif` (index ou nom)
    * `phase` (ex. `"exploration"`, `"combat"`, `"dialogue"`)
    * `game_over` (bool)

2. **Schéma minimal de boucle**

    1. Tant que `not game_over` :

        1. Afficher un résumé rapide (PV, mana, position, quêtes).
        2. Présenter un **menu d’actions** au joueur actif.
        3. Lancer la fonction associée à son choix (déplacement, attaque, dialogue, inventaire, etc.).
        4. Passer au joueur suivant, ou à la manche suivante si tu veux que les monstres/NPC réagissent entre chaque
           tour.

3. **Fin de partie** : déclenchée si tous les joueurs sont morts ou si un objectif global est atteint (ex. boss final
   battu).

---

## 2. Menus et parsing des commandes

### A. Menu racine (toujours le même)

```
[1] Se déplacer
[2] Interagir (PNJ, coffre…)
[3] Combattre
[4] Inventaire / équipement
[5] Feuille de personnage
[0] Quitter la partie
```

* **Astuce :** stocke chaque entrée du menu comme un tuple `(label, fonction_callback)` pour éviter les longs `if/elif`.

### B. Sous-menus et validation d’input

* Écris une fonction utilitaire : `ask_int(prompt, valid_range)` qui boucle tant qu’on ne reçoit pas un entier dans
  l’intervalle.
* Centralise l’affichage dans une couche I/O : ça te permettra un jour de greffer une interface différente sans toucher
  au cœur logique.

---

## 3. Mouvement & carte du monde

1. **Classe Map**

    * largeur, hauteur
    * grille 2D de **Tile** (case) -> type de terrain, contenu (PNJ, mob, trésor).

2. **Coordonnées du joueur**

    * Ajoute `x`, `y` à `Player`.
    * Dans « Se déplacer », liste les directions possibles selon les bords de la carte.

3. **Vision**

    * À chaque déplacement, affiche le contenu de la nouvelle case.
    * Gère l’apparition d’un combat automatique si la case contient un `Hostile`.

---

## 4. Tour-par-tour en combat

1. **Pile d’initiative simple**

    * Les combattants sont rangés par ordre fixe (joueur puis monstre) ou aléatoire.
    * Chaque entité vivante possède une action par round.

2. **Menu de combat**

   ```
   [1] Attaquer
   [2] Utiliser un objet
   [3] Fuir
   ```

3. **Résolution**

    * Après l’action du joueur, résout les contre-coups (dégâts, mort) puis passe au mob.
    * Quand tous les ennemis sont morts : loot + éventuellement passage automatique à la phase exploration.

---

## 5. Quêtes & dialogues

* Rends `Quest.start()` plus général : passe-lui un callback `input_func` pour pouvoir réutiliser la même logique hors
  du terminal (tests, GUI…).
* Dans `DialogQuest`, construis un texte‐menu identique aux autres actions ; tu profites ainsi de ta fonction utilitaire
  de saisie.

---

## 6. Gestion de l’inventaire

1. **Afficher** : un tableau numéroté (`index : nom (qté)`).
2. **Choisir un item** : via `ask_int`.
3. **Limiter la taille** : ton exception `InventoryFullException` existe déjà, utilise-la pour refuser un ramassage
   automatique.
4. **Raccourcis** : clavier « e » pour équiper/retirer, « u » pour utiliser potion.

---

## 7. Structuration et propreté du code

| Problème actuel                            | Amélioration suggérée                                                              |
|--------------------------------------------|------------------------------------------------------------------------------------|
| Mélange logique/affichage                  | Sépare **métier** (dans les méthodes) et **print** (dans une couche CLI)           |
| Répétitions de `print` pour les stats      | Implémente `__str__` ou `as_dict()` dans tes classes                               |
| Gestion d’erreurs éparpillée               | Centralise via décorateur `@cli_action` qui intercepte et affiche proprement       |
| Initialisation lourde dans `Game.__init__` | Déplace la génération aléatoire d’items/mobs dans des fonctions ou builders dédiés |
| Attributs publics non protégés             | Ajoute des `@property` seulement quand validation nécessaire                       |

---

## 8. Petites touches de confort

* **Couleurs** : utilise `colorama` pour distinguer dégâts, soins, narratif.
* **Sauvegarde rapide** : un export JSON de l’état global (players + map + quêtes) quand le joueur tape `save`.
* **Mode démo** : un drapeau « debug » qui accélère les combats (ignore `sleep()`).

---

## 9. Étapes concrètes pour toi

1. **Extrais** dans `game_loop.py` une boucle minimaliste qui appelle déjà toutes tes méthodes existantes.
2. **Remplace** toutes les saisies directes (`input(...)`) par une petite fonction Helpers.io.
3. **Implémente** les directions et les coordonnées, même avec une map 3×3 pour commencer : c’est suffisant pour tester
   le déplacement et les rencontres aléatoires.
4. **Scinde** le combat en sa propre classe (`Battle`) pour isoler le tour-par-tour.
5. **Teste** à blanc : exécute une partie avec un seul joueur, un seul mob, une potion dans l’inventaire.
6. **Élargis** ensuite : plusieurs joueurs, NPC vendeurs, quêtes multiples.

---

***Mot de la fin***
Ne cherche pas à tout perfectionner d’un coup ; pose d’abord un squelette jouable (déplacement → rencontre → combat →
loot) avant d’ajouter l’économie ou l’XP fine. Essaie de commit / push à chaque étape pour pouvoir revenir en arrière
facilement. Bon dev !
