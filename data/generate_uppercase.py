import random

# Expanded lists
subjects = ["Elephant", "Owl", "Ice cream", "Umbrella", "Engine", "Apple", "Octopus", "Iguana", "Eagle", "Artist", "Astronaut", "Island", "Orchestra", "Urchin", "Albatross", "Elevator", "Insect", "Opera", "Unicorn", "Airport", "Dog", "Cat", "Tree", "House", "Car", "Book", "Teacher", "Friend", "Scientist", "Neighbor", "Mountain", "River", "School", "Giraffe", "Penguin", "Butterfly", "Train", "Kangaroo", "Lion", "Flower"]

verbs = ["runs", "jumps", "talks", "sleeps", "teaches", "observes", "reads", "drives", "listens", "cooks", "paints", "glows", "cooks", "flows", "travels", "calculates", "dances", "grows", "sings", "ticks"]

objects = ["in the park", "on the wall", "very quickly", "all night", "with passion", "through the telescope", "with interest", "to the city", "to music", "delicious meals", "in the studio", "in the sky", "in the kitchen", "along the valley", "in space", "with precision", "in the hall", "in the forest", "in the morning", "every second"]

adverbs = ["happily", "eagerly", "slowly", "quietly", "enthusiastically", "carefully", "intently", "fast", "attentively", "expertly", "creatively", "brightly", "skillfully", "smoothly", "adventurously", "accurately", "gracefully", "steadily", "melodiously", "consistently"]

def capitalize_random_character(sentence):
    sentence = sentence.lower()
    char_index = random.randint(0, len(sentence) - 2)  # Exclude the last period
    return sentence[:char_index] + sentence[char_index].upper() + sentence[char_index + 1:]

def generate(random_seed):
    random.seed(random_seed)

    # Using lists to maintain order
    uppercase_sentences = []
    lowercase_sentences = []

    while len(uppercase_sentences) < 150:
        sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + " " + random.choice(adverbs) + "."
        if sentence not in uppercase_sentences:
            uppercase_sentences.append(sentence)

    while len(lowercase_sentences) < 150:
        sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + " " + random.choice(adverbs) + "."
        if sentence not in lowercase_sentences:
            lowercase_sentences.append(sentence)

    # Converting lists to uppercase and lowercase
    true_instances = [capitalize_random_character(sentence) for sentence in uppercase_sentences]
    false_instances = [sentence.lower() for sentence in lowercase_sentences]

    return true_instances, false_instances