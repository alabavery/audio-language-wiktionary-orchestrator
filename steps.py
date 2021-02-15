import os

from functions import lemma_regroup, final_words_list
import db

def get_steps(data_directory, language, database_directory=None, alternate_words_directory=None):
    def get_path(sub_path):
        return os.path.join(data_directory, sub_path)
    
    words_directory = get_path('word_list') if alternate_words_directory is None else alternate_words_directory
    pages_directory = get_path('pages')
    tokens_directory = get_path('tokens')
    definitions_directory = get_path('definitions')
    lemmas_directory = get_path('lemmas')
    final_directory = get_path('combined')
    lemmas_words_dir = get_path('lemmas_regroup_words_list')
    final_words_dir = get_path('final_word_list')

    tokens_dir_successes = os.path.join(tokens_directory, 'successes')
    return [
        {
            "name": "clear paths",
            "description": "Clear stale data",
            "script": "clear.sh",
            "args": [
                tokens_directory,
                definitions_directory,
                lemmas_directory,
                final_directory,
                lemmas_words_dir,
                final_words_dir,
            ],
        },
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
                lemmas_words_dir,
                lambda: get_steps(data_directory, language, alternate_words_directory=lemmas_words_dir)
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
            "name": "create final words",
            "description": "Combine original word list with lemma regroup word list",
            "function": final_words_list.make,
            "args": [
                words_directory,
                lemmas_words_dir,
                final_words_dir,
            ],
        },
        {
            "name": "combine",
            "description": "Combine inputs from previous steps",
            "script": "combine.sh",
            "args": [
                final_words_dir,
                definitions_directory,
                lemmas_directory,
                final_directory,
            ]
        },
        {
            "name": "start db",
            "description": "start db docker (harmless error if it's already running)",
            "script": "start-db.sh",
            "args": [
                db.DB.HOST,
                db.DB.PASSWORD,
                db.DB.USER,
                db.DB.DB_NAME,
                db.DB.NETWORK,
                database_directory,
            ],
        },
        {
            "name": "populate db",
            "description": "create and populate tables in a sql store",
            "script": "db.sh",
            "args": [
                final_directory,
                db.DB.NETWORK,
                db.CONNECTION_STRING,
            ]
        },
        {
            "name": "stop db",
            "description": "kill the postgres container",
            "script": "stop-db.sh",
            "args": [
                db.DB.HOST,
            ],
        },
    ]
        