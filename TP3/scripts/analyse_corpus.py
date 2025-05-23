# analyse_corpus.py

import os
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'TP2', 'data', 'raw_articles'))

def lire_articles():
    textes = []
    for nom_fichier in os.listdir(DATA_DIR):
        if nom_fichier.endswith('.txt'):
            chemin = os.path.join(DATA_DIR, nom_fichier)
            with open(chemin, 'r', encoding='utf-8') as f:
                textes.append(f.read())
    return textes

def analyser_longueurs(textes):
    longueurs = [len(word_tokenize(texte, preserve_line=True)) for texte in textes]
    plt.hist(longueurs, bins=10, color='skyblue', edgecolor='black')
    plt.title("Distribution des longueurs d’articles (en nombre de mots)")
    plt.xlabel("Nombre de mots")
    plt.ylabel("Nombre d’articles")
    plt.show()

def mots_frequents(textes, top_n=20):
    mots = []
    stop_words = set(stopwords.words('french'))
    for texte in textes:
        tokens = word_tokenize(texte.lower())
        mots += [mot for mot in tokens if mot.isalpha() and mot not in stop_words]
    compteur = Counter(mots)
    print("\nTop mots fréquents :")
    for mot, freq in compteur.most_common(top_n):
        print(f"{mot}: {freq}")

    # Optionnel : visualisation simple
    mots, freqs = zip(*compteur.most_common(top_n))
    plt.bar(mots, freqs, color='orange')
    plt.xticks(rotation=45)
    plt.title("Mots les plus fréquents")
    plt.xlabel("Mot")
    plt.ylabel("Fréquence")
    plt.tight_layout()
    plt.show()

def main():
    textes = lire_articles()
    analyser_longueurs(textes)
    mots_frequents(textes)

if __name__ == "__main__":
    main()
