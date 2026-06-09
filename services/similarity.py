from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def compare_documents(doc1, doc2):

    emb1 = model.encode([doc1])

    emb2 = model.encode([doc2])

    score = cosine_similarity(
        emb1,
        emb2
    )[0][0]

    return float(round(score * 100, 2))