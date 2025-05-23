# TP6 – Évaluation du modèle NER fine-tuné

---

## 🎯 Objectif

Évaluer les performances du modèle CamemBERT fine-tuné à la tâche de **Reconnaissance d'Entités Nommées (NER)** sur les articles sportifs.

---

## 📏 Métriques utilisées

- **Précision (precision)** : parmi les entités détectées, combien sont correctes ?
- **Rappel (recall)** : parmi toutes les vraies entités, combien ont été trouvées ?
- **F1-score** : moyenne harmonique précision/rappel (équilibre entre les deux)

---

## 🧰 Outils

- [`transformers`](https://huggingface.co/docs/transformers/)
- [`seqeval`](https://github.com/chakki-works/seqeval) : métrique NER standard
- PyTorch

---

## 📁 Organisation

TP6/
├── tp6.md
└── scripts/
└── evaluate_model.py


---

## 📌 Procédure d’évaluation

1. Charger le modèle fine-tuné depuis `TP5/model/`
2. Charger le jeu de test depuis `TP5/data/test.json`
3. Appliquer le modèle pour prédire les entités sur chaque séquence
4. Comparer les étiquettes prédites avec les étiquettes réelles
5. Calculer les scores `precision`, `recall`, `f1-score` par classe et au global

---

## 📊 Résultat attendu

Un rapport comme :

          precision    recall  f1-score   support

   B-PER       0.91      0.88      0.90        40
   I-PER       0.87      0.85      0.86        30
   B-ORG       0.83      0.79      0.81        25
   I-ORG       0.78      0.75      0.76        20
       O       0.97      0.98      0.98       500
micro avg      0.95      0.95      0.95       615
macro avg      0.87      0.85      0.86       615
weighted avg   0.94      0.95      0.94       615

---

## 🔜 Améliorations possibles

- Ajouter plus de données d'entraînement
- Raffiner l’annotation des entités
- Ajuster les hyperparamètres (batch size, learning rate, etc.)

