import os
import json
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

RAW_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'TP2', 'data', 'raw_articles'))
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
os.makedirs(OUT_DIR, exist_ok=True)

KNOWN_ENTITIES = {
    "PER": ["Mbappé", "Messi", "Benzema", "Griezmann"],
    "ORG": ["PSG", "Real", "Barça", "Marseille"]
}

def label_token(token):
    for label, values in KNOWN_ENTITIES.items():
        if token in values:
            return f"B-{label}"
    return "O"

def annotate_article(text):
    tokens = word_tokenize(text, preserve_line=True)
    tags = [label_token(token) for token in tokens]
    label_map = {"O": 0}
    label_counter = 1
    ner_tags = []
    for tag in tags:
        if tag not in label_map:
            label_map[tag] = label_counter
            label_counter += 1
        ner_tags.append(label_map[tag])
    return {"tokens": tokens, "ner_tags": ner_tags}

def main():
    examples = []
    for fname in os.listdir(RAW_DIR):
        if fname.endswith(".txt"):
            with open(os.path.join(RAW_DIR, fname), "r", encoding="utf-8") as f:
                text = f.read()
                example = annotate_article(text)
                examples.append(example)

    # Split 80/20
    split = int(len(examples) * 0.8)
    train_data = examples[:split]
    test_data = examples[split:]

    with open(os.path.join(OUT_DIR, "train.json"), "w", encoding="utf-8") as f:
        json.dump(train_data, f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT_DIR, "test.json"), "w", encoding="utf-8") as f:
        json.dump(test_data, f, indent=2, ensure_ascii=False)

    print("✅ Corpus annoté automatiquement sauvegardé dans TP5/data/")

if __name__ == "__main__":
    main()
