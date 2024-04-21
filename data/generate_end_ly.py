import random

# Lists for sentence components
subjects = ["Cat", "Dog", "She", "He", "Teacher", "Neighbor", "Scientist", "Book", "Car", "Friend", "Painter", "Moon", "Chef", "River", "Astronaut", "Computer", "Dancer", "Tree", "Bird", "Clock"]

verbs = ["runs", "jumps", "talks", "sleeps", "teaches", "observes", "reads", "drives", "listens", "cooks", 
         "paints", "glows", "flows", "travels", "calculates", "dances", "grows", "sings", "ticks"]

objects = ["in the park", "on the wall", "very quickly", "all night", "with passion", "through the telescope", 
           "with interest", "to the city", "to music", "delicious meals", "in the studio", "in the sky", 
           "in the kitchen", "along the valley", "in space", "with precision", "in the hall", "in the forest", 
           "in the morning", "every second"]

# Adverbs ending with 'ly' and with something else
adverbs_ending_ly = ["happily", "eagerly", "slowly", "quietly", "enthusiastically", "carefully", "intently", 
                     "attentively", "expertly", "creatively", "brightly", "skillfully", "smoothly", "adventurously", 
                     "accurately", "gracefully", "steadily", "melodiously", "consistently"]

adverbs_ending_else = ["very", "quite", "almost", "too", "enough", "so", "just", "well", "fast", "hard", 
                       "late", "early", "long", "far", "high", "low", "near", "straight", "wrong", "right"]

def generate(random_seed):
    random.seed(random_seed)

    sentences_with_ly = []
    sentences_with_else = []

    # Generate sentences with adverbs ending in 'ly'
    while len(sentences_with_ly) < 150:
        sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + " " + random.choice(adverbs_ending_ly) + "."
        if sentence not in sentences_with_ly:
            sentences_with_ly.append(sentence)

    # Generate sentences with adverbs ending in something else
    while len(sentences_with_else) < 150:
        sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + " " + random.choice(adverbs_ending_else) + "."
        if sentence not in sentences_with_else:
            sentences_with_else.append(sentence)

    true_instances = sentences_with_ly
    false_instances = sentences_with_else

    return true_instances, false_instances