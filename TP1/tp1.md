# TP1 – Projet NER : Étude de cas CoNLL 2003 & Définition du projet

---

## Partie 1 : Étude de cas CoNLL 2003

Le CoNLL 2003 est un corpus annoté qui a été utilisé pour la tâche de Reconnaissance d'Entités Nommées (NER - Named Entity Recognition) lors de la conférence CoNLL (Conference on Computational Natural Language Learning) en 2003.

### 📌 Type de tâche proposée par CoNLL 2003

CoNLL 2003 est conçu pour la tâche de NER (Named Entity Recognition), qui consiste à identifier et classifier les entités nommées dans un texte en différentes catégories, comme :

- Personne (PER)
- Organisation (ORG)
- Lieu (LOC)
- Miscellaneous (MISC) (catégorie pour les entités qui ne rentrent pas dans les autres)

### 📌 Type de données dans CoNLL 2003

Le corpus contient :

- Des articles de presse issus de l'agence Reuters.
- Des phrases annotées avec des labels NER.
- Un format de fichier basé sur le BIO tagging (Begin, Inside, Outside), utilisé pour marquer le début, l’intérieur ou l’absence d’une entité nommée.

### 📌 Besoin auquel répond CoNLL 2003

Ce corpus a été conçu pour évaluer les systèmes de NER et améliorer les modèles de traitement automatique du langage naturel (NLP) dans l'extraction d'informations à partir de textes.

### 📌 Types de modèles entraînés sur CoNLL 2003

Différents modèles de NER ont été entraînés sur ce corpus, notamment :

- Modèles statistiques comme les Conditional Random Fields (CRF).
- Réseaux de neurones (LSTMs, CNNs, Transformers).
- Modèles modernes basés sur BERT comme BERT-NER, Flair, spaCy.

### 📌 Monolingue ou multilingue ?

CoNLL 2003 est **multilingue** : il contient des données pour l'anglais et l'allemand.

---

## Partie 2 : Définition du projet

En s’inspirant de la tâche CoNLL 2003, ce projet propose de créer un système de reconnaissance d’entités nommées (NER) pour les **articles sportifs francophones** disponibles en ligne. Le but est de collecter, structurer et analyser automatiquement les informations essentielles à partir de textes journalistiques.

### 📌 Besoin dans lequel s’inscrit le projet

Ce projet s’inscrit dans un **besoin d’extraction automatique d’information**. Il vise à identifier les éléments clés (joueurs, clubs, lieux, événements sportifs, etc.) dans des textes pour :

- Faciliter la création de bases de données sportives.
- Aider les journalistes et analystes à structurer les informations.
- Fournir un socle pour des applications de veille ou de résumé automatique.

### 📌 Sujet traité

**Reconnaissance des entités nommées dans les articles sportifs français.**

Le projet portera notamment sur des articles de football et de tennis, deux disciplines populaires avec une grande richesse textuelle et un grand nombre d'entités à extraire (joueurs, équipes, stades, compétitions…).

### 📌 Type de tâche à réaliser

Le projet repose sur une tâche de **NER (Named Entity Recognition)**, identique à celle de CoNLL 2003.  
Il s’agit de détecter dans les articles des entités nommées, que l’on classera dans les catégories suivantes (non exhaustives) :

- `PER` : personnes (joueurs, entraîneurs…)
- `ORG` : organisations (clubs, fédérations…)
- `LOC` : lieux (villes, stades…)
- `EVENT` : événements sportifs (matchs, tournois…)
- `MISC` : autres entités (ex : sponsors)

### 📌 Type de données exploitées

Les données exploitées seront des **articles de presse sportive** extraits depuis le web, sous forme de texte brut HTML ou nettoyé.  
Elles seront ensuite annotées manuellement ou automatiquement pour former un corpus de NER.

### 📌 Source des données

Les données seront collectées à partir de sites web sportifs publics comme :

- [L’Équipe](https://www.lequipe.fr/)
- [Eurosport](https://www.eurosport.fr/)
- [RMC Sport](https://rmcsport.bfmtv.com/)

Le scraping se fera à l’aide de scripts Python (`requests`, `BeautifulSoup`) sans utiliser d’API.

### 📌 Données libres d’accès ?

Les articles sont **publiquement accessibles en ligne** pour consultation humaine.  
L’usage académique et non commercial, sans dépassement du scraping raisonnable, permet de les exploiter dans un cadre pédagogique et expérimental.

---
