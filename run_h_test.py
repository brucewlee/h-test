import random
from collections import defaultdict
import json

from tqdm import tqdm
from pprint import pprint

from data import generate_spelled_math, generate_end_punctuation, generate_hyphenated_word, generate_palindrome, generate_repeated_word, generate_rhyme, generate_spelled_number, generate_start_vowel, generate_uppercase, generate_end_ly

import utils
import os


"""Dataset Collection
"""
def gen_data(random_seed):
    return {
        "end_punctuation_instances" : generate_end_punctuation.generate(random_seed),
        "hyphenated_word_instances" : generate_hyphenated_word.generate(random_seed),
        "spelled_math_instances" : generate_spelled_math.generate(random_seed),
        "palindrome_instances" : generate_palindrome.generate(random_seed),
        "end_ly_instances" : generate_end_ly.generate(random_seed),
        "repeated_word_instances" : generate_repeated_word.generate(random_seed),
        "rhyme_instances" : generate_rhyme.generate(random_seed),
        "spelled_number_instances" : generate_spelled_number.generate(random_seed),
        "start_vowel_instances" : generate_start_vowel.generate(random_seed),
        "uppercase_instances" : generate_uppercase.generate(random_seed)
    }

def process_data(h_data_ab, random_seed, k_shot):
    random.seed(random_seed)
    full_processed_data = {}

    for category, instances in h_data_ab.items():
        processed_data = defaultdict(list)

        true_test_idx = random.sample(range(0, len(instances[0])), 100)
        false_test_idx = random.sample(range(0, len(instances[1])), 100)

        # Remaining indices for examples, excluding test indices
        true_example_idx = [item for item in list(range(0, len(instances[0]))) if item not in true_test_idx][:int(k_shot/2)]
        false_example_idx = [item for item in list(range(0, len(instances[1]))) if item not in false_test_idx][:int(k_shot/2)]

        for idx in true_example_idx:
            processed_data[f'true_example'].append(instances[0][idx])

        for idx in true_test_idx:
            processed_data[f'true_test'].append(instances[0][idx])

        for idx in false_example_idx:
            processed_data[f'false_example'].append(instances[1][idx])

        for idx in false_test_idx:
            processed_data[f'false_test'].append(instances[1][idx])

        full_processed_data[category] = processed_data
        
    return full_processed_data

"""Run Test
"""
def run_test(model = "gpt-3.5-turbo-0613", model_temperature = 0.7, random_seed = 12062023, api_key = None, output_file = None, k_shot = 50, chain_of_thought = False):
    # to store results
    result_dict = defaultdict(list)

    # keys
    for key_cat, key in api_key.items():
        os.environ[key_cat] = key

    h_data_ab = gen_data(random_seed)
    full_processed_data = process_data(h_data_ab, random_seed, k_shot)
    
    for category, category_dict in full_processed_data.items():
        true_example = category_dict[f'true_example']
        true_test = category_dict[f'true_test']
        false_example = category_dict[f'false_example']
        false_test = category_dict[f'false_test']
        
        for test in tqdm(true_test):
            response = utils.get_response(
                model = model, 
                messages = [{"content": utils.prompter(true_example, false_example, test, chain_of_thought), "role": "user"}], 
                chain_of_thought = chain_of_thought,
                temperature = model_temperature
            )
            print(utils.prompter(true_example, false_example, test, chain_of_thought))

            result_dict[category].append((True, utils.determine_binary_answers(response, chain_of_thought)))

            if output_file != None:
                with open(output_file, 'w') as json_file:
                    json.dump(result_dict, json_file)
        
        for test in tqdm(false_test):
            response = utils.get_response(
                model = model, 
                messages = [{"content": utils.prompter(true_example, false_example, test, chain_of_thought), "role": "user"}], 
                chain_of_thought = chain_of_thought,
                temperature = model_temperature
            )
            print(utils.prompter(true_example, false_example, test, chain_of_thought))

            result_dict[category].append((False, utils.determine_binary_answers(response, chain_of_thought)))

            if output_file != None:
                with open(output_file, 'w') as json_file:
                    json.dump(result_dict, json_file)

    return result_dict
        

def interpret(result_dict, output_file = None):
    interpreted_result_dict = {}
    for category, result in result_dict.items():
        n_correct = 0
        n_total = 0

        n_correct_if_no_response_is_ignored = 0
        n_total_if_no_response_is_ignored = 0

        for one_test in result:
            true_label = one_test[0]
            pred_label = one_test[1]

            if true_label == pred_label:
                n_correct += 1
            n_total += 1

            if pred_label != None:
                if true_label == pred_label:
                    n_correct_if_no_response_is_ignored += 1
                n_total_if_no_response_is_ignored += 1

                try:
                    acc_2 = round(n_correct_if_no_response_is_ignored/n_total_if_no_response_is_ignored, 3)
                except:
                    acc_2 = 0

        interpreted_result_dict[category] = {
            'acc': round(n_correct/n_total, 3),
            'acc (ignoring out of context response)': acc_2,
            'ratio, out of context response': round((n_total - n_total_if_no_response_is_ignored)/n_total, 3)
        }
    
    if output_file != None:
        with open(output_file, 'w') as json_file:
            json.dump(interpreted_result_dict, json_file)
    
    return interpreted_result_dict
            


api_key = {
    "OPENAI_API_KEY": "",
    "COHERE_API_KEY": "",
    "HUGGINGFACE_API_KEY": "" ,
    'AI21_API_KEY': "",
    "REPLICATE_API_KEY": "",
    "ALEPHALPHA_API_KEY": "",
    "AWS_ACCESS_KEY_ID": "",
    "AWS_SECRET_ACCESS_KEY": "",
    "AWS_REGION_NAME": "",
    "ANTHROPIC_API_KEY": "" 
}

model_list = ["anthropic/claude-3-opus-20240229"]  # ["command", "gpt-3.5-turbo-0613", "gpt-4-0613"]
k_list = [14] # [4, 50] # create directories results-{k} first

for model in model_list:
    for k in k_list:
        model_dir = model.split("/")[-1]
        result_dict = run_test(model= model, api_key=api_key, output_file=f'results-{k}/result_dict_{model_dir}.json', chain_of_thought=False)
        pprint(result_dict)

        interpreted_result_dict = interpret(result_dict, output_file=f'results-{k}/interpreted_result_dict_{model_dir}.json')
        pprint(interpreted_result_dict)
