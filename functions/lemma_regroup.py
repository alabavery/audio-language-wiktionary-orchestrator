import os
import json

import run_step
from colors import Bcolors as bc


def main(lemmas_dir, data_dir, pipeline_step_getter):
    lemma_word_list_dir = make_lemmas_words_list(lemmas_dir, data_dir)

    print(f"{bc.WARNING} \n\n\nBegin lemma-regroup sub-steps")
    print("----------------------------------------------------------------------------------------------")
    print(f"{bc.ENDC}")


    for step in pipeline_step_getter(lemma_word_list_dir):
        if step["name"] == "lemmas":
            break
        run_step.run(step)

    print(f"{bc.WARNING} End lemma-regroup sub-steps")
    print("---------------------------------------------------------------------------------------------")
    print(f"{bc.ENDC}")


def make_lemmas_words_list(lemmas_dir, target_dir):
    paths = [os.path.join(lemmas_dir, f) for f in os.listdir(lemmas_dir)]

    def get_lemmas_from_path(path):
        with open(path, 'r') as f:
            content = json.loads(f.read())
        l = []
        for item in content:
            l = l + (item["lemmas"] if item["exists"] else [])
        return l

    lemmas = []
    for path in paths:
        lemmas += get_lemmas_from_path(path)
    
    output_dir = os.path.join(target_dir, 'lemmas_regroup_word_list')
    with open(os.path.join(output_dir, 'words.json'), 'w') as f:
        f.write(json.dumps(lemmas))
    return output_dir
