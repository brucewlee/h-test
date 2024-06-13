# H-TEST: Language Models Don’t Learn the Physical Manifestation of Language

---

[Paper](https://arxiv.org/abs/2402.11349) 
[Twitter Thread](https://twitter.com/BruceWLee1/status/1801046746505630042)

---

This repository contains the code and data for the paper "Language Models Don't Learn the Physical Manifestation of Language". The paper introduces H-TEST, a series of tasks designed to assess the ability of language models to understand and utilize the visual and auditory properties of language.

<div style="text-align: center;">
<img src="resources/task.png" alt="drawing" width="600"/>
</div>

## Overview
The key components of this repository are:

- data/: Contains scripts for generating test instances for each task in H-TEST.
- generate_train_data.py: Script for generating training data for fine-tuning experiments.
- run_test.py: Main script for running H-TEST on various language models.
- run_letter_geometry_test.py: Script for running the Letter Geometry challenge on language models.
- utils.py: Utility functions for interacting with language model APIs and processing responses.

## Usage

### Running H-TEST
To run H-TEST on a set of language models, modify the model_list and other setups in run_test.py to include the models you wish to test, and then run the script:

```
python run_test.py
```

The script will generate test instances, run the tests on the specified models, and print the results.

### Running the Letter Geometry Challenge
To run the Letter Geometry challenge on a set of language models, modify the model_list in run_letter_geometry_test.py to include the models you wish to test, and then run the script:

```
python run_letter_geometry_test.py
```

The script will generate challenge instances, run the tests on the specified models, and print the results.

### Generating Training Data
To generate training data for fine-tuning experiments, run the generate_train_data.py script:

```
python generate_train_data.py
```

The script will generate training instances for each task in H-TEST and save them in the specified format in the train/ directory.

## Citation
If you use this code or the H-TEST benchmark in your research, please cite our paper:

```
@misc{lee2024language,
      title={Language Models Don't Learn the Physical Manifestation of Language}, 
      author={Bruce W. Lee and JaeHyuk Lim},
      year={2024},
      eprint={2402.11349},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
