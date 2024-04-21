import random

# Separate lists for hyphenated and non-hyphenated sentence components
hyphenated_subjects = ["Mother-in-law", "Check-in", "Well-being", "Long-term", "Part-time", "High-speed", "Mass-produced", "User-friendly", "Double-check", "Second-hand"]
hyphenated_verbs = ["double-checks", "check-ins", "mass-produces", "part-times", "fast-tracks", "dry-cleans", "baby-sits", "air-drops", "proof-reads", "second-guesses"]
hyphenated_objects = ["a well-being", "a check-in", "a second-hand", "a long-term plan", "a part-time job", "a high-speed chase", "a mass-produced item", "a user-friendly interface", "a double-check", "a mother-in-law"]

subjects = ["The elephant", "An owl", "The vendor", "My umbrella", "This engine", "An apple", "An octopus", "An iguana", "An eagle", "Our artist"]
verbs = ["runs", "jumps", "talks", "sleeps", "teaches", "observes", "reads", "drives", "listens", "cooks"]
objects = ["in the park", "on the wall", "quickly", "all night", "with passion", "through the telescope", "with interest", "to the city", "to music", "delicious meals"]
adverbs = ["happily", "eagerly", "slowly", "quietly", "enthusiastically", "carefully", "intently", "fast", "attentively", "expertly"]

def generate(random_seed):
    random.seed(random_seed)

    sentences_with_hyphen = []
    sentences_without_hyphen = []

    while len(sentences_with_hyphen) < 150:
        # Randomly choose which component to be hyphenated
        hyphenated_component = random.choice(["subject", "verb", "object"])

        if hyphenated_component == "subject":
            subject = random.choice(hyphenated_subjects)
            verb = random.choice(verbs)
            object = random.choice(objects)
        elif hyphenated_component == "verb":
            subject = random.choice(subjects)
            verb = random.choice(hyphenated_verbs)
            object = random.choice(objects)
        else:  # hyphenated_component == "object"
            subject = random.choice(subjects)
            verb = random.choice(verbs)
            object = random.choice(hyphenated_objects)

        adverb = random.choice(adverbs)
        sentence_with_hyphen = f"{subject} {verb} {object} {adverb}."
        if sentence_with_hyphen not in sentences_with_hyphen:
            sentences_with_hyphen.append(sentence_with_hyphen)

    while len(sentences_without_hyphen) < 150:
        subject = random.choice(subjects)
        verb = random.choice(verbs)
        object = random.choice(objects)
        adverb = random.choice(adverbs)
        sentence_without_hyphen = f"{subject} {verb} {object} {adverb}."
        if sentence_without_hyphen not in sentences_without_hyphen:
            sentences_without_hyphen.append(sentence_without_hyphen)

    true_instances = sentences_with_hyphen
    false_instances = sentences_without_hyphen

    return true_instances, false_instances