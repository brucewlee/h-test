import random
import json
import utils
import os
from tqdm import tqdm
from pprint import pprint
from data import generate_letter_geometry

"""Dataset Collection
"""
def gen_data(random_seed):
    return generate_letter_geometry.generate(random_seed)

def run_test(model = "gpt-3.5-turbo-0613", model_temperature = 0.7, random_seed = 12062023, api_key = None):
    # keys
    for key_cat, key in api_key.items():
        os.environ[key_cat] = key

    challenge_data = gen_data(random_seed)
    
    n_correct = 0
    n_total = 0
    for test_instance in tqdm(challenge_data):
        response = utils.get_response(
            model = model, 
            messages = [{"content": utils.challenge_prompter(test_instance)[0], "role": "user"}], 
            temperature = model_temperature,
            max_tokens = 1
        )
        n_total += 1
        if response.strip() == utils.challenge_prompter(test_instance)[1]:
            n_correct += 1
    
    return n_total, n_correct

api_key = {
    "OPENAI_API_KEY": "",
    "COHERE_API_KEY": "",
    "HUGGINGFACE_API_KEY": "" ,
    'AI21_API_KEY': "",
    "REPLICATE_API_KEY": "",
    "ALEPHALPHA_API_KEY": "",
    "AWS_ACCESS_KEY_ID": "",
    "AWS_SECRET_ACCESS_KEY": "",
    "AWS_REGION_NAME": ""
}

model_list = ["command"] # ["command", "gpt-3.5-turbo-0613", "gpt-4-0613"]
result = []
for model in tqdm(model_list):
    model_dir = model.split("/")[-1]
    output = run_test(model= model, api_key=api_key)
    result.append({
        'model': model,
        'n_total': output[0],
        'n_correct': output[1]
    })
pprint(result)