import os
import datetime
from pathlib import Path
from funcs import make_com_script, parser, is_program_in_path
import typer

warpIT = typer.Typer()
@warpIT.command(no_args_is_help=True)
def run(config_file: Path = typer.Option(..., help="Path to config.ini file"),
        out_path: Path = typer.Option(..., help="Path to where the script file should go")):
    isIMOD = is_program_in_path("3dmod")
    isAreTomo = is_program_in_path("AreTomo")
    isRelion = is_program_in_path("relion")

    #if isIMOD and isAreTomo and isRelion:
    if isIMOD and isRelion:
        print("All required binaries are in $PATH")

    settings = parser(config_file)
    filename = os.path.join(out_path, f"warpTools_{datetime.datetime.now():%Y%m%d_%H%M%S}.sh")

    with open(filename, 'w') as file:
        file.write("#!/bin/bash\n")
        file.write("\n")

        # Assuming tasks are the sections in the config file
        for task, options in settings.items():
            routine = task.split(":")[0]
            com = make_com_script(options, routine)
            file.write(f'{com}\n')


if __name__ == "__main__":
    warpIT()
