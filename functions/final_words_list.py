import os
import json

def make(words_directory, lemma_words_directory, final_words_dir):
    with open(os.path.join(words_directory, 'words.json'), 'r') as f:
        original_words = json.loads(f.read())
    with open(os.path.join(lemma_words_directory, 'words.json'), 'r') as f:
        lemmas = json.loads(f.read())
    # unique
    final_word_tracker = dict()
    for word in original_words:
        final_word_tracker[word] = True
    for word in lemmas:
        final_word_tracker[word] = True
    final_words = list(final_word_tracker.keys())

    with open(os.path.join(final_words_dir, 'words.json'), 'w') as f:
        f.write(json.dumps(final_words))
