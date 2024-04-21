import random

# Sample subjects and objects for the sentences
subjects = ["The value of x", "The sum", "The integral", "The derivative", "The limit", "The fraction", "The product", "The square root", "The cube of", "The angle"]
objects = ["5", "7", "10", "3", "12", "6", "8", "4", "9", "11"]

# Expanded mathematical operations spelled out and as symbols
spelled_math_operations = ["plus", "minus", "times", "divided by", "equals to", "greater than", "less than", "approximately equal to", "to the power of", "modulo"]
symbol_math_operations = ["+", "-", "*", "/", "=", ">", "<", "≈", "^", "%"]

def generate(random_seed):
    random.seed(random_seed)

    # Generate sentences with spelled-out math symbols
    spelled_sentences = []
    for _ in range(150):
        subject = random.choice(subjects)
        operation = random.choice(spelled_math_operations)
        obj = random.choice(objects)
        spelled_sentence = f"{subject} {operation} {obj}."
        spelled_sentences.append(spelled_sentence)

    # Generate sentences with actual math symbols
    symbol_sentences = []
    for _ in range(150):
        subject = random.choice(subjects)
        operation = random.choice(symbol_math_operations)
        obj = random.choice(objects)
        symbol_sentence = f"{subject} {operation} {obj}."
        symbol_sentences.append(symbol_sentence)

    true_instances = spelled_sentences
    false_instances = symbol_sentences

    return true_instances, false_instances