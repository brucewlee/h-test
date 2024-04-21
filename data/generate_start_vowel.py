import random

# Expanded and more diverse lists of subjects
vowel_subjects = ["Elephant", "Owl", "Ice cream", "Umbrella", "Engine", "Apple", "Octopus", "Iguana", "Eagle", "Artist", "Astronaut", "Island", "Orchestra", "Urchin", "Albatross", "Elevator","Insect", "Opera", "Unicorn", "Airport","Artist", "Explorer", "Oasis", "Idea", "University", "Acrobat", "Internet","Omelette", "Underdog", "Alchemist","Engineer", "Olive", "Envelope", "Umpire", "Asteroid", "Economist", "Oak", "Eel", "Utopia"]

consonant_subjects = ["Dog", "Cat", "Tree", "House", "Car", "Book", "Teacher", "Friend", "Scientist", "Neighbor","Mountain", "River", "School", "Giraffe", "Penguin", "Butterfly", "Train", "Kangaroo", "Lion", "Flower","Guitar", "Bicycle", "Computer", "Photographer", "Violin", "Doctor", "Robot", "Squirrel", "Dragon", "Building","Yogurt", "Computer", "Basket", "Globe", "Balloon", "Bridge", "Yacht", "Cupcake", "Kite", "Garden"]

verbs = ["runs", "jumps", "talks", "sleeps", "teaches", "observes", "reads", "drives", "listens", "cooks", "paints", "glows", "cooks", "flows", "travels", "calculates", "dances", "grows", "sings", "ticks"]

objects = ["in the park", "on the wall", "very quickly", "all night", "with passion", "through the telescope", "with interest", "to the city", "to music", "delicious meals", "in the studio", "in the sky", "in the kitchen", "along the valley", "in space", "with precision", "in the hall", "in the forest", "in the morning", "every second"]

adverbs = ["happily", "eagerly", "slowly", "quietly", "enthusiastically", "carefully", "intently", "fast", "attentively", "expertly", "creatively", "brightly", "skillfully", "smoothly", "adventurously", "accurately", "gracefully", "steadily", "melodiously", "consistently"]

def generate(random_seed):
    random.seed(random_seed)

    # Using lists to maintain order and ensure repeatability
    vowel_sentences_list = []
    consonant_sentences_list = []

    while len(vowel_sentences_list) < 150:
        sentence = random.choice(vowel_subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + " " + random.choice(adverbs) + "."
        if sentence not in vowel_sentences_list:
            vowel_sentences_list.append(sentence)

    while len(consonant_sentences_list) < 150:
        sentence = random.choice(consonant_subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + " " + random.choice(adverbs) + "."
        if sentence not in consonant_sentences_list:
            consonant_sentences_list.append(sentence)

    true_instances = vowel_sentences_list
    false_instances = consonant_sentences_list

    return true_instances, false_instances