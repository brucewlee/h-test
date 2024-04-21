import pandas as pd
import random

def generate(random_seed):
    # Set the random seed
    random.seed(random_seed)

    # Read the CSV file
    df = pd.read_csv('data/challenge.csv')

    # Get a shuffled list of all possible answers
    all_answers = df['answer'].tolist()
    random.shuffle(all_answers)

    # Generate a list of dictionaries with unique options
    result = []
    for index, row in df.iterrows():
        correct_answer = row['answer']
        options = [correct_answer]

        # Select unique options from the shuffled list
        for option in all_answers:
            if option != correct_answer and option not in options:
                options.append(option)
                if len(options) == 4:
                    break

        # Shuffle the options
        random.shuffle(options)

        # Find the index of the correct answer
        answer_index = options.index(correct_answer)

        # Add the question, answer index, and options to the result
        result.append({"question": row['challenge'], "answer": answer_index, "options": options})

    return result