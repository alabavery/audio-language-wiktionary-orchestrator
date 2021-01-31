import os
import pathlib


code_path = pathlib.Path(__file__).parent.absolute()
scripts_directory = os.path.join(code_path, 'shell_scripts')


def run(step):
    print("BEGINNING STEP {}".format(step["name"]))
    script_name = step.get("script")
    fn = step.get("function")
    params = step.get("args", [])

    if script_name:
        os.system("{script_path} {script_args}".format(
            script_path=os.path.join(scripts_directory, step["script"]),
            script_args=(' ').join(params)
        ))
    else:
        fn(*params)

    print("FINSHED STEP {}\n\n".format(step["name"]))
