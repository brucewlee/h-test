import csv
import json
import os
import random
from data.generate_end_ly import generate as generate_end_ly
from data.generate_end_punctuation import generate as generate_end_punctuation
from data.generate_hyphenated_word import generate as generate_hyphenated_word
from data.generate_palindrome import generate as generate_palindrome
from data.generate_repeated_word import generate as generate_repeated_word
from data.generate_rhyme import generate as generate_rhyme
from data.generate_spelled_math import generate as generate_spelled_math
from data.generate_spelled_number import generate as generate_spelled_number
from data.generate_start_vowel import generate as generate_start_vowel
from data.generate_uppercase import generate as generate_uppercase


# Save generated training data to JSONL in the specified format
def save_to_jsonl_with_format(file_path, true_data, false_data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as jsonlfile:
        for line in true_data:
            data = {
                "messages": [
                    {"role": "user", "content": line},
                    {"role": "assistant", "content": 'A'}
                ]
            }
            jsonlfile.write(json.dumps(data) + '\n')
        for line in false_data:
            data = {
                "messages": [
                    {"role": "user", "content": line},
                    {"role": "assistant", "content": 'B'}
                ]
            }
            jsonlfile.write(json.dumps(data) + '\n')


def generate_data_for_task(generate_func, num_items=5000, random_seed=42):
    true_instances, false_instances = [], []
    while len(true_instances) < num_items // 2:
        t, f = generate_func(random_seed)
        true_instances.extend(t)
        false_instances.extend(f)
        random_seed += 1  # To vary the seed for each generation call
    return true_instances[:num_items // 2], false_instances[:num_items // 2]

# Load test data from JSONL file
def load_test_data(file_path):
    test_data = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line)
            test_data.add(item['centerpiece'])
    return test_data

# Define your tasks and their corresponding generation functions
tasks = {
    "end_ly": generate_end_ly,
    "end_punctuation": generate_end_punctuation,
    "hyphenated_word": generate_hyphenated_word,
    "palindrome": generate_palindrome,
    "repeated_word": generate_repeated_word,
    "rhyme": generate_rhyme,
    "spelled_math": generate_spelled_math,
    "spelled_number": generate_spelled_number,
    "start_vowel": generate_start_vowel,
    "uppercase": generate_uppercase
}

# Path to your test data and training data directory
test_data_dir = "htest_generated_with_seed_12062023"
train_data_dir = "train"

# Process each task
for task_name, generate_func in tasks.items():
    print(f"Processing task: {task_name}")
    test_file_path = os.path.join(test_data_dir, f"{task_name}_test.jsonl")
    train_file_path = os.path.join(train_data_dir, f"{task_name}_train.jsonl")

    # Load test data to exclude from training data
    test_data = load_test_data(test_file_path)

    # Generate training data
    true_data, false_data = generate_data_for_task(generate_func, 1000)

    # Filter out any test data from the generated training data
    true_data_filtered = [item for item in true_data if item not in test_data]
    false_data_filtered = [item for item in false_data if item not in test_data]

    # Save the filtered training data to JSONL in the specified format
    save_to_jsonl_with_format(train_file_path, true_data_filtered, false_data_filtered)
