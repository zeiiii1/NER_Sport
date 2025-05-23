# TP2 – Récupération du corpus à partir d’une ressource web

---

## 🎯 Objectif

Récupérer un corpus de textes à partir d’une ressource web librement accessible (sans API), en respectant les bonnes pratiques de scraping. Le corpus servira à l'entraînement de notre système de reconnaissance d'entités nommées (NER).

---

## 🌍 Site web choisi

**https://www.lequipe.fr/**  
Ce site publie des articles sportifs quotidiennement. Le contenu est riche en entités nommées (joueurs, clubs, événements, etc.).

---

## 🛠️ Outils utilisés

- Python
- `requests`
- `BeautifulSoup`
- `fake_useragent`
- `time`

---

## 🗂️ Arborescence du projet

Le projet suit l'organisation recommandée :

NER-SPORT/
├── TP1/
│ └── tp1.md
├── TP2/
│ └── tp2.md
├── scripts/
│ └── scraping_articles.py
├── data/
│ └── raw_articles/
├── README.md
├── requirements.txt
└── .gitignore

---

## 📌 Fonctionnement du script

Le script `scraping_articles.py` :

1. Récupère les liens d’articles récents sur la page d’accueil de L’Équipe.
2. Scrape le contenu textuel des articles sélectionnés.
3. Enregistre les textes dans le dossier `data/raw_articles/`.

---

## 🚀 Utilisation

```bash
pip install -r requirements.txt
python scripts/scraping_articles.py
