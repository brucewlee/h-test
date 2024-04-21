import random

# Lists for sentence components
subjects = ["The cat", "A dog", "The teacher", "Our neighbor", "The scientist", "This book", "The car", "My friend", "A painter", "The moon", "Artist", "Astronaut", "Island", "Orchestra", "Urchin", "Albatross", "Elevator", "Insect", "Opera", "Unicorn", "Airport", "Dog", "Cat", "Tree", "House", "Car", "Book", "Teacher", "Friend", "Scientist", "Neighbor", "Mountain", "River", "School", "Giraffe", "Penguin", "Butterfly", "Train", "Kangaroo", "Lion", "Flower"]

verbs = ["runs", "jumps", "talks", "sleeps", "teaches", "observes", "reads", "drives", "listens", "cooks", "paints", "glows", "cooks", "flows", "travels", "calculates", "dances", "grows", "sings", "ticks"]

nouns = ["apples", "trees", "books", "cars", "paintings", "stars", "computers", "birds", "songs", "ideas"]

adverbs = ["happily", "eagerly", "slowly", "quietly", "enthusiastically", "carefully", "intently", "fast", "attentively", "expertly", "creatively", "brightly", "skillfully", "smoothly", "adventurously", "accurately", "gracefully", "steadily", "melodiously", "consistently"]

numbers_spelled_out = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

numbers_numeric = [str(i) for i in range(1, 21)]

def generate(random_seed):
    random.seed(random_seed)

    # Lists to store sentences
    sentences_with_spelled_out_numbers = []
    sentences_with_numeric_numbers = []

    # Generate sentences with spelled-out numbers
    while len(sentences_with_spelled_out_numbers) < 150:
        sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(numbers_spelled_out) + " " + random.choice(nouns) + " " + random.choice(adverbs) + "."
        if sentence not in sentences_with_spelled_out_numbers:
            sentences_with_spelled_out_numbers.append(sentence)

    # Generate sentences with numeric numbers
    while len(sentences_with_numeric_numbers) < 150:
        sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(numbers_numeric) + " " + random.choice(nouns) + " " + random.choice(adverbs) + "."
        if sentence not in sentences_with_numeric_numbers:
            sentences_with_numeric_numbers.append(sentence)

    true_instances = sentences_with_spelled_out_numbers
    false_instances = sentences_with_numeric_numbers

    return true_instances, false_instances