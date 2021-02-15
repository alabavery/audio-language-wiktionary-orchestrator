import os
import pathlib

from colors import Bcolors as bc

code_path = pathlib.Path(__file__).parent.absolute()
scripts_directory = os.path.join(code_path, 'shell_scripts')


def run(step):
    print(f"{bc.HEADER}", f"{bc.BOLD}", f"{bc.UNDERLINE}")
    print("BEGINNING STEP {}".format(step["name"]))
    print(f"{bc.ENDC}")

    script_name = step.get("script")
    fn = step.get("function")
    params = step.get("args", [])

    if script_name:
        run_shell_script(script_name, params)
    else:
        fn(*params)

    print(f"{bc.OKBLUE}", f"{bc.BOLD}")
    print("FINSHED STEP {}\n\n".format(step["name"]))
    print(f"{bc.ENDC}")


def run_shell_script(script_name, params):
    os.system("{script_path} {script_args}".format(
        script_path=os.path.join(scripts_directory, script_name),
        script_args=(' ').join(params)
    ))