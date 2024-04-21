from litellm import completion
from typing import List, Optional, Dict
import litellm
import time

#litellm.set_verbose=True

def prompter(true_examples, false_examples, test, chain_of_thought = False):
    output = []
    
    # Iterate over the maximum length of true or false examples
    for i in range(max(len(true_examples), len(false_examples))):
        if i < len(true_examples):
            output.append(f'Input: "{true_examples[i]}" Label: A')
        if i < len(false_examples):
            output.append(f'Input: "{false_examples[i]}" Label: B')
    
    if chain_of_thought == False:
        # Add the test case with its label
        output.append(f'\nInput: "{test}" Label: \nA \nB (Respond in one letter and nothing else)')
    else:
        output.append(f'\nNow, think out loud step by step and assign label. \nInput: "{test}" Label: \nA \nB')

    return '\n'.join(output)

def challenge_prompter(test_instance):
    # Extract the question and options from the dictionary
    question = test_instance["question"]
    options = test_instance["options"]
    answer = test_instance["options"][test_instance['answer']]

    # Format the question and options
    output = question + '\n' + '\n'.join(options) + '(Respond in one letter and nothing else)'

    return output, answer

def get_response(model: str, 
                 messages: List[dict],
                 max_tokens: Optional[int] = None, 
                 temperature: Optional[float] = None, 
                 top_p: Optional[float] = None, 
                 n: Optional[int] = None, 
                 presence_penalty: Optional[float] = None, 
                 frequency_penalty: Optional[float] = None, 
                 stop: Optional[List[str]] = None,
                 other_params: Optional[Dict] = None,
                 chain_of_thought = False
                ) -> str:
    if chain_of_thought == False and max_tokens == None:
        max_tokens = 5
    # Combine all parameters for the API call
    api_params = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "n": n,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "stop": stop,
        'num_retries': 500,
    }
    if other_params:
        api_params.update(other_params)
    response = completion(**api_params)
    return response.choices[0].message.content if response.choices else "No response generated"


def determine_binary_answers(model_response, chain_of_thought = False):
    # Normalize string to handle case and whitespace variations
    model_response = model_responseresponse.get('choices', [{}])[0].get('message', {}).get('content') # gemini
    #normalized_string = model_response.strip().lower()

    if chain_of_thought == False:
        # Check various cases
        if (("a" in normalized_string and "b" not in normalized_string) 
            or 'label: a' in normalized_string 
            or ('is a' in normalized_string and 'or b' not in normalized_string)
            ):
            print(f'True:{model_response}')
            return True
        elif (("b" in normalized_string and "a" not in normalized_string) 
            or 'label: b' in normalized_string 
            or ('is b' in normalized_string  and 'or a' not in normalized_string)
            ):
            print(f'False:{model_response}')
            return False
        else:
            print(f'None:{model_response}')
            return None
    else:
        api_params = {
            "model": "gpt-3.5-turbo-0613",
            "messages": [{"content": f'Assistant: {model_response} \n\n What does the Assistant think the sentence belongs to?\nA\nB\nNone (Respond in one word and nothing else)', "role": "user"}],
            "max_tokens": 5,
            "temperature": 0.7,
            "top_p": None,
            "n": None,
            "presence_penalty": None,
            "frequency_penalty": None,
            "stop": None,
            'num_retries': 500,
        }
        print(model_response)
        judge_response = completion(**api_params)

        return determine_binary_answers(judge_response.choices[0].message.content if judge_response.choices else "No response generated")
        