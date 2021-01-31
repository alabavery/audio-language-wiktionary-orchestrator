import os
import json

import run_step


def main(lemmas_dir, data_dir, pipeline_step_getter):
    lemma_word_list_dir = make_lemmas_words_list(lemmas_dir, data_dir)

    for step in pipeline_step_getter(lemma_word_list_dir):
        if step["name"] == "lemmas":
            break
        run_step.run(step)


def make_lemmas_words_list(lemmas_dir, target_dir):
    with open(os.path.join(lemmas_dir, "lemmas.json"), 'r') as f:
        lemma_data = json.loads(f.read())
    
    content_lists = [d["Content"] for d in lemma_data if d["HasContent"]]
    lemmas = []
    for content_list in content_lists:
        for content_item in content_list:
            lemmas += content_item["Lemma"]
    
    output_dir = os.path.join(target_dir, 'lemmas_regroup_word_list')
    with open(os.path.join(output_dir, 'words.json'), 'w') as f:
        f.write(json.dumps(lemmas))
    return output_dir
