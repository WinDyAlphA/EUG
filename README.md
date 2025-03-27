# EUG
## Entreprise Username generator

Un outil simple mais efficace pour générer des listes d'usernames potentiels à partir d'une liste de noms complets. Particulièrement utile pour les tests de pénétration et les audits de sécurité.

## Description

Cet outil génère de manière exhaustive des combinaisons d'usernames possibles à partir de noms complets, en se basant sur les formats couramment utilisés dans les entreprises. Il prend en compte :
- Les formats standards (prénom.nom, prénomnom)
- Les troncatures (première lettre du prénom + nom, etc.)
- Les combinaisons partielles
- Les inversions (nom.prénom, etc.)

## Utilisation

1. Créez un fichier texte contenant les noms complets (un par ligne) :
```txt
John Doe
Jane Smith
```
les noms doivent être composé de deux attributs (généralement prénom et nom)

2. Exécutez le script :
```bash
python EUG.py noms.txt
```

3. Le script générera un fichier `usernames.txt` contenant toutes les combinaisons possibles d'usernames.


## Cas d'utilisation

- Tests de pénétration
- Audits de sécurité
- Énumération d'utilisateurs
- Tests de force brute (avec les précautions appropriées)

## Avantages par rapport aux alternatives

- Simple à utiliser
- Pas de dépendances externes
- Génération exhaustive des combinaisons
- Format de sortie propre et utilisable
- Adapté aux besoins des pentests

## Note de sécurité

Cet outil est destiné à être utilisé uniquement dans le cadre de tests de sécurité autorisés. L'utilisation malveillante de cet outil est interdite et peut être illégale.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à proposer des améliorations ou à signaler des bugs.
