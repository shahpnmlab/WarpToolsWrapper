# WarpToolsWrapper
A light wrapper around warp/M

# Description
The aim of this wrapper is to be a light layer over WarpTools (and assoc. programs) command line arguments.
The options to the different subprograms is intended to be provided via a config (e.g.``movie_preprocessing.ini``) file.
Think of the config files as recipes that you use to run WarpTools on your linux box (cluster).
While it is possible to run through the entire processing pipeline by concatenating all the commands into a single
bash file, it is hoped that by providing different config files for different sub-routines, the user will be in a slightly
better position to track their actions and allow them to be more exploratory with the data in their lab.

# Installation
Since it is meant to be a light wrapper there arent many significant dependencies. However, ``typer`` is required.
To install - 
```commandline
git clone git@github.com:shahpnmlab/WarpToolsWrapper.git
cd WarpToolsWrapper
pip install -e .
```
If you want to update the program, simple navigate to the WarpToolsWrapper directory on your computer and simply run
```commandline
git pull
```
# Running
Once installed you can call the program with
`warper`

One can call the program in several ways -
1. `warper -c <recipe>.ini` -> This will generate a script file with the following name `warpTools_<HHMMSS>_<YYMMDD>.sh`
2. `warper -c <recipe>.ini -o <a_unique_name>.sh` -> This will generate a script file a user provided file name.
3. `warper -c <recipe>.ini -s <a_submission_script>.sh` -> This will generate a submission script based on the user provided template.
    #### Note: Sucesssive calls `-s` will result in a submission script with accumulated bash commands. It is up to the user to review the submission script before submitting it.  