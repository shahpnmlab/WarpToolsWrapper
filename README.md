# WarpToolsWrapper
A light wrapper around warp/M

# Description
The aim of this wrapper is to be a light layer over WarpTools (and assoc. programs) command line arguments.
The options to the different subprograms is intended to be provided via a config (e.g.``config.ini``) file.
The hope is that the config file will provide a human-readable record of the commands used to execute the different 
processing steps.

While it is possible to run through the entire processing pipeline by concatenating all the commands into a single
bash file, it is hoped that by providing different config files for different sub-routines, the user will be in a slightly
better position to track their actions and allow them to be more exploratory with the data in their lab.

# Installation
Since it is meant to be a light wrapper there arent many significant dependencies. However, ``typer`` is required.
To install - 
```commandline
git clone git@github.com:shahpnmlab/WarpToolsWrapper.git
cd WarpToolsWrapper
pip install .
```
