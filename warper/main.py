import os
import datetime
from pathlib import Path
from warper.funcs import make_com_script, parser
import typer
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

warper = typer.Typer(add_completion=False)

app_version = 0.3
def version_callback(value: bool):
    if value:
        typer.echo(f"Version: {app_version}")
        raise typer.Exit()

@warper.command(no_args_is_help=True)
def main(config_file: Path = typer.Option(None, "--config", "-c", help="input configuration file (eg. config.ini)"),
         out_path: Path = typer.Option(None, "--output", "-o", help="Output name for bash script"),
         submission_script_template: Path = typer.Option(None, "--submission_script", "-s",
                                                         help="Path to a submission script template"),
         version: bool = typer.Option(None, "--version", callback=version_callback, is_eager=True, help="Show the version and exit")):

    if not config_file:
        typer.echo("Error: Missing option '--config' / '-c'.")
        raise typer.Exit(code=1)

    settings = parser(config_file)

    if out_path is None:
        filename = os.path.join(os.getcwd(), f"warpTools_{datetime.datetime.now():%Y%m%d_%H%M%S}.sh")
    else:
        filename = out_path

    commands = []  # List to store all commands

    with open(filename, 'w') as file:
        file.write("#!/bin/bash\n")
        file.write("\n")

        # Assuming tasks are the sections in the config file
        for task, options in settings.items():
            com = make_com_script(task, options)
            commands.append(com)  # Append each command to the list
            file.write(f'{com}\n')

    # Log all commands after they have been written to the file
    logger.info(f"Generating a command script {filename}\nScript contains the following commands:\n" + "\n".join(commands))

    if submission_script_template is not None and submission_script_template.is_file():
        with open(submission_script_template, "a") as sub:
            sub.write("\n")
            sub.write(f"bash {filename}")
            sub.write("\n")

if __name__ == "__main__":
    warper()(main)

