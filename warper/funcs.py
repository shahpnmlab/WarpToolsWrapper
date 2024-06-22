import os
import datetime
import configparser

def parser(in_config_file, section=None):
    config = configparser.ConfigParser()
    config.read(in_config_file)

    def parse_section(section):
        return tuple(section.split(":"))

    if section:
        section_tuple = parse_section(section)
        return {option: config.get(section, option) for option in config.options(section)}
    else:
        sections = {parse_section(sec): {option: config.get(sec, option) for option in config.options(sec)} for sec in config.sections()}
        indexed_sections = {index + 1: task for index, task in enumerate(sections)}
        return indexed_sections, sections

def make_com_script(section_tuple, settings):
    if len(section_tuple) == 1:
        command_parts = [f"{section_tuple[0]}"]
    else:
        command_parts = [f"{section_tuple[0]} {section_tuple[1]}"]

    # Iterate over all settings
    for key, value in settings.items():
        if isinstance(value, str) and value.lower() in ['true', 'false']:  # Handle Boolean values
            if value.lower() == 'true':  # Only add the flag if true
                command_parts.append(f"--{key}")  # Add the flag
        elif value:  # Handle other parameters that are not empty
            command_parts.append(f"--{key} {value}")  # Add parameter and value

    command = " ".join(command_parts)
    return command

