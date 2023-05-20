# 5teams

1) Les bases de l'objet

Créer une classe bureau avec les champs :
- nb prises réseau
- nb prises secteur
- nb prises tél
- nb chaises
- nb tables
- nb personnes
et la méthode :
* int tauxespacedispo()

Créer deux sous-classes bureaudeveloppeur et bureaucommercial
* int tauxespacedispo()

Calculer le taux d'espace disponible selon les formules :

classe générique :
  tauxespacedispo=
    personne-reseau+
    personne-secteur+
    personne-tel+
    personne-chaises+
    personne-table

classe commercial:
  tauxespacedispo=
    personne-reseau+
    personne-secteur+
    personne-2*tel+
    personne-2*chaises+
    personne-table
   
classe developpeur:
  tauxespacedispo=
    personne-3*reseau+
    personne-3*secteur+
    personne-tel+
    personne-1.5*chaises+
    personne-table

Créer une classe société et ajouter 3 bureaux commerciaux et 2 bureaux developpeurs. Leur ajouter prises, tables, téléphones etc. pour que chaque bureau puisse accueillir plusieurs personnes

Faire une boucle d'ajout de personnel (commerciaux ou développeur selon une valeur aléatoire). A chaque itération, afficher le nombre de commerciaux, de développeurs, le taux d'espace dispo de chaque bureau et le taux général de la société en appelant tauxespacedispo().
Stopper quand il n'y a plus d'espace disponible.




2) Interface utilisateur

Faire une petite application de gestion de tickets de caisse (date,intitulé,montant) :
- liste des tickets
- création
- modification
- suppression
- total par mois
- total général
* contrainte : Il ne peut y avoir 2 tickets avec la même date



3) Traitement sur les textes

- Lire un fichier texte contenant un article quelconque, et afficher tous les mots du texte, un mot sur chaque ligne




4) Résolution de problème

Ecrire 4 classes : 

chasseur
{
  nombre de balles [0-10]
  niveau de faim [0-10]
  nombre de kilomètres parcourus [0-10]
  position xy
  void chasser();
}

lapin
{
  rapidité [0-10]
  couleur [blanc/brun]
  nombre de kilomètres parcourus [0-10]
  position xy
  void poursuivi();
}

terrier
{
  position xy
  bool occuppé
}

foret
{
  terriers[]
  lapins[]
  kilomètres carrés totaux [1-10]
  nombre d'arbres pouvant cacher un lapin [0-1000]
}

- Créer 1 chasseur et 1 forêt avec des lapins et des terriers
- Lorsque la méthode "chasser" est appelée une routine automatique va faire vivre les personnages qui vont intéragir entre eux (si un lapin est vu, le nombre de balles doit diminuer, le nombre de kilomètres augmente aléatoirement, un lapin proche d'un terrier peut s'y réfugier s'il est vide...)

Conditions obligatoires :
- Il faut choisir les paramètres initiaux de telle sorte que le chasseur perde à tous les coups et les lapins soient toujours sauvés de justesse (ça ne doit pas être trop facile pour les lapins)
- rédiger l'intégralité du code source avec des termes anglais (noms de variables, de classe, commentaires, noms de fichiers)
