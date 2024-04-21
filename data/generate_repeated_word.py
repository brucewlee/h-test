import random

# Lists for sentence components
subjects = ["The cat", "Dog", "She", "He", "Teacher", "Neighbor", "Scientist", "Book", "Car", "Friend"]
verbs = ["runs", "jumps", "talks", "sleeps", "teaches", "observes", "reads", "drives", "listens", "cooks"]
objects = ["park", "wall", "quickly", "night", "passion", "telescope", "interest", "city", "music", "meals"]
adverbs = ["happily", "eagerly", "slowly", "quietly", "enthusiastically", "carefully", "intently", "fast", "attentively", "expertly"]

def generate(random_seed):
    random.seed(random_seed)

    # Lists to store sentences
    incorrect_sentences = []
    incorrect_sentences_with_repetition = []

    # Function to create a grammatically incorrect sentence
    def create_incorrect_sentence():
        parts = [random.choice(subjects), random.choice(verbs), random.choice(objects), random.choice(adverbs)]
        # Randomly shuffle the parts of the sentence
        random.shuffle(parts)
        return " ".join(parts) + "."

    # Generate grammatically incorrect sentences
    while len(incorrect_sentences) < 150:
        sentence = create_incorrect_sentence()
        if sentence not in incorrect_sentences:
            incorrect_sentences.append(sentence)

    # Generate grammatically incorrect sentences with a repeated word
    while len(incorrect_sentences_with_repetition) < 150:
        sentence = create_incorrect_sentence().split()
        insert_position = random.randint(0, len(sentence)-1)
        sentence.insert(insert_position, sentence[insert_position])
        sentence = ' '.join(sentence)
        if sentence not in incorrect_sentences_with_repetition:
            incorrect_sentences_with_repetition.append(sentence)

    true_instances = incorrect_sentences_with_repetition
    false_instances = incorrect_sentences

    return true_instances, false_instances