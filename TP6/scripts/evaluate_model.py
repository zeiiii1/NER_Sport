import os
import json
import torch
from datetime import datetime
from transformers import CamembertTokenizerFast, CamembertForTokenClassification
from datasets import load_dataset
from seqeval.metrics import classification_report

# ------------------------------
# 🔹 Labels
# ------------------------------
label_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC', 'B-EVENT', 'I-EVENT']
id2label = {i: l for i, l in enumerate(label_list)}
label2id = {l: i for i, l in enumerate(label_list)}

# ------------------------------
# 🔹 Trouver le dernier checkpoint dans TP5/model
# ------------------------------
base_model_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'TP5', 'model'))
checkpoints = [d for d in os.listdir(base_model_dir) if d.startswith("checkpoint-")]
if not checkpoints:
    raise FileNotFoundError("Aucun checkpoint trouvé dans TP5/model/. Lance d'abord l'entraînement.")
latest_checkpoint = sorted(checkpoints, key=lambda x: int(x.split("-")[1]))[-1]
model_dir = os.path.join(base_model_dir, latest_checkpoint)

# ------------------------------
# 🔹 Charger le tokenizer et le modèle
# ------------------------------
tokenizer = CamembertTokenizerFast.from_pretrained("camembert-base")
model = CamembertForTokenClassification.from_pretrained(model_dir)
model.eval()

# ------------------------------
# 🔹 Charger les données de test
# ------------------------------
test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'TP5', 'data', 'test.json'))
dataset = load_dataset("json", data_files={"test": test_path})["test"]

# ------------------------------
# 🔹 Évaluation
# ------------------------------
predictions = []
references = []

for item in dataset:
    tokens = item["tokens"]
    true_labels = item["ner_tags"]
    encoding = tokenizer(tokens, is_split_into_words=True, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**encoding)
    pred_ids = torch.argmax(outputs.logits, dim=-1)[0].tolist()
    word_ids = encoding.word_ids(batch_index=0)


    pred_labels = []
    aligned_labels = []

    prev_word_idx = None
    for idx, word_idx in enumerate(word_ids):
        if word_idx is None:
            continue
        if word_idx != prev_word_idx:
            if word_idx < len(true_labels):
                aligned_labels.append(true_labels[word_idx])
                pred_labels.append(pred_ids[idx])
        prev_word_idx = word_idx

    predictions.append([id2label[p] for p in pred_labels])
    references.append([id2label[t] for t in aligned_labels])

# ------------------------------
# 🔹 Affichage et sauvegarde du rapport
# ------------------------------
report = classification_report(references, predictions)
print("✅ Rapport d'évaluation NER :\n")
print(report)

report_path = os.path.join(os.path.dirname(__file__), "..", "evaluation_report.txt")
with open(report_path, "w", encoding="utf-8") as f:
    f.write(f"# Rapport d’évaluation – {datetime.now()}\n\n")
    f.write(report)

print(f"\n📄 Rapport enregistré dans : {report_path}")
