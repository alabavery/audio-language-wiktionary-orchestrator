import sys
import os
import pathlib

from run_step import run
from steps import get_steps


if __name__ == '__main__':
    args = sys.argv[1:]
    data_directory = args[0]
    language = args[1]
    dir_to_save_sql = args[2]

    steps = get_steps(data_directory, language, database_directory=dir_to_save_sql)
    for step in steps:
        run(step)
