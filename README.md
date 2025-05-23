# 📚 Projet NER Sportif – Extraction d'entités nommées dans la presse française 📰⚽

---

## 🎯 Objectif

Créer un pipeline complet de traitement automatique du langage (NLP) pour la **reconnaissance d'entités nommées (NER)** dans des articles de presse sportive francophone.

---

## 📁 Structure du projet

.
├── TP1/ # Étude CoNLL 2003 + définition du projet
├── TP2/ # Scraping des articles (L'Équipe, etc.)
├── TP3/ # Statistiques & visualisation du corpus
├── TP4/ # Augmentation des données + choix du modèle
├── TP5/ # Fine-tuning de CamemBERT avec Hugging Face
├── TP6/ # Évaluation (precision, recall, f1)
├── README.md
└── requirements.txt


---

## 🔧 Entraînement (TP5)

L'entraînement du modèle se fait via `Trainer` :

```bash
python TP5/scripts/finetuning.py
```


