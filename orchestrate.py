import sys
import os
import pathlib

from run_step import run
from steps import get_steps


if __name__ == '__main__':
    args = sys.argv[1:]
    data_directory = args[0]
    language = args[1]

    steps = get_steps(data_directory, language)
    if len(args) > 2:
        step_name_to_run = args[2]
        step_to_run = [s for s in steps if s["name"] == step_name_to_run]
        if (len(step_to_run) == 0):
            raise RuntimeError("Provided argument '{}' is not a step name".format(step_name_to_run))
        run(step_to_run[0])
    else:
        for step in steps:
            run(step)
