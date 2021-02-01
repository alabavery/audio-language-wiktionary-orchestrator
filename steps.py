import os

from functions import lemma_regroup


def get_steps(data_directory, language, alternate_words_directory=None):
    def get_path(sub_path):
        return os.path.join(data_directory, sub_path)
    
    words_directory = get_path('word_list') if alternate_words_directory is None else alternate_words_directory
    pages_directory = get_path('pages')
    tokens_directory = get_path('tokens')
    definitions_directory = get_path('definitions')
    lemmas_directory = get_path('lemmas')
    final_directory = get_path('combined')

    tokens_dir_successes = os.path.join(tokens_directory, 'successes')

    lemma_regroup_directory = get_path('lemma_regroup')

    print("word list path", words_directory)
    print("pages path", pages_directory)
    print("tokens path", tokens_directory)

    return [
        {
            "name": "download",
            "description": "Download wiki pages",
            "script": "downloads.sh",
            "args": [
                words_directory,
                pages_directory,
                pages_directory,
            ],
        },
        {
            "name": "tokens",
            "description": "Breakdown/tokenize wiki pages",
            "script": "tokens.sh",
            "args": [
                words_directory,
                os.path.join(pages_directory, "downloads"),
                tokens_directory,
                language,
            ],
        },
        {
            "name": "lemmas",
            "description": "Lemmas",
            "script": "lemmas.sh",
            "args": [
                words_directory,
                tokens_dir_successes,
                lemmas_directory,
                language,
            ],
        },
        {
            "name": "lemma-regroup",
            "description": "Run download and tokens steps for lemmas identified in lemmas step",
            "function": lemma_regroup.main,
            "args": [
                lemmas_directory,
                data_directory,
                lambda lemmas_words_dir: get_steps(data_directory, language, alternate_words_directory=lemmas_words_dir)
            ],
        },
        {
            "name": "definitions",
            "description": "Parse definitions from the tokens directory",
            "script": "definitions.sh",
            "args": [
                tokens_dir_successes,
                definitions_directory,
            ],
        },
        {
            "name": "combine",
            "description": "Combine inputs from previous steps",
            "script": "combine.sh",
            "args": [
                words_directory,
                definitions_directory,
                lemmas_directory,
                final_directory,
            ]
        }
    ]
