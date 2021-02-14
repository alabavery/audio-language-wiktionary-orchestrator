import os
import json

import run_step
from colors import Bcolors as bc


def main(lemmas_dir, data_dir, pipeline_step_getter):
    lemma_word_list_dir, lemma_to_pos = make_lemmas_words_list(lemmas_dir, data_dir)

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

    print(f"{bc.WARNING} Creating missing lemmas files")
    created = create_missing_lemmas_files(lemmas_dir, lemma_to_pos)
    print("Done creating {} missing lemmas files".format(created))
    print(f"{bc.ENDC}")


def make_lemmas_words_list(lemmas_dir, target_dir):
    paths = [os.path.join(lemmas_dir, f) for f in os.listdir(lemmas_dir)]
    part_of_speech_tracker = dict() # { [lemma]: { [pos]: true } }

    def get_lemmas_from_path(path):
        with open(path, 'r') as f:
            content = json.loads(f.read())
        l = []
        for item in content:
            if item["exists"]:
                l = l + item["lemmas"]
                for lemma in item["lemmas"]:
                    if part_of_speech_tracker.get(lemma) is None:
                        part_of_speech_tracker[lemma] = dict()
                    part_of_speech_tracker[lemma][item["part_of_speech"]] = True

        return l

    lemmas = []
    for path in paths:
        lemmas += get_lemmas_from_path(path)
    
    output_dir = os.path.join(target_dir, 'lemmas_regroup_word_list')
    with open(os.path.join(output_dir, 'words.json'), 'w') as f:
        f.write(json.dumps(lemmas))
    
    lemma_to_parts_of_speech = dict()
    for lemma in list(part_of_speech_tracker.keys()):
        lemma_to_parts_of_speech[lemma] = list(part_of_speech_tracker[lemma].keys())

    return output_dir, lemma_to_parts_of_speech


def create_missing_lemmas_files(lemmas_dir, lemma_to_parts_of_speech):
    existing = [f.split(".")[0] for f in os.listdir(lemmas_dir)]    
    lemmas = list(lemma_to_parts_of_speech.keys())
    to_create = [lemma for lemma in lemmas if lemma not in existing]

    for lemma in to_create:
        parts_of_speech = lemma_to_parts_of_speech[lemma]
        new_file_content = [{"part_of_speech": pos, "lemmas": [lemma], "exists": True } for pos in parts_of_speech]

        with open(os.path.join(lemmas_dir, lemma + ".json"), 'w') as f:
            f.write(json.dumps(new_file_content))
    return len(to_create)