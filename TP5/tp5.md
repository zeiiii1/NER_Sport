# TP5 – Fine-tuning du modèle pré-entraîné CamemBERT

---

## 🎯 Objectif

Adapter le modèle `camembert-base` à notre tâche de NER sur les articles sportifs français via un fine-tuning supervisé avec les données annotées.

---

## 🧠 Modèle sélectionné

- **Architecture** : Transformer type BERT
- **Modèle** : `camembert-base` (disponible sur Hugging Face)
- **Tête de classification** : classification token-level avec `num_labels` = nombre d’étiquettes NER

---

## 🧾 Format des données

Les données doivent être au format compatible avec `datasets` de Hugging Face :  
Chaque exemple est un dictionnaire avec :

```json
{
  "tokens": ["Kylian", "Mbappé", "a", "marqué", "deux", "buts"],
  "ner_tags": [1, 2, 0, 0, 0, 0]
}
```

`tokens` : liste de mots
`ner_tags` : indices d’étiquettes (O, B-PER, I-PER, etc.)

---

## 🧰 Entraînement avec Hugging Face Trainer

🔧 Étapes
Tokenisation avec CamembertTokenizerFast
Entraînement avec Trainer
Évaluation automatique possible (précision, rappel, F1)