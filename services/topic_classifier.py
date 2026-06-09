TOPICS = {
    "Economy": [
        "economy", "tax", "gdp", "investment",
        "business", "inflation", "manufacturing"
    ],

    "Healthcare": [
        "health", "hospital", "medicine",
        "doctor", "insurance", "medical"
    ],

    "Education": [
        "education", "school", "college",
        "university", "student", "teacher"
    ],

    "Employment": [
        "employment", "jobs", "skill",
        "worker", "salary", "startup"
    ],

    "Agriculture": [
        "farmer", "crop", "agriculture",
        "irrigation", "fertilizer", "rural"
    ]
}


def classify_topics(text):

    text = text.lower()

    scores = {}

    total = 0

    for topic, keywords in TOPICS.items():

        count = 0

        for keyword in keywords:
            count += text.count(keyword)

        scores[topic] = count
        total += count

    if total == 0:
        return scores

    percentages = {}

    for topic, count in scores.items():
        percentages[topic] = round(
            (count / total) * 100,
            2
        )

    return percentages