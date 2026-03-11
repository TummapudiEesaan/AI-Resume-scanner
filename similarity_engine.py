"""
Similarity Engine Module
========================
Handles text preprocessing, TF-IDF vectorization, and cosine similarity
computation between a job description and candidate resumes.
"""

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _ensure_nltk_data():
    """Download required NLTK data if not already present."""
    for resource in ["punkt", "punkt_tab", "stopwords"]:
        try:
            nltk.data.find(f"tokenizers/{resource}" if "punkt" in resource else f"corpora/{resource}")
        except LookupError:
            nltk.download(resource, quiet=True)


def preprocess_text(text):
    """
    Clean and normalize text for NLP processing.

    Steps:
        1. Convert to lowercase
        2. Remove punctuation
        3. Remove stop words
        4. Tokenize words

    Args:
        text (str): Raw text string.

    Returns:
        str: Cleaned and preprocessed text.
    """
    _ensure_nltk_data()

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra whitespace and special characters
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words and len(token) > 1]

    return " ".join(tokens)


def compute_similarity(job_description, resumes_dict):
    """
    Compute cosine similarity between a job description and multiple resumes.

    Args:
        job_description (str): The raw job description text.
        resumes_dict (dict): Dictionary mapping {filename: raw_resume_text}.

    Returns:
        list[tuple]: Sorted list of (filename, similarity_percentage) tuples,
                     ordered from highest to lowest similarity.
    """
    if not resumes_dict:
        print("[WARNING] No resumes to compare.")
        return []

    # Preprocess all texts
    processed_job = preprocess_text(job_description)
    processed_resumes = {name: preprocess_text(text) for name, text in resumes_dict.items()}

    # Combine all documents: job description first, then resumes
    filenames = list(processed_resumes.keys())
    all_documents = [processed_job] + [processed_resumes[name] for name in filenames]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_documents)

    # Separate job description vector (first row) from resume vectors
    job_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]

    # Calculate cosine similarity
    similarities = cosine_similarity(job_vector, resume_vectors).flatten()

    # Create results as (filename, percentage) tuples
    results = []
    for i, filename in enumerate(filenames):
        score_percent = round(similarities[i] * 100, 2)
        results.append((filename, score_percent))

    # Sort by similarity score in descending order
    results.sort(key=lambda x: x[1], reverse=True)

    return results
