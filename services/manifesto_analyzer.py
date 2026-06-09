from services.pdf_parser import extract_text
from services.preprocess import clean_text
from services.topic_classifier import classify_topics


def analyze_manifesto(path):

    text = extract_text(path)

    text = clean_text(text)

    word_count = len(text.split())

    topics = classify_topics(text)

    return {
        "word_count": word_count,
        "topic_distribution": topics
    }