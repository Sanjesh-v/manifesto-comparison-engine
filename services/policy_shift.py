from services.topic_classifier import classify_topics


def detect_policy_shift(doc1, doc2):

    topics1 = classify_topics(doc1)
    topics2 = classify_topics(doc2)

    result = {}

    for topic in topics1:

        result[topic] = {
            "old": topics1[topic],
            "new": topics2[topic],
            "change": round(
                topics2[topic] - topics1[topic],
                2
            )
        }

    return result