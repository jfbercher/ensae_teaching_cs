﻿

.. _l-projinfo2a:

2A - Projets informatiques
==========================

**en construction**

Le projet informatique sera centré sur la résolution d'un problème de 
machine learning :

* **Jeux de données :**
    * Il devra être choisi parmi les sources proposées ci-dessous.
    * Aucun exemple d'algorithme de machine learning fonctionnant sur des graphes 
      (clustering, recommandations) n'a été montré en TD mais il est possible de choisir un tel jeu.
* **Travail attendu :** 
    * Un rapport (Word, PDF, Notebook - pour ce dernier, il faudra s'assurer que l'impression de le déforme pas trop, 
      il peut être converti au format PDF avec `nbconvert <>` et Latex).
    * Une introduction : quel est le problème à résoudre, un aperçu des données ?
    * Une attention particulière sur la rigueur de la démarche (base d'apprentissage / test,
      overfitting, validation croisée, vérification sur quelques exemples, 
      type de variable - continues, discrètes, catégorielles).
    * La comparaison de deux modèles sur le même jeu de données (soit deux modèles différents,
      soit le même modèle avec des paramètres différents), on s'intéressera aux observations
      pour lesquelles les modèles sont en désaccords. On pourra également comparer 
      les vitesse d'apprentissages et les performances.
    * La présence d'au moins un graphique.
    * Quelques exemples de codes (la sélection d'un hyper paramètre par exemple).
    * L'ajout d'une variable/feature non présente dans le jeu de données initial 
      (cela peut être une combinaison des précédentes).
    * Une conclusion : le modèle est-il exploitable ou ses performances sont-elles trop faibles ?
    * Prolongements / perspectives : le problème à résoudre est souvent extrait de son contexte, 
      il s'agit de le replacer dans un environnement industriel. Cela peut passer par 
      une réflexion autour des questions suivantes 
      (qui ne s'appliquent pas forcément à tous les jeux de données) :
        * Le modèle est-il exploitable avec ses performances ?
        * Est-il exploitable seul ou associé à autre chose (est-il une feature d'un autre modèle) ?
        * Quel est sa durée de vie ? Ses performances vont-elle se dégrader dans le temps ? Peut-on le détecter ?
        * Le modèle peut-il passer à l'échelle et être entraîné sur des jeux 10, 100, 1000 fois plus grand ?
        * Certaines variables/information sont coûteuses à obtenir, 
          est-il envisageable de faire moins coûteux sans trop de perte de performances ?
        * Doit-il être maintenu, rafraîchi, à quel coût ? 
        * Si le modèle doit être rafraîchi régulèrement, le modèle peut-il être utilisé 
          voire réappris sans intervention humaine ?
        * Si le modèle est rafraîchi régulièrement et automatique,
          serai-il facile de détecter qu'une mise à jour a échoué ?
        * Lorsque l'apprentissage est long et coûteux, l'estimation d'un nouveau
          modèle pourrait-elle être faite à partir de la précédente ou non ? 
          (nouvel apprentissage ou simple mise à jour)
        * Si vous deviez vendre ce modèle de machine learning, quel modèle économique choisiez-vous ?
          (une application, une extension Excel, un service distant payé à chaque prédiction, 
          une application smartphone, le modèle seulement...)
        * Lorsque le modèle se trompe, se trompe-t-il de beaucoup ? Quel serait le coût de l'erreur ?
          Peut-on le réduire ?
        
* **Barème :**    
    * rapport / introduction / conclusion : 4 points
    * rigueur : 4 points
    * graphiques : 4 points
    * code / feature : 4 points
    * prolongements / perspectives : 4 points

Le projet doit être réalisé par un seul élève ou par groupe de deux s'il valide
les trois conditions suivantes :

* Le jeu de données contient plus de 500.000 d'observations.
* L'un des deux modèles n'est pas linéaire et n'est pas un arbre de décision.
* Il y a plus de 10 variables ou le jeu de données est un graphe.

``Soutenance ?``



Liens
+++++

* :ref:`Bien démarrer un projet de machine learning <l-debutermlprojet>`
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_


Sources de jeux de données
++++++++++++++++++++++++++

* `Stanford Large Network Dataset Collection <http://snap.stanford.edu/data/>`_ :
    collection de graphes
* `UCI Machine Learning Repository <https://archive.ics.uci.edu/ml/datasets.html>`_ :
    collection de jeux de données classés par type de problème - régression, classification, ...
* Votre propre jeu de données (à valider avec l'encadrant).