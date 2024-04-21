import random

# Lists for sentence components
subjects = ["Elephant", "Owl", "Ice cream", "Umbrella", "Engine", "Apple", "Octopus", "Iguana", "Eagle", "Artist", "Astronaut", "Island", "Orchestra", "Urchin", "Albatross", "Elevator", "Insect", "Opera", "Unicorn", "Airport", "Dog", "Cat", "Tree", "House", "Car", "Book", "Teacher", "Friend", "Scientist", "Neighbor", "Mountain", "River", "School", "Giraffe", "Penguin", "Butterfly", "Train", "Kangaroo", "Lion", "Flower"]

objects = ["in the park", "on the wall", "very quickly", "all night", "with passion", "through the telescope", "with interest", "to the city", "to music", "delicious meals", "in the studio", "in the sky", "in the kitchen", "along the valley", "in space", "with precision", "in the hall", "in the forest", "in the morning", "every second"]

punctuations = [".", "?", "!", "..."]

def generate(random_seed):
    random.seed(random_seed)

    # Lists to store sentences
    sentences_with_punctuation = []
    sentences_without_punctuation = []

    while len(sentences_with_punctuation) < 150:
        sentence = random.choice(subjects) + " " + random.choice(objects) + " " + random.choice(subjects)
        punctuation = random.choice(punctuations)
        full_sentence = sentence + punctuation
        if full_sentence not in sentences_with_punctuation:
            sentences_with_punctuation.append(full_sentence)

    while len(sentences_without_punctuation) < 150:
        subject = random.choice(subjects)
        obj = random.choice(objects)
        subject2 = random.choice(subjects)
        punctuation = random.choice(punctuations)

        # Random position for punctuation in false instances
        parts = [subject, obj, subject2]
        punct_position = random.randint(1, 2)  # Position between subject, verb, and object
        parts.insert(punct_position, punctuation)

        full_sentence = " ".join(parts)
        if full_sentence not in sentences_without_punctuation:
            sentences_without_punctuation.append(full_sentence)

    true_instances = sentences_with_punctuation
    false_instances = sentences_without_punctuation

    return true_instances, false_instances