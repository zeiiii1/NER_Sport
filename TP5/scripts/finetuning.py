from transformers import (
    CamembertTokenizerFast,
    CamembertForTokenClassification,
    Trainer,
    TrainingArguments,
    DataCollatorForTokenClassification
)
from datasets import load_dataset

# ------------------------------
# 🔹 Chargement du dataset JSON
# ------------------------------
dataset = load_dataset(
    "json",
    data_files={
        "train": "../data/train.json",
        "test": "../data/test.json"
    }
)

# ------------------------------
# 🔹 Définition des labels NER
# ------------------------------
label_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC', 'B-EVENT', 'I-EVENT']
label2id = {label: i for i, label in enumerate(label_list)}
id2label = {i: label for label, i in label2id.items()}

# ------------------------------
# 🔹 Chargement du tokenizer et modèle
# ------------------------------
tokenizer = CamembertTokenizerFast.from_pretrained("camembert-base")
model = CamembertForTokenClassification.from_pretrained(
    "camembert-base",
    num_labels=len(label_list),
    id2label=id2label,
    label2id=label2id
)

# ------------------------------
# 🔹 Tokenisation avec alignement des labels
# ------------------------------
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(
        examples["tokens"],
        truncation=True,
        is_split_into_words=True
    )

    labels_batch = []
    for i, word_ids in enumerate(tokenized_inputs.word_ids(batch_index=i) for i in range(len(examples["tokens"]))):
        word_labels = examples["ner_tags"][i]
        aligned_labels = []
        previous_word_idx = None
        for word_idx in word_ids:
            if word_idx is None:
                aligned_labels.append(-100)
            elif word_idx != previous_word_idx:
                aligned_labels.append(word_labels[word_idx] if word_idx < len(word_labels) else -100)
            else:
                aligned_labels.append(word_labels[word_idx] if word_idx < len(word_labels) else -100)
            previous_word_idx = word_idx
        labels_batch.append(aligned_labels)

    tokenized_inputs["labels"] = labels_batch
    return tokenized_inputs

encoded_dataset = dataset.map(tokenize_and_align_labels, batched=True)

# ------------------------------
# 🔹 Configuration entraînement
# ------------------------------
training_args = TrainingArguments(
    output_dir="../model",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="../logs"
)

# ------------------------------
# 🔹 Data collator pour padding dynamique
# ------------------------------
data_collator = DataCollatorForTokenClassification(tokenizer)

# ------------------------------
# 🔹 Entraîneur Hugging Face
# ------------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_dataset["train"],
    eval_dataset=encoded_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator
)

# ------------------------------
# 🔹 Lancement de l'entraînement
# ------------------------------
trainer.train()
