import os
import datetime
import configparser

def is_program_in_path(program):
    # Get the system's PATH variable
    path = os.environ.get("PATH", "")

    # Determine the right separator based on the operating system
    if os.name == 'nt':  # Windows
        separator = ';'
    else:  # POSIX (Linux, Unix, MacOS)
        separator = ':'

    # Split the PATH into directories
    directories = path.split(separator)

    # Check each directory in the PATH
    for directory in directories:
        # Build the full path to where the program would be if it's in this directory
        executable_path = os.path.join(directory, program)

        # Check if the executable exists in this path and is executable
        if os.path.exists(executable_path) and os.access(executable_path, os.X_OK):
            return True

    # Return False if the program is not found in any directories in the PATH
    return False

# def parser(section, in_config_file):
#     config = configparser.ConfigParser()
#     config.read(in_config_file)
#     out = {option: config.get(section, option) for option in config.options(section)}
#     return out

def parser(in_config_file, section=None):
    config = configparser.ConfigParser()
    config.read(in_config_file)
    if section:
        # Return a dictionary of options for a specific section
        return {option: config.get(section, option) for option in config.options(section)}
    else:
        # Return a dictionary of all sections with their corresponding options if no specific section is provided
        return {sec: {option: config.get(sec, option) for option in config.options(sec)} for sec in config.sections()}

def make_com_script(settings, routine):
    command_parts = [f"WarpTools {routine}"]

    # Iterate over all settings
    for key, value in settings.items():
        if isinstance(value, str) and value.lower() in ['true', 'false']:  # Handle Boolean values
            if value.lower() == 'true':  # Only add the flag if true
                command_parts.append(f"--{key}")  # Add the flag
        elif value:  # Handle other parameters that are not empty
            command_parts.append(f"--{key} {value}")  # Add parameter and value

    command = " ".join(command_parts)
    return command

    # with open(filename, 'w') as file:
    #     file.write("#!/bin/bash\n")
    #     file.write(command + "\n")
    #
    # return filename