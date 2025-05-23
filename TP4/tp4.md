# TP4 – Augmentation de données & Choix du modèle

---

## 🎯 Objectif

Améliorer la qualité et la diversité du corpus NER en créant un **dataset synthétique**. Ensuite, identifier **l’architecture de modèle** et un **modèle pré-entraîné** adapté à notre tâche.

---

## 🧪 1. Augmentation de données (data augmentation)

### Pourquoi ?

- Le corpus de TP2 est limité.
- Les modèles de NER s’améliorent avec des données variées.
- Augmenter les phrases permet d’améliorer la robustesse et la généralisation du modèle.

### Méthodes utilisées

1. **Paraphrases automatiques** (modification de la structure syntaxique)
2. **Remplacement d'entités par d'autres du même type** (ex : remplacer "Mbappé" par "Griezmann")
3. **Insertion de nouvelles phrases artificielles** générées avec un modèle de langue

### Outils proposés

- [`nlpaug`](https://github.com/makcedward/nlpaug) : bibliothèque Python pour augmenter du texte.
- [`textattack`](https://github.com/TextAttack/TextAttack) : outils pour génération de paraphrases.
- Modèle LLM comme GPT-2, GPT-3 (via API) ou fine-tuné localement pour produire du texte.

---

## 📁 Exemple de donnée augmentée

**Original :**

Kylian Mbappé a marqué un doublé contre l’Olympique de Marseille.

**Version synthétique :**

Griezmann a inscrit deux buts face à l’OM.

---

## 🧠 2. Choix de l’architecture adaptée

La tâche de NER nécessite de traiter une séquence mot par mot et d’assigner à chaque token une étiquette.

### Architecture choisie : **Transformers avec étiquetage par token**

- Modèle de type `BERT` avec une tête de classification token-level.
- L’entrée est une séquence de tokens → chaque token reçoit une prédiction d’étiquette (PER, LOC, ORG...).

---

## ✅ 3. Modèle choisi

### 🧩 Modèle : `CamemBERT` (de la famille BERT)

- Préentraîné sur un large corpus français.
- Performant pour les tâches de NER, POS, classification.
- Disponible via Hugging Face : `camembert-base`.

### Intégration avec `transformers` de Hugging Face

```python
from transformers import CamembertTokenizerFast, CamembertForTokenClassification

tokenizer = CamembertTokenizerFast.from_pretrained("camembert-base")
model = CamembertForTokenClassification.from_pretrained("camembert-base", num_labels=9)
```

📁 Préparation des données

Format CoNLL (token par ligne, séparé par une tabulation)

Exemple :

Kylian  B-PER
Mbappé  I-PER
a       O
marqué  O
...
