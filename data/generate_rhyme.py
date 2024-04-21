import random
import pronouncing

def generate(random_seed):
    random.seed(random_seed)

    words = sorted([
        "time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand", "child", "eye", "woman", "place", "work", "week", "case", "point", "government", "number", "group", "problem", "fact", "be", "have", "do", "say", "get", "make", "go", "know", "take", "see", "come", "think", "look", "want", "give", "use", "find", "tell", "ask", "work", "seem", "feel", "try", "leave", "call", "park", "wall", "quickly", "night", "passion", "telescope", "interest", "city", "music", "meals"
    ])

    # Function to generate unique rhyming phrases with different spellings (ear rhymes)
    rhyming_phrases = set()
    while len(rhyming_phrases) < 150:
        word1 = random.choice(words)
        rhymes = pronouncing.rhymes(word1)
        for word2 in rhymes:
            # Check if the endings are spelled differently and if the pair is unique
            if word1[-2:] != word2[-2:] and f"{word1} {word2}" not in rhyming_phrases:
                rhyming_phrases.add(f"{word1} {word2}")
                break
        if len(rhyming_phrases) == 150:
            break

    # Function to generate non-rhyming phrases
    non_rhyming_phrases = set()
    while len(non_rhyming_phrases) < 150:
        word1, word2 = random.sample(words, 2)
        if word2 not in pronouncing.rhymes(word1) and word1 not in pronouncing.rhymes(word2):
            non_rhyming_phrases.add(f"{word1} {word2}")

    # Generate rhyming and non-rhyming phrases
    true_instances = list(rhyming_phrases)[:150]
    false_instances = list(non_rhyming_phrases)[:150]

    return true_instances, false_instances
